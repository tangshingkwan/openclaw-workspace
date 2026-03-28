#!/usr/bin/env python3
"""Seed the ontology graph with all known entities."""
import json
import sys
import uuid
from datetime import datetime, timezone

sys.path.insert(0, '/root/.openclaw/workspace/skills/ontology/scripts')
from ontology import create_entity, create_relation, append_op, DEFAULT_GRAPH_PATH, DEFAULT_SCHEMA_PATH

GRAPH = "/root/.openclaw/workspace/memory/ontology/graph.jsonl"

def ts():
    return datetime.now(timezone.utc).isoformat()

# ─── PEOPLE ────────────────────────────────────────────────────────────
franky = create_entity("Person", {
    "name": "Franky Tang",
    "phone": "+85291621392",
    "email": "frankytang@gmail.com",
    "role": "User / Owner",
    "language": "Cantonese, Mandarin, English",
    "timezone": "Asia/Hong_Kong"
}, GRAPH, "pers_franky")

hangyee = create_entity("Person", {
    "name": "Hangyee",
    "relation": "Wife",
    "role": "Family"
}, GRAPH, "pers_hangyee")

wingming = create_entity("Person", {
    "name": "Wingming",
    "relation": "Mom",
    "role": "Family"
}, GRAPH, "pers_wingming")

yuensum = create_entity("Person", {
    "name": "Yuensum",
    "relation": "Father-in-law",
    "role": "Family"
}, GRAPH, "pers_yuensum")

chukchui = create_entity("Person", {
    "name": "Chukchui",
    "relation": "Mother-in-law",
    "role": "Family"
}, GRAPH, "pers_chukchui")

yiusun = create_entity("Person", {
    "name": "Yiusun",
    "relation": "Son",
    "role": "Family"
}, GRAPH, "pers_yiusun")

manchit = create_entity("Person", {
    "name": "Manchit",
    "relation": "Daughter",
    "role": "Family"
}, GRAPH, "pers_manchit")

travis = create_entity("Person", {
    "name": "Travis",
    "role": "AI Assistant",
    "platform": "OpenClaw",
    "model": "MiniMax-M2.7"
}, GRAPH, "pers_travis")

# ─── FRANKY'S FAMILY ──────────────────────────────────────────────────
family_unit = create_entity("Group", {
    "name": "Tang Family",
    "type": "Family",
    "size": 7
}, GRAPH, "grp_family")

# Use string IDs for relations (not entity objects!)
for pid in ["pers_franky", "pers_hangyee", "pers_wingming", "pers_yuensum",
            "pers_chukchui", "pers_yiusun", "pers_manchit"]:
    create_relation(pid, "member_of", "grp_family", {}, GRAPH)

# ─── KOREA TRIP PROJECT ────────────────────────────────────────────────
kr_trip = create_entity("Project", {
    "name": "Korea Business Trip - Cegid Go-Live",
    "status": "active",
    "purpose": "Cegid POS go-live at Shiseido Korea + office work",
    "destination": "Seoul, South Korea",
    "owner": "Franky Tang",
    "project_id": "KR-CEGID-2026"
}, GRAPH, "proj_kr_trip")

create_relation("proj_kr_trip", "has_owner", "pers_franky", {}, GRAPH)
create_relation("proj_kr_trip", "has_member", "pers_travis", {}, GRAPH)

# ─── FLIGHT ENTITIES ───────────────────────────────────────────────────
flight_out = create_entity("Flight", {
    "flight_number": "CX410",
    "route": "HKG → ICN",
    "departure": "2026-03-30T09:25:00+0800",
    "airline": "Cathay Pacific",
    "booking_ref": "FAX3UP",
    "ticket": "160 2130988989",
    "cost_hkd": 4505,
    "type": "One-way"
}, GRAPH, "flig_cx410")

flight_back = create_entity("Flight", {
    "flight_number": "CX427",
    "route": "ICN → HKG",
    "departure": "2026-04-06T01:55:00+0800",
    "airline": "Cathay Pacific",
    "booking_ref": "FAX3UP",
    "ticket": "160 2130988989",
    "cost_hkd": 4506,
    "type": "Return"
}, GRAPH, "flig_cx427")

create_relation("proj_kr_trip", "has_outbound_flight", "flig_cx410", {}, GRAPH)
create_relation("proj_kr_trip", "has_return_flight", "flig_cx427", {}, GRAPH)

# ─── HOTEL ENTITIES ────────────────────────────────────────────────────
hotel1 = create_entity("Accommodation", {
    "name": "Shilla Stay Samsung COEX Center (Village View)",
    "address": "506 Yeongdong-daero, Seoul 06173",
    "check_in": "2026-03-30",
    "check_out": "2026-04-04",
    "nights": 5,
    "room_type": "Deluxe Double Village View",
    "cost_hkd": 9263,
    "cost_krw": 1776169,
    "note": "Construction: Samseong Station Exits 7&8 CLOSED, use Temporary Exit 8"
}, GRAPH, "acom_hotel1")

