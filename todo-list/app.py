from flask import Flask, render_template, request, redirect, url_for
from db import db

from service import add_item, get_all_items, change_item_status, delete_item


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db.init_app(app)


@app.route("/")
def home():
    items = get_all_items()
    # print(items)

    return render_template('index.html', items=items)


@app.route('/about')
def about():

    return render_template('about.html')


@app.route('/add')
def add():

    return render_template('add.html')


@app.route('/create', methods=['POST'])
def create():
    item_data = {"description": request.form['description']}
    item_id = add_item(item_data)
    print(f"Item id: {item_id}")

    return redirect(url_for('home'))


@app.route('/remove/<int:item_id>')
def remove(item_id: int):
    deleted_item_id = delete_item(item_id)
    print(f"Item {deleted_item_id} was deleted")

    return redirect(url_for('home'))


@app.route('/toggle-status/<int:item_id>')
def change_status(item_id: int):
    change_item_status(item_id)

    return redirect(url_for('home'))

