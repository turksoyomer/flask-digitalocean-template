from flask import Blueprint

stage1 = Blueprint('stage1', __name__, url_prefix='/stage1')

from . import views