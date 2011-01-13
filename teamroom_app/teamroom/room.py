from teamroom.models.room import Room
from teamroom import request

class Handler(request.RequestHandler):
    def get( self, slug ):
        
        room = Room.get_by_slug(slug);

        if not room:
            return self.error(404)

        path = "templates/room.html"

        template_values = {
            "room": room,
        }

        self.render_template(path, template_values)

