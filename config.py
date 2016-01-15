# -*- coding: utf-8 -*-
CSRF_ENABLED = True
SECRET_KEY = 'you will-never-guess'
# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50
OPENID_PROVIDERS = [
    {'name' : 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name' : 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name' : 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name' : 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name' : 'MyOpenID', 'url': 'http://www.myopenid.com'}]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True
#slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5
WHOOSH_BASE = os.path.join(basedir, 'search.db')

# Whoosh does not work on Heroku
WHOOSH_ENABLED = os.environ.get('HEROKU') is None

# mail server settings
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

#administrataor list
ADMINS = ['silvercrow1229@gmail.com']

#...
# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = 'microblog_josh_test'
MS_TRANSLATOR_CLIENT_SECRET = 'aYac3jbFP+wADl5C8scW7rmlvmhGZj+r07EPL0jc3js='