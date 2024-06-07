import os
import redis
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_DB = int(os.getenv("REDIS_DB"))

CACHE_TTL = 300

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

def set_cache(key, value):
    redis_client.setex(key, CACHE_TTL, value)

def get_cache(key):
    return redis_client.get(key)
