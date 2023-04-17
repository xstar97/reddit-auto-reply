import logging
from peewee import SqliteDatabase, Model, CharField

# Define the SQLite database
db = SqliteDatabase("./config.db")

# Define the CommentedSubmission model
class CommentedSubmission(Model):
    submission_id = CharField(unique=True)

    class Meta:
        database = db

# Connect to the database and create the table (if it doesn't exist)
db.connect()
db.create_tables([CommentedSubmission])

def get_sqlite_commented_submissions():
    # Retrieve the commented submissions from the database
    comments = [c.submission_id for c in CommentedSubmission.select()]
    return comments

def add_sqlite_commented_submission(submission_id):
    """Add a submission ID to the list of commented submissions in the SQLite database."""
    CommentedSubmission.create(submission_id=submission_id)