from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

from teamroom import holding

def main():
    application = webapp.WSGIApplication(
        [
            ('/', holding.Handler),
        ],
        debug=True
    )
    
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()