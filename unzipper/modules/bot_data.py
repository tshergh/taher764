# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Inline buttons
class Buttons:
    START_BUTTON = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("مساعدة | help 📜", callback_data="helpcallback"),
                InlineKeyboardButton("حول | about ⁉️", callback_data="aboutcallback")
            ]
        ])
    
    CHOOSE_E_F__BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("استخراج الملف|extract file 📂", callback_data="extract_file|tg_file|no_pass"),
            ],
            [
                InlineKeyboardButton("استخراج ملف |extract file password📁", callback_data="extract_file|tg_file|with_pass")
            ],
            [
                InlineKeyboardButton("إلغاء (cancel)❌", callback_data="cancel_dis")
            ]
        ])

    CHOOSE_E_U__BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🔗 استخراج عنوان URL 📂", callback_data="extract_file|url|no_pass"),
            ],
            [
                InlineKeyboardButton("🔗 (كلمة المرور) استخراج عنوان URL 📂", callback_data="extract_file|url|with_pass")
            ],
            [
                InlineKeyboardButton("إلغاء (cancel)❌", callback_data="cancel_dis")
            ]
        ])

    CLN_BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("تنظيف ملفاتي (clean files)😇", callback_data="cancel_dis")
            ],
            [
                InlineKeyboardButton("لا تنظف no clean", callback_data="nobully")
            ]
        ])
    
    ME_GOIN_HOME = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("رجوع (Back)🏡", callback_data="megoinhome")
            ]
        ])

    SET_UPLOAD_MODE_BUTTONS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("كمستند (doc) 📄", callback_data="set_mode|doc")
            ],
            [
                InlineKeyboardButton("كفيديو (video) 📹 ", callback_data="set_mode|video")
            ]
        ])


