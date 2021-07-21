from flask import Flask, render_template, request,session
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
#import json
#with open('config.json','r') as c:
#     params= json.load(c)["params"]

params={"local_server": "True",
      "admin_user": "amitmakkad18@gmail.com",
      "admin_password": "am",
       "upload_location":"C:\\Users\\dell\\PycharmProjects\\pythonProject\\faceregcognitionml\\ImageBasics"
        }

app=Flask(__name__)
app.config['UPLOAD_FOLDER']=params['upload_location']

app.secret_key='super-secret-key'

@app.route("/dashboard",methods=['GET','POST'])
def dashboard():
    # if ('user' in session and session['user']==params['admin_user']):
    #     return render_template('dashboard.html',params=params)

    if request.method=='POST':
        username=request.form.get('uname')
        userpass=request.form.get('pass')
        if username==params['admin_user'] and userpass==params['admin_password']:
            # session['user']=username
            return render_template('dashboard.html',params=params)

        else:
            

            return render_template('login.html',params=params)
    return render_template('login.html',params=params)

@app.route("/uploader",methods=['GET','POST'])
def uploader():
    if(request.method=='POST'):
        f=request.files['file1']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        return "upload success"

@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)