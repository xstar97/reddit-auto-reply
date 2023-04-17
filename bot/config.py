import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define environment variables
BOT_STATE = os.environ.get("BOT_STATE", "development")
DB_TYPE = os.getenv("DB_TYPE", "sqlite")

# Reddit API credentials
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
USER_AGENT = os.environ.get("USER_AGENT")

# Subreddits to monitor
SUBREDDITS = os.environ.get("SUBREDDITS")
if SUBREDDITS is not None:
    SUBREDDITS = SUBREDDITS.split(",")

#Exclude User List
EXCLUDE_USERS = os.environ.get("EXCLUDE_USERS")
if EXCLUDE_USERS is not None:
    EXCLUDE_USERS = EXCLUDE_USERS.split(",")

# Comment text
COMMENT_TEXT = os.environ.get("COMMENT_TEXT")
COMMENT_WAIT_SECONDS = int(os.environ.get("COMMENT_WAIT_SECONDS", 10))

# Trigger words for comments
TRIGGER_WORDS = os.environ.get("TRIGGER_WORDS")
if TRIGGER_WORDS is not None:
    TRIGGER_WORDS = TRIGGER_WORDS.split(",")