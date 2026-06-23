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
    DATABASE_CHANNEL_ID,
    UPDATES_CHANNEL,
    FILE_CAPTION
)

from database import (
    get_movie
)

from handlers.search import (
    SEARCH_DATA,
    make_buttons
)


# ---------------- NONE BUTTON ---------------- #

@bot.on_callback_query(
    filters.regex("^none$")
)
async def none_btn(
    client,
    query
):

    await query.answer()


# ---------------- PAGINATION ---------------- #

@bot.on_callback_query(
    filters.regex("^page_")
)
async def page_btn(
    client,
    query
):

    page = int(
        query.data.split("_")[1]
    )


    data = SEARCH_DATA.get(
        query.from_user.id
    )


    if not data:

        return await query.answer(
            "Search expired!",
            show_alert=True
        )


    await query.message.edit_reply_markup(
        reply_markup=make_buttons(
            data,
            page
        )
    )


    await query.answer()



# ---------------- SEND FILE ---------------- #

@bot.on_callback_query(
    filters.regex("^file_")
)
async def file_btn(
    client,
    query
):


    msg_id = int(
        query.data.split("_")[1]
    )


    movie = await get_movie(
        msg_id
    )


    if not movie:

        return await query.answer(
            "File not found!",
            show_alert=True
        )


    msg = await client.get_messages(
        DATABASE_CHANNEL_ID,
        msg_id
    )


    file_name = movie.get(
        "file_name",
        "Movie"
    )


    caption = FILE_CAPTION.format(
        file_name=file_name,
        updates=UPDATES_CHANNEL
    )


    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📢 Updates",
                    url=f"https://t.me/{UPDATES_CHANNEL}"
                )
            ]
        ]
    )


    try:


        if msg.document:


            await query.message.reply_document(
                document=msg.document.file_id,
                caption=caption,
                reply_markup=buttons
            )


        elif msg.video:


            await query.message.reply_video(
                video=msg.video.file_id,
                caption=caption,
                reply_markup=buttons
            )


        elif msg.photo:


            await query.message.reply_photo(
                photo=msg.photo.file_id,
                caption=caption,
                reply_markup=buttons
            )


        await query.answer(
            "📥 Sending..."
        )


    except Exception as e:


        print(e)

        await query.answer(
            "Failed to send file",
            show_alert=True
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
