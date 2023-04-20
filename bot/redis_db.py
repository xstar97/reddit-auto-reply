import logging
import redis
import json
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Redis connection
try:
    redis_conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
    # Log Redis connection status
    if redis_conn.ping():
        logging.info("Redis connection established")
    else:
        logging.error("Failed to establish Redis connection")
except Exception as e:
    logging.error(f"Failed to establish Redis connection. Error message: {e}")
    redis_conn = None

def get_redis_submissions():
    """Get submission IDs, titles and authors as a list of dicts from Redis."""
    try:
        submissions = redis_conn.smembers("submissions")
        submissions = [json.loads(submission_str) for submission_str in submissions]
        return submissions
    except Exception as e:
        logging.error(f"Failed to get submissions from Redis. Error message: {e}")
        return []

def add_redis_submission(submission):
    """Add a submission ID, title, and author to the list of commented submissions in Redis."""
    try:
        submission_data = {"id": submission.id, "author": str(submission.author), "shortlink": submission.shortlink}
        submission_str = json.dumps(submission_data)
        logging.info(f"Adding submission to Redis: {submission_str}")
        redis_conn.sadd("submissions", submission_str)
    except Exception as e:
        logging.error(f"Failed to add submission to Redis. Error message: {e}")
