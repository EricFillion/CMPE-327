import pytest
import subprocess
import os
import signal
import time
import tempfile
from qa327 import set_db_path
from qa327.models import db, create_sql_tables
from qa327.__main__ import FLASK_PORT
from qa327.__main__ import app
import threading
from werkzeug.serving import make_server


base_url = 'http://localhost:{}'.format(FLASK_PORT)

class ServerThread(threading.Thread):

    def __init__(self, db_path=None):
        threading.Thread.__init__(self)
        # If we've provided a database file path,
        # set it up in the app's config
        if db_path is not None:
            set_db_path(db_path)
        self.srv = make_server('127.0.0.1', FLASK_PORT, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.srv.serve_forever()

    def shutdown(self):
        self.srv.shutdown()

# Use session scope instead of module for added speed
@pytest.fixture(scope="session", autouse=True)
def server():
    on_win = os.name == 'nt'
    with tempfile.TemporaryDirectory() as tmp_folder:
        # create a live server for testing
        # with a temporary file as database
        db = os.path.join(tmp_folder, 'db.sqlite')
        # ...actually pass the temporary database file path
        # to the server we are creating
        server = ServerThread(db)
        server.start()
        time.sleep(5)
        yield
        server.shutdown()
        time.sleep(2)

# Clean the database after every function that is run
@pytest.fixture(scope="function", autouse=True)
def clean_db():
    # Make sure table structure is properly defined
    create_sql_tables()
    # Remove all data from user and ticket tables
    for table in ['user', 'ticket']:
        # From https://www.techonthenet.com/sqlite/truncate.php
        # "In SQLite, when you execute a DELETE statement without a WHERE clause,
        #    the TRUNCATE optimizer is run instead of the normal delete behavior.
        #    The TRUNCATE optimizer removes all data from the table without the need to
        #    visit each row in the table. This is much faster than a normal delete operation."
        # "You might choose to truncate a table instead of dropping the table and recreating it.
        #    Truncating a table is a faster method of removing all data from the table.""
        sql = "DELETE FROM {};".format(table)
        db.session.execute(sql)
    db.session.commit()
