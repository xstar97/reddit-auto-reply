import logging
from config import DB_TYPE
from sqlite_db import get_sqlite_commented_submissions,add_sqlite_commented_submission

def get_commented_submissions():
    """Get submission IDs as a the list."""
    comments = get_sqlite_commented_submissions()
    return comments

def add_commented_submission(submission_id):
    """Add a submission ID to the list of commented submissions in the SQLite database."""
    logging.info(f"submission ID: {submission_id}")
    add_sqlite_commented_submission(submission_id)
