# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #


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


    total = 0


    async for message in scanner.get_chat_history(
        DATABASE_CHANNEL_ID
    ):


        try:


            file_name = None
            file_type = None



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



            if file_name:


                await save_movie(
                    file_name,
                    message.id,
                    file_type
                )


                total += 1



                if total % 100 == 0:

                    print(
                        f"Indexed {total} files"
                    )



        except Exception as e:

            print(e)



    print(
        f"🎉 Scan Complete : {total}"
    )



async def main():

    await scanner.start()

    await scan_database()

    await scanner.stop()



if __name__ == "__main__":

    asyncio.run(main())

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
