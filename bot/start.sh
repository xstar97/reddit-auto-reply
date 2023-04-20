#!/bin/bash

# Start bot process in the background
python3 bot.py &

# Save the process ID of the bot process
BOT_PID=$!

# Start web process in the foreground
gunicorn web:web_app --bind 0.0.0.0:3000 -w 4

# Wait for the bot process to finish
wait $BOT_PID
