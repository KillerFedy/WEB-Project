from importlib.resources import path
from flask import Flask, render_template
from pathlib import Path


app = Flask(__name__)

POSTS_DIR = Path('products')

if not POSTS_DIR.exists():
    POSTS_DIR.mkdir()


def get_products():
    products = []
    for file in POSTS_DIR.iterdir():
        with open(file, 'rt', encoding="utf-8") as f:
            lines = f.read().split('\n')
        product = {"name": lines[0], "description": lines[1]}
        products.append(product)
    return products



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = "Магазин Шаурмы", products = get_products())