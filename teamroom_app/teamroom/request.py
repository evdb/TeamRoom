import logging
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users

class RequestHandler(webapp.RequestHandler):
    def render_template( self, path, template_values ):

        # add the user to the template as well as the login/out links
        user = users.get_current_user();
        template_values["user"] = user;

        if user:
            template_values["logout_url"] = users.create_logout_url('/');
        else:
            template_values["login_url"] = users.create_login_url( self.request.url );

        self.response.out.write(
            template.render(path, template_values)
        )

