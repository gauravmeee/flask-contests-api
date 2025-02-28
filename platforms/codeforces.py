import requests
import json
from datetime import datetime
import pytz


def getCodeforcesContests():
    response = requests.get("https://codeforces.com/api/contest.list")
    codeforcesContests = []
    if response.status_code == 200:
        jsonResponse = json.loads(response.text)
        contests = jsonResponse["result"]
        for contest in contests:
            if contest["phase"] == "BEFORE":
                codeforcesContest = {}
                codeforcesContest["platform"] = "CodeForces"
                codeforcesContest["contestName"] = contest["name"]
                codeforcesContest["contestLink"] = "https://codeforces.com/contests/" + str(contest["id"])
                
                # Create datetime from UTC timestamp and convert to IST
                utc_time = datetime.fromtimestamp(contest["startTimeSeconds"], tz=pytz.UTC)
                ist_time = utc_time.astimezone(pytz.timezone('Asia/Kolkata'))
                codeforcesContest["startTime"] = ist_time.strftime('%Y-%m-%dT%H:%M:%S') + '+0530'
                
                codeforcesContest["contestDuration"] = f"{int(contest['durationSeconds']) // 3600:02d}:{int((contest['durationSeconds']) % 3600) // 60:02d} hours"
                codeforcesContests.append(codeforcesContest)
    return codeforcesContests
print(getCodeforcesContests())
