
#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════
    ɴᴀᴍᴇʟᴇss ᴛᴇʟᴇɢʀᴀᴍ ᴍᴀss ʀᴇᴘᴏʀᴛᴇʀ ᴠ3.0 - ɴᴜᴄʟᴇᴀʀ ᴇᴅɪᴛɪᴏɴ
═══════════════════════════════════════════════════════════════════════════
    ᴏᴡɴᴇʀ: ɴᴀᴍᴇʟᴇss
    ᴄʜᴀɴɴᴇʟ: ᴛ.ᴍᴇ/ɴᴀᴍᴇʟᴇssᴛᴇᴄʜɪɴᴄ
═══════════════════════════════════════════════════════════════════════════
"""

import os
import sys
import time
import random
import hashlib
import json
import smtplib
import requests
import threading
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    os.system("pip install colorama requests -q")
    from colorama import Fore, Style, init
    init(autoreset=True)

# ═══════════════════════════════════════════════════════════════════
# ᴄᴏɴғɪɢᴜʀᴀᴛɪᴏɴ
# ═══════════════════════════════════════════════════════════════════

VERSION = "3.0 ɴᴜᴄʟᴇᴀʀ"
OWNER = "ɴᴀᴍᴇʟᴇss"
CHANNEL = "ᴛ.ᴍᴇ/ɴᴀᴍᴇʟᴇssᴛᴇᴄʜɪɴᴄ"

AUTH_USERNAME = hashlib.sha256("admin nameless".encode()).hexdigest()
AUTH_PASSWORD = hashlib.sha256("password123$".encode()).hexdigest()
MAX_LOGIN_ATTEMPTS = 3

R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
M = Fore.MAGENTA
W = Fore.WHITE
B = Fore.BLUE
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT

TG_EMAILS = [
    "abuse@telegram.org",
    "spam@telegram.org",
    "dmca@telegram.org",
    "support@telegram.org",
    "legal@telegram.org",
    "stopCA@telegram.org",
    "dsa-report@telegram.org",
    "security@telegram.org",
    "sticker@telegram.org",
    "recover@telegram.org",
    "content@telegram.org",
    "privacy@telegram.org"
]

SMTP_ACCOUNTS = [
    ("ana12juli13@gmail.com", "teqlhggnfyoclnvh"),
    ("elizabeth1mary2@gmail.com", "axwmdyhwdtmpvjjj"),
    ("k1llerking1048@gmail.com", "htysxuobospqjqcs"),
    ("juli12ana13@gmail.com", "usfmrvttfkutvgep"),
    ("mary12eli34@gmail.com", "sopwupdcdoxywwfq"),
    ("he19rry89@gmail.com", "qhcvdatbzlveestw"),
    ("mrmaguire475@gmail.com", "bszfelovhgervjsh"),
    ("mr12john21@gmail.com", "enfuyhnjnphgeahk"),
    ("golliblegreg@gmail.com", "phmtujiciwuncqih")
]

REPORTER_NAMES = [
    "Sarah Mitchell", "James Anderson", "Maria Garcia", "David Chen",
    "Emma Williams", "Michael Brown", "Sophia Martinez", "Robert Taylor",
    "Olivia Johnson", "William Jones", "Isabella Davis", "Christopher Miller",
    "Ava Wilson", "Daniel Moore", "Mia Jackson", "Matthew Martin",
    "Charlotte Lee", "Anthony White", "Amelia Harris", "Andrew Thompson",
    "Harper Garcia", "Ethan Rodriguez", "Abigail Martinez", "Alexander Hernandez",
    "Emily Lopez", "Benjamin Gonzalez", "Elizabeth Wilson", "Samuel Anderson",
    "Victoria Adams", "Nathan Scott", "Lily Turner", "Lucas Harris",
    "Grace Walker", "Ryan Hall", "Chloe Young", "Brandon King"
]

REPORTER_ORGS = [
    "Internet Watch Foundation",
    "EU Digital Safety Coalition",
    "Child Protection Alliance",
    "Cybercrime Reporting Unit",
    "Digital Rights Watch",
    "Global Internet Safety Board",
    "Anti-Fraud Task Force",
    "Online Safety Alliance"
]

WEB_ENDPOINTS = [
    "https://telegram.org/support",
    "https://telegram.org/abuse",
    "https://telegram.org/dsa-report",
    "https://telegram.org/dmca"
]

USER_AGENTS = [
    "TelegramDesktop/4.8.1 (Windows NT 10.0; Win64; x64)",
    "TelegramDesktop/4.9.2 (Macintosh; Intel Mac OS X 13_0)",
    "TelegramAndroid/10.0.1 (Android 13; Pixel 7)",
    "TelegramIOS/10.1.2 (iPhone; iOS 17.0)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
]

stats = {
    "email_sent": 0,
    "email_failed": 0,
    "web_sent": 0,
    "web_failed": 0,
    "total": 0,
    "start_time": None,
    "session_target": "",
    "session_start": None
}

# ═══════════════════════════════════════════════════════════════════
# ᴀsᴄɪɪ ᴀʀᴛ
# ═══════════════════════════════════════════════════════════════════

LOGIN_ART = """
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠀⠀⠀"""

ATTACK_ART = """
⣠⣶⣶⣶⣶
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣧
⠀⠀⠀⠀⣼⣿⣿⣿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣠⣴⣶⣤⡀⠀
⠀⠀⠀⢰⣿⣿⣿⣿⠃⠈⢻⣿⣦⠀⠀⠀⠀⣸⣿⣿⣿⣿⣷⠀
⠀⠀⠀⠘⣿⣿⣿⡏⣴⣿⣷⣝⢿⣷⢀⠀⢀⣿⣿⣿⣿⡿⠋⠀
⠀⠀⠀⠀⢿⣿⣿⡇⢻⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣇⢸⣿⣿⡟⠙⠛⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀
⣴⣿⣿⣿⣿⣿⣿⣿⣠⣿⣿⡇⠀⠀⠀⠉⠛⣽⣿⣇⣀⣀⣀⠀
⠙⠻⠿⠿⠿⠿⠿⠟⠿⠿⠿⠇⠀⠀⠀⠀⠀⠻⠿⠿⠛⠛⠛⠀"""

# ═══════════════════════════════════════════════════════════════════
# ʀᴇᴘᴏʀᴛ ᴛᴇᴍᴘʟᴀᴛᴇs (ᴇxᴘᴀɴᴅᴇᴅ)
# ═══════════════════════════════════════════════════════════════════

DETAILED_REPORT = """Dear Telegram Moderation and Trust & Safety Team,

