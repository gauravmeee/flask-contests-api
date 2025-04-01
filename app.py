from flask import Flask, render_template
from flask_restful import Api, Resource
from flask_cors import CORS  # Import CORS
import contest_scrap


app = Flask(__name__)
# Configure CORS with specific settings
CORS(app, resources={
    r"/*": {
        "origins": [
            "https://mycodebank.vercel.app",  # Your production frontend
            "http://localhost:3000",          # Local development
            "http://127.0.0.1:3000"          # Alternative local development
        ],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Accept"],
        "supports_credentials": True
    }
})

api = Api(app)

# Define API resource for fetching contest data
class cpAPI(Resource):
    @staticmethod
    def get():
        return contest_scrap.fetchContests() # Call scrap function to get latest contest data

# Add API resource to Flask app with endpoint '/'
api.add_resource(cpAPI, "/") # Whenever a request is made to '/', call the cpAPI class. The get() method inside cpAPI will handle GET requests.


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000) # Uncomment this to run on all network interfaces
    app.run(debug=True) # Run in debug mode (auto-restarts on code changes)