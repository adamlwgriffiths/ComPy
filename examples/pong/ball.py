'''
Created on 10/05/2012

@author: adam
'''

import random

from compy.entity import Entity
from compy.component import Component


class BallMovementComponent( Component ):
    type = "ball_movement"
    
    def __init__( self, name ):
        super( BallMovementComponent, self ).__init__(
            BallMovementComponent.type,
            name
            )

    def update( self ):
        self.entity.data[ 'position' ] += self.entity.data[ 'velocity' ]

class BallContactComponent( Component ):
    type = "ball_contact"

    def __init__( self, name ):
        super( BallContactComponent, self ).__init__(
            BallContactComponent.type,
            name
            )

    def serve( self ):
        if self.entity == None:
            raise ValueError( "Entity not set" )

        # reset the ball's position
        self.entity.data[ 'position' ] = 0.0

        # select a velocity
        velocity = random.random()

        # pick a random direction
        if random.random() > 0.5:
            velocity *= -1.0

        # apply the velocity
        self.entity.data[ 'velocity' ] = velocity

    def hit( self, velocity ):
        # set our velocity
        self.entity.data[ 'velocity' ] = velocity


def create():
    entity = Entity( "ball" )
    entity.add_component(
        BallMovementComponent( 'movement' )
        )
    entity.add_component(
        BallContactComponent( 'contact' )
        )
    entity.data[ 'position' ] = 0.0
    entity.data[ 'velocity' ] = 0.0
    return entity

