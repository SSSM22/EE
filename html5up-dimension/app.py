from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/')

def home():
    return render_template("index.html")
@app.route('/submitted.html')
  
  
def home():
     return render_template("submitted.html")    