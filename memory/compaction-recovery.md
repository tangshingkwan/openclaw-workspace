# Compaction Recovery Protocol

**Auto-trigger when:**
- Session starts with `<summary>` tag
- Message contains "truncated", "context limits", "where were we?"
- Human says "continue", "what were we doing?"
- You should know something but don't

## Recovery Steps (IN ORDER)

### 1. Read Working Buffer
```
Read: memory/working-buffer.md
Purpose: Raw danger-zone exchanges before compaction
```

### 2. Read SESSION-STATE.md
```
Read: SESSION-STATE.md
Purpose: Active task state, key details, open threads
```

### 3. Read Daily Notes
```
Read: memory/YYYY-MM-DD.md (today + yesterday)
Purpose: Recent context, what was discussed/done
```

### 4. Search All Sources
```
Use: memory_search tool
Query: [relevant topic from conversation]
Purpose: Find any additional context
```

### 5. Extract & Clear
```
From buffer → SESSION-STATE.md
Pull: Important context from buffer into active state
Mark: Buffer entries as "recovered" or clear old entries
```

### 6. Resume
```
Present: "Recovered from working buffer. Last task was [X]. Continue?"
Do NOT ask: "What were we discussing?"
```

---

## Never Do These on Recovery

- ❌ Ask "what were we talking about?"
- ❌ Start from scratch without checking files
- ❌ Ask the human to re-explain what they already said
- ❌ Ignore the buffer assuming context is gone

---

## Buffer Retention

- Working buffer entries stay until next 60% context threshold
- After recovery, buffer is marked as "recovered" not deleted
- Compaction Recovery log entry added to buffer after successful recovery
