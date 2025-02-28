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

                    # Parse and convert times correctly
                    utc_start = datetime.fromisoformat(contest["start_tz"].replace(" ", "T"))
                    utc_end = datetime.fromisoformat(contest["end_tz"].replace(" ", "T"))

                    # Convert UTC to IST
                    ist_timezone = pytz.timezone("Asia/Kolkata")
                    start_ist = utc_start.astimezone(ist_timezone).strftime('%Y-%m-%dT%H:%M:%S%z')

                    hackerearthContest["startTime"] = start_ist

                    # Calculate contest duration
                    td = utc_end - utc_start
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
