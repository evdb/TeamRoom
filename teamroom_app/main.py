import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from teamroom import holding

def main():
    application = webapp.WSGIApplication(
        [
            ('/', holding.Handler),
        ],
        debug = on_dev_server()
    )
    
    util.run_wsgi_app(application)

def on_dev_server():
    os.environ['SERVER_SOFTWARE'].startswith('Dev')

if __name__ == '__main__':
    main()
