from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from WebStreamer.bot import StreamBot
from WebStreamer.db.users import Users
from WebStreamer.utils.ikb import ikb

PMTEXT = """
Hi {}!
I'm File streamer Bot!

<i>Click on the below buttons to learn more!</i>

<b><u>WARNING:</u></b> <i>NSFW content will lead to ban!</i>
"""

HELPTEXT = """
<b>Commands:</b>
/start: <i>Start the bot.</i>
/help: <i>Show this message again.</i>
/expire: <i>Set the expire time for your links. Available unites: m/h/d/w. Example: 5d for 5 days</i>
/mylinks: <i>Get a list of your links and a command to delete them.</i>

Just Send or Forward me any file or media, I'll give you a direct download link for it!
"""

ABOUT = """
Hi there, I'm an Advanced and Fast File Streamer Bot! Made with love from @DivideSupport using pyrogram :)

<b><u>Here are the few questions that are answered:</u></b>

<b>1) The direct link given by me is valid for how much time ?</b>
<u>Ans</u>) <i>The direct link to telegram files are valid for upto 24 hours!</i>

<b>2) How to use me ?</b>
<u>Ans</u>) <i>Read /help and if you get some issues join @DivideSupport and tell what issues are you facing to use me :)</i>

<b>3) Is NSFW allowed ?</b>
<u>Ans</u>) <i>NOOOOOOO !!</i>

<b>4) You want to contact support for something ?</b>
<u>Ans</u>) <i>You can Contact My devs or if you need any help or found any bugs report it at @DivideSupport asap !</i>

<i><u>Atlast, Thanks for using me!!</u></i>
"""


@StreamBot.on_message(filters.command("start") & filters.private)
async def start(_, m: Message):
    """
    Start the bot
    :param _: pyrogram.Client
    :param m: pyrogram.types.Message
    """
    await Users().user_exists(m.from_user.id)
    return await m.reply_text(
        text=PMTEXT.format(m.from_user.mention),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=ikb(
            [
                [
                    ("Support Group", "https://t.me/DivideSupport", "url"),
                    ("Channel", "https://t.me/DivideProjects", "url"),
                ],
            ],
        ),
    )


@StreamBot.on_message(filters.command("help") & filters.private)
async def help_handler(_, m: Message):
    """
    Help message handler
    :param _: pyrogram.Client
    :param m: pyrogram.types.Message
    """
    return await m.reply_text(
        HELPTEXT,
        parse_mode=ParseMode.HTML,
    )
