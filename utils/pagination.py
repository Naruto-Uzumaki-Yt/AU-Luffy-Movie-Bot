# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from math import ceil


def get_total_pages(
    total,
    per_page
):

    if total == 0:
        return 1

    return ceil(
        total / per_page
    )



def get_page_items(
    items,
    page,
    per_page
):

    start = (
        page * per_page
    )

    end = (
        start + per_page
    )

    return items[start:end]

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
