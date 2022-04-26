# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae

import os
import re
import shutil
import asyncio
import subprocess

from pyrogram.errors import FloodWait
from unzipper.helpers_nexa.database import get_upload_mode
from config import Config


# To get video duration and thumbnail
async def run_shell_cmds(command):
    run = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    shell_ouput = run.stdout.read()[:-1].decode("utf-8")
    return shell_ouput

# Send file to a user
async def send_file(unzip_bot, c_id, doc_f, query, full_path):
    try:
        cum = await get_upload_mode(c_id)
        # Checks if url file size is bigger than 2GB (Telegram limit)
        u_file_size = os.stat(doc_f).st_size
        if Config.TG_MAX_SIZE < int(u_file_size):
            return await unzip_bot.send_message(
                chat_id=c_id,
                text="`حجم الملف كبير جدًا بحيث لا يمكن إرساله في تيلكرام!` \n\n**آسف ، لكن لا يمكنني فعل أي شيء حيال هذا لأنه تقييد بتليكرام 😔!**"
            )
        if cum == "video":
            vid_duration = await run_shell_cmds(f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {doc_f}")
            thmb_pth = f"Dump/thumbnail_{os.path.basename(doc_f)}.jpg"
            if os.path.exists(thmb_pth):
                os.remove(thmb_pth)
            thumb = await run_shell_cmds(f"ffmpeg -i {doc_f} -ss 00:00:01.000 -vframes 1 {thmb_pth}")
            await unzip_bot.send_video(chat_id=c_id, video=doc_f, caption="**تم استخراج بواسطة: @unzipunrarprobot**", duration=int(vid_duration) if vid_duration.isnumeric() else 0, thumb=str(thumb))
        else:
            await unzip_bot.send_document(chat_id=c_id, document=doc_f, caption="**تم استخراج بواسطة: @unzipunrarprobot**")
        os.remove(doc_f)
    except FloodWait as f:
        asyncio.sleep(f.x)
        return send_file(c_id, doc_f)
    except FileNotFoundError:
        await query.answer("آسف! لا يمكنني العثور على هذا الملف", show_alert=True)
    except BaseException:
        shutil.rmtree(full_path)


# Function to remove basic markdown characters from a string
async def rm_mark_chars(text: str):
    return re.sub("[*`_]", "", text)


# Function to answer queries
async def answer_query(query, message_text: str, answer_only: bool = False, unzip_client = None):
    try:
        if answer_only:
            await query.answer(await rm_mark_chars(message_text), show_alert=True)
        else:
            await query.message.edit(message_text)
    except:
        if unzip_client:
            await unzip_client.send_message(chat_id=query.message.chat.id, text=message_text)
