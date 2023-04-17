import os
import logging
import praw
from config import BOT_STATE
from database import get_commented_submissions, add_commented_submission
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
    monitor_subreddits()