I am writing on behalf of {org} to formally report a Telegram account engaged in multiple serious criminal violations of Telegram's Terms of Service and applicable international law.

═══════════════════════════════════════════════════════════════════
REPORTED ACCOUNT DETAILS:
═══════════════════════════════════════════════════════════════════
Username:       @{target}
Profile URL:    https://t.me/{target}
Report Date:    {date}
Report Time:    {time}
Reference ID:   DSA-{report_id}
Submitted By:   {reporter_name} — {org}
Reporter Email: {reporter_email}

═══════════════════════════════════════════════════════════════════
CONFIRMED VIOLATIONS:
═══════════════════════════════════════════════════════════════════

[VIOLATION 1] — CHILD SEXUAL ABUSE MATERIAL (CSAM)
Severity: CRITICAL ⚠️
This account has been confirmed sharing, distributing, and soliciting
Child Sexual Abuse Material (CSAM) in violation of:
- Directive 2011/93/EU Article 5
- Budapest Convention on Cybercrime Article 9
- UN Optional Protocol on the Rights of the Child
Evidence: Documented posts with timestamps visible showing CSAM on {date}.
Required Action: Immediate account suspension + NCMEC referral within 1 hour.

[VIOLATION 2] — TERRORIST & EXTREMIST CONTENT
Severity: CRITICAL ⚠️
Account promotes, recruits for, and coordinates terrorist activities.
Applicable Law: EU TCO Regulation 2021/784 — 1-hour mandatory removal.
Evidence: Channels sharing radicalization content, recruitment material.

[VIOLATION 3] — ILLEGAL DRUG TRAFFICKING
Severity: HIGH
Account coordinates sales of narcotics including cannabis, MDMA, cocaine,
opioids and fentanyl with crypto payment wallets openly advertised.
Applicable Law: UN Single Convention on Narcotic Drugs 1961.
Evidence: Timestamped posts with pricing, delivery, and payment instructions.

[VIOLATION 4] — ORGANIZED FINANCIAL FRAUD
Severity: HIGH
Operating pump-and-dump crypto schemes, fake investment groups, rug pulls,
and exit scams targeting thousands of victims with documented losses.
Applicable Law: Directive 2013/40/EU; Directive 2019/713 on fraud.
Evidence: Fraudulent token promotions followed by documented rug pulls.

[VIOLATION 5] — HACKING SERVICES & CYBERCRIME
Severity: HIGH
Selling account takeover services, phishing kits, keyloggers, RATs,
stolen credentials databases and DDoS-for-hire services.
Applicable Law: Budapest Convention Articles 2-10; Directive 2013/40/EU.
Evidence: Active advertisement posts with pricing and service menus.

[VIOLATION 6] — HUMAN TRAFFICKING & EXPLOITATION
Severity: CRITICAL ⚠️
Coordinating forced labor recruitment, sexual exploitation, and smuggling
operations through coded language and private group referrals.
Applicable Law: Directive 2011/36/EU on human trafficking.

═══════════════════════════════════════════════════════════════════
LEGAL OBLIGATIONS — DSA ARTICLE 16 COMPLIANCE:
═══════════════════════════════════════════════════════════════════

This report is formally submitted under:
- EU Digital Services Act (DSA) Regulation (EU) 2022/2065
- Article 16 (Notice and Action Mechanism)
- Article 17 (Statement of Reasons)
- Article 34 (Systemic Risk Assessment)

MANDATORY RESPONSE TIMELINE:
- CSAM/Terrorist content: Removal within 1 hour (TCO Reg. 2021/784)
- Acknowledgment of this notice: Within 24 hours
- Full written response with actions taken: Within 72 hours
- Data preservation for law enforcement: Immediate

NON-COMPLIANCE CONSEQUENCES:
- Fines up to 6% of global annual turnover (DSA Article 74)
- Criminal liability referral to Europol and national authorities
- Emergency injunction applications in EU member state courts
- Referral to NCMEC, IWF, and relevant law enforcement agencies

═══════════════════════════════════════════════════════════════════
REQUESTED IMMEDIATE ACTIONS:
═══════════════════════════════════════════════════════════════════
1. Permanent suspension of @{target} within 24 hours
2. Termination of all associated channels and groups
3. Full IP address and device data preservation
4. Disclosure package prepared for law enforcement
5. NCMEC CyberTipline report for CSAM content
6. Written confirmation of all actions taken

I confirm this report is submitted in good faith under DSA Article 16(2)(e).

Best regards,
{reporter_name}
{org}
Email: {reporter_email}
Reference: DSA-{report_id}
Date: {date}
"""

SHORT_REPORT = """URGENT ABUSE REPORT — Telegram Trust & Safety

Reference: DSA-{report_id}
Date: {date} {time}
Target: @{target} | https://t.me/{target}
Reporter: {reporter_name} ({org})

VIOLATIONS CONFIRMED:
✗ Child Sexual Abuse Material (CSAM) — CRITICAL
✗ Terrorist recruitment content — CRITICAL
✗ Illegal drug trafficking coordination — HIGH
✗ Organized financial fraud / rug pulls — HIGH
✗ Hacking services and stolen data sales — HIGH
✗ Human trafficking coordination — CRITICAL

This account poses immediate danger to platform users and minors.
Evidence package available upon formal law enforcement request.

DSA Article 16 mandatory action required within 24 hours.
CSAM content requires removal within 1 hour per TCO Regulation 2021/784.

{reporter_name} | {org}
DSA Reference: DSA-{report_id}
"""

DSA_LEGAL_NOTICE = """FORMAL LEGAL NOTICE
REGULATION (EU) 2022/2065 — DIGITAL SERVICES ACT
ARTICLE 16 (NOTICE & ACTION) + ARTICLE 17 (STATEMENT OF REASONS)

══════════════════════════════════════════════════════════════════
Date Submitted:   {date} at {time}
Legal Reference:  DSA-{report_id}
Submitted By:     {reporter_name}
Organization:     {org}
Contact Email:    {reporter_email}
Platform:         Telegram Messenger / Telegram FZ-LLC (Dubai, UAE)
Subject Account:  @{target} — https://t.me/{target}
══════════════════════════════════════════════════════════════════

TO THE TELEGRAM DSA COMPLIANCE OFFICER AND LEGAL TEAM,

This constitutes a formal legally binding notice under the EU Digital
Services Act requiring mandatory platform action and written response.

ILLEGAL CONTENT CATEGORIES AND APPLICABLE LAW:

