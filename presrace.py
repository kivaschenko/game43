"""
*Map
 -next_scene
 -opening_scene
*Engine
 -play
*Scene
 - enter
 *Own Party
 *First Election
 *Second Election
 *Loser
 *President
 *Premier Ministre
 *Oligarch
 *Opposition Leader
 *Overseas Partners
 *North Neighbors
 *Radicals
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
from statemachine import StateMachine

def start_state():
    print(textwrap.dedent(phrases.START_INTRODUCTION))
    choice = input("--> ")
    if choice == "We must seek compromises.":
        print(textwrap.dedent(phrases.COMPROMISES))
        newState = "money"
    elif choice == "I can do it without money!":
        print(textwrap.dedent(phrases.NO_MONEY))
        newState = "loser"
    else:
        print("DOESN'T COMPUTE!")
        continue


def money_state():
    print(textwrap.dedent(phrases.MONEY_INTRODUCTION))
    choice = input("--> ")
    if choice == "join the consolidated opposition":
        print(textwrap.dedent(phrases.ANTI_CORRUPTION))
        newState = "loser"
    elif choice == "No":
        print(textwrap.dedent())
        newState = "loser"
    else:
        print("DOESN'T COMPUTE!")
        continue

def revolution_state():
    pass

def first_election_state():
    pass

def second_election():
    pass

def loser_state():
    jokes = phrases.JOKES
    joke = random.choice(jokes)
    print("-" * len(joke))
    print(joke)
    print("-" * len(joke))
    print("\tYou lose!" * 3)

def president_state():
    print(textwrap.dedent(phrases.INAUGURATION))

def premier_ministre():
        jokes = phrases.PREMIER_MINISTRE
        joke = random.choice(jokes)
        print("#" * len(joke))
        print(joke)
        print("#" * len(joke))


if __name__ == '__main__':
    race = StateMachine()
    race.add_state("Start", start_state)
    race.add_state("Money", money_state)
    race.add_state("Revolution", revolution_state)
    race.add_state("First_Election", first_election_state)
    race.add_state("Second_Election", second_election)
    race.add_state("Loser", loser_state, end_state=1)
    race.add_state("President", president_state, end_state=1)
    race.add_state("Premier_Ministre", premier_ministre, end_state=1)
    race.set_start("Start")
    race.run()
