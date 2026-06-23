
import asyncio

from pyrogram import Client

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    DATABASE_CHANNEL_ID
)

from database import save_movie


scanner = Client(
    "database_scanner",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


async def scan_database():

    # Fix peer error
    chat = await scanner.get_chat(
        DATABASE_CHANNEL_ID
    )

    print(
        f"Scanning: {chat.title}"
    )


    total = 0


    async for message in scanner.get_chat_history(
        chat.id
    ):

        try:

            file_name = None
            file_type = None


            if message.document:

                file_name = (
                    message.document.file_name
                    or "Unknown"
                )

                file_type = "document"


            elif message.video:

                file_name = (
                    message.video.file_name
                    or "Unknown"
                )

                file_type = "video"


            elif message.photo:

                file_name = "Photo"
                file_type = "photo"


            if file_name:

                await save_movie(
                    file_name,
                    message.id,
                    file_type
                )

                total += 1


                if total % 1000 == 0:

                    print(
                        f"Indexed {total}"
                    )


        except Exception as e:

            print(e)



    print(
        f"Completed: {total}"
    )


async def main():

    await scanner.start()

    await scan_database()

    await scanner.stop()



if __name__ == "__main__":

    asyncio.run(main())
