#!/bin/bash

# Set the default port to 3000
PORT=${1:-3000}

# Start bot process in the background
python3 bot.py &

# Save the process ID of the bot process
BOT_PID=$!

# Start web process in the foreground
gunicorn web:web_app --bind 0.0.0.0:$PORT -w 4

# Wait for the bot process to finish
wait $BOT_PID
