import requests
from datetime import datetime
import pytz
import json

def getLeetcodeContests():
    leetcodeContests = []
    
    try:
        # LeetCode GraphQL API endpoint
        url = "https://leetcode.com/graphql"
        
        # GraphQL query to fetch contests
        query = """
        query {
            allContests {
                title
                titleSlug
                startTime
                duration
                isVirtual
                originStartTime
                company {
                    name
                }
            }
        }
        """
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Origin": "https://leetcode.com",
            "Referer": "https://leetcode.com/contest/",
            "X-Requested-With": "XMLHttpRequest"
        }
        
        # Make the GraphQL request
        response = requests.post(
            url,
            json={"query": query},
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            
            if "data" in data and "allContests" in data["data"]:
                contests = data["data"]["allContests"]
                current_time = datetime.now(pytz.UTC)
                
                for contest in contests:
                    try:
                        # Convert contest start time to datetime
                        start_time = datetime.fromtimestamp(contest["startTime"], tz=pytz.UTC)
                        
                        # Skip if contest has already started
                        if start_time <= current_time:
                            continue
                            
                        title = contest["title"]
                        link = f"https://leetcode.com/contest/{contest['titleSlug']}"
                        
                        # Convert to IST for display
                        ist_timezone = pytz.timezone("Asia/Kolkata")
                        ist_time = start_time.astimezone(ist_timezone)
                        
                        # Format duration
                        duration_seconds = contest["duration"]
                        hours = duration_seconds // 3600
                        minutes = (duration_seconds % 3600) // 60
                        duration_str = f"{hours:02d}:{minutes:02d} hours"
                        
                        # Create contest object
                        leetcodeContest = {
                            "platform": "LeetCode",
                            "contestName": title,
                            "contestLink": link,
                            "startTime": ist_time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                            "contestDuration": duration_str
                        }
                        
                        leetcodeContests.append(leetcodeContest)
                        print(f"Successfully added upcoming contest: {title}")
                        
                    except Exception as e:
                        print(f"Error processing contest {title}: {e}")
                        continue
                        
        else:
            print(f"Failed to fetch contests. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"Error fetching LeetCode contests: {e}")
        
    print(f"Total upcoming contests found: {len(leetcodeContests)}")
    return leetcodeContests

if __name__ == "__main__":
    contests = getLeetcodeContests()
    print("\nFinal contests list:")
    print(json.dumps(contests, indent=2))