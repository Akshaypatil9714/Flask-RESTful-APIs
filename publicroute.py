from flask import Blueprint, jsonify

fitness_bp = Blueprint('fitness', __name__)

# Sample fitness website content
registered_users = 1000  # Replace with the actual number of registered users

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
    return jsonify({"registered_users": registered_users}), 200

@fitness_bp.get("/fitness-articles")
def get_fitness_articles():
    return jsonify(fitness_articles), 200