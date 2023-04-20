from flask import Flask, render_template
from database import get_submissions
import os, logging
from config import TRIGGER_WORDS

def web_app(environ, start_response):
    app = Flask(__name__)

    @app.route('/')
    def index():
        submissions = get_submissions()

        if not submissions:
            return render_template('empty.html', trigger_words=TRIGGER_WORDS)

        headers = {
            'Refresh': '30'
        }

        return render_template('submissions.html', submissions=submissions), 200, headers

    return app(environ, start_response)

if __name__ == "__main__":
    app = web_app()
    app.run(host="0.0.0.0", port=3000)
