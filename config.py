# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import os


# Telegram API
API_ID = int(
    os.getenv(
        "API_ID",
        "0"
    )
)

API_HASH = os.getenv(
    "API_HASH",
    ""
)

BOT_TOKEN = os.getenv(
    "BOT_TOKEN",
    ""
)


# Bot Details
BOT_USERNAME = os.getenv(
    "BOT_USERNAME",
    "AU_LuffyFilters_bot"
)


OWNER_ID = int(
    os.getenv(
        "OWNER_ID",
        "7284759394"
    )
)


# Channels
DATABASE_CHANNEL_ID = int(
    os.getenv(
        "DATABASE_CHANNEL_ID",
        "-1004391658489"
    )
)

UPDATES_CHANNEL = os.getenv(
    "UPDATES_CHANNEL",
    "Anime_UpdatesAU"
)


SUPPORT_GROUP = os.getenv(
    "SUPPORT_GROUP",
    "AU_Bot_Discussion"
)


FORCE_SUB = os.getenv(
    "FORCE_SUB",
    "Anime_UpdatesAU"
)


# MongoDB
MONGO_URI = os.getenv(
    "MONGO_URI",
    ""
)


# IMDb API
OMDB_API_KEY = os.getenv(
    "OMDB_API_KEY",
    ""
)


# Start Image
START_PIC = os.getenv(
    "START_PIC",
    ""
)


# Search Settings
FILES_PER_PAGE = 10

MAX_RESULTS = 50


# Caption

FILE_CAPTION = """

{file_name}

Join ~ @{updates}

"""


# Start Message

START_TEXT = """
<b>👋 Hello {mention}</b>

🎬 Welcome To <b>AU Luffy Filters</b>

Search Movies, Series & Anime
Powered By @Anime_UpdatesAU 

<b>Enjoy Your Movies 🍿</b>
"""


# About

ABOUT_TEXT = """
<b>🤖 AU Luffy Filters Bot</b>

• Developer: @Mr_Mohammed_29\n
• Channel: @Anime_UpdatesAU 
"""

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
