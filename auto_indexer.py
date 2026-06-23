# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import filters

from bot import bot

from config import DATABASE_CHANNEL_ID

from database import save_movie


@bot.on_message(
    filters.chat(DATABASE_CHANNEL_ID)
    & (
        filters.document
        | filters.video
        | filters.photo
    )
)
async def auto_index(
    client,
    message
):

    try:

        file_name = "Unknown File"
        file_type = "unknown"


        if message.document:

            file_name = (
                message.document.file_name
                or "Unknown File"
            )

            file_type = "document"


        elif message.video:

            file_name = (
                message.video.file_name
                or "Unknown Video"
            )

            file_type = "video"


        elif message.photo:

            file_name = "Photo"
            file_type = "photo"



        await save_movie(
            file_name,
            message.id,
            file_type
        )


        print(
            f"✅ Indexed : {file_name}"
        )


    except Exception as e:

        print(
            f"Index Error : {e}"
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
