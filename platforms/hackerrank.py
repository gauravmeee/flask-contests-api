import requests
from datetime import datetime

def getHackerrankContests():
    # Headers to mimic a web browser request and avoid potential blocking
    headers = {
        'User-Agent': 'Mozilla/5.0',  # Identifies the request as coming from a standard web browser
        'Accept': 'application/json'  # Indicates we expect a JSON response
    }
    
    try:
        response = requests.get(
            "https://www.hackerrank.com/community/engage/events", 
            headers=headers
        )
        response.raise_for_status()
        
        jsonResponse = response.json()
        hackerrankContests = []
        
        contests = jsonResponse["data"]["events"]["ongoing_events"]
        for contest in contests:
            hackerrankContest = {
                "platform": "HackerRank",
                "contestName": contest["attributes"]["name"],
                "contestLink": contest["attributes"]["microsite_url"],
                "startTime": contest["attributes"]["start_time"],
                "contestDuration": str(
                    datetime.strptime(contest["attributes"]["end_time"], "%Y-%m-%dT%H:%M:%S.%fZ") - 
                    datetime.strptime(contest["attributes"]["start_time"], "%Y-%m-%dT%H:%M:%S.%fZ")
                )
            }
            hackerrankContests.append(hackerrankContest)
        
        return hackerrankContests
    
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return []

print(getHackerrankContests())


import urllib.parse
url1 = "https://practice.geeksforgeeks.org/contest/gfg-weekly-195-rated-contest"
url2 = "https://practice.geeksforgeeks.org/contest/gfg-weekly-195-rated-contest"
print(urllib.parse.unquote(url1) == urllib.parse.unquote(url2))
