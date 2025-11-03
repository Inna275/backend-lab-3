from flask import Blueprint, jsonify
from datetime import datetime


general_bp = Blueprint("general", __name__)


@general_bp.route("/")
def greeting():
    return jsonify({
        "message": "Hello!"
    }), 200


@general_bp.route("/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({
        "status": "ok", 
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }), 200
    