#!/usr/bin/env python

# Monty Hall Problem
# http://en.wikipedia.org/wiki/Monty_Hall_problem

# Simulator by M.G.Chambers - 6/04/2015

import random, tempfile

timesWon = 0

# Loop through the simulation a reasonable amount of times...
for x in range(0,1000):

    # Fill the cupbaords with goats...
    cupboards = ['goat', 'goat', 'goat']

    # Replace one goat with a car, at random...
    carLocation = random.randrange(0, 3)
    cupboards[carLocation] = 'car'

    # We are going to 'choose' cupboard one[0] - its not a random choice, 
    # but the filling of the cupboards was random in the first place.   
    
    # Monty is going to open one of the other cupboards
    # then ask us if we want to change our mind (and we do, we always do).
    if cupboards[1] == 'goat':
        # Monty opens cupboard 2, we see a goat, so we will choose three[2]...
        if cupboards[2] == 'car':
            # Yay!  We won a car!
            timesWon = timesWon + 1
    elif cupboards[2] == 'goat':
        # There wasn't a goat in cupboard two[1].. hint hint, so Monty will show us cupboard three[2],
        # There must be a car in cupboard two[1]!! We're going to win, but lets just check...
        if cupboards[1] == 'car':
            # Yay!  We won a car!
            timesWon = timesWon + 1
    
    # We only loose if the car was in the first cupboard.  So we have a 2/3 chance of winning!

# Output the result (number of cars won) to a randomly named file, 
# allows script to be run concurrently in the same shell.
tempfile.tempdir = "./"
tf = tempfile.NamedTemporaryFile(delete=False)
tf.write(bytes(str(timesWon), 'UTF-8'))
tf.close()
