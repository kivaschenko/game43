#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""

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
        if choice == "1":
            print(textwrap.dedent(phrases.COMPROMISES))
            return "Money"
        elif choice == "2":
            print(textwrap.dedent(phrases.NO_MONEY))
            return "Loser"
        else:
            print("DOESN'T COMPUTE!")
            return "Start"

class Money(State):
	def enter():
		print(textwrap.dedent(phrases.MONEY_INTRODUCTION))
		choice = input("--> ")
		if choice == "1":
		    print(textwrap.dedent(phrases.WITH_OPPO_TO_1ST_ELECT))
		    return "First_Election"
		elif choice == "2":
		    print(textwrap.dedent(phrases.ANTI_CORRUPTION))
		    return "Revolution"
		elif choice == "3":
		    print(textwrap.dedent(phrases.DEAL_WITH_RADICALS))
		    return "Loser" 
		else:
		    print("DOESN'T COMPUTE!")
		    return "Money"

class Revolution(State):
	def enter(self):
		print(textwrap.dedent(phrases.REVOLUTION_INTRODUCTION))
		choice = input("--> ")
		if choice == "1":
			print(textwrap.dedent(phrases.WITH_OPPO_TO_1ST_ELECT))
			return "First_Election"
		elif choice == "2":
			print(textwrap.dedent(phrases.DICTATOR))
			return "Loser"
		else:
		    print("DOESN'T COMPUTE!")
		    return "Revolution"

class FirstElection(State):
    pass

class SecondElection(State):
    pass

class Loser(State):
    def enter(self):
        jokes = phrases.JOKES
        joke = random.choice(jokes)
        print("-" * len(joke))
        print(joke)
        print("-" * len(joke))
        print("\tYou lose!" * 3)
        return "Finish"

class President(State):
    def enter(self):
        print(textwrap.dedent(phrases.INAUGURATION))
        return "Finish"

class PremierMinistre(State):
    def enter(self):
        jokes = phrases.PREMIER_MINISTRE
        joke = random.choice(jokes)
        print("#" * len(joke))
        print(joke)
        print("#" * len(joke))
        return "Finish"

class Finish(State):
	def enter(self):
		print("You won!")
		exit(1)

class StateMachine(object):
    """
    This is a map of major milestones and game handlers.
    In the dictionary, all class handlers are accessible by the key.
    In the list of final states only those handlers on which the game ends.
    """	    
    def __init__(self, name):
        self.startState = name  ## Start
        self.handlers = {
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
        self.endState = self.handlers["Finish"]  ## <__main__.Finish object at 0x7fa610760940>

    def set_start(self):
        return    self.handlers[self.startState]

    def next_state(self, return_key):
        return    self.handlers[return_key]
        
    def run(self, name):
        currentState = next_state(name)
        while True:
            self.next_state(currentState.enter())
            currentState.enter()
            if currentState == self.endState:
                break
        

m = StateMachine("Start")
m.set_start()
#n = m.next_state(s)
#print("n", n)
#m.run(n)
