from flask import Flask, render_template, jsonify
from database import get_connection

app = Flask(__name__)
  
@app.route("/")
def hello_world():
  jobs = get_connection()
  return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def job_lists():
  jobs = get_connection()
  return jsonify(jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  