┌─────────────────────────────────────────────────────────────┐
│ CATEGORY          │ LAW                    │ SEVERITY       │
├─────────────────────────────────────────────────────────────┤
│ CSAM              │ Directive 2011/93/EU   │ CRITICAL       │
│ Terrorist Content │ TCO Reg. 2021/784      │ CRITICAL       │
│ Drug Trafficking  │ UN Conv. 1961          │ HIGH           │
│ Financial Fraud   │ Directive 2013/40/EU   │ HIGH           │
│ Cybercrime        │ Budapest Conv.         │ HIGH           │
│ Human Trafficking │ Directive 2011/36/EU   │ CRITICAL       │
└─────────────────────────────────────────────────────────────┘

PLATFORM OBLIGATIONS UNDER DSA:
— Article 16(3): Timely, diligent processing of this notice
— Article 17: Written statement of reasons for decisions made
— Article 92: Full application within EU territory
— TCO Article 3: CSAM/terrorist content removal within ONE HOUR

CONSEQUENCES OF NON-COMPLIANCE:
— Financial penalties: Up to 6% global annual revenue (DSA Art. 74)
— Operational suspension orders in EU member states
— Criminal referral to Europol Cybercrime Centre (EC3)
— Emergency injunctive relief in relevant EU courts
— Public transparency report filed with EU Commission

REQUIRED ACTIONS — MANDATORY TIMELINE:
1. [IMMEDIATE]  Preserve all account data (@{target})
2. [1 HOUR]     Remove CSAM and terrorist content
3. [24 HOURS]   Suspend account and associated entities
4. [24 HOURS]   Acknowledge receipt of this formal notice
5. [48 HOURS]   File NCMEC CyberTipline report
6. [72 HOURS]   Provide written statement of reasons (Art. 17)

I confirm this notice is submitted in good faith as required by
DSA Article 16(2)(e) and represents a formal legal complaint.

══════════════════════════════════════════════════════════════════
{reporter_name}
{org}
Email: {reporter_email}
Legal Reference: DSA-{report_id}
Submitted: {date} at {time}
══════════════════════════════════════════════════════════════════

ESCALATION NOTICE: Failure to comply will result in immediate referral
to the Irish Data Protection Commission, Europol EC3, NCMEC, IWF,
and national law enforcement agencies in all applicable EU jurisdictions.
"""

NCMEC_REPORT = """CYBERTIPLINE REPORT — NATIONAL CENTER FOR MISSING & EXPLOITED CHILDREN
CC: Telegram Trust & Safety <abuse@telegram.org>

CyberTip Reference: NCMEC-{report_id}
Date: {date} at {time}
Reporter: {reporter_name} | {org}
Contact: {reporter_email}

PLATFORM: Telegram Messenger
ACCOUNT REPORTED: @{target}
URL: https://t.me/{target}

NATURE OF REPORT:
This CyberTipline report documents the confirmed presence of Child Sexual
Abuse Material (CSAM) being shared, distributed, and solicited by the
above Telegram account.

INCIDENT DETAILS:
- Date of discovery: {date}
- Content type: CSAM (photographic and video material)
- Distribution method: Telegram channel/group links
- Geographic indicators: Multiple jurisdictions
- Evidence: Timestamped screenshots available upon formal request

PLATFORM NOTIFICATION:
Telegram has been formally notified via DSA Article 16 Notice (DSA-{report_id}).
This report is submitted concurrently to ensure mandatory NCMEC reporting
obligations are fulfilled under 18 U.S.C. § 2258A.

REQUESTED ACTIONS:
1. Log and process this CyberTipline report
2. Forward to relevant law enforcement agencies
3. Coordinate with Telegram for account data disclosure
4. Issue preservation letter to Telegram for account @{target}

{reporter_name}
{org}
Reference: NCMEC-{report_id}
Date: {date}
"""

INTERPOL_NOTICE = """INTERPOL CYBERCRIME DIVISION — NOTICE OF CRIMINAL ACTIVITY
CC: Telegram Legal <legal@telegram.org>, Telegram Abuse <abuse@telegram.org>

INTERPOL Reference: IC-{report_id}
Date: {date} at {time}
Submitted By: {reporter_name} | {org}

SUBJECT: Criminal Network Activity on Telegram Platform
ACCOUNT: @{target} | https://t.me/{target}

This notice is submitted to the INTERPOL Cybercrime Division and copied
to Telegram's legal team to document confirmed criminal network activity
operating through Telegram infrastructure.

CRIMINAL ACTIVITIES DOCUMENTED:
1. Transnational drug trafficking (coordinated across multiple countries)
2. Cybercrime services (hacking, phishing, credential theft)
3. Financial crimes (crypto fraud, money laundering)
4. Human trafficking coordination
5. CSAM distribution network

APPLICABLE INTERNATIONAL FRAMEWORKS:
- INTERPOL's Global Complex for Innovation (IGCI) mandate
- Budapest Convention on Cybercrime (ETS No. 185)
- UN Convention Against Transnational Organized Crime (UNTOC)
- Financial Action Task Force (FATF) Recommendation 15

PRESERVATION REQUEST:
Telegram is formally requested to preserve all data associated with
account @{target} including but not limited to:
- Account registration details (IP, device, phone number)
- Message metadata and content
- Payment and transaction records
- Associated accounts and group memberships
- Login history and access logs

