# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_URI


# Mongo Connection

mongo = AsyncIOMotorClient(
    MONGO_URI
)

db = mongo["AU_LuffyFilters"]


# Collections

users_col = db["users"]
movies_col = db["movies"]
search_col = db["searches"]


# ---------------- USERS ----------------


async def add_user(user_id):

    await users_col.update_one(
        {
            "_id": user_id
        },
        {
            "$set": {
                "_id": user_id
            }
        },
        upsert=True
    )


async def get_users():

    users = []

    async for user in users_col.find():

        users.append(
            user["_id"]
        )

    return users


async def total_users():

    return await users_col.count_documents(
        {}
    )


# ---------------- MOVIES ----------------


async def save_movie(
    file_name,
    msg_id,
    file_type
):

    await movies_col.update_one(
        {
            "msg_id": msg_id
        },
        {
            "$set": {
                "file_name": file_name,
                "msg_id": msg_id,
                "type": file_type
            }
        },
        upsert=True
    )


async def search_movies(query):

    cursor = movies_col.find(
        {
            "file_name": {
                "$regex": query,
                "$options": "i"
            }
        }
    ).limit(50)


    results = []

    async for item in cursor:
        results.append(item)

    return results


async def get_movie(
    msg_id
):

    return await movies_col.find_one(
        {
            "msg_id": msg_id
        }
    )


async def total_movies():

    return await movies_col.count_documents(
        {}
    )


# ---------------- SEARCH COUNT ----------------


async def increase_search():

    await search_col.update_one(
        {
            "_id": "count"
        },
        {
            "$inc": {
                "value": 1
            }
        },
        upsert=True
    )


async def get_search_count():

    data = await search_col.find_one(
        {
            "_id": "count"
        }
    )

    if data:

        return data.get(
            "value",
            0
        )

    return 0



# ---------------- INDEX ----------------


async def create_indexes():

    await movies_col.create_index(
        [
            (
                "file_name",
                "text"
            )
        ]
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
