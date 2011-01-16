import logging
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users

from teamroom.models.member import Member

class RequestHandler(webapp.RequestHandler):
    def render_template( self, path, template_values ):

        # add the user to the template as well as the login/out links
        user   = users.get_current_user()
        member = self.get_current_member()
        template_values["user"] = user
        template_values["member"] = member

        if user:
            template_values["logout_url"] = users.create_logout_url('/')
        else:
            template_values["login_url"] = users.create_login_url( self.request.url )

        self.response.out.write(
            template.render(path, template_values)
        )

    def get_current_member( self ):
        user = users.get_current_user();
        return Member.get_or_insert_from_user( user );