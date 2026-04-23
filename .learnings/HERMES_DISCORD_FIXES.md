# Hermes Discord Bot - Troubleshooting & Permanent Fixes

## Common Issues & Solutions

### Issue 1: Service not responding / gateway crashed
**Symptoms:** No response in Discord, service shows inactive/dead

**Diagnostic:**
```bash
systemctl status hermes-discord
journalctl -u hermes-discord -n 30 --no-pager
ps aux | grep hermes | grep -v grep
tail -20 /root/.hermes/logs/agent.log
```

**Root Causes:**
1. Stale PID file (`/root/.hermes/gateway.pid`) - process previously left PID behind
2. Restart policy was `Restart=on-failure` instead of `Restart=always`
3. Manual `hermes gateway run --replace` conflicting with systemd service

**Permanent Fix:**
```bash
# Kill stale processes and remove stale PID
systemctl stop hermes-discord
pkill -f "hermes gateway" 2>/dev/null; sleep 1
rm -f /root/.hermes/gateway.pid

# Fix restart policy
sed -i 's/Restart=on-failure/Restart=always/' /etc/systemd/system/hermes-discord.service
echo "RestartSec=5" >> /etc/systemd/system/hermes-discord.service
systemctl daemon-reload

# Start clean
systemctl start hermes-discord
```

### Issue 2: Bot not responding in specific channels
**Symptoms:** Bot connects but ignores messages in some channels

**Diagnostic:**
```bash
grep -A8 '^discord:' /root/.hermes/config.yaml
cat /root/.hermes/channel_directory.json
```

**Root Cause:** `require_mention: true` - bot only responds when @mentioned

**Solution:** Set `require_mention: false` for all channels to respond freely:
```bash
sed -i 's/require_mention: true/require_mention: false/' /root/.hermes/config.yaml
systemctl restart hermes-discord
```

**Note:** For free-response in specific channels only (not all), set:
```yaml
free_response_channels: 'CHANNEL_ID_1,CHANNEL_ID_2'
```
But NO wildcard exists - must list channel IDs explicitly.

### Issue 3: PrivilegedIntentsRequired error
**Symptoms:** Gateway connects but messages never arrive, errors in logs

**Diagnostic:**
```bash
grep 'PrivilegedIntentsRequired' /root/.hermes/logs/agent.log
```

**Root Cause:** Discord bot doesn't have required intents enabled in Developer Portal

**Fix:** Must be done in Discord Developer Portal:
1. Go to https://discord.com/developers/applications
2. Click your bot → Bot → Privileged Gateway Intents
3. Enable ALL THREE:
   - ✅ Presence Intent
   - ✅ Server Members Intent
   - ✅ Message Content Intent
4. Save and re-invite bot to server

### Issue 4: Disk full causing silent failures
**Symptoms:** Service crashes, processes stop

**Diagnostic:**
```bash
df -h /
du -sh /root/.hermes/logs/*
```

**Permanent Fix:**
```bash
# Journal size limit
mkdir -p /etc/systemd/journald.conf.d/
cat > /etc/systemd/journald.conf.d/hermes.conf << 'HERMESEOF'
[Journal]
SystemMaxUse=200M
MaxRetentionSec=7day
HERMESEOF
systemctl restart systemd-journald

# Logrotate for hermes logs
cat > /etc/logrotate.d/hermes << 'LOGEOF'
/root/.hermes/logs/*.log {
    daily
    rotate 7
    compress
    missingok
    notifempty
    copytruncate
}
LOGEOF

# Resize LXC disk (from Proxmox host)
pct resize LXC_ID rootfs 20G
```

## Key File Locations
- Service definition: `/etc/systemd/system/hermes-discord.service`
- Config: `/root/.hermes/config.yaml`
- Gateway PID: `/root/.hermes/gateway.pid`
- Logs: `/root/.hermes/logs/agent.log`, `errors.log`, `gateway-restart.log`
- Channel directory: `/root/.hermes/channel_directory.json`
- Dashboard: runs on port 9119

## Golden Rules
1. **NEVER run `hermes gateway run` manually** - always use `systemctl restart hermes-discord`
2. **Use `Restart=always`** in systemd - catches clean exits too
3. **Delete stale PID files** before restart if service fails to start
4. **Set `require_mention: false`** if you want bot to respond without @mention
5. **Resize disk** to at least 20G to prevent full-disk outages

## Service Management Commands
```bash
systemctl start hermes-discord     # Start
systemctl stop hermes-discord      # Stop
systemctl restart hermes-discord   # Restart (preferred over manual run)
systemctl status hermes-discord   # Check status
journalctl -u hermes-discord -f    # Watch live logs
```

## What Claude Code Did That I Should Remember
1. Checked `journalctl` output for SIGTERM signs (PID takeover pattern)
2. Identified stale PID file by checking `find / -name "*.pid"` 
3. Used `sed -i` to fix config and service files non-interactively
4. Set up logrotate and journald size limits for long-term health
5. Recommended LXC disk resize from 9.8G to 20G
