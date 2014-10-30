from flask import Flask
from flask import request
import os, sys
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
    if request.method == 'GET':
	return "Get Command\n"
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

@app.route("/heya/")
def hey():
     return "Hello Guy! Welcome to my page"

@app.route("/square/<int:number>")
def squarenum(number):
     return number*number

#Code found through google
@app.route("/files")
def list_files():
     path = "./uploads/"
     dirs = os.listdir(path)
     for file in dirs:
	print file

@app.route("/euler1")
def euler1():
     sum = 0
     for i in range (1, 1000):
	if i%3 or i%5:
	   sum = sum + i
     print sum
