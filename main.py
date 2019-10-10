from flask import Flask, escape, request, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import jinja2
import os

app = Flask(__name__)
app.config['DEBUG']= True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:lc101@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(255))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/', methods=['POST', 'GET'])
@app.route('/blog', methods=['POST', 'GET'])
def index():
    posts = Blog.query.all()
    new_post = Blog.query
    new_id = new_post

    if new_id.id != 0:
        return render_template('entry.html', posts=posts, new_id=new_id)
    else:
        return render_template('blog.html', posts=posts, page_title="Home", ids=id)

    # if request.method=='GET':
    #     return render_template('blog.html', posts=posts, page_title="Home", ids=id)
    # else:
    #     return "<h1>I'm a post</h1>"
    
    # if posts.id != 0:
    #     blog_id = Blog.query.filter_by(id=id).first()
    #     return render_template('entry.html', posts=posts, blog_id=blog_id)


@app.route('/blog/<string:id>', methods=['POST', 'GET'])
def individ(id):
    posts = Blog.query.all()
    new_id = Blog.id
    blog_id = Blog.query.filter_by(id=id).first()
    return render_template('entry.html', posts=posts, blog_id=blog_id)

@app.route('/add', methods=['POST', 'GET'])
def add():
    posts = Blog.query.all()
    # form_value = request.args.get('id')


    if request.method == 'POST':
        new_title = request.form['title']
        new_body = request.form['body']
        new_post = Blog(new_title, new_body)
        db.session.add(new_post)
        db.session.commit()
        new_id = new_post
        paramater = "/blog?id=" + str(new_id.id)
        # return render_template('individ_entry.html', new_id=new_id)
        return redirect (paramater)

    else:
        return render_template('newpost.html', page_title="Add a New Entry")


if __name__ == '__main__':
    app.run()