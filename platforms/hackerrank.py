import requests
from datetime import datetime
from pytz import timezone

def getHackerrankContests():
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json'
    }

    try:
        response = requests.get("https://www.hackerrank.com/community/engage/events", headers=headers)
        response.raise_for_status()
        
        jsonResponse = response.json()
        hackerrankContests = []
        contests = jsonResponse["data"]["events"]["ongoing_events"]

        for contest in contests:
            utc_format = "%Y-%m-%dT%H:%M:%S.%fZ"
            utc = timezone("UTC")
            ist = timezone("Asia/Kolkata")

            start_time_utc = datetime.strptime(contest["attributes"]["start_time"], utc_format).replace(tzinfo=utc)
            end_time_utc = datetime.strptime(contest["attributes"]["end_time"], utc_format).replace(tzinfo=utc)

            start_time_ist = start_time_utc.astimezone(ist).strftime("%Y-%m-%d %H:%M:%S %Z")
            duration = end_time_utc - start_time_utc
            duration_str = f"{duration.seconds // 3600:02}:{(duration.seconds % 3600) // 60:02}:{duration.seconds % 60:02}"

            hackerrankContest = {
                "platform": "HackerRank",
                "contestName": contest["attributes"]["name"],
                "contestLink": contest["attributes"]["microsite_url"],
                "startTime": start_time_ist,  # Converted to IST
                "contestDuration": duration_str  # HH:MM:SS format
            }
            hackerrankContests.append(hackerrankContest)

        return hackerrankContests

    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return []

print(getHackerrankContests())
