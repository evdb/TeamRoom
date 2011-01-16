from google.appengine.ext   import db

class Member(db.Model):

    user_id            = db.StringProperty(required=True)
    # federated_identity = db.StringProperty(required=True)
    # federated_provider = db.StringProperty(required=True)

    name               = db.StringProperty(required=True)
    email              = db.StringProperty(required=True)

    created            = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_or_insert_from_user( self, user ):

        member_key = self.create_key_from_user( user )
        
        member = self.get_or_insert(
            member_key,
            user_id = user.user_id(),            
            name    = user.nickname(),
            email   = user.email(),
        )
        member.put()
        
        return member
    
    @classmethod
    def create_key_from_user( self, user ):
        return user.user_id()
        