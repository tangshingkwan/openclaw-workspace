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

Add whatever helps you do your job. This is your cheat sheet.

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
