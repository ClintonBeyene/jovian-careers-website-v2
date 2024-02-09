from flask import Flask, render_template, jsonify
from database import get_connection, get_connection_from_db

app = Flask(__name__)
  
@app.route("/")
def hello_world():
  jobs = get_connection()
  return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def job_lists():
  jobs = get_connection()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = get_connection_from_db(id)

  if not job:
    return "Not Found", 404
  else:
    return render_template('jobpage.html', job=job)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  