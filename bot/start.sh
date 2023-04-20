#!/bin/bash

# Set the default port to 3000
PORT=${1:-3000}

# Start bot process with pm2
pm2 start bot.py --interpreter=python3 --name reddit-reply-bot

# Start web process with pm2
pm2 start "gunicorn web:web_app --bind 0.0.0.0:$PORT -w 4" --name reddit-reply-web