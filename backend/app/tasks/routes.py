from flask import Blueprint, request, jsonify
from ..models import Task
from ..extensions import db


tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/', methods=["POST"])
def create_task():
    data=request.get_json()

    if not data or "title" not in data:
        return {"error":"Task title required"}, 400

    task=Task(title=data["title"])
    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201

@tasks_bp.route("/", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@tasks_bp.route("/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()

    if "title" in data:
        task.title = data["title"]
    if "completed" in data:
        task.completed = data["completed"]

    db.session.commit()
    return jsonify(task.to_dict())

@tasks_bp.route("/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return {"message": "Task deleted"}, 200