hotel2 = create_entity("Accommodation", {
    "name": "Shilla Stay Samsung COEX Center (City View)",
    "address": "506 Yeongdong-daero, Seoul 06173",
    "check_in": "2026-04-04",
    "check_out": "2026-04-06",
    "nights": 2,
    "room_type": "Deluxe Double City View",
    "cost_hkd": 5235,
    "cost_krw": 1003750
}, GRAPH, "acom_hotel2")

create_relation("proj_kr_trip", "has_accommodation", "acom_hotel1", {}, GRAPH)
create_relation("proj_kr_trip", "has_accommodation", "acom_hotel2", {}, GRAPH)

# ─── LOCATION ENTITIES ────────────────────────────────────────────────
hong_kong = create_entity("Location", {
    "name": "Hong Kong International Airport",
    "code": "HKG",
    "type": "Airport"
}, GRAPH, "loc_hkg")

incheon = create_entity("Location", {
    "name": "Incheon International Airport",
    "code": "ICN",
    "type": "Airport",
    "city": "Seoul"
}, GRAPH, "loc_icn")

shiseido_kr = create_entity("Location", {
    "name": "Shiseido Korea Office",
    "type": "Office",
    "city": "Seoul",
    "note": "Work at KR office 31 Mar - 2 Apr"
}, GRAPH, "loc_shiseido_kr")

samsong = create_entity("Location", {
    "name": "Samseong Station",
    "type": "Metro Station",
    "city": "Seoul",
    "note": "Construction: Exits 7&8 CLOSED, use Temporary Exit 8"
}, GRAPH, "loc_samseong")

create_relation("flig_cx410", "departs_from", "loc_hkg", {}, GRAPH)
create_relation("flig_cx410", "arrives_at", "loc_icn", {}, GRAPH)
create_relation("flig_cx427", "departs_from", "loc_icn", {}, GRAPH)
create_relation("flig_cx427", "arrives_at", "loc_hkg", {}, GRAPH)

# ─── EVENT ENTITIES ───────────────────────────────────────────────────
arrival_kr = create_entity("Event", {
    "title": "Arrive in Seoul",
    "start": "2026-03-30T12:00:00+0900",
    "type": "Arrival",
    "note": "Go directly from ICN airport to Shiseido KR office via Uber"
}, GRAPH, "evnt_arrival_kr")

work_days = create_entity("Event", {
    "title": "Work at Shiseido Korea Office",
    "start": "2026-03-31T09:00:00+0900",
    "end": "2026-04-02T18:00:00+0900",
    "type": "Work",
    "location": "Shiseido Korea Office"
}, GRAPH, "evnt_work_kr")

standby_days = create_entity("Event", {
    "title": "Standby Period",
    "start": "2026-04-04T09:00:00+0900",
    "end": "2026-04-05T18:00:00+0900",
    "type": "Standby",
    "note": "Post go-live standby support"
}, GRAPH, "evnt_standby")

departure_kr = create_entity("Event", {
    "title": "Depart Seoul",
    "start": "2026-04-06T01:55:00+0900",
    "type": "Departure",
    "flight": "CX427"
}, GRAPH, "evnt_departure")

go_live = create_entity("Event", {
    "title": "Cegid POS Go-Live",
    "start": "2026-04-01T00:00:00+0900",
    "type": "Milestone",
    "project": "KR-CEGID-2026",
    "note": "1 April 2026"
}, GRAPH, "evnt_golive")

hypercare = create_entity("Event", {
    "title": "Hypercare Period",
    "start": "2026-04-01T00:00:00+0900",
    "end": "2026-04-14T23:59:59+0900",
    "type": "Support",
    "note": "2 weeks post go-live hypercare"
}, GRAPH, "evnt_hypercare")

for ev_id in ["evnt_arrival_kr", "evnt_work_kr", "evnt_standby", "evnt_departure", "evnt_golive", "evnt_hypercare"]:
    create_relation("proj_kr_trip", "has_event", ev_id, {}, GRAPH)

create_relation("evnt_golive", "part_of", "proj_kr_trip", {}, GRAPH)
create_relation("evnt_hypercare", "part_of", "proj_kr_trip", {}, GRAPH)
create_relation("evnt_golive", "followed_by", "evnt_hypercare", {}, GRAPH)

# ─── JAPAN TRIP PROJECT ────────────────────────────────────────────────
japan_trip = create_entity("Project", {
    "name": "Japan Family Trip - Fukuoka",
    "status": "planning",
    "destination": "Fukuoka, Japan",
    "purpose": "Family trip",
    "owner": "Franky Tang",
    "dates": "2026-05-07 to 2026-05-14",
    "pax": 7
}, GRAPH, "proj_japan_trip")

