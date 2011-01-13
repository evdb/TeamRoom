from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from teamroom.models import Room

class Handler(webapp.RequestHandler):
    def get( self, slug ):
        
        room = Room.get_by_slug(slug);

        if not room:
            return self.error(404)

        path = "templates/room.html"

        template_values = {
            "room": room,
        }

        self.response.out.write(
            template.render(path, template_values)
        )

