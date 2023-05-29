from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/me', methods=['GET'])
def message():
    if request.method == 'GET':
        print("We recived GET")
        return render_template ("parent.html")  

@app.route('/contact', methods=['GET', 'POST'])
def message_2(): 
    if request.method == 'GET':
        print("We recived GET")
        return render_template ("kid.html")
    elif request.method == 'POST':
        print("We recived POST")
        print(request.method)
        return redirect ("/contact")
    