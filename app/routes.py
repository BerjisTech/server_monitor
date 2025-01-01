from flask import Blueprint, jsonify, request
from .models import Server

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return jsonify({"message": "Welcome to the Server Monitor API!"})

@main_bp.route("/servers", methods=["GET"])
def list_servers():
    """List all monitored servers."""
    servers = Server.query.all()
    return jsonify([server.to_dict() for server in servers])

@main_bp.route("/servers", methods=["POST"])
def add_server():
    """Add a new server to monitor."""
    data = request.json
    new_server = Server(
        name=data.get("name"),
        ip_address=data.get("ip_address"),
        status="unknown"  # Default status
    )
    db.session.add(new_server)
    db.session.commit()
    return jsonify(new_server.to_dict()), 201
