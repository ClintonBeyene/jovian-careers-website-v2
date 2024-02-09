import psycopg2
import psycopg2.extras
import os

cur = None
conn = None

def get_connection():
  global conn, cur
  conn = psycopg2.connect(
  host = os.environ['HOST_NAME'],
  dbname = os.environ['DATABASE'],
  user = os.environ['USERNAME'],
  password = 'OyQubbAArOP7MUYvAQGAGTNsWCIXvu7U',
  port = os.environ['PORT_ID']
)
  
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

  cur.execute('SELECT * FROM jobs')

  jobs = []
  for row in cur.fetchall():
    jobs.append(dict(row))
  return jobs
  
