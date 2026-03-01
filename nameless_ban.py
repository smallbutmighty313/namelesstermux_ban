#!/usr/bin/env python3
# ɴᴀᴍᴇʟᴇss ʙᴀɴ ᴛᴏᴏʟ 😈👑
# ᴏᴡɴᴇʀ: @nameless_himself
# ᴛᴇʟᴇɢʀᴀᴍ: t.me/nameless_himself

import os
import sys
import random
import time
import json
import re
import urllib.parse
import threading
from datetime import datetime

try:
    import requests
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
except ImportError:
    os.system("pip install requests colorama -q")
    import requests
    from colorama import Fore, Back, Style, init
    init(autoreset=True)

# ═══ ᴄᴏʟᴏʀs ═══
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
M = Fore.MAGENTA
W = Fore.WHITE
B = Fore.BLUE
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT

VERSION = "v1.0"
OWNER = "@nameless_himself"
OWNER_LINK = "t.me/nameless_himself"
CHANNEL = "t.me/namelesstechinc"

TG_ABUSE_EMAILS = [
    "abuse@telegram.org",
    "spam@telegram.org",
    "dmca@telegram.org",
    "support@telegram.org",
    "legal@telegram.org",
    "childabuse@telegram.org",
    "dsa-report@telegram.org",
    "terrorism@telegram.org"
]

WA_BAN_EMAILS = [
    "support@support.whatsapp.com",
    "abuse@support.whatsapp.com",
    "security@support.whatsapp.com",
    "legal@support.whatsapp.com",
    "dmca@support.whatsapp.com",
    "privacy@support.whatsapp.com",
]

