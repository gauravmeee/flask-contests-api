
import requests
import json
from datetime import datetime


def getGeeksforgeeksContests():
    response = requests.get("https://practiceapi.geeksforgeeks.org/api/vr/events/?page_number=1&sub_type=all&type=contest")
    geeksforgeeksContests = []
    if response.status_code == 200:
        jsonResponse = json.loads(response.text)
        contests = jsonResponse["results"]["upcoming"]
        for contest in contests:
            geeksforgeeksContest = {}
            geeksforgeeksContest["platform"] = "GeeksforGeeks"
            geeksforgeeksContest["contestName"] = contest["name"]
            geeksforgeeksContest["contestLink"] = "https://practice.geeksforgeeks.org/contest/" + contest["slug"]
            geeksforgeeksContest["startTime"] = contest["start_time"] + '+0530'
            duration = datetime.strptime(contest["end_time"], "%Y-%m-%dT%H:%M:%S") - datetime.strptime(contest["start_time"], "%Y-%m-%dT%H:%M:%S")
            geeksforgeeksContest["contestDuration"] = f"{int(duration.total_seconds()) // 3600:02d}:{int((duration.total_seconds()) % 3600) // 60:02d} hours"
            geeksforgeeksContests.append(geeksforgeeksContest)
    return geeksforgeeksContests
print(getGeeksforgeeksContests())
