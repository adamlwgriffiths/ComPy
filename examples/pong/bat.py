'''
Created on 10/05/2012

@author: adam
'''

import random

from compy.entity import Entity
from compy.component import Component

import ball


class BatPositionComponent( Component ):
    type = "bat_position"
    
    def __init__( self, name ):
        super( BatPositionComponent, self ).__init__(
            BatPositionComponent.type,
            name
            )

    def update( self ):
        # find the ball
        ball_entity = Entity.find_entity( "ball" )
        if ball == None:
            raise ValueError( "No ball entity" )

        # see if it's within our hit distance
        ball_position = ball_entity.data[ 'position' ]

        bat_position = self.entity.data[ 'position' ]
        hit_distance = self.entity.data[ 'hit_distance' ]
        max_distance = bat_position + hit_distance
        min_distance = bat_position - hit_distance

        if \
            ball_position > max_distance or \
            ball_position < min_distance:
            # ball is too far away
            # do nothing
            return

        # see if it's coming in our direction
        # simply compare velocity direction with bat
        # position and assume only 2 bats
        # not the best component but its just an example
        ball_velocity = ball_entity.data[ 'velocity' ]
        if \
            ball_velocity < 0.0 and \
            bat_position > 0.0:
            # heading away
            return
        if \
            ball_velocity > 0.0 and \
            bat_position < 0.0:
            # heading away
            return

        # hit it!
        bat_hit = self.entity.find_component(
            BatHitComponent.type
            )
        if bat_hit == None:
            raise ValueError( "No bat hit component" )

        # hit the ball
        bat_hit.hit_ball()

class BatHitComponent( Component ):
    type = "bat_hit"

    def __init__( self, name, sleep_time, hit_chance ):
        super( BatHitComponent, self ).__init__(
            BatHitComponent.type,
            name
            )

        self.sleep_time = sleep_time
        self.last_hit = 0
        self.hit_chance = hit_chance

    def hit_ball( self ):
        # see if we can hit yet
        if self.last_hit > 0:
            # we already tried to hit it
            # don't continue
            return

        # set our last hit to our sleep time
        # this stops us taking unlimited hits
        self.last_hit = self.sleep_time

        # roll a dice and see if we hit it or not
        chance = random.random()

        if chance > self.hit_chance:
            # we've missed
            print "%s missed the ball!" % self.entity.name
            return

        # find the ball
        ball_entity = Entity.find_entity( "ball" )
        if ball == None:
            raise ValueError( "No ball entity" )

        ball_contact = ball_entity.find_component(
            ball.BallContactComponent.type
            )
        if ball_contact == None:
            raise ValueError( "No ball contact component" )

        velocity = random.random()
        position = self.entity.data[ 'position' ]

        if position > 0.0:
            velocity *= -1.0

        ball_contact.hit( velocity )

        print "%s hit the ball!" %self.entity.name

    def update( self ):
        if self.last_hit > 0:
            self.last_hit -= 1


def create( name, position, hit_distance, hit_chance, sleep_time ):
    entity = Entity( name )
    entity.add_component(
        BatPositionComponent( 'position' )
        )
    entity.add_component(
        BatHitComponent(
            'hit',
            sleep_time,
            hit_chance
            )
        )

    entity.data[ 'position' ] = position
    entity.data[ 'hit_distance' ] = hit_distance

    return entity

