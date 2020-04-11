
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Om@shantiom123@localhost:5432/kmrl"
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2
SESSION_TYPE = 'sqlalchemy'
#SESSION_FILE_DIR = BASE_DIR

SESSION_SQLALCHEMY_TABLE = 'sessions'
SESSION_SQLALCHEMY = ''
#WHOOSH_BASE = "whoosh"
#WHOOSH_BASE = "postgresql://postgres:Om@shantiom123@localhost:5432/kmrl2"

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"
ELASTICSEARCH_URL="http://localhost:9200"
# Secret key for signing cookies
SECRET_KEY = "secret"

