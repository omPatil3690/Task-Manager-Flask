from flask import Blueprint, request, jsonify
from ..models import Task
from ..extensions import db


tasks_bp = Blueprint('tasks', __name__)