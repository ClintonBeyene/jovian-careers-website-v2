import psycopg2
import psycopg2.extras

hostname = 'dpg-cn1j990l5elc73d919g0-a.singapore-postgres.render.com'
database = 'joviancareers'
username = 'joviancareers_user'
pwd = 'OyQubbAArOP7MUYvAQGAGTNsWCIXvu7U'
port_id = 5432
cur = None
conn = None

def get_connection():
  conn = psycopg2.connect(
  host = hostname,
  dbname = database,
  user = username,
  password = pwd,
  port = port_id
)
  
  cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

  cur.execute('SELECT * FROM jobs')

  jobs = []
  for row in cur.fetchall():
    jobs.append(dict(row))
  return jobs
  
