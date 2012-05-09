'''
Created on 09/05/2012

@author: adam
'''

from compy.entity import Entity

import ball
import bat
import table


games_to_play = 10
table_size = 30.0
player_positions = [ -10.0, 10.0 ]
player_hit_distance = 1.0
player_hit_chance = 0.8
player_time_between_hits = 5

# create the ball
ball_entity = ball.create()

# create player 1
bat_left = bat.create(
    "Player 1",
    player_positions[ 0 ],
    player_hit_distance,
    player_hit_chance,
    player_time_between_hits
    )

# create player 2
bat_right = bat.create(
    "Player 2",
    player_positions[ 1 ],
    player_hit_distance,
    player_hit_chance,
    player_time_between_hits
    )

# create the table
table_entity = table.create( table_size / 2.0 )

# begin playing
print "Playing to %i" % games_to_play

# serve the ball
ball_contact = ball_entity.find_component(
    ball.BallContactComponent.type
    )

if ball_contact == None:
    raise ValueError( "No ball contact component" )


ball_contact.serve()

# keep playing until the game is over
while True:
    Entity.update_entities()

    if table_entity.data[ 'games' ] >= games_to_play:
        break

# print final score
print "Final score"
player1_score = table_entity.data[ 'left_score' ]
player2_score = table_entity.data[ 'right_score' ]
print "Player 1: %i" % player1_score
print "Player 2: %i" % player2_score

if player1_score > player2_score:
    print "Player 1 Wins!"
elif player1_score < player2_score:
    print "Player 2 Wins!"
else:
    print "Tied game!"

