from flask import Blueprint

main = Blueprint('main', __name__)

from .stage1 import stage1 as stage1_blueprint
main.register_blueprint(stage1_blueprint)

from . import views