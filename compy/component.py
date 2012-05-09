'''
Created on 09/05/2012

@author: adam
'''


class Component( object ):
    
    def __init__( self, type, name ):
        super( Component, self ).__init__()

        self.type = type
        self.name = name
        self.entity = None

    def _set_entity( self, entity ):
        self.entity = entity

    def update( self ):
        pass

