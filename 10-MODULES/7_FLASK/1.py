from flask import Flask
app = Flask(__name__)

@app.route("/")
def greet():
    return "Hello dear hitesh welcomes you in website! "

@app.route("/about")
def details():
    return " this is my first website which i make with flask and python "
    
app.run(debug=True)
