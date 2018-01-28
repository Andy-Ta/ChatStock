from app import app
from flask import render_template, request, flash, redirect, session
from functools import wraps
import json


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', hello="Hello World")
