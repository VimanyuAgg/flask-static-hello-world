from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from app1!"


@app.route("/show")
def showhtml():
	return render_template("show.html")