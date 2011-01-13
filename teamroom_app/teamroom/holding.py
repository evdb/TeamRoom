from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class Handler(webapp.RequestHandler):
    def get(self):
        path = "templates/holding.html"
        template_values = {}
        self.response.out.write(
            template.render(path, template_values)
        )