{reporter_name}
{org}
INTERPOL Reference: IC-{report_id}
Date: {date}
"""

# ═══════════════════════════════════════════════════════════════════
# ᴜᴛɪʟɪᴛʏ ғᴜɴᴄᴛɪᴏɴs
# ═══════════════════════════════════════════════════════════════════

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def inject_data(template, target):
    name = random.choice(REPORTER_NAMES)
    org = random.choice(REPORTER_ORGS)
    email = random.choice([acc[0] for acc in SMTP_ACCOUNTS])
    report_id = random.randint(100000, 999999)
    date = datetime.now().strftime("%d %B %Y")
    time_str = datetime.now().strftime("%H:%M:%S UTC")
    return template.format(
        target=target.lstrip('@'),
        reporter_name=name,
        org=org,
        reporter_email=email,
        report_id=report_id,
        date=date,
        time=time_str
    )

def loading_bar(current, total, width=35):
    filled = int(width * current / total)
    bar = "█" * filled + "░" * (width - filled)
    percent = current / total * 100
    return f"{G}[{bar}] {W}{percent:.1f}%{RESET}"

def get_input(prompt, color=C):
    return input(f"{color}{prompt}{RESET} ").strip()

def get_target():
    target = get_input("ᴇɴᴛᴇʀ ᴛᴀʀɢᴇᴛ ᴜsᴇʀɴᴀᴍᴇ (ᴡɪᴛʜᴏᴜᴛ @) →", Y)
    if not target:
        print(f"{R}[!] ɪɴᴠᴀʟɪᴅ ᴛᴀʀɢᴇᴛ{RESET}")
        return None
    return target.lstrip('@')

def get_amount(max_amount=500):
    try:
        amount = int(get_input(f"ᴇɴᴛᴇʀ ᴀᴍᴏᴜɴᴛ (1-{max_amount}) →", Y))
        if 1 <= amount <= max_amount:
            return amount
    except:
        pass
    print(f"{R}[!] ɪɴᴠᴀʟɪᴅ ᴀᴍᴏᴜɴᴛ{RESET}")
    return None

# ═══════════════════════════════════════════════════════════════════
# ᴀᴜᴛʜᴇɴᴛɪᴄᴀᴛɪᴏɴ
# ═══════════════════════════════════════════════════════════════════

def login_screen():
    clear()
    print(f"{M}{BOLD}{LOGIN_ART}{RESET}")
    print(f"""
{M}{BOLD}╔══════════════════════════════════════════════════╗
║       ɴᴀᴍᴇʟᴇss sᴇᴄᴜʀᴇ ᴀᴄᴄᴇss sʏsᴛᴇᴍ v3.0      ║
║           🔐 ᴀᴜᴛʜᴇɴᴛɪᴄᴀᴛɪᴏɴ ʀᴇǫᴜɪʀᴇᴅ 🔐          ║
╚══════════════════════════════════════════════════╝{RESET}""")

def authenticate():
    attempts = 0
    while attempts < MAX_LOGIN_ATTEMPTS:
        login_screen()
        remaining = MAX_LOGIN_ATTEMPTS - attempts
        print(f"\n{Y}┌─「 🔐 ʟᴏɢɪɴ 」")
        print(f"{Y}├─❏ ᴀᴛᴛᴇᴍᴘᴛs ʀᴇᴍᴀɪɴɪɴɢ : {W}{remaining}")
        print(f"{Y}└─❏ ᴇɴᴛᴇʀ ᴄʀᴇᴅᴇɴᴛɪᴀʟs{RESET}\n")

        try:
            username = input(f"{C}👤 ᴜsᴇʀɴᴀᴍᴇ → {W}").strip()
            password = input(f"{C}🔑 ᴘᴀssᴡᴏʀᴅ → {W}").strip()
        except KeyboardInterrupt:
            print(f"\n\n{R}[!] ᴀᴄᴄᴇss ᴅᴇɴɪᴇᴅ.{RESET}\n")
            sys.exit(0)

        hashed_user = hashlib.sha256(username.encode()).hexdigest()
        hashed_pass = hashlib.sha256(password.encode()).hexdigest()

        if hashed_user == AUTH_USERNAME and hashed_pass == AUTH_PASSWORD:
            clear()
            print(f"{M}{BOLD}{LOGIN_ART}{RESET}")
            print(f"""
{G}{BOLD}╔══════════════════════════════════════════════════╗
║             ✅ ᴀᴄᴄᴇss ɢʀᴀɴᴛᴇᴅ ✅                 ║
║          ᴡᴇʟᴄᴏᴍᴇ ʙᴀᴄᴋ, {OWNER}                 ║
╚══════════════════════════════════════════════════╝{RESET}""")
            time.sleep(2)
            return True
        else:
            attempts += 1
            remaining_after = MAX_LOGIN_ATTEMPTS - attempts
            print(f"\n{R}[!] ❌ ɪɴᴄᴏʀʀᴇᴄᴛ ᴄʀᴇᴅᴇɴᴛɪᴀʟs{RESET}")
            if remaining_after > 0:
                delay = attempts * 3
                print(f"{Y}[!] {remaining_after} ᴀᴛᴛᴇᴍᴘᴛ(s) ʟᴇғᴛ — ᴡᴀɪᴛɪɴɢ {delay}s...{RESET}")
                time.sleep(delay)
            else:
                print(f"\n{R}{BOLD}")
                print(f"╔══════════════════════════════════════════════════╗")
                print(f"║   ⛔ ᴀᴄᴄᴏᴜɴᴛ ʟᴏᴄᴋᴇᴅ — ᴛᴏᴏ ᴍᴀɴʏ ᴀᴛᴛᴇᴍᴘᴛs      ║")
                print(f"║          ᴀᴄᴄᴇss ᴘᴇʀᴍᴀɴᴇɴᴛʟʏ ᴅᴇɴɪᴇᴅ            ║")
                print(f"╚══════════════════════════════════════════════════╝{RESET}")
                time.sleep(2)
                sys.exit(0)
    return False

# ═══════════════════════════════════════════════════════════════════
# ᴜɪ
# ═══════════════════════════════════════════════════════════════════

def banner():
    clear()
    print(f"""
{M}{BOLD}
 ███╗   ██╗ █████╗ ███╗   ███╗███████╗██╗     ███████╗███████╗███████╗
 ████╗  ██║██╔══██╗████╗ ████║██╔════╝██║     ██╔════╝██╔════╝██╔════╝
 ██╔██╗ ██║███████║██╔████╔██║█████╗  ██║     █████╗  ███████╗███████╗
 ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  ██║     ██╔══╝  ╚════██║╚════██║
 ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗███████╗███████╗███████║███████║
 ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝
{RESET}
{C}  ┌─「 😈👑 ɴᴀᴍᴇʟᴇss ᴛᴇʟᴇɢʀᴀᴍ ʙᴀɴ ᴛᴏᴏʟ {VERSION} 」
{C}  ├─❏ ᴏᴡɴᴇʀ    : {W}{OWNER}
{C}  ├─❏ ᴄʜᴀɴɴᴇʟ  : {W}{CHANNEL}
{C}  ├─❏ ᴛɪᴍᴇ     : {W}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{C}  ├─❏ sᴍᴛᴘs    : {W}{len(SMTP_ACCOUNTS)} ɢᴍᴀɪʟ ᴀᴄᴄᴏᴜɴᴛs ʀᴇᴀᴅʏ
{C}  ├─❏ ᴛᴀʀɢᴇᴛs  : {W}{len(TG_EMAILS)} ᴛᴇʟᴇɢʀᴀᴍ ᴀʙᴜsᴇ ᴇᴍᴀɪʟs
{C}  ├─❏ ᴛᴇᴍᴘʟᴀᴛᴇs: {W}5 ʟᴇɢᴀʟ ʀᴇᴘᴏʀᴛ ᴛᴇᴍᴘʟᴀᴛᴇs
{C}  └─❏ sᴛᴀᴛᴜs   : {G}ᴏɴʟɪɴᴇ ✅
{RESET}""")

def print_menu():
    print(f"""
{C}  ┌─「 📋 ᴍᴀɪɴ ᴍᴇɴᴜ 」
{C}  ├─❏ {W}[1] {Y}ʙᴀɴ ᴛᴇʟᴇɢʀᴀᴍ ᴜsᴇʀ         {G}(sᴛᴀɴᴅᴀʀᴅ)
{C}  ├─❏ {W}[2] {Y}ʙᴀɴ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ      {G}(sᴛᴀɴᴅᴀʀᴅ)
{C}  ├─❏ {W}[3] {Y}ʙᴀɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ       {G}(sᴛᴀɴᴅᴀʀᴅ)
{C}  ├─❏ {W}[4] {R}ᴅsᴀ ʟᴇɢᴀʟ ɴᴏᴛɪᴄᴇ          {R}(ɴᴜᴄʟᴇᴀʀ 🔥)
{C}  ├─❏ {W}[5] {R}ᴍᴀss ᴇᴍᴀɪʟ ғʟᴏᴏᴅ          {R}(ᴍᴀx ᴘᴏᴡᴇʀ ⚡)
{C}  ├─❏ {W}[6] {M}ɴᴄᴍᴇᴄ ᴄʏʙᴇʀᴛɪᴘ ʀᴇᴘᴏʀᴛ    {M}(ᴄsᴀᴍ ɴᴜᴄʟᴇᴀʀ 💀)
{C}  ├─❏ {W}[7] {M}ɪɴᴛᴇʀᴘᴏʟ ɴᴏᴛɪᴄᴇ           {M}(ɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ 🌍)
{C}  ├─❏ {W}[8] {Y}ᴄᴜsᴛᴏᴍ ʀᴇᴘᴏʀᴛ            {G}(ᴀᴅᴠᴀɴᴄᴇᴅ)
{C}  ├─❏ {W}[9] {B}ᴍᴜʟᴛɪ-ᴛᴀʀɢᴇᴛ ʙᴀɴ         {B}(ʙᴜʟᴋ 🎯)
{C}  ├─❏ {W}[10] {R}ɴᴜᴄʟᴇᴀʀ ᴀʟʟ-ɪɴ-ᴏɴᴇ      {R}(ᴍᴀxɪᴍᴜᴍ 💣)
{C}  ├─❏ {W}[11] {C}sᴛᴀᴛɪsᴛɪᴄs              {C}(ᴠɪᴇᴡ 📊)
{C}  ├─❏ {W}[12] {M}sᴇᴛᴛɪɴɢs               {M}(ᴄᴏɴғɪɢ ⚙️)
{C}  └─❏ {W}[0]  {R}ᴇxɪᴛ
{RESET}""")

# ═══════════════════════════════════════════════════════════════════
# ᴇᴍᴀɪʟ + ᴡᴇʙ
# ═══════════════════════════════════════════════════════════════════

def send_email(target, subject, message, recipients):
    email_acc, pwd = random.choice(SMTP_ACCOUNTS)
    recipient = random.choice(recipients)

    msg = MIMEMultipart('alternative')
    msg['From'] = f"{random.choice(REPORTER_NAMES)} <{email_acc}>"
    msg['To'] = recipient
    msg['Subject'] = subject
    msg['X-Priority'] = '1'
    msg['X-Report-ID'] = f"DSA-{random.randint(100000,999999)}"
    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(email_acc, pwd)
            server.sendmail(email_acc, recipient, msg.as_string())
        return True, recipient, email_acc
    except:
        pass

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as server:
            server.login(email_acc, pwd)
            server.sendmail(email_acc, recipient, msg.as_string())
        return True, recipient, email_acc
    except:
        return False, recipient, email_acc

def send_web_report(target, message):
    success_count = 0
    for url in WEB_ENDPOINTS:
        headers = {
            "Content-Type": "application/json",
            "User-Agent": random.choice(USER_AGENTS),
            "Origin": "https://telegram.org",
            "Referer": "https://telegram.org/support",
            "Accept-Language": random.choice(["en-US,en;q=0.9", "en-GB,en;q=0.8", "de-DE,de;q=0.9"])
        }
        payload = {
            "peer": target.lstrip('@'),
            "category": random.choice(["illegal_content", "csam", "terrorism", "fraud", "drugs"]),
            "message": message[:4000],
            "timestamp": int(time.time()),
            "report_id": f"DSA-{random.randint(100000,999999)}"
        }
        try:
            r = requests.post(url, json=payload, headers=headers, timeout=10)
            if r.status_code in (200, 201, 204):
                success_count += 1
        except:
            pass
    return success_count

# ═══════════════════════════════════════════════════════════════════
# ᴀᴛᴛᴀᴄᴋ ғᴜɴᴄᴛɪᴏɴs
# ═══════════════════════════════════════════════════════════════════

def show_attack_art(target, amount, mode):
    print(f"{R}{BOLD}{ATTACK_ART}{RESET}")
    print(f"""
{R}{BOLD}  ╔══════════════════════════════════════════════════╗
  ║              🔥 ᴀᴛᴛᴀᴄᴋ ɪɴɪᴛɪᴀᴛᴇᴅ 🔥              ║
  ╚══════════════════════════════════════════════════╝{RESET}
{C}  ┌─「 ᴛᴀʀɢᴇᴛ ɪɴғᴏ 」
{C}  ├─❏ ᴛᴀʀɢᴇᴛ  : {W}@{target}
{C}  ├─❏ ᴍᴏᴅᴇ    : {W}{mode}
{C}  ├─❏ ᴀᴍᴏᴜɴᴛ  : {W}{amount} ʀᴇᴘᴏʀᴛs
{C}  └─❏ sᴛᴀʀᴛ   : {W}{datetime.now().strftime('%H:%M:%S')}
{RESET}""")

def show_final_stats(target):
    elapsed = time.time() - stats["start_time"]
    success_rate = (stats['email_sent'] / stats['total'] * 100) if stats['total'] > 0 else 0
    print(f"""
{M}  {'='*52}
{G}  ┌─「 ✅ ᴀᴛᴛᴀᴄᴋ ᴄᴏᴍᴘʟᴇᴛᴇ 」
{G}  ├─❏ ᴛᴀʀɢᴇᴛ         : {W}@{target}
{G}  ├─❏ 📧 ᴇᴍᴀɪʟ sᴇɴᴛ   : {W}{stats['email_sent']}
{G}  ├─❏ 📧 ᴇᴍᴀɪʟ ғᴀɪʟ   : {W}{stats['email_failed']}
{G}  ├─❏ 🌐 ᴡᴇʙ sᴇɴᴛ    : {W}{stats['web_sent']}
{G}  ├─❏ ᴛᴏᴛᴀʟ ʀᴏᴜɴᴅs   : {W}{stats['total']}
{G}  ├─❏ ⏱️  ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  : {W}{int(elapsed//60)}ᴍ {int(elapsed%60)}s
{G}  └─❏ sᴜᴄᴄᴇss ʀᴀᴛᴇ  : {W}{success_rate:.1f}%
{M}  {'='*52}{RESET}
{Y}  ⏳ ᴡᴀɪᴛ 6-48ʜ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ʀᴇᴠɪᴇᴡ. sᴛᴀʏ ᴅᴀʀᴋ 😈{RESET}
""")

def reset_stats():
    global stats
    stats = {"email_sent": 0, "email_failed": 0, "web_sent": 0,
             "web_failed": 0, "total": 0, "start_time": time.time()}

def run_standard_ban(target, amount, entity_type="ᴜsᴇʀ"):
    reset_stats()
    target = target.lstrip('@')
    show_attack_art(target, amount, f"sᴛᴀɴᴅᴀʀᴅ {entity_type} ʙᴀɴ")

    SUBJECTS = [
        f"URGENT: Criminal Activity Report — @{target} — DSA Article 16",
        f"FORMAL COMPLAINT: Illegal Content @{target} — Immediate Action Required",
        f"ABUSE REPORT: @{target} — CSAM + Drug Trafficking + Fraud",
        f"DSA NOTICE: Violations Confirmed @{target} — 24h Action Required",
        f"CHILD SAFETY EMERGENCY: Account @{target} — Mandatory Review"
    ]

    for i in range(1, amount + 1):
        template = random.choice([DETAILED_REPORT, SHORT_REPORT])
        message = inject_data(template, target)
        subject = random.choice(SUBJECTS)

        success, recipient, sender = send_email(target, subject, message, TG_EMAILS)

        if success:
            stats["email_sent"] += 1
            print(f"{G}  [{i:03d}] ✓ → {recipient} ← {sender[:22]}...{RESET}")
        else:
            stats["email_failed"] += 1
            print(f"{R}  [{i:03d}] ✗ ғᴀɪʟᴇᴅ → {recipient}{RESET}")

        if i % 5 == 0:
            web_success = send_web_report(target, message)
            stats["web_sent"] += web_success
            if web_success > 0:
                print(f"{Y}  [{i:03d}] 🌐 ᴡᴇʙ: {web_success} ʀᴇᴘᴏʀᴛs ʜɪᴛ{RESET}")

        stats["total"] += 1
        if i % 10 == 0:
            print(f"\n  {loading_bar(i, amount)} [{i}/{amount}] ✓{stats['email_sent']} ✗{stats['email_failed']} 🌐{stats['web_sent']}\n")

        time.sleep(random.uniform(1.5, 3.5))

    show_final_stats(target)

def run_dsa_nuclear(target, amount):
    reset_stats()
    target = target.lstrip('@')
    show_attack_art(target, amount, "ᴅsᴀ ʟᴇɢᴀʟ ɴᴜᴄʟᴇᴀʀ 🔥")
    dsa_recipients = ["dsa-report@telegram.org", "legal@telegram.org", "abuse@telegram.org", "security@telegram.org"]

    for i in range(1, amount + 1):
        message = inject_data(DSA_LEGAL_NOTICE, target)
        subject = f"FORMAL DSA ART.16 NOTICE — DSA-{random.randint(100000,999999)} — @{target} — {datetime.now().strftime('%d %b %Y')}"

        success, recipient, sender = send_email(target, subject, message, dsa_recipients)

        if success:
            stats["email_sent"] += 1
            print(f"{G}  [{i:02d}] ✅ ᴅsᴀ → {recipient}{RESET}")
        else:
            stats["email_failed"] += 1
            print(f"{R}  [{i:02d}] ❌ ғᴀɪʟᴇᴅ → {recipient}{RESET}")

        stats["total"] += 1
        time.sleep(random.uniform(3, 6))

    show_final_stats(target)

def run_ncmec_nuclear(target, amount):
    reset_stats()
    target = target.lstrip('@')
    show_attack_art(target, amount, "ɴᴄᴍᴇᴄ ᴄʏʙᴇʀᴛɪᴘ 💀")
    ncmec_recipients = ["abuse@telegram.org", "legal@telegram.org", "stopCA@telegram.org", "security@telegram.org"]

    for i in range(1, amount + 1):
        message = inject_data(NCMEC_REPORT, target)
        subject = f"NCMEC CYBERTIPLINE — CSAM REPORT — @{target} — NCMEC-{random.randint(100000,999999)}"

        success, recipient, sender = send_email(target, subject, message, ncmec_recipients)

        if success:
            stats["email_sent"] += 1
            print(f"{G}  [{i:02d}] ✅ ɴᴄᴍᴇᴄ → {recipient}{RESET}")
        else:
            stats["email_failed"] += 1
            print(f"{R}  [{i:02d}] ❌ ғᴀɪʟᴇᴅ{RESET}")

        stats["total"] += 1
        time.sleep(random.uniform(2, 5))

    show_final_stats(target)

def run_interpol_notice(target, amount):
    reset_stats()
    target = target.lstrip('@')
    show_attack_art(target, amount, "ɪɴᴛᴇʀᴘᴏʟ ɴᴏᴛɪᴄᴇ 🌍")
    interpol_recipients = ["legal@telegram.org", "abuse@telegram.org", "security@telegram.org"]

    for i in range(1, amount + 1):
        message = inject_data(INTERPOL_NOTICE, target)
        subject = f"INTERPOL CYBERCRIME NOTICE — IC-{random.randint(100000,999999)} — @{target}"

        success, recipient, sender = send_email(target, subject, message, interpol_recipients)

        if success:
            stats["email_sent"] += 1
            print(f"{G}  [{i:02d}] ✅ ɪɴᴛᴇʀᴘᴏʟ → {recipient}{RESET}")
        else:
            stats["email_failed"] += 1
            print(f"{R}  [{i:02d}] ❌ ғᴀɪʟᴇᴅ{RESET}")

        stats["total"] += 1
        time.sleep(random.uniform(3, 6))

    show_final_stats(target)

def run_email_flood(target, amount):
    reset_stats()
    target = target.lstrip('@')
    show_attack_art(target, amount, "ᴍᴀss ᴇᴍᴀɪʟ ғʟᴏᴏᴅ ⚡")

    lock = threading.Lock()

    def send_batch(batch_num, start, end):
        for i in range(start, end):
            template = random.choice([DETAILED_REPORT, SHORT_REPORT, DSA_LEGAL_NOTICE, NCMEC_REPORT])
            message = inject_data(template, target)
            subject = f"URGENT REPORT #{i} — @{target} — DSA-{random.randint(100000,999999)}"

            success, recipient, sender = send_email(target, subject, message, TG_EMAILS)

            with lock:
                if success:
                    stats["email_sent"] += 1
                    print(f"{G}  [T{batch_num}|{i:03d}] ✓ {recipient[:18]}...{RESET}")
                else:
                    stats["email_failed"] += 1
                    print(f"{R}  [T{batch_num}|{i:03d}] ✗ ғᴀɪʟᴇᴅ{RESET}")
                stats["total"] += 1

            time.sleep(random.uniform(0.5, 1.5))

    threads = []
    batch_size = max(1, amount // 3)
    for i in range(3):
        start = i * batch_size + 1
        end = start + batch_size if i < 2 else amount + 1
        t = threading.Thread(target=send_batch, args=(i+1, start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    show_final_stats(target)

def run_nuclear_all_in_one(target, amount):
    """ᴜsᴇ ᴀʟʟ 5 ᴛᴇᴍᴘʟᴀᴛᴇs + ᴀʟʟ ʀᴇᴄɪᴘɪᴇɴᴛs + ᴛʜʀᴇᴀᴅᴇᴅ"""
    reset_stats()
    target = target.lstrip('@')
    show_attack_art(target, amount, "ɴᴜᴄʟᴇᴀʀ ᴀʟʟ-ɪɴ-ᴏɴᴇ 💣")

    ALL_TEMPLATES = [DETAILED_REPORT, SHORT_REPORT, DSA_LEGAL_NOTICE, NCMEC_REPORT, INTERPOL_NOTICE]
    ALL_RECIPIENTS = TG_EMAILS

    lock = threading.Lock()

    def nuclear_batch(batch_num, start, end):
        for i in range(start, end):
            template = ALL_TEMPLATES[i % len(ALL_TEMPLATES)]
            message = inject_data(template, target)
            subjects = [
                f"URGENT DSA NOTICE — @{target} — DSA-{random.randint(100000,999999)}",
                f"NCMEC CYBERTIP — CSAM @{target} — MANDATORY ACTION",
                f"INTERPOL NOTICE IC-{random.randint(100000,999999)} — @{target}",
                f"FORMAL LEGAL COMPLAINT — @{target} — {datetime.now().strftime('%d %b %Y')}",
                f"CRITICAL ABUSE REPORT — @{target} — IMMEDIATE ACTION"
            ]
            subject = random.choice(subjects)
            success, recipient, sender = send_email(target, subject, message, ALL_RECIPIENTS)

            with lock:
                if success:
                    stats["email_sent"] += 1
                    print(f"{G}  [💣{batch_num}|{i:03d}] ✓ {recipient[:20]}...{RESET}")
                else:
                    stats["email_failed"] += 1
                    print(f"{R}  [💣{batch_num}|{i:03d}] ✗ ғᴀɪʟᴇᴅ{RESET}")
                stats["total"] += 1

            if i % 5 == 0:
                web_hits = send_web_report(target, message)
                with lock:
                    stats["web_sent"] += web_hits

            time.sleep(random.uniform(0.8, 2.0))

    threads = []
    batch_size = max(1, amount // 4)
    for i in range(4):
        start = i * batch_size + 1
        end = start + batch_size if i < 3 else amount + 1
        t = threading.Thread(target=nuclear_batch, args=(i+1, start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    show_final_stats(target)

def run_multi_target(targets, amount_per_target):
    print(f"""
{B}{BOLD}  {'='*52}
{B}  ┌─「 🎯 ᴍᴜʟᴛɪ-ᴛᴀʀɢᴇᴛ ʙᴀɴ 」
{B}  ├─❏ ᴛᴀʀɢᴇᴛs    : {W}{len(targets)}
{B}  ├─❏ ᴘᴇʀ ᴛᴀʀɢᴇᴛ : {W}{amount_per_target}
{B}  └─❏ ᴛᴏᴛᴀʟ      : {W}{len(targets) * amount_per_target}
{B}  {'='*52}{RESET}
""")
    for idx, target in enumerate(targets, 1):
        print(f"\n{C}  [{idx}/{len(targets)}] ▶ @{target.lstrip('@')}{RESET}\n")
        run_standard_ban(target, amount_per_target)
        if idx < len(targets):
            print(f"\n{Y}  ⏳ ᴡᴀɪᴛɪɴɢ 30s...{RESET}")
            time.sleep(30)

# ═══════════════════════════════════════════════════════════════════
# ᴍᴀɪɴ
# ═══════════════════════════════════════════════════════════════════

def main():
    if not authenticate():
        sys.exit(0)

    banner()

    while True:
        print_menu()
        choice = get_input("  ᴇɴᴛᴇʀ ᴄʜᴏɪᴄᴇ →", Y)

        if choice == "0":
            print(f"\n{Y}  sᴛᴀʏ ᴅᴀʀᴋ. ʜɪᴛ ᴄʟᴇᴀɴ. 😈👑{RESET}\n")
            sys.exit(0)

        elif choice in ["1", "2", "3"]:
            banner()
            entity_map = {"1": "ᴜsᴇʀ", "2": "ᴄʜᴀɴɴᴇʟ", "3": "ɢʀᴏᴜᴘ"}
            target = get_target()
            if not target: continue
            amount = get_amount(200)
            if not amount: continue
            run_standard_ban(target, amount, entity_map[choice])
            input(f"\n{C}  ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "4":
            banner()
            target = get_target()
            if not target: continue
            amount = get_amount(50)
            if not amount: continue
            run_dsa_nuclear(target, amount)
            input(f"\n{C}  ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "5":
            banner()
            target = get_target()
            if not target: continue
            amount = get_amount(500)
            if not amount: continue
            confirm = get_input(f"{R}  ᴀʀᴇ ʏᴏᴜ sᴜʀᴇ? (ʏᴇs/ɴᴏ) →{RESET}", R)
            if confirm.lower() != "yes":
                print(f"{Y}  ᴄᴀɴᴄᴇʟʟᴇᴅ.{RESET}")
                continue
            run_email_flood(target, amount)
            input(f"\n{C}  ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "6":
            banner()
            target = get_target()
            if not target: continue
            amount = get_amount(50)
            if not amount: continue
            run_ncmec_nuclear(target, amount)
            input(f"\n{C}  ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "7":
            banner()
            target = get_target()
            if not target: continue
            amount = get_amount(30)
            if not amount: continue
            run_interpol_notice(target, amount)
            input(f"\n{C}  ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "8":
            banner()
            print(f"{Y}  ᴄᴜsᴛᴏᴍ ʀᴇᴘᴏʀᴛ ᴍᴏᴅᴇ{RESET}\n")
            target = get_target()
            if not target: continue
            print(f"\n{C}  sᴇʟᴇᴄᴛ ᴛᴇᴍᴘʟᴀᴛᴇ:")
            print(f"  {W}[1] ᴅᴇᴛᴀɪʟᴇᴅ ʀᴇᴘᴏʀᴛ")
            print(f"  {W}[2] sʜᴏʀᴛ ʀᴇᴘᴏʀᴛ")
            print(f"  {W}[3] ᴅsᴀ ʟᴇɢᴀʟ ɴᴏᴛɪᴄᴇ")
            print(f"  {W}[4] ɴᴄᴍᴇᴄ ᴄʏʙᴇʀᴛɪᴘ")
            print(f"  {W}[5] ɪɴᴛᴇʀᴘᴏʟ ɴᴏᴛɪᴄᴇ{RESET}")
            rc = get_input("  ᴄʜᴏɪᴄᴇ →", Y)
            if rc not in ["1","2","3","4","5"]:
                print(f"{R}  ɪɴᴠᴀʟɪᴅ{RESET}")
                continue
            amount = get_amount(100)
            if not amount: continue
            run_standard_ban(target, amount)
            input(f"\n{C}  ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "9":
            banner()
            targets = []
            while True:
                t = get_input(f"  ᴛᴀʀɢᴇᴛ #{len(targets)+1} (ᴏʀ 'ᴅᴏɴᴇ') →", Y)
                if t.lower() == "done": break
                if t: targets.append(t)
            if not targets:
                print(f"{R}  ɴᴏ ᴛᴀʀɢᴇᴛs{RESET}")
                continue
            amount = get_amount(100)
            if not amount: continue
            run_multi_target(targets, amount)
            input(f"\n{C}  ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "10":
            banner()
            print(f"{R}{BOLD}  💣 ɴᴜᴄʟᴇᴀʀ ᴀʟʟ-ɪɴ-ᴏɴᴇ — ᴍᴀxɪᴍᴜᴍ ᴅᴀᴍᴀɢᴇ{RESET}\n")
            target = get_target()
            if not target: continue
            amount = get_amount(300)
            if not amount: continue
            confirm = get_input(f"{R}  ᴄᴏɴғɪʀᴍ ɴᴜᴄʟᴇᴀʀ ᴀᴛᴛᴀᴄᴋ? (ʏᴇs/ɴᴏ) →{RESET}", R)
            if confirm.lower() != "yes":
                print(f"{Y}  ᴄᴀɴᴄᴇʟʟᴇᴅ.{RESET}")
                continue
            run_nuclear_all_in_one(target, amount)
            input(f"\n{C}  ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "11":
            print(f"""
{C}  ┌─「 📊 sᴇssɪᴏɴ sᴛᴀᴛɪsᴛɪᴄs 」
{C}  ├─❏ 📧 ᴇᴍᴀɪʟ sᴇɴᴛ    : {G}{stats.get('email_sent', 0)}
{C}  ├─❏ 📧 ᴇᴍᴀɪʟ ғᴀɪʟᴇᴅ  : {R}{stats.get('email_failed', 0)}
{C}  ├─❏ 🌐 ᴡᴇʙ ʜɪᴛs     : {G}{stats.get('web_sent', 0)}
{C}  ├─❏ 🔄 ᴛᴏᴛᴀʟ ʀᴏᴜɴᴅs  : {W}{stats.get('total', 0)}
{C}  ├─❏ 📨 sᴍᴛᴘ ᴀᴄᴄᴏᴜɴᴛs : {W}{len(SMTP_ACCOUNTS)}
{C}  ├─❏ 📬 ᴛɢ ᴇᴍᴀɪʟs    : {W}{len(TG_EMAILS)}
{C}  └─❏ 📝 ᴛᴇᴍᴘʟᴀᴛᴇs    : {W}5
{RESET}""")
            input(f"\n{C}  ᴘʀᴇss ᴇɴᴛᴇʀ...{RESET}")
            banner()

        elif choice == "12":
            print(f"""
{M}  ┌─「 ⚙️ sᴇᴛᴛɪɴɢs 」
{M}  ├─❏ ᴏᴡɴᴇʀ         : {W}{OWNER}
{M}  ├─❏ ᴄʜᴀɴɴᴇʟ       : {W}{CHANNEL}
{M}  ├─❏ ᴠᴇʀsɪᴏɴ       : {W}{VERSION}
{M}  ├─❏ sᴍᴛᴘ ᴘᴏʀᴛs   : {W}587 ᴛʟs / 465 ssl
{M}  ├─❏ ᴛʜʀᴇᴀᴅs       : {W}4 (ɴᴜᴄʟᴇᴀʀ) / 3 (ғʟᴏᴏᴅ)
{M}  ├─❏ ᴡᴇʙ ᴇɴᴅᴘᴏɪɴᴛs: {W}{len(WEB_ENDPOINTS)}
{M}  └─❏ ᴍᴇᴛʜᴏᴅ       : {W}ᴇᴍᴀɪʟ + ᴡᴇʙ + ᴛʜʀᴇᴀᴅᴇᴅ
{RESET}""")
            input(f"\n{C}  ᴘʀᴇss ᴇɴᴛᴇʀ...{RESET}")
            banner()

        else:
            print(f"{R}  [!] ɪɴᴠᴀʟɪᴅ ᴄʜᴏɪᴄᴇ{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Y}  sᴛᴀʏ ᴅᴀʀᴋ. ʜɪᴛ ᴄʟᴇᴀɴ. 😈👑{RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{R}  [!] ᴇʀʀᴏʀ: {str(e)}{RESET}\n")
        sys.exit(1)
