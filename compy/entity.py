'''
Created on 09/05/2012

@author: adam
'''


class Entity( object ):
    
    def __init__( self, name ):
        super( Entity, self ).__init__()

        self.name = name
        self.components = {}

    def add_component( self, type, component ):
        if type in self.components:
            raise ValueError(
                "Component type already registered"
                )
        else:
            component._set_entity( self )
            self.components[ type ] = component

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

