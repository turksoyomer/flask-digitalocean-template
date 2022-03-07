from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from .panel import panel as panel_blueprint
from .main import main as main_blueprint

app.register_blueprint(panel_blueprint)
app.register_blueprint(main_blueprint)