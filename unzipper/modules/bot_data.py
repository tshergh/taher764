# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Inline buttons
class Buttons:
    START_BUTTON = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("مساعدة 📜", callback_data="helpcallback"),
                InlineKeyboardButton("حول ⁉️", callback_data="aboutcallback")
            ]
        ])
    
    CHOOSE_E_F__BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("استخراج الملف 📂", callback_data="extract_file|tg_file|no_pass"),
            ],
            [
                InlineKeyboardButton("ملف (كلمة المرور) استخراج 📂", callback_data="extract_file|tg_file|with_pass")
            ],
            [
                InlineKeyboardButton("إلغاء ❌", callback_data="cancel_dis")
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
                InlineKeyboardButton("إلغاء ❌", callback_data="cancel_dis")
            ]
        ])

    CLN_BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("تنظيف ملفاتي 😇", callback_data="cancel_dis")
            ],
            [
                InlineKeyboardButton("لا تنظف", callback_data="nobully")
            ]
        ])
    
    ME_GOIN_HOME = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("رجوع 🏡", callback_data="megoinhome")
            ]
        ])

    SET_UPLOAD_MODE_BUTTONS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("كما دوك 📁", callback_data="set_mode|doc")
            ],
            [
                InlineKeyboardButton("كفيديو 📹", callback_data="set_mode|video")
            ]
        ])


class Messages:
    START_TEXT = """
 🗂مرحبًا {} ، أنا بوت فك ضغط عن ملفات 😇!
`يمكنني استخراج أرشيفات مثل zip و rar و tar إلخ.`

**Made with ❤️ by Dev&Eng: @ta_ja199 👨🏻‍💻**
[⭐️ تقييم البوت ⭐️](https://t.me/tlgrmcbot?start=unzipunrarprobot-review)
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
    """

    ABOUT_TXT = """
**About Nexa Unzipper Bot,**

✘ **قناة البوت:** [channal dev taher](https://t.me/engineering_electrical9)
✘ **موقع بوت:** [website dev taher](https://electrical-engineer-cc40b.web.app/)
✘ **استفسار ودعم:** [dev Taher](https://t.me/ta_ja199)
✘ **⭐️ تقييم البوت ⭐️:** [⭐️Rate⭐️](https://t.me/tlgrmcbot?start=unzipunrarprobot-review)


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

**Download time(وقت التحميل):** `{}`
**Status(الحالة):** `محاولة استخراج الأرشيف`
    """

    EXT_OK_TXT = """
**تم الاستخراج بنجاح!**

**Extraction time(وقت الاستخراج:):** `{}`
**الحالة:** `في محاولة لتحميل`
    """

    EXT_FAILED_TXT = """
**فشل الاستخراج 😕!**

**ما يجب القيام به؟**

 - `يرجى التأكد من عدم تلف الأرشيف`
 - `يرجى التأكد من تحديد الوضع الصحيح!`
 - `قد يكون تنسيق الأرشيف الخاص بك غير مدعوم 😔`

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
    """

    CLEAN_TXT = """
**هل تريد بالتأكيد حذف ملفاتك من خادمي 🤔؟**

**ملاحظة:** `لا يمكن التراجع عن هذا الإجراء!`
    """

    SELECT_UPLOAD_MODE_TXT = """
`الرجاء تحديد وضع التحميل من خلال النقر على الأزرار أدناه!`

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
