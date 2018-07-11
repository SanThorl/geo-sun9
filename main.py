from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route("/")

def main():
    return render_template("index.html")
            
@app.route("/compose")

def compose():
    return render_template("compose.html")
