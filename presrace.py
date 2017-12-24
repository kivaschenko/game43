#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
import random
import textwrap
import phrases
import time
from statemachine import FSM
##============================================================================
## TRANSITIONS

class Transition(object):
    """Creates an object with an attribute,
        which is the name of the state to go to it."""

    def __init__(self, toState):
        self.toState = toState

    def execute(self):
        print("\nTransitioning to next situation...\n")
        time.sleep(3)


##============================================================================
## STATES

class State(object):
    """The metaclass that initialize
        object with names of current state"""
    def __init__(self, FSM):
        self.FSM = FSM

    def execute(self):
        print("This condition has not yet been written.")
        print("Subclass it and implement enter().")

    def exit(self):
        pass

class Start(State):
    """START state of game."""

    def __init__(self, FSM):
        self.FSM = FSM

    def execute(self):
        print(textwrap.dedent(phrases.START_INTRODUCTION))    
        choice = input("--> ")
        if choice == "I seek compromises!":
            print(textwrap.dedent(phrases.COMPROMISES))
            self.FSM.to_transition("toMoney")
        elif choice == "No money!":
            print(textwrap.dedent(phrases.NO_MONEY))
            self.FSM.to_transition("toLoser")
        else:
            print("DOESN'T COMPUTE!")
            self.FSM.to_transition("toStart")


class Money(State):
    """Get choice to take MONEY from somebody."""

    def __init__(self, FSM):
        self.FSM = FSM

    def execute(self):
        print(textwrap.dedent(phrases.MONEY_INTRODUCTION))
        choice = input("--> ")
        if choice == "join the opposition!":
            print(textwrap.dedent(phrases.WITH_OPPO_TO_1ST_ELECT))
            self.FSM.to_transition("toFirst_Election")
        elif choice == "I gonna go my way!":
            print(textwrap.dedent(phrases.YOU_ARE_REVOLUTIONER))
            self.FSM.to_transition("toRevolution")
        elif choice == "Only one oligarch.":
            print(textwrap.dedent(phrases.DEAL_WITH_RADICALS))
            self.FSM.to_transition("toLoser")
        else:
            print("DOESN'T COMPUTE!")
            self.FSM.to_transition("toMoney")

class Revolution(State):
    """Revolution state in game. """

    def __init__(self, FSM):
        self.FSM = FSM

    def execute(self):
        print(textwrap.dedent(phrases.REVOLUTION_INTRODUCTION))    
        choice = input("--> ")
        if choice == "I gonna go democracy election!":
            print(textwrap.dedent(phrases.WITH_OPPO_TO_1ST_ELECT))
            self.FSM.to_transition("toFirst_Election")
        elif choice == "I got the military help.":
            print(textwrap.dedent(phrases.DICTATOR))
            self.FSM.to_transition("toLoser")
        else:
            print("DOESN'T COMPUTE!")
            self.FSM.to_transition("toRevolution")

class FirstElection(State):
    """State of game where first election became."""

    def __init__(self, FSM):
        self.FSM = FSM

    def execute(self):
        print(textwrap.dedent(phrases.FIRST_ELECTION_INTRODUCTION))    
        choice = input("--> ")
        if choice == "I will only tell the truth!":
            print(textwrap.dedent(phrases.TELL_TRUE_PLAY_CLEANLY))
            self.FSM.to_transition("toLoser")
        elif choice == "I can spread unrealistic promises to voters!":
            print(textwrap.dedent(phrases.UNREALISTIC_PROMISES))
            self.FSM.to_transition("toPresident")
        elif choice == "I will become a technical candidate.":
            print(textwrap.dedent(phrases.AGREEMENT_TO_PM))
            self.FSM.to_transition("toPremier_Ministre")
        elif choice == "I will fight by any available means.":
            print(textwrap.dedent(phrases.WITH_FALSICATION_TO_2ND_ELECT))
            self.FSM.to_transition("toSecond_Election")
        else:
            print("DOESN'T COMPUTE!")
            self.FSM.to_transition("toFirst_Election")


class SecondElection(State):
    """Second Edition state"""
    
    def __init__(self, FSM):
        self.FSM = FSM
        
    def execute(self):
        print(textwrap.dedent(phrases.SECOND_ELECTION_INTRODUCTION))
        choice = input("--> ")
        if choice == "I can promise voters everything they want to hear!":
            print(textwrap.dedent(phrases.UNREALISTIC_PROMISES))
            self.FSM.to_transition("toPresident")
        elif choice == "I use black PR!":
            print(textwrap.dedent(phrases.ANTI_CORRUPTION))
            self.FSM.to_transition("toLoser")            
        elif choice == "I made deal with opponent!":
            print(textwrap.dedent(phrases.AGREEMENT_TO_PM))
            self.FSM.to_transition("toPremier_Ministre")        
        else:
            print("DOESN'T COMPUTE!")
            self.FSM.to_transition("toSecond_Election")        

class Loser(State):
    """ State when you lose the game. """

    def __init__(self, FSM):
        self.FSM = FSM

    def execute(self):
        jokes = phrases.JOKES
        joke = random.choice(jokes)
        print("\t\t","-" * len(joke))
        print('\t\t',joke.upper())
        print("\t\t", "-" * len(joke))
        print("\t" * 6, "You lose!")
#        self.FSM.to_transition("toFinish")
        exit(1)

class President(State):
    """The state when player reaches President post."""

    def __init__(self, FSM):
        self.FSM = FSM

    def execute(self):
        print("\t\t\t",textwrap.dedent(phrases.INAUGURATION))    
#        self.FSM.to_transition("toFinish")
        exit(1)
        

class PremierMinistre(State):
    """Premier Ministre state of game """

    def __init__(self, FSM):
        self.FSM = FSM

    def execute(self):
        print("\t\t\t",textwrap.dedent(phrases.YOU_PREMIER))
        jokes = phrases.PREMIER_MINISTRE
        joke = random.choice(jokes)
        print("\t\t\t","#" * len(joke))
        print("\t\t\t", joke)
        print("\t\t\t", "#" * len(joke))
#        self.FSM.to_transition("toFinish")
        exit(1)
        
        
#class Finish(State):
#    """ Game over."""
#
#    def __init__(self, FSM):
#        self.FSM = FSM
#
#    def execute(self):
#        print("\n\t\tYou won!")    
#        print("\t\t\tBye, bye! ))")
#        exit(1)



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
        self.FSM.add_state("Loser", Loser(self.FSM), end_state=1)
        self.FSM.add_state("President", President(self.FSM), end_state=1)
        self.FSM.add_state("Premier_Ministre", \
                           PremierMinistre(self.FSM), end_state=1)
#        self.FSM.add_state("Finish", Finish(self.FSM), end_state=1)

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
    while True:
        gm.execute()  # now working but double time need input-return choice...

