import os
import praw
import logging
import time
import datetime
from database import get_commented_submissions, add_commented_submission
from config import CLIENT_ID,CLIENT_SECRET,USERNAME,PASSWORD,USER_AGENT,SUBREDDITS,COMMENT_TEXT,TRIGGER_WORDS,COMMENT_WAIT_SECONDS,EXCLUDE_USERS,USER_AGENT

if COMMENT_WAIT_SECONDS < 10:
    COMMENT_WAIT_SECONDS = 10

def connect_to_reddit_api():
    try:
        reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, username=USERNAME, password=PASSWORD, user_agent=USER_AGENT)
        return reddit
    except Exception as e:
        logging.info(f"Failed to connect to Reddit API. Error message: {e}")

# Monitor a single subreddit
def monitor_subreddit(reddit, subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    ten_minutes_ago = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)
    for submission in subreddit.stream.submissions(skip_existing=True):
        # Only process submissions that were created within the last 10 minutes plus the duration of the bot run.
        if submission.created_utc > ten_minutes_ago.timestamp():
            if submission.author in EXCLUDE_USERS:
                logging.info(f"skipping author {submission.author} post {submission.id}...")
                continue
            title_words = submission.title.lower().split()
            text_words = submission.selftext.lower().split()
            trigger_words = set(TRIGGER_WORDS)
            if trigger_words.intersection(title_words) or trigger_words.intersection(text_words):
                add_commented_submission(submission.id)
                comment_on_submission(submission)
                log_commented_submission(submission)
        else:
            # The bot missed this submission, so process it now.
            if submission.id in get_commented_submissions():
                logging.info(f"skipping post {submission.id}...")
                continue
            if submission.author in EXCLUDE_USERS:
                logging.info(f"skipping author {submission.author} post {submission.id}...")
                continue
            title_words = submission.title.lower().split()
            text_words = submission.selftext.lower().split()
            trigger_words = set(TRIGGER_WORDS)
            if trigger_words.intersection(title_words) or trigger_words.intersection(text_words):
                add_commented_submission(submission.id)
                comment_on_submission(submission)
                log_commented_submission(submission)

# Check if a submission contains trigger words and reply with a comment
def comment_on_submission(submission):
    logging.info(f"commenting on post...")
    time.sleep(COMMENT_WAIT_SECONDS)
    submission.reply(COMMENT_TEXT)

# Log the post title and comment
def log_commented_submission(submission):
    logging.info(f"Post Title: {submission.title}")
    logging.info(f"Comment made in response to submission {submission.id}, direct link: {submission.shortlink}")

# Main function to monitor multiple subreddits
def monitor_subreddits():
    reddit = connect_to_reddit_api()
    for subreddit_name in SUBREDDITS:
        monitor_subreddit(reddit, subreddit_name)