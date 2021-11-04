from flask import Flask
from flask.templating import render_template
app = Flask(__name__)


# Refer to https://flask.palletsprojects.com/en/2.0.x/quickstart/

@app.route('/')
def index():
    return render_template("home.html")
    # pass
    # Your code here

@app.route('/aboutme')
def me():
    return render_template("me.html")


if __name__ == "__main__":
    app.run(debug=True)