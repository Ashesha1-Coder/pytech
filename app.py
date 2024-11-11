from flask import Flask
from controller.user_controller import user_controller 
def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_controller)

    @app.route("/")
    def welcome():
        return "hello world"

    @app.route("/home")
    def home():
        return "This is the home page"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
