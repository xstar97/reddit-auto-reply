import os,praw,logging,time,datetime,threading
from database import get_submissions, add_submission
from config import CLIENT_ID,CLIENT_SECRET,USERNAME,PASSWORD,USER_AGENT,SUBREDDITS,COMMENT_TEXT,TRIGGER_WORDS,COMMENT_WAIT_SECONDS,EXCLUDE_USERS,USER_AGENT

if COMMENT_WAIT_SECONDS < 10:
    COMMENT_WAIT_SECONDS = 10

if SUBREDDITS is not None:
    SUBREDDITS = SUBREDDITS.split(",")

if EXCLUDE_USERS is not None:
    EXCLUDE_USERS = EXCLUDE_USERS.split(",")

if TRIGGER_WORDS is not None:
    TRIGGER_WORDS = TRIGGER_WORDS.split(",")

def connect_to_reddit_api():
    try:
        reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, username=USERNAME, password=PASSWORD, user_agent=USER_AGENT)
        logging.info(f"Connected to Reddit API, as user {USERNAME}!")
        return reddit
    except Exception as e:
        logging.info(f"Failed to connect to Reddit API. Error message: {e}")

def process_submission(submission):
    if submission.author in EXCLUDE_USERS:
        logging.info(f"skipping author {submission.author} post {submission.id}...")
        return False

    title_words = submission.title.lower().split()
    text_words = submission.selftext.lower().split()
    trigger_words = set(TRIGGER_WORDS)
    if trigger_words.intersection(title_words) or trigger_words.intersection(text_words):
        add_submission(submission)
        comment_on_submission(submission)
        log_submission(submission)
        return True

    return False


def monitor_subreddit(reddit, subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    ten_minutes_ago = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    # Extract the IDs of previously commented submissions
    submission_ids = [submission["id"] for submission in get_submissions()]

    for submission in subreddit.stream.submissions(skip_existing=True):
        # Only process submissions that were created within the last 10 minutes plus the duration of the bot run.
        if submission.created_utc <= ten_minutes_ago.timestamp():
            # The bot missed this submission, so process it now.
            if submission.id in submission_ids:
                logging.info(f"skipping post {submission.id}...")
                continue
            if not process_submission(submission):
                continue
        else:
            if not process_submission(submission):
                continue

def comment_on_submission(submission):
    logging.info(f"commenting on post...")
    time.sleep(COMMENT_WAIT_SECONDS)
    submission.reply(COMMENT_TEXT)

# Log the post title and comment
def log_submission(submission):
    logging.info(f"Post Title: {submission.title}")
    logging.info(f"Comment made in response to submission {submission.id}, direct link: {submission.shortlink}")

# Main function to monitor multiple subreddits
def monitor_subreddits():
    reddit = connect_to_reddit_api()
    threads = []
    for subreddit_name in SUBREDDITS:
        logging.info(f"Monitoring r/{subreddit_name}")
        thread = threading.Thread(target=monitor_subreddit, args=(reddit, subreddit_name))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    monitor_subreddits()