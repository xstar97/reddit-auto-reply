# reddit-auto-reply
reddit-auto-reply python docker bot

```yaml
version: "3.8"

services:
  my-service:
    image: ghcr.io/xstar97/reddit-auto-reply:latest
    ports:
      - "8000:8000"
    volumes:
      - ./config:/config
    environment:
      - BOT_STATE=production
      - DB_TYPE=sqlite
      - CLIENT_ID=reddit_client_id
      - CLIENT_SECRET=reddit_client_secret
      - USERNAME=REDDIT_USER
      - PASSWORD=REDDIT_PASS
      - USER_AGENT=linux:script:v0.0.1 (by u/USER)
      - SUBREDDITS=subreddit1,subreddit2 #delim by ,
      - TRIGGER_WORDS=word1,word2 #delim by ,
      - COMMENT_WAIT_SECONDS=10
      - EXCLUDE_USERS=user1,user2 #delim by ,
      - COMMENT_TEXT="Hello world!"
    restart: always
```