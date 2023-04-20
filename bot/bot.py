import os,logging,threading,subprocess
from config import BOT_STATE
from reddit import monitor_subreddits
from web import web_app

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    if BOT_STATE == "development":
        logging.info("Bot is in development mode. Not running.")
    elif BOT_STATE == "production":
        logging.info("Bot is in production mode. Running.")
        try:
            monitor_thread = threading.Thread(target=monitor_subreddits)
            monitor_thread.start()
        except Exception as e:
            logging.error("An error occurred: {}".format(e))