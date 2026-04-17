#!/bin/bash
# Wiki auto-sync script for GitHub

cd /root/.openclaw/workspace/wiki

# Check for changes
if git diff-index --quiet HEAD -- 2>/dev/null; then
    echo "No changes to sync"
    exit 0
fi

# Add all changes
git add -A

# Commit with timestamp
git commit -m "Auto-sync: $(date '+%Y-%m-%d %H:%M')"

# Push to GitHub
git push origin master

echo "Wiki synced successfully at $(date)"
