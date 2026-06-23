# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from bot import bot

from config import (
    START_PIC,
    START_TEXT,
    ABOUT_TEXT,
    BOT_USERNAME,
    UPDATES_CHANNEL,
    SUPPORT_GROUP
)

from database import add_user

from force_sub import check_sub



# ---------------- START ---------------- #

@bot.on_message(
    filters.private &
    filters.command("start")
)
async def start_cmd(
    client,
    message
):

    user_id = message.from_user.id


    if not await check_sub(
        client,
        user_id
    ):

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📢 Join Updates",
                        url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔄 Try Again",
                        url=f"https://t.me/{BOT_USERNAME}?start=true"
                    )
                ]
            ]
        )


        return await message.reply_text(
            "🔒 Please join our updates channel first.",
            reply_markup=buttons
        )



    await add_user(
        user_id
    )


    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ Add Me",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                )
            ],

            [
                InlineKeyboardButton(
                    "📢 Updates",
                    url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
                InlineKeyboardButton(
                    "💬 Support",
                    url=f"https://t.me/{SUPPORT_GROUP}"
                )
            ],

            [
                InlineKeyboardButton(
                    "ℹ️ About",
                    callback_data="about"
                )
            ]
        ]
    )


    text = START_TEXT.format(
        mention=message.from_user.mention
    )


    if START_PIC:


        await message.reply_photo(
            photo=START_PIC,
            caption=text,
            reply_markup=buttons
        )


    else:


        await message.reply_text(
            text,
            reply_markup=buttons
        )



# ---------------- ABOUT ---------------- #

@bot.on_callback_query(
    filters.regex("^about$")
)
async def about_callback(
    client,
    query
):

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🏠 Home",
                    callback_data="home"
                )
            ]
        ]
    )


    await query.message.edit_caption(
        caption=ABOUT_TEXT,
        reply_markup=buttons
    )


    await query.answer()



# ---------------- HOME ---------------- #

@bot.on_callback_query(
    filters.regex("^home$")
)
async def home_callback(
    client,
    query
):

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📢 Updates",
                    url=f"https://t.me/{UPDATES_CHANNEL}"
                )
            ],
            [
                InlineKeyboardButton(
                    "ℹ️ About",
                    callback_data="about"
                )
            ]
        ]
    )


    await query.message.edit_caption(
        caption=START_TEXT.format(
            mention=query.from_user.mention
        ),
        reply_markup=buttons
    )


    await query.answer()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
