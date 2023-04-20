import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define environment variables
BOT_STATE = os.environ.get("BOT_STATE", "development")
DB_TYPE = os.getenv("DB_TYPE", "redis")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
PORT = int(os.getenv("PORT", 3000))

# Reddit API credentials
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
USER_AGENT = os.environ.get("USER_AGENT")

# Subreddits to monitor
SUBREDDITS = os.environ.get("SUBREDDITS")

#Exclude User List
EXCLUDE_USERS = os.environ.get("EXCLUDE_USERS")

# Comment text
COMMENT_TEXT = os.environ.get("COMMENT_TEXT")
COMMENT_WAIT_SECONDS = int(os.environ.get("COMMENT_WAIT_SECONDS", 10))

# Trigger words for comments
TRIGGER_WORDS = os.environ.get("TRIGGER_WORDS")
