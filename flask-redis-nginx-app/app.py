from flask import Flask
from redis import Redis

import os

host = os.getenv("REDIS_HOST", "redis")
port = int(os.getenv("REDIS_PORT", 6379))

client = Redis(host=host, port=port, db=0)

app = Flask(__name__)

# Route 1 > Just a welcome message
@app.route('/')
def home():
    return "Welcome to Mudda's Coderco App!"

# Route 2 > Increment counter in redis

@app.route('/count')
def count():
    visits = client.incr('hits')
    return f"Thanks for visiting Mudda's container! Hits: {visits}"

# Route 3 → Reset counter
@app.route('/reset')
def reset():
    client.set('hits', 0)
    return "The counter has been reset."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)