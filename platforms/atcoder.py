from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
from pytz import timezone

def getAtCoderContests():
    url = "https://atcoder.jp/contests/"
    response = requests.get(url)
    atCoderContests = []

    if response.status_code == 200:
        soup = bs(response.content, "html.parser")
        contests = soup.select("#contest-table-upcoming tbody tr")

        for contest in contests:
            elements = contest.find_all("td")

            atCoderContest = {
                "platform": "AtCoder",
                "contestName": elements[1].text.strip().split("\n", 1)[-1],  # More robust extraction
                "contestLink": "https://atcoder.jp" + elements[1].select_one("a")["href"],
                "startTime": datetime.strptime(elements[0].text.strip(), "%Y-%m-%d %H:%M:%S%z")
                                      .astimezone(timezone("Asia/Kolkata"))
                                      .strftime("%Y-%m-%d %H:%M:%S %Z"),
                "contestDuration": elements[2].text.strip()  # Keeping original format
            }
            atCoderContests.append(atCoderContest)

    return atCoderContests

print(getAtCoderContests())
