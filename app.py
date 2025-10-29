# app.py
from flask import Flask
import random
import datetime

app = Flask(__name__)

quotes = [
    "Moo! Keep calm and code on.",
    "Wisdom comes from cows — chew your thoughts slowly.",
    "Don’t rush — even cows take their time."
]

@app.route('/')
def home():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quote = random.choice(quotes)
    return f"<h1>🐄 Wisecow</h1><p>{quote}</p><small>{now}</small>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

