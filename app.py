from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db
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

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobPage.html', job=job)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
