from flask import Flask
import os

"""
This file defines global variables and config values
"""


package_dir = os.path.dirname(
    os.path.abspath(__file__)
)

templates = os.path.join(
    package_dir, "templates"
)

app = Flask('this is a simple web application', template_folder=templates)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '69cae04b04756f65eabcd2c5a11c8c24'
# Previously:
# # if the user supplies a database file name, we use
# # that instead, and it should an absolute path
# # for windows user, C:\ is the root directory, so it
# # should not be included. e.g. Users/xxx/Document/db.sqlite
# We no longer do this, since set_db_path will be called with
# a temp dir from tempfile.TemporaryDirectory(), which WILL
# have the drive letter specifier on it. In other words, this
# should always take an absolute path, including drive specifier
# on Windows.
db_name_from_env = os.getenv('DB_NAME')
db_string = os.getenv('db_string')
def set_db_path(db_path: str):
    if db_path:
        database_url = "sqlite:///" + db_path
    elif db_string:
        database_url = db_string
    else:
        # Default to using 'db.sqlite' file in current directory.
        database_url = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
set_db_path(db_name_from_env)