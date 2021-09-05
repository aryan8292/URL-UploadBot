import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from translation import Translation

from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Config.UPDATE_CHANNEL = Config.UPDATES_CHANNEL

@Client.on_message(filters.command(["help"]))
async def help_user(bot, update):
    if Config.JOIN_CHANNEL is not None:
        try:
            user = await c.get_chat_member(Config.JOIN_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="Sorry Sir, You are Banned to use me. Contact my [👥 Support Group](https://t.me/hxsupport).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Config.JOIN_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await c.send_message(
                chat_id=m.chat.id,
                text="Something went Wrong. Contact my [👥 Support Group](https://t.me/HxSupport).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ JOIN OUR CHANNEL ⭕️", url=f"https://t.me/{Config.JOIN_CHANNEL}")]]),
   )

@Client.on_message(filters.command(["upgrade"]))
async def upgrade(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ CHANNEL ⭕️", url=f"https://t.me/{Config.UPDATES_CHANNEL}")], [InlineKeyboardButton(text="😇 SUPPORT", url="https://t.me/HxSupport"),
                                                    InlineKeyboardButton(text="Donate ♐️", url="https://upayme.vercel.app/kkirodewal@ybl")]]),
    )


@Client.on_message(filters.command(["donate"]))
async def donate(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.DONATE_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="☕ Buy Me A Coffee ☕", url="https://upayme.vercel.app/kkirodewal@ybl")]]),
   )
    
@Client.on_message(filters.command(["about"]))
def about(bot, update):
    
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True   
    ) 
        
