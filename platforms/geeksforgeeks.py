from datetime import datetime
import pytz
import requests
import json

def getGeeksforgeeksContests():
    url = "https://practiceapi.geeksforgeeks.org/api/latest/events/recurring/gfg-weekly-coding-contest"
    response = requests.get(url)
    geeksforgeeksContests = []
    
    if response.status_code == 200:
        jsonResponse = json.loads(response.text)
        contests = jsonResponse.get("upcoming_entity_details", [])
        
        for contest in contests:
            start_time_str = contest["start_time"]

            # Normalize time string
            if "Z" not in start_time_str:
                start_time_str += "Z"  # Ensure it ends with 'Z'
            
            # Try parsing with multiple formats
            time_formats = ["%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S"]
            utc_time = None

            for fmt in time_formats:
                try:
                    utc_time = datetime.strptime(start_time_str, fmt)
                    break  # Stop when successful
                except ValueError:
                    continue

            if utc_time is None:
                print(f"Error: Could not parse time {start_time_str}")
                continue

            utc_time = utc_time.replace(tzinfo=pytz.utc)
            ist_time = utc_time.astimezone(pytz.timezone("Asia/Kolkata"))

            geeksforgeeksContest = {
                "platform": "GeeksforGeeks",
                "contestName": contest["name"],
                "contestLink": contest["event_entity_url"],
                "startTime": ist_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
                "contestDuration": f"{int(contest['total_time']) // 60:02}:{int(contest['total_time']) % 60:02} hours"
            }
            geeksforgeeksContests.append(geeksforgeeksContest)
    
    return geeksforgeeksContests

print(getGeeksforgeeksContests())
