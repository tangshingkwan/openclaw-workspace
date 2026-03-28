#!/bin/bash
# Auto-backup script: commits and pushes workspace changes to GitHub
# Run via cron: 0 9 * * * /root/.openclaw/workspace/scripts/auto-backup.sh

set -e

WORKSPACE="/root/.openclaw/workspace"
cd "$WORKSPACE"

# Check if there are changes
if git diff --quiet && git diff --cached --quiet && git status --porcelain | grep -q "^??"; then
    # Only untracked files (no staged/tracked changes) - check if meaningful
    if git status --porcelain | grep -v "^\?\?" | grep -q .; then
        echo "Changes detected, committing..."
    else
        echo "No tracked changes, skipping."
        exit 0
    fi
fi

# Add all changes
git add -A

# Get list of changed files for commit message
CHANGED=$(git diff --cached --name-only | tr '\n' ', ' | sed 's/, $//')
UNTRACKED=$(git status --porcelain | grep "^??" | awk '{print $2}' | tr '\n' ', ' | sed 's/, $//')

# Generate commit message
if [ -n "$CHANGED" ] && [ -n "$UNTRACKED" ]; then
    MSG="📝 Auto-backup: Updated: $CHANGED | New: $UNTRACKED"
elif [ -n "$CHANGED" ]; then
    MSG="📝 Auto-backup: Updated: $CHANGED"
else
    MSG="📝 Auto-backup: New files: $UNTRACKED"
fi

# Commit and push
git commit -m "$MSG"
git push origin master

echo "✅ Backup complete: $MSG"
