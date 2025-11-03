from flask import Flask 
import redis 

app = Flask(__name__)

# Connect to Redis (container name from docker-compose)
client = redis.Redis(host='redis-server', port=6379)

# Initialize visits
client.set('visits', 0)

@app.route('/')
def index():
    visits = client.get('visits')
    visits = int(visits) if visits else 0
    client.set('visits', visits + 1)
    return f"Members Visited : {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
