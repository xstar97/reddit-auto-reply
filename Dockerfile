# Use the official Python image as the base image
FROM python:3.9-alpine3.17

# Set the working directory to /config
WORKDIR /config

# Copy all files from the bot directory into the container
COPY bot/* ./

# Install the required packages
RUN apk add --no-cache gcc musl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev

# Set environment variables

#DB
ENV BOT_STATE=development
ENV DB_TYPE=sqlite

# Reddit
ENV CLIENT_ID=id
ENV CLIENT_SECRET=secret
ENV USERNAME=user
ENV PASSWORD=reddit
ENV USER_AGENT=usr_agent
ENV SUBREDDITS=subreddit1,subreddit2
ENV EXCLUDE_USERS=user1,user2
ENV TRIGGER_WORDS=word1
ENV COMMENT_TEXT=hello world
ENV COMMENT_WAIT_SECONDS=15

# Set the user and group as environment variables
ENV PUID=1000
ENV PGID=1000

# Create a non-root user with the given user and group IDs
RUN addgroup -g $PGID kah && \
    adduser -D -u $PUID -G kah kah

# Change the ownership of the working directory to the non-root user
RUN chown kah:kah /config

# Set the non-root user as the user to run the container
USER kah

# Set the volume to /config
VOLUME /config

# Run the bot script when the container launches
CMD ["python3", "bot.py"]