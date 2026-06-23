# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram.errors import (
    UserNotParticipant,
    ChannelPrivate
)

from config import FORCE_SUB


async def check_sub(
    client,
    user_id
):

    try:

        member = await client.get_chat_member(
            FORCE_SUB,
            user_id
        )

        if member:

            return True


    except UserNotParticipant:

        return False


    except ChannelPrivate:

        return True


    except Exception as e:

        print(
            f"ForceSub Error: {e}"
        )

        return False


    return False

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