class Messages:
    START_TEXT = """
 مرحبًا {} ، أنا بوت فك ضغط عن ملفات 😇🗂!
`يمكنني استخراج أرشيفات مثل zip و rar و tar إلخ.`

𝐇𝐈 𝐈 𝐁𝐎𝐓 𝐃𝐄𝐂𝐎𝐌𝐏𝐑𝐄𝐒𝐒 𝐅𝐈𝐋𝐄𝐒 😇
`𝙸 𝙲𝙰𝙽 𝙴𝚇𝚃𝚁𝙰𝙲𝚃 𝙰𝚁𝙲𝙷𝙸𝚅𝙴𝚂 𝙻𝙸𝙺𝙴 𝚉𝙸𝙿, 𝚁𝙰𝚁, 𝚃𝙰𝚁 𝙴𝚃𝙲.`

**Dev&Eng: @ta_ja199 👨🏻‍💻**
[⭐️ تقييم البوت |Rate bot⭐️](https://t.me/tlgrmcbot?start=unzipunrarprobot-review)
    """

    HELP_TXT = """
**كيف تستخرج؟ 🤔**

`1. أرسل الملف أو الرابط الذي تريد استخراجه.`
`2. انقر فوق الزر "استخراج" (إذا قمت بإرسال ارتباط ، فاستخدم الزر "استخراج عنوان URL". إذا كان ملفًا ، استخدم الزر "استخراج ملف").`

**كيف تغير وضع التحميل؟ 🤔**
 `أرسل` **/mode** `الأمر إلى الروبوت. يمكنك تغيير وضع التحميل من هناك.`

**ملاحظة:**
    **1.** `إذا كان أرشيفك محميًا بكلمة مرور ، حدد` **(كلمة المرور) استخراج 📂** `الوضع. البوت ما يعلم الغيب🙄 لمعرفة كلمة مرور ملفك ، لذا إذا حدث هذا ، فما عليك سوى إرسال كلمة المرور هذه!`
    
    **2.** `من فضلك لا ترسل ملفات تالفة! إذا قمت بإرسال واحد عن طريق الخطأ فقط أرسل أمر ` **/clean** 
    
    **3.** `إذا كان الأرشيف الخاص بك يحتوي على 95 ملفًا أو أكثر ، فلن يتمكن برنامج الروبوت من إظهار جميع الملفات المستخرجة للاختيار من بينها. لذلك في هذه الحالة ، إذا لم تتمكن من رؤية ملفك في الأزرار ، فما عليك سوى النقر فوق` "تحميل الكل ♻️" `زر. سيرسل لك جميع الملفات المستخرجة!`

**How To Extract? 🤔**
`1. Send the file or link that you want to extract.`
`2. Click on extract button (If you sent a link use "Url Extract" button. If it's a file just use "File Extract" button).`
**How To Change Upload Mode? 🤔**
 `Send` **/mode** `command to the bot. You can change upload mode from there.`
**Note:**
    **1.** `If your archive is password protected select` **(Password) Extract 📂** `mode. Bot isn't a GOD to know your file's password so If this happens just send that password!`
    
    **2.** `Please don't send corrupted files! If you sent a one by a mistake just send` **/clean** `command!`
    
    **3.** `If your archive have 95 or more files in it then bot can't show all of extracted files to select from. So in that case if you can't see your file in the buttons just click on` "Upload All ♻️" `button. It'll send all extracted files to you!`  
 """

    ABOUT_TXT = """
**حول بوت فك الضغط**
**About the decompression bot**

**🤖 Bot(البوت)**
✘ **Name(أسم):** ZIP & RAR EXTRACTOR
✘ **Username(معرف):** @unzipunrarprobot
✘ **Version(إلإصدار):** 2.5
 
 
**👤 Developer(المطور)**
✘ **Name(أسم ):** Taher Alnoori (طاهر النوري)
✘ **Username(معرف):** @ta_ja199 
✘ **Instagram(انستا)🎛:**[Click here | إضغط  هنا] (https://www.instagram.com/ta_9_ja/)
✘ **Website(موقع)🌐:**[Click here | إضغط  هنا](https://electrical-engineer-cc40b.web.app)


✘ **⭐️ تقييم البوت ⭐️:** [⭐️Rate⭐️](https://t.me/tlgrmcbot?start=unzipunrarprobot-review)
✘ **قناة البوت:** [channal dev taher](https://t.me/engineering_electrical9)
✘ **موقع بوت:** [website dev taher](https://electrical-engineer-cc40b.web.app/)
✘ **استفسار ودعم:** [dev Taher](https://t.me/ta_ja199)
**Made with ❤️ by Dev&Eng:- @ta_ja199**
    """

    LOG_TXT = """
**Extract Log 📝!**

**User ID:** `{}`
**File Name:** `{}`
**File Size:** `{}`
    """

    AFTER_OK_DL_TXT = """
**تم التنزيل بنجاح**
**𝓓𝓞𝓦𝓝𝓛𝓞𝓐𝓓𝓔𝓓 𝓢𝓤𝓒𝓒𝓔𝓢𝓢𝓕𝓤𝓛𝓛𝓨**

**Download time(وقت التحميل):** `{}`
**Status(الحالة):** `محاولة استخراج الأرشيف`
    """

    EXT_OK_TXT = """
**تم الاستخراج بنجاح!**
**𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙴𝚇𝚃𝚁𝙰𝙲𝚃𝙴𝙳!**

**Extraction time(وقت الاستخراج:):** `{}`
**الحالة:** `في محاولة لتحميل`
    """

    EXT_FAILED_TXT = """
**فشل الاستخراج 😕!**
**EXTRACTION FAILED 😕!**

**ما يجب القيام به؟**

 - `يرجى التأكد من عدم تلف الأرشيف`
 - `يرجى التأكد من تحديد الوضع الصحيح!`
 - `قد يكون تنسيق الأرشيف الخاص بك غير مدعوم 😔`
 
**what should be done?**

  - `Please make sure the archive is not damaged`
  - `Please make sure you select the correct mode!`
  - `Your archive format may not be supported 😔`
  
**report: @ta_ja199 **
    """

    ERROR_TXT = """
**حدث خطا**

**ERROR:** {}


**report: @ta_ja199 **
    """

    CANCELLED_TXT = """
**{} ✅!**

`الآن تم حذف جميع ملفاتك من خادمي 😏!`
`𝑁𝑂𝑊 𝐴𝐿𝐿 𝑌𝑂𝑈𝑅 𝐹𝐼𝐿𝐸𝑆 𝐻𝐴𝑉𝐸 𝐵𝐸𝐸𝑁 𝐷𝐸𝐿𝐸𝑇𝐸𝐷 𝐹𝑅𝑂𝑀 𝑀𝑌 𝑆𝐸𝑅𝑉𝐸𝑅 😏!`
   
   """

    CLEAN_TXT = """
**هل تريد بالتأكيد حذف ملفاتك من خادمي 🤔؟**
**𝘈𝘙𝘌 𝘠𝘖𝘜 𝘚𝘜𝘙𝘌 𝘠𝘖𝘜 𝘞𝘈𝘕𝘛 𝘛𝘖 𝘋𝘌𝘓𝘌𝘛𝘌 𝘠𝘖𝘜𝘙 𝘍𝘐𝘓𝘌𝘚 𝘍𝘙𝘖𝘔 𝘔𝘠 𝘚𝘌𝘙𝘝𝘌𝘙 🤔?**

**ملاحظة:** `لا يمكن التراجع عن هذا الإجراء!`
**Note:** `This action cannot be undone!`
    """

    SELECT_UPLOAD_MODE_TXT = """
`الرجاء تحديد وضع التحميل من خلال النقر على الأزرار أدناه!`
`Please select a download mode by clicking on the buttons below!`

**Current Upload mode is(وضع التحميل الحالي هو):** `{}`
"""
    CHANGED_UPLOAD_MODE_TXT = """
**Successfully changed upload mode to(تم تغيير وضع التحميل بنجاح إلى)** `{}` **✅!**
"""


# List of error messages from p7zip
ERROR_MSGS = [
    "Error",
    "Can't open as archive"
    ]
