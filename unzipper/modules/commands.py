# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae
import os
import asyncio
import re
import shutil
import psutil

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

from .bot_data import Buttons, Messages
from unzipper.helpers_nexa.database import (
    check_user,
    del_user,
    count_users,
    get_users_list,
    # Banned Users db
    add_banned_user,
    del_banned_user,
    count_banned_users,
    get_upload_mode
)
from unzipper.helpers_nexa.unzip_help import humanbytes
from config import Config


# Regex for http/https urls
https_url_regex = ("((http|https)://)(www.)?" +
                   "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                   "{2,256}\\.[a-z]" +
                   "{2,6}\\b([-a-zA-Z0-9@:%" +
                   "._\\+~#?&//=]*)")

# Function to check user status (is banned or not)


@Client.on_message(filters.private)
async def _(_, message: Message):
    await check_user(message)


@Client.on_message(filters.private & filters.command("start"))
async def start_bot(_, message: Message):
    await message.reply_text(text=Messages.START_TEXT.format(message.from_user.mention), reply_markup=Buttons.START_BUTTON, disable_web_page_preview=True)


@Client.on_message(filters.private & filters.command("clean"))
async def clean_ma_files(_, message: Message):
    await message.reply_text(text=Messages.CLEAN_TXT, reply_markup=Buttons.CLN_BTNS)


@Client.on_message(filters.incoming & filters.private & filters.regex(https_url_regex) | filters.document)
async def extract_dis_archive(_, message: Message):
    unzip_msg = await message.reply("`جارٍ المعالجة ⚙️ ...`", reply_to_message_id=message.message_id)
    user_id = message.from_user.id
    download_path = f"{Config.DOWNLOAD_LOCATION}/{user_id}"
    if os.path.isdir(download_path):
        return await unzip_msg.edit("`هناك بالفعل عملية واحدة جارية ، لا ترسل بريدًا عشوائيًا أيها الأحمق 😑🌝!` \n\nهل تريد مسح الملفات من الخادم الخاص بي؟ ثم أرسل فقط **/clean** أمر!")
    if message.text and (re.match(https_url_regex, message.text)):
        await unzip_msg.edit("**ماذا تريد؟**", reply_markup=Buttons.CHOOSE_E_U__BTNS)
    elif message.document:
        await unzip_msg.edit("**ماذا تريد؟**", reply_markup=Buttons.CHOOSE_E_F__BTNS)
    else:
        await unzip_msg.edit("`أصمد! ما الذي يجب علي استخراجه 🙄😳؟`")


# Database Commands
@Client.on_message(filters.private & filters.command(["mode", "setmode"]))
async def set_up_mode_for_user(_, message: Message):
    upload_mode = await get_upload_mode(message.from_user.id)
    await message.reply(Messages.SELECT_UPLOAD_MODE_TXT.format(upload_mode), reply_markup=Buttons.SET_UPLOAD_MODE_BUTTONS)


@Client.on_message(filters.private & filters.command("stats") & filters.user(Config.BOT_OWNER))
async def send_stats(_, message: Message):
    stats_msg = await message.reply("`جارٍ المعالجة ⚙️ ...`")
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await count_users()
    total_banned_users = await count_banned_users()
    await stats_msg.edit(f"""
**💫 احصائيات البوت الحالية 💫**

**👥 Users:** 
 ↳**المستخدمون في قاعدة البيانات:** `{total_users}`
 ↳**إجمالي المستخدمين المحظورين:** `{total_banned_users}`


**💾 استخدام القرص ،**
 ↳**Total Disk Space(مساحة قرص) :** `{total}`
 ↳**Used(مستخدم):** `{used}({disk_usage}%)`
 ↳**Free(مجاني):** `{free}`


**🎛 Hardware Usage(استخدام الأجهزة):-**
 ↳**CPU Usage(استخدام المعالج):** `{cpu_usage}%`
 ↳**RAM Usage(استخدام الرام):** `{ram_usage}%`"""
                         )


async def _do_broadcast(message, user):
    try:
        await message.copy(chat_id=int(user))
        return 200
    except FloodWait as e:
        asyncio.sleep(e.x)
        return _do_broadcast(message, user)
    except Exception:
        await del_user(user)


@Client.on_message(filters.private & filters.command("broadcast") & filters.user(Config.BOT_OWNER))
async def broadcast_dis(_, message: Message):
    bc_msg = await message.reply("`جارٍ المعالجة ⚙️ ...`")
    r_msg = message.reply_to_message
    if not r_msg:
        return await bc_msg.edit("`الرد على رسالة للبث!`")
    users_list = await get_users_list()
    # trying to broadcast
    await bc_msg.edit("`بدأ البث ، قد يستغرق هذا الوقت 🥱!`")
    success_no = 0
    failed_no = 0
    total_users = await count_users()
    for user in users_list:
        b_cast = await _do_broadcast(message=r_msg, user=user["user_id"])
        if b_cast == 200:
            success_no += 1
        else:
            failed_no += 1
    await bc_msg.edit(f"""
**اكتمل البث ✅!**

**إجمالي المستخدمين:** `{total_users}`
**الردود الناجحة:** `{success_no}`
**الردود الفاشلة:** `{failed_no}`
    """)


@Client.on_message(filters.private & filters.command("ban") & filters.user(Config.BOT_OWNER))
async def ban_user(_, message: Message):
    ban_msg = await message.reply("`جارٍ المعالجة ⚙️ ...`")
    try:
        user_id = message.text.split(None, 1)[1]
    except:
        return await ban_msg.edit("`أعط معرف المستخدم للحظر!`")
    await add_banned_user(user_id)
    await ban_msg.edit(f"**تم حظر هذا المستخدم بنجاح ✅** \n\n**معرف:** `{user_id}`")


@Client.on_message(filters.private & filters.command("unban") & filters.user(Config.BOT_OWNER))
async def unban_user(_, message: Message):
    unban_msg = await message.reply("`جارٍ المعالجة ⚙️ ...`")
    try:
        user_id = message.text.split(None, 1)[1]
    except:
        return await unban_msg.edit("`إعطاء معرف المستخدم لألغاء حظر`")
    await del_banned_user(user_id)
    await unban_msg.edit(f"**تم بنجاح إلغاء حظر هذا المستخدم ✅** \n\n**معرف:** `{user_id}`")
