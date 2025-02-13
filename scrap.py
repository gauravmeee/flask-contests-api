# Cloud Cache Upstash-Redis
import redis
import json
import os
from platforms import atcoder, codechef, codeforces, hackerearth, hackerrank, geeksforgeeks


redis_host = "gorgeous-rodent-12506.upstash.io"  # Set this in your Vercel environment variables
redis_port = 6379
redis_password = "ATDaAAIjcDEzNzEyOTQxM2M0ZmQ0NmI2OGZkZTk0OTk4OWY4Mzg5NXAxMA"

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

    # Store in Redis for 30 minutes (1800 seconds)
    redis_client.setex("contests_data", 1800, json.dumps(result)) # 604800 seconds -> 1 week cache

    return result
