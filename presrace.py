#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
import random
import textwrap
import phrases
##============================================================================
## TRANSITIONS

class Transition(object):
    """Creates an object with an attribute,
        which is the name of the state to go to it."""

    def __init__(self, toState):
        self.toState = toState

    def execute(self):
        print("Transitioning to new state...")


##============================================================================
## STATES

class State(object):
    """The metaclass that initialize
        object with names of current state"""
    def __init__(self, FSM):
        self.FSM = FSM

    def enter(self):
        print("This condition has not yet been written.")
        print("Subclass it and implement enter().")

    def execute(self):
        pass

    def exit(self):
        pass

class Start(State):
    """Starting state of game."""

    def __init__(self, FSM):
        self.FSM = FSM

    def enter(self):
        print(textwrap.dedent(phrases.START_INTRODUCTION))

    def execute(self):
        choice = input("--> ")
        if choice == "1":
            print(textwrap.dedent(phrases.COMPROMISES))
            self.FSM.to_transition("toMoney")
        elif choice == "2":
            print(textwrap.dedent(phrases.NO_MONEY))
            self.FSM.to_transition("toLoser")
        else:
            print("DOESN'T COMPUTE!")
            self.FSM.to_transition("Start")

    def exit(self):
        print('You got choice in "Start", go next.')

class Money(State):
    """Get choice to take money from somebody."""

    def __init__(self, FSM):
        self.FSM = FSM

    def enter():
        print(textwrap.dedent(phrases.MONEY_INTRODUCTION))

    def execute(self):
        choice = input("--> ")
        if choice == "1":
            print(textwrap.dedent(phrases.WITH_OPPO_TO_1ST_ELECT))
            self.FSM.to_transition("toFirst_Election")
        elif choice == "2":
            print(textwrap.dedent(phrases.ANTI_CORRUPTION))
            self.FSM.to_transition("toRevolution")
        elif choice == "3":
            print(textwrap.dedent(phrases.DEAL_WITH_RADICALS))
            self.FSM.to_transition("toLoser")
        else:
            print("DOESN'T COMPUTE!")
            self.FSM.to_transition("toMoney")

class Revolution(State):
    """Revolution state in game. """

    def __init__(self, FSM):
        self.FSM = FSM

    def enter(self):
        print(textwrap.dedent(phrases.REVOLUTION_INTRODUCTION))

    def execute(self):
        choice = input("--> ")
        if choice == "1":
            print(textwrap.dedent(phrases.WITH_OPPO_TO_1ST_ELECT))
            self.FSM.to_transition("toFirst_Election")
        elif choice == "2":
            print(textwrap.dedent(phrases.DICTATOR))
            self.FSM.to_transition("toLoser")
        else:
            print("DOESN'T COMPUTE!")
            self.FSM.to_transition("toRevolution")

class FirstElection(State):
    """State of game where first election became."""

    def __init__(self, FSM):
        self.FSM = FSM

    def enter(self):
        print(textwrap.dedent(phrases.FIRST_ELECTION_INTRODUCTION))

    def execute(self):
        choice = input("--> ")
        if choice == "1":
            print(textwrap.dedent(phrases.TELL_TRUE_PLAY_CLEANLY))

        elif choice == "4":
            print(textwrap.dedent(phrases.WITH_FALSICATION_TO_2ND_ELECT))



class SecondElection(State):
    pass

class Loser(State):
    """ State when you lose the game. """

    def __init__(self, FSM):
        self.FSM = FSM

    def enter(self):
        jokes = phrases.JOKES
        joke = random.choice(jokes)
        print("-" * len(joke))
        print(joke)
        print("-" * len(joke))
        print("\tYou lose!" * 3)

    def execute(self):
        self.FSM.to_transition("toFinish")

class President(State):
    """The state when player reaches President post."""

    def __init__(self, FSM):
        self.FSM = FSM

    def enter(self):
        print(textwrap.dedent(phrases.INAUGURATION))

    def execute(self):
        self.FSM.to_transition("toFinish")

class PremierMinistre(State):
    """Premier Ministre state of game """

    def __init__(self, FSM):
        self.FSM = FSM

    def enter(self):
        jokes = phrases.PREMIER_MINISTRE
        joke = random.choice(jokes)
        print("#" * len(joke))
        print(joke)
        print("#" * len(joke))

    def execute(self):
        self.FSM.to_transition("toFinish")

class Finish(State):
    """ Game over."""

    def __init__(self, FSM):
        self.FSM = FSM

    def enter(self):
        print("You won!")

    def execute(self):
        print("Bye, bye! ))")
        exit(1)

##============================================================================
## FINITE STATE MACHINE

class FSM(object):
    """
    This is a map of major milestones and game handlers.
    """
    def __init__(self, character):
        self.char = character
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.prevState = None
        self.trans = None

    def add_transition(self, transName, transition):
        self.transitions[transName] = transition

    def add_state(self, stateName, state):
        self.states[stateName] = state

    def set_state(self, stateName):
        # assign previos state as current state
        self.prevState = self.curState
        # assign current state of got stateName
        # that is key to dictionary states
        self.curState = self.states[stateName]

    def to_transition(self, toTrans):
        self.trans = toTrans

    def execute(self):
        # if return attribute "trans" than go to next activites
        if self.trans:
            self.curState.exit()   # exit from current state
            self.trans.execute()   # execute print "Transitioning..."
            # get the name to to_transition function from current State
            # and pass one to set_state function as stateName argument
            self.set_state(self.trans.toState)
            self.curState.enter()  # open the new state as currently
            self.trans = None      # remove old value of trans variable
            self.curState.execute()    # run the moving current state

##============================================================================
## IMPLEMENTATION


class Char(object):
    def __init__(self):
        self.FSM = FSM(self)

class GameMaid(Char):
    def __init__(self):
        self.FSM = FSM(self)

        ##STATES
        self.FSM.add_state("Start", Start(self.FSM))
        self.FSM.add_state("Money", Money(self.FSM))
        self.FSM.add_state("Revolution", Revolution(self.FSM))
        self.FSM.add_state("First_Election", FirstElection(self.FSM))
        self.FSM.add_state("Second_Election", SecondElection(self.FSM))
        self.FSM.add_state("Loser", Loser(self.FSM))
        self.FSM.add_state("President", President(self.FSM))
        self.FSM.add_state("Premier_Ministre", PremierMinistre(self.FSM))
        self.FSM.add_state("Finish", Finish(self.FSM))

        ##TRANSITIONS
        self.FSM.add_transition("toStart", Transition("Start"))
        self.FSM.add_transition("toMoney", Transition("Money"))
        self.FSM.add_transition("toRevolution", Transition("Revolution"))
        self.FSM.add_transition("toFirst_Election", \
                                    Transition("First_Election"))
        self.FSM.add_transition("toSecond_Election", \
                                    Transition("Second_Election"))
        self.FSM.add_transition("toLoser", Transition("Loser"))
        self.FSM.add_transition("toPresident", Transition("President"))
        self.FSM.add_transition("toPremier_Ministre", \
                                    Transition("Premier_Ministre"))
        self.FSM.add_transition("toFinish", Transition("Finish"))
    
        self.FSM.set_state("Start")
    
    def execute(self):    
        self.FSM.execute()

##=============================================================================

if __name__ == '__main__':
   
    gm = GameMaid()

