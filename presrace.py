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
from statemachine import StateMachine

def start_state():
    print(textwrap.dedent("""
        You are in Ukraine one year before the presidential elections
        and you want to take this post through elections or another way.
        You agree at least get post of premier ministre too, for begin.
        You have few possibilities but some variants are maybe.

        You can:
         - "To achieve this goal, we must seek compromises.
            Politics is the art of the possible." ,

         - "I do not need money! I do not want to depend on anyone.
            I can do it without money."

        What the strategy you will choice?"""))
    choice = input("--> ")
    if choice == "We must seek compromises.":
        print(textwrap.dedent("""
        Every cloud has a silver lining!
        You must pay 3 millions bucks for part in race!
        Look for money, bro and "jump on the bandwagon"!
        We could do with the extra cash, Bro ))."""))
        newState = "money"
    elif choice == "I can do it without money!":
        print(textwrap.dedent("""
        Actions speak louder than words!
        No money no honey!"""))
        newState = "loser"
    else:
        print("DOESN'T COMPUTE!")
        continue


def money_state():
    print(textwrap.dedent("""
        It's big money, brother!
        You have three options today.

        You can conclude an agreement with foreign partners
        and promise the development of democracy in the country.
        Then you will be helped to create your new party
        and join the consolidated opposition.

        The second case is when you take money from both
        the oligarch and foreign partners at the same time,
        but they do not know about each other.
        Then you make your own political party to go your own way.

        Thirdly. Circumstances are such that you will be able to agree
        with only one of the oligarchs to create a new political party.
        Do you promise to service me at least 5 years
        and lobby his interests in parliament."""))
    choice = input("--> ")
    if choice == "agreement with foreign partners and join the consolidated opposition":
        print(textwrap.dedent("""
        Two month later...
        The Anti-Corruption Bureau starts an investigation
        and you are a suspect.
        "A hot potato"."""))
        newState = "loser"
    elif choice == "No":
        print(textwrap.dedent("""
        "No money no honey".
        All debts must be paid."""))
        newState = "loser"
    else:
        print("DOESN'T COMPUTE!")
        continue

def revolution():
    pass

def first_election_state():
    pass

def second_election():
    pass


def loser_state():
    jokes = [
        "Add insult to injury.",
        "Bite off more than you can chew.",
        "Can't judge a book by its cover.",
        "Cry over spilt milk.",
        "Curiosity killed the cat",
    ]
    joke = random.choice(jokes)
    print("You lose!")
    print(joke)
    exit(1)

def president_state():
    print(textwrap.dedent("""
    ##### Ta-da-a! You won! #####
    ### Now You are President! ##
    ### \_|$|_/**\$/**\_|$|_/ ###""")
    exit(1)

def premier_ministre():
    pass

race = StateMachine()
