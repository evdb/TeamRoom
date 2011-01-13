from google.appengine.ext import db
import logging
import re

class Room(db.Model):
    name    = db.StringProperty(required=True)
    slug    = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    
    @classmethod
    def get_by_slug( self, slug ):
        query  = db.Query(self).filter("slug =", slug)
        return query.get()
    
    @classmethod
    def is_name_valid( self, name ):
        regex = re.compile(r'[a-z][a-z0-9 ]{3,19}$', re.IGNORECASE)
        return regex.match(name)

    @classmethod
    def name_requirements( self ):
        return """Room names must be made up only of letters, 
            numbers or spaces, must be 4 to 20 letters long and 
            must start with a letter"""

    @classmethod
    def convert_name_to_slug( self, name ):
        slug = name
        slug = slug.lower()
        slug = re.sub( r'[^a-z0-9]+', '-', slug )
        slug = slug.strip('-')
        # logging.debug( "name to slug: '%s' to '%s'" % (name, slug) )        
        return slug

    @classmethod
    def is_slug_taken( self, slug ):
        query = db.Query(self, keys_only=True).filter("slug =", slug)
        return bool( query.count() )
