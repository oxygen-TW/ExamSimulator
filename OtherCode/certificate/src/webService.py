from server import *
import flask
from flask import send_file
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def checkFile(id):
    if (not(os.path.isfile("server/{0}.pub".format(id)))):
        return False
    else:
        return True

@app.route('/newKey/<id>', methods=['GET'])
def newKey(id):
    rsa = RSATools()
    rsa.GenerateKey("server/{0}.pem".format(id),"server/{0}.pub".format(id),1024)
    path = "server/{0}.pem".format(id)
    return send_file(path, as_attachment=True)

@app.route('/check/<id>', methods=['POST'])
def check(id):
    print(id)
    if(not(checkFile(id))):
        return "Not found"
        
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('server/tmp', id + ".bin"))
    
    rsa = RSATools()
    try:
        code = rsa.Decode("server/{0}.pub".format(id),"server/tmp/{0}.bin".format(id))
    except Exception as identifier:
        return "False"
    
    if(code == id):
        return "True"
    else:
        return "False"


app.run()