from flask import Flask, render_template, redirect
from collector import run_collector
from database import init_db, get_logs

app = Flask(__name__)
init_db()

@app.route("/")
def index():
    return render_template("index.html", logs=get_logs(5))

@app.route("/run")
def run():
    run_collector()
    return redirect("/")

@app.route("/logs")
def logs():
    return render_template("logs.html", logs=get_logs(100))

if __name__ == "__main__":
    app.run(debug=True)
