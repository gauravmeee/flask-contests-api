import requests
import json
from datetime import datetime
import pytz


def getCodechefContests():
    response = requests.get("https://www.codechef.com/api/list/contests/all?sort_by=START&sorting_order=asc&offset=0&mode=all")
    codechefContests = []
    if response.status_code == 200:
        jsonResponse = json.loads(response.text)
        contests = jsonResponse["future_contests"]
        for contest in contests:   
            codechefContest = {}
            codechefContest["platform"] = "CodeChef"
            codechefContest["contestName"] = "Codechef " + contest["contest_name"]
            codechefContest["contestLink"] = "https://www.codechef.com/" + str(contest["contest_code"])
            
            # Parse the ISO date string from CodeChef
            utc_time = datetime.fromisoformat(contest["contest_start_date_iso"].replace('Z', '+00:00'))
            # Convert to IST
            ist_time = utc_time.astimezone(pytz.timezone('Asia/Kolkata'))
            codechefContest["startTime"] = ist_time.strftime('%Y-%m-%dT%H:%M:%S') + '+05:30'
            
            
            codechefContest["contestDuration"] = "0" + str(int(contest["contest_duration"])//60) + ":00 hours."
            codechefContests.append(codechefContest)
    return codechefContests
print(getCodechefContests())
