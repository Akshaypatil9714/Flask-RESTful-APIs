from flask import Blueprint, jsonify
from models import User

fitness_bp = Blueprint('fitness', __name__)


# Sample fitness articles
fitness_articles = [
    {
        "id": 1,
        "title": "Get Started with Cardio",
        "content": "Cardio workouts are great for improving cardiovascular health.",
    },
    {
        "id": 2,
        "title": "Strength Training Tips",
        "content": "Learn how to build strength with weightlifting exercises.",
    },
    {
        "id": 3,
        "title": "Healthy Eating Habits",
        "content": "Discover the importance of a balanced diet for your fitness journey.",
    },
]

@fitness_bp.get("/registered-users")
def get_registered_users():
    # Query the SQLite database to count the registered users
    registered_users_count = User.query.count()

    return jsonify({"registered_users": registered_users_count}), 200

@fitness_bp.get("/fitness-articles")
def get_fitness_articles():
    return jsonify(fitness_articles), 200
