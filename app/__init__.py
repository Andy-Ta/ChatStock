from flask import Flask

app = Flask(__name__)
app.secret_key = 'gietmamaw'

from app.routes import views, api
