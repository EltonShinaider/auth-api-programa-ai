from flask import Blueprint, request, jsonify
from ..models import User
from ..auth.service import create_user, authenticate
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint("users", __name__, url_prefix="/users")

@bp.post("")
def register():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 409
    
    user = create_user(email, password)
    
    return jsonify({"id": user.id, "email": user.email}), 201

@bp.post("/login")
def login():
    data = request.get_json() or {}
    token = authenticate(data.get("email", ""), data.get("password", ""))
    if not token:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"access_token": token}), 200

@bp.get("")
@jwt_required()
def list_user():
    
    _ = get_jwt_identity
    
    users = User.query.with_entities(User.id, User.email).all()
    
    return jsonify([{"id" : u.id, "email" : u.email} for u in users])