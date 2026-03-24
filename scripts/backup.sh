#!/bin/bash
# Daily Backup Script for OpenClaw Workspace
# Backs up all settings, memory, and skills to USB HDD

USB_MOUNT="/mnt/usbhdd"
BACKUP_DIR="${USB_MOUNT}/openclaw-backup"
WORKSPACE="/root/.openclaw/workspace"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="openclaw_backup_${TIMESTAMP}.tar.gz"

# Check if USB is mounted
if [ ! -d "$BACKUP_DIR" ]; then
    echo "USB not mounted, exiting"
    exit 1
fi

# Create backup
tar -czf "${BACKUP_DIR}/${BACKUP_FILE}" \
    -C /root/.openclaw openclaw.json \
    -C /root/.openclaw workspace/AGENTS.md \
    -C /root/.openclaw workspace/SOUL.md \
    -C /root/.openclaw workspace/USER.md \
    -C /root/.openclaw workspace/IDENTITY.md \
    -C /root/.openclaw workspace/TOOLS.md \
    -C /root/.openclaw workspace/MEMORY.md \
    -C /root/.openclaw workspace/HEARTBEAT.md \
    -C /root/.openclaw workspace/memory/ \
    -C /root/.openclaw workspace/skills/ \
    2>/dev/null

# Keep only last 7 backups
cd $BACKUP_DIR && ls -t openclaw_backup_*.tar.gz | tail -n +8 | xargs -r rm

echo "Backup created: ${BACKUP_FILE}"
echo "Path: ${BACKUP_DIR}/${BACKUP_FILE}"
