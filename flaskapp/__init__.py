from flask import Flask
import os




app = Flask(__name__)
app.config["APP_SETTINGS"] = os.getenv("APP_SETTINGS")