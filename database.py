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
