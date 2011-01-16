from google.appengine.ext   import db
from teamroom.models.room   import Room
from teamroom.models.member import Member

class Membership(db.Model):
    room    = db.ReferenceProperty(required=True, reference_class=Room)
    member  = db.ReferenceProperty(required=True, reference_class=Member)
    is_admin = db.BooleanProperty(default=False, required=True)
    created = db.DateTimeProperty(auto_now_add=True)
