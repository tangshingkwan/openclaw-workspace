#!/usr/bin/env python3
"""Check emails and report urgent ones to Franky."""
import imaplib
import email
from email.header import decode_header
from datetime import datetime, timedelta
import sys

EMAIL_USER = "tangyiusuntravis@gmail.com"
EMAIL_PASS = "gnmj zmpf gqqp vmrm"
IMAP_SERVER = "imap.gmail.com"

# Urgent keywords to look for
URGENT_KEYWORDS = [
    "urgent", "asap", "emergency", "critical", "deadline",
    "action required", "immediate", "important", "priority"
]

def decode_str(s):
    if s is None:
        return ""
    if isinstance(s, bytes):
        parts = decode_header(s)
        result = []
        for part, enc in parts:
            if isinstance(part, bytes):
                result.append(part.decode(enc or "utf-8", errors="replace"))
            else:
                result.append(part)
        return "".join(result)
    return str(s)

def check_emails():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")
        
        # Search for unseen emails from last 24 hours
        status, messages = mail.search(None, "UNSEEN")
        email_ids = messages[0].split()
        
        urgent_emails = []
        
        for eid in email_ids:
            status, msg_data = mail.fetch(eid, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])
            
            subject = decode_str(msg["Subject"])
            sender = decode_str(msg.get("From", ""))
            date = msg.get("Date", "")
            
            # Check if urgent
            is_urgent = any(kw in subject.lower() for kw in URGENT_KEYWORDS)
            
            urgent_emails.append({
                "subject": subject,
                "sender": sender,
                "date": date,
                "urgent": is_urgent
            })
        
        mail.logout()
        
        # Output results
        if not email_ids:
            print("NO_URGENT_EMAILS")
            return
        
        urgent_count = sum(1 for e in urgent_emails if e["urgent"])
        
        if urgent_count > 0:
            print(f"URGENT_EMAILS_FOUND:{urgent_count}")
            for e in urgent_emails:
                if e["urgent"]:
                    print(f"- [{e['date']}] {e['subject']}")
        else:
            print("NO_URGENT_EMAILS")
            
    except Exception as e:
        print(f"ERROR:{e}")
        sys.exit(1)

if __name__ == "__main__":
    check_emails()
