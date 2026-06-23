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
    FILES_PER_PAGE,
    UPDATES_CHANNEL
)

from database import (
    search_movies,
    increase_search
)

from force_sub import check_sub


# Store searches temporarily
SEARCH_DATA = {}


def make_buttons(
    results,
    page=0
):

    start = page * FILES_PER_PAGE

    end = start + FILES_PER_PAGE

    files = results[start:end]


    buttons = []


    for item in files:

        name = item["file_name"]

        buttons.append(
            [
                InlineKeyboardButton(
                    text=f"🎬 {name[:45]}",
                    callback_data=f"file_{item['msg_id']}"
                )
            ]
        )


    total_pages = (
        len(results)
        + FILES_PER_PAGE - 1
    ) // FILES_PER_PAGE


    navigation = []


    if page > 0:

        navigation.append(
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data=f"page_{page-1}"
            )
        )


    navigation.append(
        InlineKeyboardButton(
            f"📄 {page+1}/{total_pages}",
            callback_data="none"
        )
    )


    if page < total_pages - 1:

        navigation.append(
            InlineKeyboardButton(
                "Next ➡️",
                callback_data=f"page_{page+1}"
            )
        )


    buttons.append(
        navigation
    )


    buttons.append(
        [
            InlineKeyboardButton(
                "📢 Updates",
                url=f"https://t.me/{UPDATES_CHANNEL}"
            )
        ]
    )


    return InlineKeyboardMarkup(
        buttons
    )



@bot.on_message(
    filters.private
    & filters.text
    & ~filters.command(
        [
            "start",
            "stats",
            "broadcast"
        ]
    )
)
async def movie_search(
    client,
    message
):


    if not await check_sub(
        client,
        message.from_user.id
    ):

        return await message.reply_text(
            "🔒 Join Updates Channel First."
        )


    query = message.text.strip()


    if len(query) < 2:
        return



    results = await search_movies(
        query
    )


    if not results:

        return await message.reply_text(
            "❌ No movies found."
        )



    await increase_search()



    SEARCH_DATA[
        message.from_user.id
    ] = results



    await message.reply_text(
        f"""
🔎 Search:

<b>{query}</b>

🎬 Found:
<b>{len(results)}</b> files
""",
        reply_markup=make_buttons(
            results,
            0
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
