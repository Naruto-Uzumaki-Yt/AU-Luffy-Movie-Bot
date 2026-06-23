# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import asyncio

from pyrogram import Client, idle

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN
)

from database import create_indexes

from app import keep_alive


# ---------------- BOT ---------------- #

bot = Client(
    "AU_LuffyFilters",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# ---------------- LOAD HANDLERS ---------------- #

async def load_plugins():

    import handlers.start
    import handlers.search
    import handlers.callback
    import handlers.admin
    import auto_indexer


# ---------------- MAIN ---------------- #

async def main():

    keep_alive()

    await load_plugins()

    await bot.start()

    await create_indexes()

    me = await bot.get_me()

    print(
        "━━━━━━━━━━━━━━━━━━"
    )
    print(
        "🤖 AU Luffy Filters Started"
    )
    print(
        f"Username: @{me.username}"
    )
    print(
        "━━━━━━━━━━━━━━━━━━"
    )

    await idle()

    await bot.stop()



if __name__ == "__main__":

    asyncio.run(
        main()
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
