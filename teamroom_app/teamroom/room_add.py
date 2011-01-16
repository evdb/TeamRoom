from google.appengine.ext import webapp
from teamroom.models.room import Room
from teamroom.models.membership import Membership
from teamroom import request

class Handler(request.RequestHandler):

    def get( self ):
        self.display_form();

    def post( self ):

        # get the room name from form
        room_name = self.request.get( "room_name" ).strip()
        slug      = Room.convert_name_to_slug( room_name )
        error     = None

        # check that the name and slug are OK
        if not Room.is_name_valid( room_name ):
            error = 'Room name not valid: ' + Room.name_requirements()
        elif Room.is_slug_taken( slug ):
            error = 'Room name is already taken'

        # bail out if there was a problem
        if error:
            return self.display_form( error= error, room_name= room_name )

        # create the room
        room = Room( name=room_name, slug=slug )
        room.put()

        # link room to user
        membership = Membership( room=room, member=self.get_current_member() )
        membership.put()
        
        self.redirect( "/" + room.slug )


    def display_form( self, error="", room_name="" ):

        path = "templates/room_add.html"

        template_values = {
            "error":     error,
            "room_name": room_name,
        }
        
        self.render_template(path, template_values);
        