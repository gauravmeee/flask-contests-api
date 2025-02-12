from flask import Flask, render_template
from flask_restful import Api, Resource
import scrap

app = Flask(__name__)
api = Api(app)

# Define API resource for fetching contest data
class cpAPI(Resource):
    @staticmethod
    def get():
        return scrap.fetchContests() # Call scrap function to get latest contest data

# Add API resource to Flask app with endpoint /api/contests
api.add_resource(cpAPI, "/api/contests") # Whenever a request is made to /api/contests, call the cpAPI class. The get() method inside cpAPI will handle GET requests.


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000) # Uncomment this to run on all network interfaces
    app.run(debug=True) # Run in debug mode (auto-restarts on code changes)
