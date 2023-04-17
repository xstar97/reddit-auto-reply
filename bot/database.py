import logging
from config import DB_TYPE
from redis_db import get_redis_commented_submissions,add_redis_commented_submission

def get_commented_submissions():
    """Get submission IDs as a list."""
    try:
        comments = get_redis_commented_submissions()
        return comments
    except Exception as e:
        logging.error(f"Error occurred while getting commented submissions: {str(e)}")
        return []

def add_commented_submission(submission_id):
    """Add a submission ID to the list of commented submissions in the Redis database."""
    try:
        logging.info(f"submission ID: {submission_id}")
        add_redis_commented_submission(submission_id)
    except Exception as e:
        logging.error(f"Error occurred while adding commented submission {submission_id}: {str(e)}")
