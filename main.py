from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def redirect():
    return render_template("redirect.html")

@app.route("/index/")
def index():
    print("HERE INDEX")
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/experience/")
def experience():
    return render_template("experience.html")

@app.route("/projects/")
def projects():
    return render_template("projects.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.ico')

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, port=8002)
