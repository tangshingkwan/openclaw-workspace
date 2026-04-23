# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## Credentials Location

All credentials stored in `.credentials/` (gitignored):
- `example-api.txt` — Example API key

**Never commit credentials to git. Never echo/print credential values.**

---

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Tool-specific configurations and settings
- Gotchas and workarounds discovered
- Common commands and patterns
- Integration notes
- Credential locations (not the credentials themselves!)
- Anything environment-specific

## Examples

### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod

---

## Tool Configuration Template

### [Tool Name]

**Status:** ✅ Working | ⚠️ Issues | ❌ Not configured

**Configuration:**
```
Key details about how this tool is configured
```

**Gotchas:**
- Things that don't work as expected
- Workarounds discovered

**Common Operations:**
```bash
# Example command
tool-name --common-flag
```

---

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## 📦 System Dependencies

| Package | Purpose | Installed |
|--------|---------|-----------|
| python3-yaml | Ontology skill schema validation | ✅ 6.0.2 |

---

Add whatever helps you do your job. This is your cheat sheet.

---

## Email Monitoring

**Status:** ✅ Working

**Dedicated Account:** tangyiusuntravis@gmail.com
- IMAP: imap.gmail.com (SSL)
- App Password: gnmj zmpf gqqp vmrm

**Cron Job:** Email Check every 2 hours
- Job ID: d2f4f1a4-e612-4016-b376-068b7e7d3d2d
- Checks for unread emails with urgent keywords (urgent, asap, critical, deadline, action required, etc.)
- Messages Franky on WhatsApp if urgent emails found
- Script: /root/.openclaw/workspace/scripts/check-emails.py

**Urgent Keywords:**
- urgent, asap, emergency, critical, deadline
- action required, immediate, important, priority

---

## Reminders (Quick-Reminders Skill)

**Installed:** skills/quick-reminders

**Target (WhatsApp):** +85291621392

**Usage:**
```bash
# Remind me in 2 hours to do something
bash skills/quick-reminders/scripts/nohup-reminder.sh add "Hey, you wanted to..." --target +85291621392 -t 2h --channel whatsapp

# List active reminders
bash skills/quick-reminders/scripts/nohup-reminder.sh list

# Remove a reminder
bash skills/quick-reminders/scripts/nohup-reminder.sh remove <id>
```

**Note:** For reminders >48h, use TickTick calendar instead.

---

## 🖼️ Image Model (MiniMax VL)

**Gotchas:**
- Batch processing (multiple images) often times out — process single images with timeout handling
- API error 1033 (system error) — retry with single image, usually works on 2nd try
- Always do single image mode for OCR/captioning tasks

---

## 📄 PDF Generation

**Font Selection (Chinese):**
- Noto Sans SC = Simplified Chinese
- Noto Sans TC = Traditional Chinese
- Always identify character set BEFORE selecting fonts
- Test Chinese text rendering early, not after multiple iterations

**Playwright PDF:**
- Relative paths fail → use `file://` URLs instead

---

## 💬 Discord File Sharing

Use the openclaw CLI for PDF/file uploads:
```bash
openclaw message send --channel discord --target channel:XXX --media /path/to/file
```

---

## 🛠️ Skills Installation

**Symlink Required:** Skills from `~/.agents/skills/` need manual symlinking:
```bash
ln -sf ~/.agents/skills/<skill-name> ~/.openclaw/workspace/skills/<skill-name>
```
The skills.sh CLI may say "symlinked: OpenClaw" but symlinks are NOT auto-created — verify manually.

---

## 🔀 Proxmox Host (192.168.1.20)

**Access:** Web UI https://192.168.1.20:8006 | SSH port 22 (blocked from outside, use LXC 102 as jump host)

**Tailscale:** ✅ Installed
- Tailscale IP: `100.81.23.65`
- Auth URL used: `https://login.tailscale.com/a/14978f22019974`
- Can now access Proxmox UI via `https://100.81.23.65:8006` from any Tailscale device

**LXCs running:**
- LXC 102: OpenClaw (192.168.1.101)
- LXC 103: Hermes/Discord bot (192.168.1.103)

---

## 🤖 Hermes Discord Bot (LXC 103 - hermes, 192.168.1.103)

**Status:** ✅ Running (as Jasmine#6934)

**SSH Access:**
```bash
ssh root@192.168.1.103
# Password: Travis123
```

**Service Management:**
```bash
systemctl status hermes-discord    # Check if running
systemctl restart hermes-discord   # Restart (preferred way)
systemctl stop hermes-discord      # Stop
systemctl start hermes-discord     # Start
journalctl -u hermes-discord -f    # Watch live logs
```

**Key Files:**
- Config: `/root/.hermes/config.yaml`
- Logs: `/root/.hermes/logs/agent.log`, `errors.log`, `gateway-restart.log`
- PID: `/root/.hermes/gateway.pid`
- Dashboard: http://192.168.1.103:9119

**Common Fixes:**
- Service not responding → Check `systemctl status hermes-discord`
- Stale PID → `rm -f /root/.hermes/gateway.pid && systemctl restart hermes-discord`
- Bot ignores messages → `sed -i 's/require_mention: true/require_mention: false/' /root/.hermes/config.yaml`

**Full troubleshooting guide:** `.learnings/HERMES_DISCORD_FIXES.md`
