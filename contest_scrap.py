# Cloud Cache Upstash-Redis
import redis
import json
import os
from platforms import atcoder, codechef, codeforces, hackerearth, hackerrank, geeksforgeeks
from dotenv import load_dotenv


load_dotenv()

redis_host = os.getenv("REDIS_HOST")
redis_port = int(os.getenv("REDIS_PORT", 6379))  # Default to 6379 if not set
redis_password = os.getenv("REDIS_PASSWORD")

redis_client = redis.StrictRedis(
    host=redis_host,
    port=redis_port,
    password=redis_password,
    decode_responses=True,
    socket_timeout=10,  # Timeout in seconds
    ssl=True  # Enable SSL
)

# redis_client.delete("contests_data") # Uncomment to clear old cache
def fetchContests():
    cached_data = redis_client.get("contests_data")
    if cached_data:
        return json.loads(cached_data)  # Return cached results if available

    # Fetch new contest data if cache is empty
    contests = []
    contests.extend(codeforces.getCodeforcesContests())
    contests.extend(codechef.getCodechefContests())
    contests.extend(hackerrank.getHackerrankContests())
    contests.extend(hackerearth.getHackerearthContests())
    contests.extend(geeksforgeeks.getGeeksforgeeksContests())
    contests.extend(atcoder.getAtCoderContests())

    contests = sorted(contests, key=lambda contest: contest['startTime'])
    result = {"contests": contests}

    # Store in Redis for 6 hour (6*60*60 seconds)
    redis_client.setex("contests_data", 6*60*60, json.dumps(result))

    return result
