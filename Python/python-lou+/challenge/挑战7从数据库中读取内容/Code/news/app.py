from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flaskapp'
db = SQLAlchemy(app)

class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category')

    def __init__(self,title, created_time, content, category):
        self.title = title
        self.created_time = created_time
        self.content = content
        self.category = category


  
class Category(db.Model):  
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    files = db.relationship('File',backref='categories')

    def __init__(self,name):
        self.name = name


    def __repr__(self):
        return self.name
@app.route('/')
def index():
    return render_template('index.html',files=File.query.all())



if __name__ == '__main__':
    app.run()



@app.route('/files/<file_id>')
def file(file_id):
   exist = File.query.filter_by(id=file_id)
   if any(exist):
       return render_template('file.html',id=exist)
   else:
       return render_template('404.html'), 404



