from . import panel
from flask import render_template

@panel.route('/')
def index():
    return render_template('panel/index.html')