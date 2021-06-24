import os
import sqlite3
import click

from flask import Flask, render_template, send_from_directory,Response, current_app, g
from dotenv import load_dotenv
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        
load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')

@app.route('/')
def index():
    # Ji-Oh just change the home.html to index.html to see your index.html
    return render_template('home.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/health', methods=["GET"])
def health():
    return Response("Something Here"), 200

