import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = 'testkey'
DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'qik-website.db')
DATABASE_CONNECT_OPTIONS = {}
ADMINS = frozenset(['http://aquariusoft.org/'])

del os
