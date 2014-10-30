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
     files = ""
     for file in dirs:
	files = str(files + file + ", \n")
     return files

@app.route("/euler1")
def euler1():
     sum = 0
     for i in range (1, 1000):
	if i%3 or i%5:
	   sum = sum + i
     return str(sum)

@app.route("/euler2")
def euler2():
     term1 = 1
     term2 = 2
     sum = 0

     for i in range (0, 4000000):
	sum = term1 + term2
	term1 = term2
	term2 = sum
	answer = "Fibinacci up to 4000000 is " + str(sum)
     return answer
