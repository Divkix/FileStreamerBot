from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from WebStreamer.utils.ikb import ikb
from WebStreamer.vars import Var

support_group = "https://t.me/DivideProjectsDiscussion"


def ban_kb(user_id: int):
    return ikb([[("Ban User", f"ban_{user_id}")]]) if user_id != Var.OWNER_ID else None


def joinCheck():
    def wrapper(func):
        async def decorator(c, m):
            if not Var.JOIN_CHECK:
                return await func(c, m)
            if m.sender_chat:
                return
            try:
                get = await c.get_chat_member(Var.AUTH_CHANNEL, m.from_user.id)
            except UserNotParticipant:
                return await m.reply_text(
                    f"You need to Join {Var.AUTH_CHANNEL} to use me.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Join Channel",
                                    url=f"https://t.me/{Var.AUTH_CHANNEL.replace('@', '')}",
                                ),
                            ],
                        ],
                    ),
                )
            if get.status in ("restricted", "kicked"):
                return await m.reply_text(
                    f"You were banned from using me. If you think this is a mistake then report this at {Var.SUPPORT_GROUP}",
                )
            if not get.status in ("creator", "administrator", "member"):
                return await m.reply_text(
                    f"You need to Join {Var.AUTH_CHANNEL} to use me.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Join Channel",
                                    url=f"https://t.me/{Var.AUTH_CHANNEL.replace('@', '')}",
                                ),
                            ],
                        ],
                    ),
                )
            return await func(c, m)

        return decorator

    return wrapper