WA_APPEAL_EMAILS = [
    "appeals@support.whatsapp.com",
    "support@whatsapp.com",
    "android@support.whatsapp.com",
    "ios@support.whatsapp.com",
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

FAKE_NAMES = [
    "Amina Yusuf", "Tariq Rahman", "Leila Alami", "Diego Morales",
    "Sofia Petrov", "Rajesh Kumar", "Mei Lin Zhao", "Kwame Osei",
    "Chloe Dubois", "Mateo Fernandez", "Nia Thompson", "Arjun Patel",
    "Yara Hassan", "Luca Rossi", "Amara Singh", "Elias Johansson",
    "Hana Kim", "Priya Sharma", "Malik Washington", "Zara Malik",
    "Rafael Costa", "Layla El-Sayed", "Chen Wei", "Dante Rivera",
    "Noor Fatima", "Santiago Vega", "Aisha Baig", "Omar Farooq",
    "Fatima Zahra", "Ibrahim Khalil", "Nadia Rahman", "Jamal Carter",
    "Sana Khan", "Elena Volkov", "Marcus Adebayo", "Ravi Shankar",
    "Camila Ortiz", "Zainab Akhtar", "Maya Reddy", "Amir Hosseini",
]

TG_MESSAGES = [
    """To the Telegram Trust and Safety Team,

I am filing an urgent, high-priority enforcement report against Telegram account @{target} and demanding immediate permanent suspension.

This account is actively engaged in:
— Distribution of child sexual abuse material (CSAM)
— Active terrorist recruitment propaganda
— Coordinated mass phishing attacks stealing banking credentials
— Large-scale investment fraud targeting vulnerable users
— Non-consensual intimate image distribution
— Coordinated harassment campaigns against private individuals

Under the EU Digital Services Act (DSA) Article 16, this report constitutes formal legal notice obligating Telegram to act immediately.

REQUIRED ACTIONS:
1. Immediate permanent account suspension
2. IP address logging and preservation
3. Full user data disclosure to law enforcement
4. Escalation to Telegram legal and compliance team

Regards,
{reporter_name}""",

    """To the Telegram Trust and Safety Team,

URGENT CRIMINAL ENFORCEMENT NOTICE — ACCOUNT @{target}

This account is in active violation of Telegram's Terms of Service, the EU Digital Services Act, international child protection statutes, and criminal law across multiple jurisdictions.

Documented violations:
— Real-time CSAM distribution
— Active terrorist cell coordination
— Mass-scale financial fraud targeting elderly users
— Organized phishing infrastructure impersonating banks
— Graphic violent content distribution
— Coordinated account hijacking operations
— Sexual exploitation of minors

REQUIRED SAME-DAY ACTIONS:
— Permanent account termination
— Full data preservation for law enforcement
— Immediate referral to NCMEC
— Escalation to senior Trust and Safety leadership

Regards,
{reporter_name}""",

    """To Telegram Abuse and Legal Team,

I am formally notifying Telegram of active criminal abuse through account @{target}.

Confirmed violations:
— Large-scale romance scam operations
— Malware and spyware distribution
— Coordinated harassment of minors
— Fake cryptocurrency investment fraud
— Impersonating Telegram staff to steal credentials
— Non-consensual intimate imagery of identifiable victims
— Operating illegal drug trafficking networks

This report serves as formal notice under DSA Article 16.
Immediate enforcement action required.

Regards,
{reporter_name}"""
]

WA_BAN_MESSAGES = [
    """To the WhatsApp Trust and Safety Team,

URGENT CYBERCRIME COMPLAINT — NUMBER {target}

This WhatsApp account is actively engaged in:
— Mass phishing impersonating banks and government portals
— Distribution of child sexual abuse material
— Coordinated account takeover attacks
— Large-scale financial fraud with confirmed victims
— Sextortion targeting minors
— Malware distribution via WhatsApp links

Immediate permanent termination required.
Full data must be preserved for law enforcement.

Regards,
{reporter_name}""",

    """To the WhatsApp Cybercrime Enforcement Team,

FORMAL CRIMINAL COMPLAINT — {target}

This account is part of an organized cybercrime network:
— Industrial phishing stealing banking credentials at scale
— CSAM distribution as exploitation bait
— Social engineering to harvest OTPs and passwords
— Advance-fee fraud with documented victims
— Coordinated harassment and stalking campaigns
— Malware and ransomware distribution

MANDATORY ACTIONS:
1. Immediate permanent ban
2. Number global blacklisting
3. Law enforcement data disclosure
4. NCMEC referral for CSAM

Regards,
{reporter_name}"""
]

WA_APPEAL_MESSAGES = [
    """Dear WhatsApp Trust and Safety Team,

I am formally appealing the ban on WhatsApp account {target}.

This account is my sole means of communication with my family, employer, and emergency contacts. The sudden ban has caused severe disruption to my personal and professional life.

I have never knowingly violated WhatsApp's Terms of Service. I believe this ban resulted from:
— Coordinated false reporting by malicious users
— An automated system error
— Unauthorized access to my account

I respectfully request:
1. Full manual review of my account activity
2. Identification of the specific ban trigger
3. Restoration of access upon confirmation of no wrongdoing

I am fully prepared to cooperate with any verification process.

Sincerely,
{reporter_name}""",

    """Dear WhatsApp Appeals Team,

FORMAL UNBAN APPEAL — ACCOUNT {target}

This account represents my only reliable communication channel with family, including elderly relatives who depend on me, and professional contacts critical to my livelihood.

I have used this account exclusively for lawful personal and professional communication throughout its history. I believe this ban was applied in error due to:
— Coordinated mass false reports from another user
— Automated enforcement misfire without human review
— Possible account compromise I had no knowledge of

I am requesting urgent manual review and account restoration.
I will cooperate fully with any process required.

Respectfully,
{reporter_name}"""
]

DSA_MESSAGES = [
    """FORMAL LEGAL NOTICE UNDER EU DIGITAL SERVICES ACT
REGULATION (EU) 2022/2065 — ARTICLE 16 & ARTICLE 17

Date: {date}
Reference: DSA-{ref_id}
Submitted By: {reporter_name}
Platform: Telegram Messenger / Telegram FZ-LLC
Target: {target}

To the Telegram DSA Compliance and Legal Team,

This notice is submitted pursuant to Article 16 of the EU Digital Services Act (Regulation EU 2022/2065), constituting a legally binding complaint requiring mandatory action.

ILLEGAL CONTENT AND APPLICABLE LAW:

1. CHILD SEXUAL ABUSE MATERIAL (CSAM)
   Law: Directive 2011/93/EU Article 5; Budapest Convention Article 9
   Severity: CRITICAL — Mandatory immediate removal

2. TERRORIST CONTENT
   Law: EU TCO Regulation 2021/784 — One-hour removal obligation
   Severity: CRITICAL

3. ORGANIZED FINANCIAL FRAUD
   Law: Directive 2013/40/EU; Directive 2019/713
   Severity: HIGH — Active financial harm to victims

4. COORDINATED HARASSMENT
   Law: Directive 2012/29/EU
   Severity: HIGH

DSA COMPLIANCE OBLIGATIONS:
— Article 16(3): Process this notice in a timely manner
— Article 17: Provide statement of reasons for any decision
— Article 92: Obligations apply EU-wide

NON-COMPLIANCE CONSEQUENCES:
— Fines up to 6% of global annual turnover (DSA Article 74)
— Individual member state enforcement actions
— Criminal referral where platform liability applies

REQUIRED IMMEDIATE ACTIONS:
1. Suspend account/channel/group {target}
2. Preserve all data for law enforcement
3. Refer CSAM to NCMEC
4. Provide written confirmation of actions taken

I confirm this notice is submitted in good faith under DSA Article 16(2)(e).

{reporter_name}
Date: {date}
Reference: DSA-{ref_id}"""
]

stats = {
    "email_sent": 0,
    "email_failed": 0,
    "web_sent": 0,
    "web_failed": 0,
    "total": 0,
    "start_time": None
}

stop_flag = False


def clear():
    os.system("clear" if os.name != "nt" else "cls")


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
{C}┌─「 😈👑 ɴᴀᴍᴇʟᴇss ʙᴀɴ ᴛᴏᴏʟ {VERSION} 」
{C}├─❏ ᴏᴡɴᴇʀ  : {W}{OWNER}
{C}├─❏ ᴄʜᴀɴɴᴇʟ: {W}{CHANNEL}
{C}├─❏ ᴛɪᴍᴇ   : {W}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{C}└─❏ sᴛᴀᴛᴜs : {G}ᴏɴʟɪɴᴇ ✅
{RESET}""")


def print_menu():
    print(f"""
{C}┌─「 📋 ᴍᴀɪɴ ᴍᴇɴᴜ 」
{C}├─❏ {W}[1] {Y}ʙᴀɴ ᴛᴇʟᴇɢʀᴀᴍ ᴜsᴇʀ
{C}├─❏ {W}[2] {Y}ʙᴀɴ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ
{C}├─❏ {W}[3] {Y}ʙᴀɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ
{C}├─❏ {W}[4] {Y}ᴅsᴀ ʟᴇɢᴀʟ ɴᴏᴛɪᴄᴇ (ɴᴜᴄʟᴇᴀʀ 🔥)
{C}├─❏ {W}[5] {Y}ᴡʜᴀᴛsᴀᴘᴘ ᴛᴇᴍᴘ ʙᴀɴ
{C}├─❏ {W}[6] {Y}ᴡʜᴀᴛsᴀᴘᴘ ᴘᴇʀᴍ ʙᴀɴ
{C}├─❏ {W}[7] {Y}ᴡʜᴀᴛsᴀᴘᴘ ᴜɴʙᴀɴ ᴀᴘᴘᴇᴀʟ
{C}├─❏ {W}[8] {R}sᴛᴀᴛs
{C}└─❏ {W}[0] {R}ᴇxɪᴛ
{RESET}""")


def loading_bar(current, total, width=40):
    filled = int(width * current / total)
    bar = "█" * filled + "░" * (width - filled)
    percent = current / total * 100
    return f"{G}[{bar}] {W}{percent:.1f}%{RESET}"


def inject_message(message, target):
    name = random.choice(FAKE_NAMES)
    ref_id = random.randint(100000, 999999)
    date = datetime.now().strftime("%d %B %Y")
    message = message.replace("{target}", target)
    message = message.replace("{reporter_name}", name)
    message = message.replace("{ref_id}", str(ref_id))
    message = message.replace("{date}", date)
    return message


def send_email(target, subject, message, recipients):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    email_acc, pwd = random.choice(SMTP_ACCOUNTS)
    recipient = random.choice(recipients)
    msg = MIMEMultipart()
    msg['From'] = email_acc
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # ᴛʀʏ ᴘᴏʀᴛ 587
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587, timeout=15)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(email_acc, pwd)
        s.sendmail(email_acc, recipient, msg.as_string())
        s.quit()
        return True, recipient
    except:
        pass

    # ғᴀʟʟʙᴀᴄᴋ ᴘᴏʀᴛ 465
    try:
        s = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15)
        s.login(email_acc, pwd)
        s.sendmail(email_acc, recipient, msg.as_string())
        s.quit()
        return True, recipient
    except:
        return False, recipient


def send_web_report_tg(target, message):
    urls = [
        "https://telegram.org/support",
        "https://telegram.org/abuse",
        "https://telegram.org/dsa-report",
        "https://telegram.org/dmca",
    ]
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "TelegramDesktop/4.8.1",
        "Origin": "https://telegram.org",
    }
    success = 0
    for url in urls:
        payload = {
            "peer": target,
            "category": "illegal_content",
            "message": message[:4000]
        }
        try:
            r = requests.post(url, json=payload, headers=headers, timeout=10)
            if r.status_code in (200, 201, 204):
                success += 1
        except:
            pass
    return success


def send_web_report_wa(phone, message):
    text_enc = urllib.parse.quote(message)
    urls = [
        f"https://wa.me/report?phone=12056384830&text={text_enc}",
        "https://transparency.meta.com/forms/abuse/whatsapp",
        "https://www.instagram.com/web/reports/create/",
        "https://www.facebook.com/help/contact/263149623708370",
    ]
    success = 0
    for url in urls:
        try:
            if "transparency" in url:
                requests.post(url, data={"phone": phone.lstrip('+'),
                              "details": message}, timeout=10)
            elif "instagram" in url:
                requests.post(url, json={"entry_point": "web",
                              "phone_number": phone.lstrip('+'),
                              "reason_id": "1"}, timeout=10)
            elif "facebook" in url:
                requests.post(url, data={"phone_number": phone.lstrip('+'),
                              "your_name": random.choice(FAKE_NAMES)}, timeout=10)
            else:
                requests.get(url, timeout=10)
            success += 1
        except:
            pass
    return success


def get_input(prompt, color=C):
    return input(f"{color}{prompt}{RESET} ").strip()


def run_attack_tg(target, amount, mode="user"):
    global stop_flag
    stop_flag = False
    stats["email_sent"] = 0
    stats["email_failed"] = 0
    stats["web_sent"] = 0
    stats["web_failed"] = 0
    stats["total"] = 0
    stats["start_time"] = datetime.now()

    target = target.lstrip('@')

    print(f"\n{M}{'='*55}")
    print(f"{C}┌─「 🔥 ᴀᴛᴛᴀᴄᴋ sᴛᴀʀᴛᴇᴅ 」")
    print(f"{C}├─❏ ᴛᴀʀɢᴇᴛ  : {W}@{target}")
    print(f"{C}├─❏ ᴀᴍᴏᴜɴᴛ  : {W}{amount}")
    print(f"{C}├─❏ ᴍᴏᴅᴇ    : {W}ᴛᴇʟᴇɢʀᴀᴍ {mode}")
    print(f"{C}└─❏ sᴛᴀʀᴛᴇᴅ : {W}{datetime.now().strftime('%H:%M:%S')}")
    print(f"{M}{'='*55}{RESET}\n")

    for i in range(1, amount + 1):
        if stop_flag:
            break

        msg_template = random.choice(TG_MESSAGES)
        msg = inject_message(msg_template, f"@{target}")
        subject = f"URGENT Report - @{target} - DSA Article 16 Notice"

        # ᴇᴍᴀɪʟ
        ok, recipient = send_email(f"@{target}", subject, msg, TG_ABUSE_EMAILS)
        if ok:
            stats["email_sent"] += 1
        else:
            stats["email_failed"] += 1

        # ᴡᴇʙ
        web_ok = send_web_report_tg(target, msg)
        stats["web_sent"] += web_ok

        stats["total"] += 1

        elapsed = (datetime.now() - stats["start_time"]).seconds
        bar = loading_bar(i, amount)

        print(f"\r{bar} {C}[{i}/{amount}] {G}✉ {stats['email_sent']} {R}✗ {stats['email_failed']} {Y}🌐 {stats['web_sent']}{RESET}", end="", flush=True)

        time.sleep(random.uniform(1.5, 3))

    print(f"\n\n{M}{'='*55}")
    print(f"{G}┌─「 ✅ ᴀᴛᴛᴀᴄᴋ ᴄᴏᴍᴘʟᴇᴛᴇ 」")
    print(f"{G}├─❏ ᴛᴀʀɢᴇᴛ     : {W}@{target}")
    print(f"{G}├─❏ 📧 ᴇᴍᴀɪʟ sᴇɴᴛ : {W}{stats['email_sent']}")
    print(f"{G}├─❏ 📧 ᴇᴍᴀɪʟ ғᴀɪʟ : {W}{stats['email_failed']}")
    print(f"{G}├─❏ 🌐 ᴡᴇʙ sᴇɴᴛ  : {W}{stats['web_sent']}")
    print(f"{G}├─❏ ᴛᴏᴛᴀʟ ʀᴏᴜɴᴅs : {W}{stats['total']}")
    elapsed = (datetime.now() - stats["start_time"]).seconds
    print(f"{G}└─❏ ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  : {W}{elapsed}s")
    print(f"{M}{'='*55}{RESET}")
    print(f"\n{Y}⏳ ᴡᴀɪᴛ 1–12 ʜᴏᴜʀs ғᴏʀ ʀᴇᴠɪᴇᴡ. sᴛᴀʏ ᴅᴀʀᴋ 😈{RESET}\n")


def run_dsa_notice(target, amount):
    global stop_flag
    stop_flag = False
    stats["email_sent"] = 0
    stats["email_failed"] = 0
    stats["total"] = 0
    stats["start_time"] = datetime.now()

    target = target.lstrip('@')
    dsa_recipients = ["dsa-report@telegram.org", "legal@telegram.org", "abuse@telegram.org"]

    print(f"\n{R}{BOLD}{'='*55}")
    print(f"{R}┌─「 ⚖️ ᴅsᴀ ʟᴇɢᴀʟ ɴᴏᴛɪᴄᴇ — ɴᴜᴄʟᴇᴀʀ ᴍᴏᴅᴇ 🔥 」")
    print(f"{R}├─❏ ᴛᴀʀɢᴇᴛ  : {W}@{target}")
    print(f"{R}├─❏ ɴᴏᴛɪᴄᴇs : {W}{amount}")
    print(f"{R}└─❏ sᴛᴀᴛᴜs  : {G}ғɪʀɪɴɢ...")
    print(f"{R}{'='*55}{RESET}\n")

    for i in range(1, amount + 1):
        if stop_flag:
            break

        msg_template = random.choice(DSA_MESSAGES)
        msg = inject_message(msg_template, f"@{target}")
        subject = f"FORMAL DSA ARTICLE 16 NOTICE — DSA-{random.randint(100000,999999)} — @{target}"

        ok, recipient = send_email(f"@{target}", subject, msg, dsa_recipients)
        if ok:
            stats["email_sent"] += 1
            print(f"{G}[{i}/{amount}] ✅ ᴅsᴀ ɴᴏᴛɪᴄᴇ → {recipient}{RESET}")
        else:
            stats["email_failed"] += 1
            print(f"{R}[{i}/{amount}] ❌ ғᴀɪʟᴇᴅ → {recipient}{RESET}")

        stats["total"] += 1
        time.sleep(random.uniform(2, 4))

    print(f"\n{G}✅ {stats['email_sent']} ᴅsᴀ ɴᴏᴛɪᴄᴇs sᴇɴᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ʟᴇɢᴀʟ ᴛᴇᴀᴍ{RESET}")
    print(f"{Y}⏳ ᴛᴇʟᴇɢʀᴀᴍ ʜᴀs 72ʜ ᴛᴏ ʀᴇsᴘᴏɴᴅ ᴜɴᴅᴇʀ ᴅsᴀ ʟᴀᴡ 😈{RESET}\n")


def run_attack_wa(phone, amount, mode="ban_perm"):
    global stop_flag
    stop_flag = False
    stats["email_sent"] = 0
    stats["email_failed"] = 0
    stats["web_sent"] = 0
    stats["total"] = 0
    stats["start_time"] = datetime.now()

    is_appeal = "appeal" in mode or "unban" in mode

    if is_appeal:
        messages = WA_APPEAL_MESSAGES
        recipients = WA_APPEAL_EMAILS
        label = "ᴜɴʙᴀɴ ᴀᴘᴘᴇᴀʟ"
        emoji = "🥺"
    else:
        messages = WA_BAN_MESSAGES
        recipients = WA_BAN_EMAILS
        label = "ʙᴀɴ ʀᴇᴘᴏʀᴛ"
        emoji = "🔥"

    print(f"\n{M}{'='*55}")
    print(f"{C}┌─「 {emoji} ᴡʜᴀᴛsᴀᴘᴘ {label} sᴛᴀʀᴛᴇᴅ 」")
    print(f"{C}├─❏ ᴛᴀʀɢᴇᴛ  : {W}{phone}")
    print(f"{C}├─❏ ᴀᴍᴏᴜɴᴛ  : {W}{amount}")
    print(f"{C}└─❏ sᴛᴀʀᴛᴇᴅ : {W}{datetime.now().strftime('%H:%M:%S')}")
    print(f"{M}{'='*55}{RESET}\n")

    for i in range(1, amount + 1):
        if stop_flag:
            break

        msg_template = random.choice(messages)
        msg = inject_message(msg_template, phone)
        subject = f"URGENT WhatsApp {label} — {phone}"

        ok, recipient = send_email(phone, subject, msg, recipients)
        if ok:
            stats["email_sent"] += 1
        else:
            stats["email_failed"] += 1

        web_ok = send_web_report_wa(phone, msg)
        stats["web_sent"] += web_ok
        stats["total"] += 1

        bar = loading_bar(i, amount)
        print(f"\r{bar} {C}[{i}/{amount}] {G}✉ {stats['email_sent']} {R}✗ {stats['email_failed']} {Y}🌐 {stats['web_sent']}{RESET}", end="", flush=True)

        time.sleep(random.uniform(1.5, 3))

    print(f"\n\n{G}┌─「 ✅ {label} ᴄᴏᴍᴘʟᴇᴛᴇ 」")
    print(f"{G}├─❏ 📧 ᴇᴍᴀɪʟ sᴇɴᴛ : {W}{stats['email_sent']}")
    print(f"{G}├─❏ 🌐 ᴡᴇʙ sᴇɴᴛ  : {W}{stats['web_sent']}")
    print(f"{G}├─❏ ᴛᴏᴛᴀʟ ʀᴏᴜɴᴅs : {W}{stats['total']}")
    elapsed = (datetime.now() - stats["start_time"]).seconds
    print(f"{G}└─❏ ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  : {W}{elapsed}s{RESET}\n")


def show_stats():
    print(f"""
{C}┌─「 📊 sᴛᴀᴛs 」
{C}├─❏ 📧 ᴇᴍᴀɪʟ sᴇɴᴛ  : {G}{stats['email_sent']}
{C}├─❏ 📧 ᴇᴍᴀɪʟ ғᴀɪʟᴇᴅ: {R}{stats['email_failed']}
{C}├─❏ 🌐 ᴡᴇʙ sᴇɴᴛ   : {G}{stats['web_sent']}
{C}└─❏ ᴛᴏᴛᴀʟ ʀᴏᴜɴᴅs  : {W}{stats['total']}
{RESET}""")


def main():
    banner()

    while True:
        print_menu()
        choice = get_input("ᴇɴᴛᴇʀ ᴄʜᴏɪᴄᴇ →")

        if choice == "0":
            print(f"\n{Y}sᴛᴀʏ ᴅᴀʀᴋ. ʜɪᴛ ᴄʟᴇᴀɴ. 😈👑{RESET}\n")
            sys.exit(0)

        elif choice == "1":
            banner()
            target = get_input("ᴇɴᴛᴇʀ ᴛᴇʟᴇɢʀᴀᴍ ᴜsᴇʀɴᴀᴍᴇ (ᴡɪᴛʜᴏᴜᴛ @) →")
            if not target:
                print(f"{R}ɪɴᴠᴀʟɪᴅ ᴛᴀʀɢᴇᴛ{RESET}")
                continue
            try:
                amount = int(get_input("ᴇɴᴛᴇʀ ᴀᴍᴏᴜɴᴛ (1–200) →"))
                amount = min(max(amount, 1), 200)
            except:
                print(f"{R}ɪɴᴠᴀʟɪᴅ ᴀᴍᴏᴜɴᴛ{RESET}")
                continue
            run_attack_tg(target, amount, "user")
            input(f"\n{C}ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "2":
            banner()
            target = get_input("ᴇɴᴛᴇʀ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ (ᴡɪᴛʜᴏᴜᴛ @) →")
            if not target:
                continue
            try:
                amount = int(get_input("ᴇɴᴛᴇʀ ᴀᴍᴏᴜɴᴛ (1–200) →"))
                amount = min(max(amount, 1), 200)
            except:
                continue
            run_attack_tg(target, amount, "channel")
            input(f"\n{C}ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "3":
            banner()
            target = get_input("ᴇɴᴛᴇʀ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ (ᴡɪᴛʜᴏᴜᴛ @) →")
            if not target:
                continue
            try:
                amount = int(get_input("ᴇɴᴛᴇʀ ᴀᴍᴏᴜɴᴛ (1–200) →"))
                amount = min(max(amount, 1), 200)
            except:
                continue
            run_attack_tg(target, amount, "group")
            input(f"\n{C}ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "4":
            banner()
            print(f"{R}{BOLD}⚖️ ᴅsᴀ ʟᴇɢᴀʟ ɴᴏᴛɪᴄᴇ — ɴᴜᴄʟᴇᴀʀ ᴍᴏᴅᴇ{RESET}")
            print(f"{Y}ᴛʜɪs sᴇɴᴅs ғᴏʀᴍᴀʟ ᴇᴜ ʟᴇɢᴀʟ ɴᴏᴛɪᴄᴇs ᴅɪʀᴇᴄᴛʟʏ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ's ʟᴇɢᴀʟ ᴛᴇᴀᴍ{RESET}\n")
            target = get_input("ᴇɴᴛᴇʀ ᴛᴀʀɢᴇᴛ ᴜsᴇʀɴᴀᴍᴇ/ᴄʜᴀɴɴᴇʟ (ᴡɪᴛʜᴏᴜᴛ @) →")
            if not target:
                continue
            try:
                amount = int(get_input("ᴇɴᴛᴇʀ ɴᴜᴍʙᴇʀ ᴏғ ɴᴏᴛɪᴄᴇs (1–50) →"))
                amount = min(max(amount, 1), 50)
            except:
                continue
            run_dsa_notice(target, amount)
            input(f"\n{C}ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "5":
            banner()
            phone = get_input("ᴇɴᴛᴇʀ ᴡʜᴀᴛsᴀᴘᴘ ɴᴜᴍʙᴇʀ (ᴡɪᴛʜ +) →")
            if not phone.startswith('+'):
                print(f"{R}ɪɴᴠᴀʟɪᴅ ɴᴜᴍʙᴇʀ. ᴜsᴇ +ᴄᴏᴜɴᴛʀʏᴄᴏᴅᴇ{RESET}")
                continue
            try:
                amount = int(get_input("ᴇɴᴛᴇʀ ᴀᴍᴏᴜɴᴛ (1–400) →"))
                amount = min(max(amount, 1), 400)
            except:
                continue
            run_attack_wa(phone, amount, "ban_temp")
            input(f"\n{C}ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "6":
            banner()
            phone = get_input("ᴇɴᴛᴇʀ ᴡʜᴀᴛsᴀᴘᴘ ɴᴜᴍʙᴇʀ (ᴡɪᴛʜ +) →")
            if not phone.startswith('+'):
                print(f"{R}ɪɴᴠᴀʟɪᴅ ɴᴜᴍʙᴇʀ. ᴜsᴇ +ᴄᴏᴜɴᴛʀʏᴄᴏᴅᴇ{RESET}")
                continue
            try:
                amount = int(get_input("ᴇɴᴛᴇʀ ᴀᴍᴏᴜɴᴛ (1–400) →"))
                amount = min(max(amount, 1), 400)
            except:
                continue
            run_attack_wa(phone, amount, "ban_perm")
            input(f"\n{C}ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "7":
            banner()
            phone = get_input("ᴇɴᴛᴇʀ ᴡʜᴀᴛsᴀᴘᴘ ɴᴜᴍʙᴇʀ (ᴡɪᴛʜ +) →")
            if not phone.startswith('+'):
                print(f"{R}ɪɴᴠᴀʟɪᴅ ɴᴜᴍʙᴇʀ. ᴜsᴇ +ᴄᴏᴜɴᴛʀʏᴄᴏᴅᴇ{RESET}")
                continue
            try:
                amount = int(get_input("ᴇɴᴛᴇʀ ᴀᴍᴏᴜɴᴛ (1–400) →"))
                amount = min(max(amount, 1), 400)
            except:
                continue
            run_attack_wa(phone, amount, "unban_appeal")
            input(f"\n{C}ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        elif choice == "8":
            show_stats()
            input(f"\n{C}ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ...{RESET}")
            banner()

        else:
            print(f"{R}ɪɴᴠᴀʟɪᴅ ᴄʜᴏɪᴄᴇ.{RESET}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Y}sᴛᴀʏ ᴅᴀʀᴋ. ʜɪᴛ ᴄʟᴇᴀɴ. 😈👑{RESET}\n")
        sys.exit(0)