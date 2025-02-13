# Competitive Programming Contests API

This is a Flask-based RESTful API that scrapes and caches upcoming competitive programming contests from multiple platforms.

## Features
- Fetches contest data from platforms like Codeforces, CodeChef, AtCoder, HackerRank, HackerEarth, and GeeksforGeeks.
- Uses Upstash Redis for caching to improve performance.
- CORS enabled for cross-origin requests.
- Simple REST API endpoint.

## Installation

### Prerequisites
- Python 3.x
- Redis (Upstash Redis recommended)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/gauravmeee/flask-contests-api.git
   cd flask-contest-api
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv myenv
   source myenv/bin/activate  # On Windows, use 'myenv\\Scripts\\activate'
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file and set the Redis credentials:
   ```ini
   REDIS_HOST=gorgeous-rodent-12506.upstash.io
   REDIS_PORT=6379
   REDIS_PASSWORD=your_redis_password
   ```

## Usage
Run the Flask app:
```sh
python app.py
```

By default, the API runs on `http://127.0.0.1:5000/`.

## API Endpoint

### Fetch Contests
- **Endpoint:** `/`
- **Method:** `GET`
- **Response:** JSON object containing upcoming contests.
- **Example Response:**
  ```json
  {
      "contests": [
          {
              "name": "Codeforces Round 1234",
              "url": "https://codeforces.com/contest/1234",
              "startTime": "2024-02-15T12:00:00Z"
          },
          {
              "name": "CodeChef Starters 99",
              "url": "https://www.codechef.com/START99",
              "startTime": "2024-02-16T18:00:00Z"
          }
      ]
  }
  ```

## Technologies Used
- **Flask** (REST API framework)
- **Flask-RESTful** (API management)
- **Flask-CORS** (CORS support)
- **Redis (Upstash)** (Caching system)
- **Python-dotenv** (Environment variable management)

## License
This project is licensed under the MIT License.

