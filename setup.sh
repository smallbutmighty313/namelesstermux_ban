#!/bin/bash
# ɴᴀᴍᴇʟᴇss ʙᴀɴ ᴛᴏᴏʟ — ᴀᴜᴛᴏ sᴇᴛᴜᴘ
# ᴏᴡɴᴇʀ: @nameless_himself

echo "
 ɴᴀᴍᴇʟᴇss ʙᴀɴ ᴛᴏᴏʟ — sᴇᴛᴜᴘ
 ᴏᴡɴᴇʀ: @nameless_himself
"

echo "[*] ᴜᴘᴅᴀᴛɪɴɢ ᴘᴀᴄᴋᴀɢᴇs..."
pkg update -y && pkg upgrade -y

echo "[*] ɪɴsᴛᴀʟʟɪɴɢ ᴅᴇᴘᴇɴᴅᴇɴᴄɪᴇs..."
pkg install -y python git

echo "[*] ɪɴsᴛᴀʟʟɪɴɢ ᴘʏᴛʜᴏɴ ᴘᴀᴄᴋᴀɢᴇs..."
pip install requests colorama --break-system-packages -q

echo ""
echo "[✅] sᴇᴛᴜᴘ ᴄᴏᴍᴘʟᴇᴛᴇ!"
echo "[*] ʀᴜɴ ᴡɪᴛʜ: python nameless_ban.py"
echo ""