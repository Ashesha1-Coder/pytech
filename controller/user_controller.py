from flask import Blueprint

from model.user_model import user_model
obj = user_model()

# Define a Blueprint named 'user_controller'
user_controller = Blueprint('user_controller', __name__)

@user_controller.route("/user")

def user_getall_controller():
    return obj.user_getall_model()