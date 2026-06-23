# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from flask import Flask
from threading import Thread


app = Flask(__name__)


@app.route("/")
def home():

    return (
        "AU Luffy Filters Bot is Running 🚀"
    )


@app.route("/health")
def health():

    return {
        "status": "online",
        "bot": "AU_LuffyFilters"
    }


def run():

    app.run(
        host="0.0.0.0",
        port=8080
    )


def keep_alive():

    server = Thread(
        target=run
    )

    server.daemon = True
    server.start()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
