from flask import Blueprint, request, jsonify

from app.models import db
from app.models.user import UserModel
from app.schemas.user_schema import UserSchema

from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

import uuid


users_bp = Blueprint("users", __name__)


@users_bp.post("/user")
def create_user():
    schema = UserSchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    user = UserModel(name=data["name"])
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User already exists"}), 409

    return jsonify(schema.dump(user)), 201


@users_bp.get("/users")
def get_users():
    schema = UserSchema(many=True)
    users = UserModel.query.all()
    return jsonify(schema.dump(users)), 200


@users_bp.get("/user/<int:user_id>")
def get_user(user_id):
    user = UserModel.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    schema = UserSchema()
    return jsonify(schema.dump(user)), 200


@users_bp.delete("/user/<int:user_id>")
def delete_user(user_id):
    user = UserModel.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200
