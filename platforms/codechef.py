import requests
import json
from datetime import datetime


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
            codechefContest["startTime"] = contest["contest_start_date_iso"]
            codechefContest["contestDuration"] = "0" + str(int(contest["contest_duration"])//60) + ":00 hours."
            codechefContests.append(codechefContest)
    return codechefContests
print(getCodechefContests())
