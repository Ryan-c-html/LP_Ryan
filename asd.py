from flask import Flask
app = Flask(__name__)

@app.route("/")
def heloo():
    return "<h1>adsadsa</h1>"
app.run()