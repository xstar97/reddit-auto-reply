import logging
from config import DB_TYPE
from redis_db import get_redis_submissions,add_redis_submission

def get_submissions():
    """Get a list of commented submissions as dictionaries."""
    try:
        submissions = get_redis_submissions()
        return submissions
    except Exception as e:
        logging.error(f"Error occurred while getting commented submissions: {str(e)}")
        return []

def add_submission(submission):
    """Add a submission ID to the list of commented submissions in the Redis database."""
    try:
        logging.info(f"\nsubmission ID: {submission.id}, \nauthor: {submission.author}, \nshortlink: {submission.shortlink}")
        add_redis_submission(submission)
    except Exception as e:
        logging.error(f"Error occurred while adding commented submission {submission.id}: {str(e)}")