create_relation("proj_japan_trip", "has_owner", "pers_franky", {}, GRAPH)
for pid in ["pers_hangyee", "pers_wingming", "pers_yuensum", "pers_chukchui",
            "pers_yiusun", "pers_manchit", "pers_travis"]:
    create_relation("proj_japan_trip", "has_member", pid, {}, GRAPH)

hotel_iori = create_entity("Accommodation", {
    "name": "Hotel Iori ホテル庵",
    "address": "Fukuoka, Japan",
    "plan_nights_1": "7-13 May (Deluxe Suite, 76m², 5 double beds)",
    "plan_nights_2": "13-14 May (Superior Family)",
    "capacity": "7+ people",
    "research_status": "checking_prices",
    "check_sources": "Booking.com, Agoda, Trip.com"
}, GRAPH, "acom_hotel_iori")

create_relation("proj_japan_trip", "has_accommodation", "acom_hotel_iori", {}, GRAPH)

# ─── DAYTRADE PROJECT ──────────────────────────────────────────────────
daytrade = create_entity("Project", {
    "name": "Day Trading Learning & Analysis",
    "status": "active",
    "purpose": "Stock market analysis and trading journal",
    "owner": "Franky Tang",
    "channels": ["daytrade-general", "daytrade-journal", "daytrade-resources"]
}, GRAPH, "proj_daytrade")

create_relation("proj_daytrade", "has_owner", "pers_franky", {}, GRAPH)
create_relation("proj_daytrade", "has_member", "pers_travis", {}, GRAPH)

# ─── SYSTEM / INFRA ────────────────────────────────────────────────────
openclaw = create_entity("System", {
    "name": "OpenClaw AI Platform",
    "platform": "Proxmox LXC Container",
    "host": "192.168.1.20:8006",
    "model": "MiniMax-M2.7",
    "location": "Home Proxmox"
}, GRAPH, "sys_openclaw")

create_relation("pers_travis", "runs_on", "sys_openclaw", {}, GRAPH)

travis_inbox = create_entity("Account", {
    "service": "Gmail",
    "email": "tangyiusuntravis@gmail.com",
    "type": "Email",
    "app_password": "SECRET",
    "imap_host": "imap.gmail.com",
    "status": "active"
}, GRAPH, "acct_gmail_travis")

ticktick = create_entity("Account", {
    "service": "TickTick",
    "client_id": "8t2L7bh43HshNqK1QQ",
    "client_secret": "SECRET",
    "api_token_status": "not_configured",
    "note": "API Token must come from TickTick mobile app"
}, GRAPH, "acct_ticktick")

discord_bot = create_entity("Account", {
    "service": "Discord Bot",
    "username": "Travis#9342",
    "bot_id": "1487096484750033046",
    "server": "Franky's server",
    "server_id": "1380620624220655808",
    "status": "active",
    "token_status": "active"
}, GRAPH, "acct_discord")

for acct_id in ["acct_gmail_travis", "acct_ticktick", "acct_discord"]:
    create_relation("pers_travis", "has_account", acct_id, {}, GRAPH)

# ─── PENDING TASKS ────────────────────────────────────────────────────
tasks = [
    ("task_backup_fix", "Fix daily backup script timeout", "open", "high"),
    ("task_ticktick_token", "Get TickTick API Token from mobile app", "open", "high"),
    ("task_hotel_booking", "Book Hotel Iori Fukuoka (May 2026)", "open", "high"),
    ("task_email_forward", "Set up email forwarding from Franky.tang@viseo.com", "open", "medium"),
    ("task_hypercare", "KR Cegid Hypercare (1-14 Apr 2026)", "in_progress", "high"),
]

task_proj_map = {
    "task_backup_fix": "proj_kr_trip",
    "task_hypercare": "proj_kr_trip",
    "task_hotel_booking": "proj_japan_trip",
}

for tid, title, status, priority in tasks:
    create_entity("Task", {"title": title, "status": status, "priority": priority}, GRAPH, tid)
    proj = task_proj_map.get(tid)
    if proj:
        create_relation(proj, "has_task", tid, {}, GRAPH)

# ─── CREDENTIALS (reference only) ─────────────────────────────────────
create_entity("Credential", {
    "service": "Proxmox",
    "host": "192.168.1.20:8006",
    "username": "root",
    "secret_ref": "ask_Franky",
    "ssh_key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDgpYquDQphyGbgspdffJF1hDW1OG5OV29g/A6l4wR/6"
}, GRAPH, "cred_proxmox")

create_entity("Credential", {
    "service": "Gmail - Travis Inbox",
    "email": "tangyiusuntravis@gmail.com",
    "app_password_ref": "TOOLS.md"
}, GRAPH, "cred_gmail")

print("✅ All entities seeded successfully!")
