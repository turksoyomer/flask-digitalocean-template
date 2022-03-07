from . import main
from .forms import *
from flask import render_template

@main.route('/')
def index():
    example_form = ExampleForm()
    if example_form.validate_on_submit():
        string = example_form.string_field.data
    return render_template('main/index.html', example_form=example_form)