from curses import flash
import os
from flask import Blueprint, jsonify, request, send_file
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

file_upload_bp = Blueprint('fitnessData', __name__)

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@file_upload_bp.post("/fileUpload")
@jwt_required()
def upload_fitness_file():
    try:
        if 'file' not in request.files:
            return jsonify({
                "error": "Missing file, choose a file to upload"
            }, 400)
        fitness_file = request.files['file']
        if fitness_file.filename == '':
            flash('No selected file')
            return jsonify({
                "error": "Missing file, choose a file to upload"
            }, 400)
        file_type_accepted = allowed_file(fitness_file.filename)

        if not file_type_accepted:
            return jsonify({
                "error": "File type not allowed"
            }, 400 )


        if fitness_file and file_type_accepted:
            filename = secure_filename(fitness_file.filename)
            fitness_file.save(os.path.join('fitnessFiles/', filename))
            return jsonify({
                "message": "Fitness file uploaded"
            }, 200)
    except RequestEntityTooLarge:
        return jsonify({
                "error": "File is larger than 1MB"
            }, 400)

        

@file_upload_bp.get("/files/<filename>")
def get_uploaded_file(filename):
    try:
        file_path = os.path.join('fitnessFiles', filename)
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        return jsonify({
            "error": "File not found"
        }, 404)