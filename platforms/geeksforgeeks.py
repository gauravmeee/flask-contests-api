
import requests
import json
from datetime import datetime


def getGeeksforgeeksContests():
    response = requests.get("https://practiceapi.geeksforgeeks.org/api/latest/events/recurring/gfg-weekly-coding-contest")
    geeksforgeeksContests = []
    if response.status_code == 200:
        jsonResponse = json.loads(response.text)
        contests = jsonResponse["upcoming_entity_details"]
        for contest in contests:
            geeksforgeeksContest = {}
            geeksforgeeksContest["platform"] = "GeeksforGeeks"
            geeksforgeeksContest["contestName"] = contest["name"]
            geeksforgeeksContest["contestLink"] = contest["event_entity_url"]
            geeksforgeeksContest["startTime"] = contest["start_time"] + '+0530'
            geeksforgeeksContest["contestDuration"] = "0" + str(int(contest["total_time"])//60) + ":00 hours."
            geeksforgeeksContests.append(geeksforgeeksContest)
    return geeksforgeeksContests
print(getGeeksforgeeksContests())
