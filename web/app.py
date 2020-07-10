# app.py

from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        post = Post(text)
        db.session.add(post)
        db.session.commit()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/api/test', methods=['GET'])
def test():
    return "Test API"

@app.route('/api/delete', methods=['POST'])
def deleteItem():
    return "Delete Item API"

if __name__ == '__main__':
    app.run()


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         text = request.form['text']
#         post = Post(text)
#         db.session.add(post)
#         db.session.commit()
#     posts = Post.query.order_by(Post.date_posted.desc()).all()
#     return render_template('index.html', posts=posts)

# if __name__ == '__main__':
#     app.run()
