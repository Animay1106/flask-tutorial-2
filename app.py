from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
import os

app = Flask(__name__)

@app.route("/")
def hi():
  JOBS = load_jobs_from_db()
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def getjobs():
  JOBS = load_jobs_from_db()
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
