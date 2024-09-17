from flask import Blueprint

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/hello-world')
def hello_world():
    return 'Hello, World!'

@main_routes.route('/main')
def main():
    # Aquí podrías llamar a un método de un controlador si es necesario
    return 'Hello from UserController!'
