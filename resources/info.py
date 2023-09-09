from flask_smorest import Blueprint
from flask.views import MethodView
from datetime import datetime
from flask import jsonify, request


blp = Blueprint("Info", "info", description="GET requests on JSON information.")

@blp.route("/api")
class Info(MethodView):
    def get(self):
        slack_name = request.args.get("slack_name")
        track = request.args.get("track")
        data = {
        "slack_name": slack_name,
        "current_day": datetime.utcnow().strftime('%A'),
        "utc_time": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        "track": track,
        "github_file_url": "",
        "github_repo_url": "",
        "status_code": 200
        }
        return jsonify(data)