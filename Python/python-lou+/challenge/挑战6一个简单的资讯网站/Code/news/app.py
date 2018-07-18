from flask import Flask
from flask import render_template

import os
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    path = r'/home/shiyanlou/files'
    filelist = os.listdir(path)
        
    return render_template('index.html', filelist=filelist)    



@app.route('/files/<filename>')
def file(filename):  
    path = r'/home/shiyanlou/files'
    if os.path.exists(os.path.join(path,filename)):
        with open(os.path.join(path,filename),'r') as file:
            file_content = json.loads(file.read())
            return render_template('file.html', content=file_content)

        
    else:    
        return render_template('404.html'), 404



@app.errorhandler(404)
def not_found(error):
        return render_template('404.html'), 404



