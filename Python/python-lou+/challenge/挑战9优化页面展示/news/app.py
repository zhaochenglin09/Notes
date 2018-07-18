from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flaskapp'
db = SQLAlchemy(app)
client = MongoClient('127.0.0.1', 27017)
dbm = client.shiyanlou

class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category')

    def __init__(self,title, created_time, category, content):
        self.title = title
        self.created_time = created_time
        self.content = content
        self.category = category

    def add_tag(self, tag_name):
        title = self.title
        tags = {'title': title, 'tag': tag_name}
        dbm.tags.insert_one(tags)
        

    def remove_tag(self, tag_name):
        title = self.title
        dbm.tags.delete_one({'title': title, 'tag': tag_name})

    @property
    def tags(self): 
        tagres = list()
        title = self.title
        tags = dbm.tags.find({'title': title}, {'tag': 1, '_id': 0})
        for tagdict in tags:
            tagres.append(tagdict['tag'])
        self.tagres = tagres    
        return self.tagres
  
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



def insert_datas():
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
    file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
    file1.add_tag('tech')
    file1.add_tag('java')
    file1.add_tag('linux')
    file2.add_tag('tech')
    file2.add_tag('python')





if __name__ == '__main__':

    db.create_all() 
    if not Category.query.filter_by(name='Java').first():
        insert_datas()
    app.run()



@app.route('/files/<file_id>')
def file(file_id):
   exist = File.query.filter_by(id=file_id)
   if any(exist):
       return render_template('file.html',id=exist)
   else:
       return render_template('404.html'), 404



