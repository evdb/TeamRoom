import os
import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from teamroom import homepage
from teamroom import room_add
from teamroom import room

def main():
    
    # should we produce dubugging?
    enable_debug = on_dev_server()

    # setup logging
    if enable_debug:
        logging.getLogger().setLevel(logging.DEBUG)

    application = webapp.WSGIApplication(
        [
            ('/',             homepage.Handler),
            ('/room_add',     room_add.Handler),
            (r'/([\w\-]*).*', room.Handler),
        ],
        debug = enable_debug
    )
    
    util.run_wsgi_app(application)

def on_dev_server():
    return os.environ['SERVER_SOFTWARE'].startswith('Dev')

if __name__ == '__main__':
    main()
