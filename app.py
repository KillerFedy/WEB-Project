from importlib.resources import path
from unicodedata import category
from flask import Flask, render_template
from pathlib import Path


app = Flask(__name__)

POSTS_DIR = Path('products')
CATEGORIES_DIR = Path('categories')

if not POSTS_DIR.exists():
    POSTS_DIR.mkdir()

if not CATEGORIES_DIR.exists():
    CATEGORIES_DIR.mkdir()

def get_items(PATH):
    items = []
    for file in PATH.iterdir():
        with open(file, 'rt', encoding="utf-8") as f:
            lines = f.read().split('\n')
        item = {"name": lines[0], "description": lines[1]}
        items.append(item)
    return items



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = "Магазин Шаурмы", products = get_items(POSTS_DIR), categories = get_items(CATEGORIES_DIR))