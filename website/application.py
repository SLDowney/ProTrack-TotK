import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from website.models import *
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Replace 'mysql://username:password@localhost/db_name' with your MySQL connection details
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:BlackFlame!1@localhost/totk_v2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
