import os
import logging
from config import BOT_STATE
from reddit import monitor_subreddits

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Check if the bot is in development mode
if BOT_STATE == "development":
    logging.info("Bot is in development mode. Not running.")
elif BOT_STATE == "production":
    logging.info("Bot is in production mode. Running.")
    try:
        monitor_subreddits()
    except Exception as e:
        logging.error("An error occurred while monitoring subreddits: {}".format(e))
