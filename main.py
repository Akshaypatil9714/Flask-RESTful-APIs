from flask import Flask, jsonify 
from werkzeug.exceptions import BadRequest, NotFound, MethodNotAllowed, InternalServerError
from extensions import db, jwt
from auth import auth_bp
from users import user_bp
from fitnessFileUpload import file_upload_bp
from publicroute import fitness_bp

def create_app():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqlite3"
    app.config['JWT_SECRET_KEY']="4c5e63801c81b198510eecf4"
    app.config['MAX_CONTENT_LENGTH']= 1 * 1024 * 1024

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(file_upload_bp, url_prefix='/fitnessData')
    app.register_blueprint(fitness_bp, url_prefix='/fitness')

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({"message": "Token has expired", "error": "token_expired"}), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Verification failed", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "message": "Request does not contain valid token",
                    "error": "authorization_header",
                }
            ),
            401,
        )

    @app.errorhandler(BadRequest)
    def handle_bad_request(e):
         return (
            jsonify(
                {
                    "message": "It is a bad request",
                    "error": "bad_request",
                }
            ),
            400,
        )

    @app.errorhandler(NotFound)
    def handle_resource_not_exist(e):
         return (
            jsonify(
                {
                    "message": "Requested resource does not exists!",
                    "error": "resource_not_exist",
                }
            ),
            404,
        )

    @app.errorhandler(MethodNotAllowed)
    def handle_method_not_allowed(e):
         return (
            jsonify(
                {
                    "message": "The method is not allowed!",
                    "error": "method_not_allowed",
                }
            ),
            405,
        )

    @app.errorhandler(InternalServerError)
    def handle_internal_server_error(e):
        return (
            jsonify(
                {
                    "message": "An internal server error occured!",
                    "error": "server_error",
                }
            ),
            500,
        )
        

    

    return app
