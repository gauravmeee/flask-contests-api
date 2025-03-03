import requests
import json
from datetime import datetime
import pytz

def getHackerearthContests():
    response = requests.get("https://www.hackerearth.com/chrome-extension/events/")
    hackerearthContests = []

    if response.status_code == 200:
        jsonResponse = json.loads(response.text)
        contests = jsonResponse["response"]

        for contest in contests:
            if contest["status"] == "UPCOMING":
                try:
                    hackerearthContest = {
                        "platform": "HackerEarth",
                        "contestName": contest["title"],
                        "contestLink": contest["url"],
                    }

                    # The start_tz is already in IST format with timezone offset
                    start_time = contest["start_tz"]
                    end_time = contest["end_tz"]

                    # Store the start time directly since it's already in IST
                    hackerearthContest["startTime"] = start_time

                    # Calculate contest duration
                    start_dt = datetime.fromisoformat(start_time.replace(" ", "T"))
                    end_dt = datetime.fromisoformat(end_time.replace(" ", "T"))
                    
                    td = end_dt - start_dt
                    days = td.days
                    hours = td.seconds // 3600
                    minutes = (td.seconds % 3600) // 60

                    if days > 0:
                        hackerearthContest["contestDuration"] = f"{days} Days & {hours} hours"
                    elif hours > 0:
                        hackerearthContest["contestDuration"] = f"{hours:02}:{minutes:02} hours"
                    else:
                        hackerearthContest["contestDuration"] = f"{minutes} minutes"

                    hackerearthContests.append(hackerearthContest)

                except Exception as e:
                    print(f"Error processing contest {contest['title']}: {e}")
                    continue

    return hackerearthContests 

print(getHackerearthContests())