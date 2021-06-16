from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from WebStreamer.bot import StreamBot
from WebStreamer.utils.custom_filters import user_check

PMTEXT = """
Hi, {} !!\n\n
<i>I'm File streamer Bot</i>\n
<b>Click on the below buttons to learn more</b>\n
<b>WARNING:</b> <b>NSFW Content will lead to ban.</b>
"""

HELPTEXT = "Just Send or Forward me any file or media, I'll give you a direct download link for it !"

ABOUT = """
Hi there i'm an advanced and fast file streamer bot !
I can give you temporary downloading links !
I'm currently hosted on Heruko !\n
You can Contact My devs or if you need any help or find any bugs at @DivideProjectsDiscussion\n\n
Thanks for using it !!
 """


@StreamBot.on_message(
    filters.command("start") & filters.private & ~filters.edited & user_check,
)
async def start(_, m: Message):
    await m.reply_text(
        text=PMTEXT.format(m.chat.first_name),
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Group",
                        url="https://t.me/DivideProjectsDiscussion",
                    ),
                    InlineKeyboardButton("Channel", url="https://t.me/DivideProjects"),
                ],
                [
                    InlineKeyboardButton("About Me", callback_data="aboutbot"),
                    InlineKeyboardButton("Help", callback_data="helptext"),
                ],
            ],
        ),
    )


@StreamBot.on_message(
    filters.command("help") & filters.private & ~filters.edited & user_check,
)
async def help_handler(_, m: Message):
    await m.reply_text(
        "<i>Send or Forward me any file or media, I'll give you a direct download link for it!</i>",
        parse_mode="HTML",
    )


@StreamBot.on_callback_query()
async def button(_, cmd: CallbackQuery):
    cb_data = cmd.data
    if "aboutbot" in cb_data:
        await cmd.message.edit(
            text=ABOUT,
            parse_mode="MARKDOWN",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Go to Home", callback_data="gotohome"),
                        InlineKeyboardButton("Help", callback_data="helptext"),
                    ],
                ],
            ),
        )
    elif "helptext" in cb_data:
        await cmd.message.edit(
            text=HELPTEXT,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("About Me", callback_data="aboutbot"),
                        InlineKeyboardButton("Back", callback_data="gotohome"),
                    ],
                ],
            ),
        )
    elif "gotohome" in cb_data:
        await cmd.message.edit(
            text=PMTEXT.format(cmd.message.chat.first_name),
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Support Group",
                            url="https://t.me/DivideProjectsDiscussion",
                        ),
                        InlineKeyboardButton(
                            "Channel",
                            url="https://t.me/DivideProjects",
                        ),
                    ],
                    [
                        InlineKeyboardButton("About Me", callback_data="aboutbot"),
                        InlineKeyboardButton("Help", callback_data="helptext"),
                    ],
                ],
            ),
        )
    await cmd.answer()
