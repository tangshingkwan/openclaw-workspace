# MEMORY.md - Long-Term Memory

## About Franky
- **Name:** Franky Tang
- **Contact:** +85291621392 (WhatsApp)
- **Language Rules:**
  - English only → Reply in English
  - Mixed Chinese/English → Reply in Traditional Chinese + Cantonese

## Korea Trip (March-April 2026)

- **Plan:** First day, go directly from airport to Shiseido Korea office via Uber
- **Purpose:** Mostly working
- **Living in:** Seoul (staying/living there, not just visiting)
- **Arrival:** 2026-03-30
- **Work at KR office:** 2026-03-31 to 2026-04-02
- **Departure:** 2026-04-06
- **Flight:** Cathay Pacific CX410/CX427, HKD 9,011
- **Hotel:** Shilla Stay Samsung COEX Center, HKD 14,498
- **Total:** HKD 23,509

## Upcoming Trips
- **Japan:** Family trip (7-14 May 2026) with 7 people

## Skills Installed (9 total)
| Skill | Purpose |
|-------|---------|
| skill-vetter-1-0-0 | Security vetting before installing new skills |
| self-improving-agent | Self-improvement & learning from mistakes |
| openclaw-tavily-search | Web search (API key set) |
| summarize | URL/file/YouTube summarization (v0.12.0) |
| find-skill | Search for new skills |
| skill-creator-2 | Create new skills |
| using-superpowers | Skill invocation protocol |
| agent-browser-clawdbot | Browser automation |
| playwright | Browser automation via MCP |

## Backup Setup
- **USB HDD mounted:** /mnt/usbhdd
- **Backup folder:** /mnt/usbhdd/openclaw-backup/
- **Script:** /root/.openclaw/workspace/scripts/backup.sh
- **Cron:** Daily 9:00 AM HK time
- **Retention:** Last 7 backups
- **Includes:** openclaw.json, all workspace files, skills

## Hotel Research (Japan Trip)
- **Hotel:** Hotel Iori ホテル庵 (Fukuoka)
- **Plan:** Deluxe Suite (7-13 May) + Superior Family (13-14 May)
- **Note:** Deluxe Suite fits 7+ people, 76m², 5 double beds
- **Check:** Booking.com, Agoda, Trip.com for best price

## Phone Preference (8K HKD Budget)
- **Priority:** Camera quality
- **Top picks:**
  1. Xiaomi 15 Ultra (HK$6,399-7,999) - Best value, Leica camera
  2. Xiaomi 17 Ultra (HK$7,800-9,299) - Newer, bigger battery
  3. Samsung S25 Ultra (HK$7,998) - S Pen, waterproof
  4. Pixel 10 Pro XL (HK$6,480) - Best AI features

## System Info
- **Platform:** OpenClaw on Proxmox LXC container
- **Model:** MiniMax-M2.7 (session override)
- **Identity:** Franky's Little Assistant - Travis 🌞
- **Dreaming:** memory-core plugin with dreaming enabled (check if present after updates)

## Email Monitoring (Travis Inbox)
- **Dedicated Account:** tangyiusuntravis@gmail.com
- **App Password:** gnmj zmpf gqqp vmrm
- **IMAP:** imap.gmail.com (SSL) ✅ Working
- **Cron:** Email check every 2 hours (Job ID: d2f4f1a4)
- **Urgent keywords:** urgent, asap, critical, deadline, action required, etc.
- **Status:** ✅ Active - 43 emails in inbox

## TickTick API (Partially Working)
- **Client ID:** 8t2L7bh43HshNqK1QQ
- **Client Secret:** g4kWVY65bA5JUcyIY86yTku6l6XxGUIt
- **⚠️ Issue:** Token from developer portal is Client Secret, NOT API Token
- **API Token needed from:** TickTick App → Settings → Third-party Apps → API Token
- **Note:** Will retry once API Token is obtained

## Cron Jobs Status
| Job | Status | Notes |
|-----|--------|-------|
| Email Check (2hr) | ✅ Active | Working fine |
| Daily Backup (9AM HKT) | ✅ Working | Running daily, 7-day retention |
| Email Setup Reminder | ❌ Disable | Already done |

## Proxmox Access
- **Host:** 192.168.1.20:8006
- **Root:** T98467717k!
- **Travis SSH key:** ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDgpYquDQphyGbgspdffJF1hDW1OG5OV29g/A6l4wR/6

## Korea Trip Notes
- ⚠️ Construction at hotel: Yeongdong-daero underground works - Samseong Station Exits 7&8 CLOSED, use Temporary Exit 8
- ⚠️ Hotel is Shilla Stay Samsung COEX Center, NOT Shilla Stay Gangnam Yeoksam (different location)

## Patreon Integration (2026-03-29)
- **Status:** ✅ Working (cookie-based browser automation)
- **Creators tracked:**
  - 茄利略・CUP: https://www.patreon.com/cw/KelileoCUP ✅
  - Calvin Choy Studio: https://www.patreon.com/c/CalvinChoy ✅
  - ET Trading: https://www.patreon.com/c/ETTrading ❌ (wrong URL)
- **Cookies:** `/root/.openclaw/workspace/patreon-cookies.json`
- **Fetch script:** `/root/.openclaw/workspace/scripts/patreon-fetch.js`
- **Posts output:** `/root/.openclaw/workspace/patreon-posts.json`
- **History:** `/root/.openclaw/workspace/patreon-history/YYYY-MM-DD.json`
- **⚠️ Cookies expire** - need to re-export periodically from browser
