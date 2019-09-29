from flask import Flask, escape, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG']= True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:lc101@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(255))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/', methods=['POST', 'GET'])
@app.route('/blog', methods=['POST', 'GET'])
def index():
    return render_template('blog.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        new_title = request.form['title']
        new_body = request.form['body']
        new_post = Post(new_title, new_body)
        db.session.add(new_post)
        db.session.commit()
    else: 
        return "<h1>Sorry, there was a problem Add</h1>"

    return render_template('newpost.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return render_template('login.html')
    else:
        return "<h1>Sorry, there was a problem Login</h1>"
    

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        return render_template('register.html')
    else:
        return "<h1>Sorry, there was a problem Register</h1>"
    
@app.route('/confirmation', methods=['POST', 'GET'])
def confirmation():
    if request.method == 'POST':
        return render_template('confirmation.html')
    else:
        return "<h1>Sorry, there was a problem Confirmation</h1>"

if __name__ == '__main__':
    app.run()