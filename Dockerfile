FROM python:3.9-alpine

# Set the working directory for the bot script
WORKDIR /config

# Copy all files from the bot directory into the container
COPY bot/ /config/

# Install system dependencies
RUN apk update && \
    apk add --no-cache build-base libffi-dev openssl-dev

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Install Node.js and npm
RUN apk add --no-cache nodejs npm

# Set the environment variables for the bot
ENV SUBREDDITS=subreddit1,subreddit2
ENV EXCLUDE_USERS=user1,user2
ENV TRIGGER_WORDS=word1
ENV COMMENT_TEXT=hello_world
ENV COMMENT_WAIT_SECONDS=15

# Set the user and group as environment variables
ENV PUID=1000
ENV PGID=1000

# Create a non-root user with the given user and group IDs
RUN addgroup -g $PGID kah && \
    adduser -D -u $PUID -G kah kah

# Change the ownership of the working directory and start script to the non-root user
RUN chown -R kah:kah /config
RUN chown kah:kah /config/start.sh
RUN chmod +x /config/start.sh

# Set the non-root user as the user to run the container
USER kah

# Run the start script when the container launches
CMD ["sh", "/config/start.sh"]
