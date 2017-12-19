#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
*Map
 -next_state
 -opening_state
*Engine
 -play
*State
 - enter
 *Money
 *FirstElection
 *SecondElection
 *Loser
 *President
 *Premier Ministre
 *Revolution

give money
get money
make revolution
make falsification election
make black piar company
make good piar
give promises to people
make deal with opponent
promise low taxes
promise low tariffs
promise high salary
promise many work places
strategy choice
"""

import sys
import random
import textwrap
import phrases


class State(object):
    def enter(self):
        print("This condition has not yet been written.")
        print("Subclass it and implement enter().")
        exit(1)

class Start(State):
    def enter(self):
        print(textwrap.dedent(phrases.START_INTRODUCTION))
        choice = input("--> ")
        if choice == "We must seek compromises.":
            print(textwrap.dedent(phrases.COMPROMISES))
            return "Money"
        elif choice == "I can do it without money!":
            print(textwrap.dedent(phrases.NO_MONEY))
            return "Loser"
        else:
            print("DOESN'T COMPUTE!")
            return start_state()

class Money(State):
	def enter():
		print(textwrap.dedent(phrases.MONEY_INTRODUCTION))
		choice = input("--> ")
		if choice == "join the consolidated opposition":
		    print(textwrap.dedent(phrases.ANTI_CORRUPTION))
		    return "Loser"
		elif choice == "No":
		    print(textwrap.dedent())
		    return "Loser"
		else:
		    print("DOESN'T COMPUTE!")
		    return enter()

def Revolution():
    pass

def FirstElection():
    pass

def SecondElection():
    pass

class Loser():
    def enter(self):
        jokes = phrases.JOKES
        joke = random.choice(jokes)
        print("-" * len(joke))
        print(joke)
        print("-" * len(joke))
        print("\tYou lose!" * 3)
        exit(1)

def President():
    def enter(self):
        print(textwrap.dedent(phrases.INAUGURATION))
        exit(1)

class PremierMinistre(State):
    def enter(self):
        jokes = phrases.PREMIER_MINISTRE
        joke = random.choice(jokes)
        print("#" * len(joke))
        print(joke)
        print("#" * len(joke))
        exit(1)


class Map(object):

	        handlers = {
		        "Start": Start(),
		        "Money": Money(),
		        "Revolution": Revolution(),
		        "First_Election": FirstElection(),
		        "Second_Election": SecondElection(),
		        "Loser": Loser(),
		        "President": President(),
		        "Premier_Ministre": PremierMinistre(),
		        "Finish": Finish()
		    }
		    
    def __init__(self, start):
        """
        This is a map of major milestones and game handlers.
        In the dictionary, all class handlers are accessible by the key.
        In the list of final states only those handlers on which the game ends.
        """
        self.start = start


    def next_state(self, new_state):
        self.new_state = new_state
        state = self.handlers[self.new_state]
        return state.enter()

#    def opening_state(self):
#        return state.enter()

class Engine(object):
    def __init__(self, state_map):
        self.state_map = state_map  #  self.state_map = <__main__.Map object at 0x7f0d60d25908>
    def play(self):
        current_state = self.state_map.next_state()
        print("current_state: {}".format(current_state))
        last_state = self.scene_map.endStates
        print("last_state: {}".format(last_state))
        while current_state not in last_state:
            next_state_name = current_scene.enter()
            current_state = self.state_map.next_state(next_scene_name)

            current_state.enter()


a_map = Map('Start')
a_map.next_state(newState)
a_game = Engine(a_map)
a_game.play()
