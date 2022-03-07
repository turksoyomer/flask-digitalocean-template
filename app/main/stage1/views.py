from . import stage1
from .forms import *
from flask import render_template

@stage1.route('/')
def index():
    # bu index stage1e ait.
    # route pathi 'www.siteadi.com/stage1/' şeklinde olacaktır.
    # Main blueprinti oluşturulurken prefix vermediğimiz için 'www.siteadi.com/main/stage1/' şeklinde oluşmaz.
    # örneğin panelde prefix panel olarak ayarlandı. Orada tanımlanan iç blueprintler önüne '/panel/' alacaktır.
    return render_template('main/stage1/index.html')