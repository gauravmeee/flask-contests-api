# Import required libraries
import json  # To handle JSON data
from platforms import atcoder, codechef, codeforces, hackerearth, hackerrank, geeksforgeeks  # Import platform-specific contest fetchers

def fetchContests():
    """
    Fetches upcoming programming contests from multiple platforms.
    """
    # Fetch contests from various platforms
    contests = []  # Initialize an empty list to store contest data
    contests.extend(codeforces.getCodeforcesContests())  # Fetch contests from Codeforces
    contests.extend(codechef.getCodechefContests())  # Fetch contests from CodeChef
    contests.extend(hackerrank.getHackerrankContests())  # Fetch contests from HackerRank
    # contests.extend(hackerearth.getHackerearthContests())  # Fetch contests from HackerEarth
    contests.extend(geeksforgeeks.getGeeksforgeeksContests())  # Fetch contests from GeeksforGeeks
    contests.extend(atcoder.getAtCoderContests())  # Fetch contests from AtCoder

    # Sort contests by start time
    contests = sorted(contests, key=lambda contest: contest['startTime'])

    # Create the final result dictionary
    result = {"contests": contests}

    return result  # Return the fetched contest data
