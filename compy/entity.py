'''
Created on 09/05/2012

@author: adam
'''

import weakref

class Entity( object ):
    entities = {}
    
    def __init__( self, name ):
        super( Entity, self ).__init__()

        self.name = name
        self.components = {}
        self.data = {}

        if name in Entity.entities:
            raise ValueError( "Entity name must be unique" )
        Entity.entities[ name ] = weakref.ref( self )

    def __del__( self ):
        del Entity.entities[ self.name ]

    @staticmethod
    def find_entity( name ):
        if name in Entity.entities:
            entity = Entity.entities[ name ]
            if entity == None:
                del Entity.entities[ name ]
                return None
            else:
                return entity()
        return None

    @staticmethod
    def update_entities():
        for entity in Entity.entities.values():
            if entity != None:
                entity().update()
            else:
                del Entity.entities[ name ]

    def add_component( self, component ):
        if component.type in self.components:
            raise ValueError(
                "Component type already registered"
                )
        else:
            component._set_entity( self )
            self.components[ component.type ] = component

    def remove_component( self, type ):
        component = self.components[ type ]
        component._set_entity( None )
        del self.components[ type ]

    def find_component( self, type ):
        if type in self.components:
            return self.components[ type ]
        else:
            return None

    def update( self ):
        for component in self.components.values():
            component.update()

