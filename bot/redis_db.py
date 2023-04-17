import logging
import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

# Define the Redis connection
redis_conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

def get_redis_commented_submissions():
    """Get submission IDs as a list from Redis."""
    comments = redis_conn.lrange("commented_submissions", 0, -1)
    comments = [comment.decode() for comment in comments]
    return comments

def add_redis_commented_submission(submission_id):
    """Add a submission ID to the list of commented submissions in Redis."""
    logging.info(f"Adding submission ID to Redis: {submission_id}")
    redis_conn.rpush("commented_submissions", submission_id)
