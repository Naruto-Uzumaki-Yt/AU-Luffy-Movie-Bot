# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import filters

from bot import bot

from config import OWNER_ID

from database import (
    total_users,
    total_movies,
    get_users,
    get_search_count
)


# ---------------- STATS ---------------- #

@bot.on_message(
    filters.private &
    filters.command("stats")
)
async def stats_cmd(
    client,
    message
):

    if message.from_user.id != OWNER_ID:
        return


    users = await total_users()

    movies = await total_movies()

    searches = await get_search_count()


    await message.reply_text(
        f"""
<b>📊 AU Luffy Filters Stats</b>

👤 Users : <b>{users}</b>

🎬 Movies : <b>{movies}</b>

🔍 Searches : <b>{searches}</b>

⚡ Status : Online
"""
    )



# ---------------- BROADCAST ---------------- #

@bot.on_message(
    filters.private &
    filters.command("broadcast")
)
async def broadcast_cmd(
    client,
    message
):

    if message.from_user.id != OWNER_ID:
        return


    if not message.reply_to_message:

        return await message.reply_text(
            "❌ Reply to a message to broadcast."
        )


    users = await get_users()


    sent = 0

    failed = 0


    status = await message.reply_text(
        "📢 Broadcasting Started..."
    )


    for user_id in users:


        try:

            await message.reply_to_message.copy(
                user_id
            )

            sent += 1


        except:

            failed += 1



    await status.edit_text(
        f"""
<b>📢 Broadcast Completed</b>

✅ Sent : {sent}

❌ Failed : {failed}
"""
    )



# ---------------- PING ---------------- #

@bot.on_message(
    filters.private &
    filters.command("ping")
)
async def ping(
    client,
    message
):

    await message.reply_text(
        "🏓 Pong!\n\nBot is alive."
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
