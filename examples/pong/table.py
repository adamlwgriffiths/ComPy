'''
Created on 10/05/2012

@author: adam
'''

import random

from compy.entity import Entity
from compy.component import Component

import ball


class BallCheckComponent( Component ):
    type = "ball_check"
    
    def __init__( self, name, half_size ):
        super( BallCheckComponent, self ).__init__(
            BallCheckComponent.type,
            name
            )
        self.half_size = half_size

    def update( self ):
        # find the ball
        ball_entity = Entity.find_entity( "ball" )
        if ball == None:
            raise ValueError( "No ball entity" )

        # see if it's out of bounds
        ball_position = ball_entity.data[ 'position' ]

        if \
            ball_position >= -self.half_size and \
            ball_position <= self.half_size:
            # ball still in play
            return


        if ball_position < -self.half_size:
            # out of bounds
            print "Ball out of bounds on left"
            self.entity.data[ 'right_score' ] += 1

        if ball_position > self.half_size:
            # out of bounds
            print "Ball out of bounds on right"
            self.entity.data[ 'left_score' ] += 1

        self.entity.data[ 'games' ] += 1

        # serve the ball
        ball_contact = ball_entity.find_component(
            ball.BallContactComponent.type
            )
        ball_contact.serve()





def create( half_size ):
    entity = Entity( "table" )
    entity.add_component(
        BallCheckComponent( 'ball_check', half_size )
        )

    entity.data[ 'left_score' ] = 0
    entity.data[ 'right_score' ] = 0
    entity.data[ 'games' ] = 0

    return entity

