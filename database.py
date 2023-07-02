from sqlalchemy import create_engine, text
import os

ssl_args = {
  "ssl": {
    "ssl_ca": "ca.pem",
    "ssl_cert": "client-cert.pem",
    "ssl_key": "client-key.pem"
  }
}


db_connection_string = os.environ['DB_CONN_STRING']

engine = create_engine( db_connection_string,connect_args=ssl_args)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
  result_dicts = []
  for row in result.all():
    result_dicts.append(row._asdict())
  return result_dicts

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs where id = :val'), parameters=dict(val=id))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()

def add_application_to_db(job_id, application):
  with engine.connect() as conn:
    query = text("Insert into applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url )")

    data = {  'job' : job_id,
    'full_name' : application['full_name'],
    'email' : application['email'],
    'education' :application['education'],
    'work_experience' : application['work_experience'],
    'linkedin_url' : application['linkedin_url'],
    'resume_url' : application['resume_url']}
    conn.execute(query, data )