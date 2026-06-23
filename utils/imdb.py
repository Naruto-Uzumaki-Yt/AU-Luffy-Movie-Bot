# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import aiohttp

from config import (
    OMDB_API_KEY
)



async def get_imdb(
    title
):

    if not OMDB_API_KEY:

        return None


    try:


        url = (
            "https://www.omdbapi.com/"
            f"?apikey={OMDB_API_KEY}"
            f"&t={title}"
        )


        async with aiohttp.ClientSession() as session:


            async with session.get(
                url
            ) as response:


                data = await response.json()



                if data.get(
                    "Response"
                ) != "True":

                    return None



                return {

                    "title":
                    data.get(
                        "Title",
                        "Unknown"
                    ),

                    "year":
                    data.get(
                        "Year",
                        "N/A"
                    ),

                    "rating":
                    data.get(
                        "imdbRating",
                        "N/A"
                    ),

                    "genre":
                    data.get(
                        "Genre",
                        "N/A"
                    ),

                    "language":
                    data.get(
                        "Language",
                        "N/A"
                    ),

                    "runtime":
                    data.get(
                        "Runtime",
                        "N/A"
                    ),

                    "plot":
                    data.get(
                        "Plot",
                        "N/A"
                    ),

                    "poster":
                    data.get(
                        "Poster",
                        ""
                    )
                }


    except Exception as e:

        print(
            f"IMDb Error: {e}"
        )

        return None

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
