from importlib.resources import path
from turtle import title
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

def get_products():
    products = []
    for file in POSTS_DIR.iterdir():
        with open(file, 'rt', encoding="utf-8") as f:
            lines = f.read().split('\n')
        product = {"id": int(lines[0]), "name": lines[1], "description": lines[2],  'browserName': lines[3], 'cost': lines[4]}
        products.append(product)
    return products

def get_category():
    categories = []
    for file in CATEGORIES_DIR.iterdir():
        with open(file, 'rt', encoding="utf-8") as f:
            lines = f.read().split('\n')
        category = {"name": lines[0], "description": lines[1], 'img': lines[2]}
        categories.append(category)
    return categories



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = "Магазин Шаурмы", products = get_products(), categories = get_category())


@app.get('/<browsername>')
def productPage(browsername):
    products = get_products()
    for product in products:
        if browsername == product["browserName"]:
            return render_template('product.html', product = product)
    return 404, "Not Found"