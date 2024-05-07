from flask import Flask
from flask import render_template

app = Flask(__name__)

# for add a template in our website we have to put a html file in template file
@app.route("/")
def form():
    return render_template("1_form.html")

# for add video in our website we have to put that video on static file
# also same for pdf image and other things which you want to insert in your website
@app.route("/video")
def video():
    return render_template("1_vid.html")
    
app.run(debug=True)