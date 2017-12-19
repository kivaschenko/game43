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


class Scene(object):
    def enter(self):
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
            return "money"
        elif choice == "I can do it without money!":
            print(textwrap.dedent("""
            Actions speak louder than words!
            No money no honey!"""))
            return "loser"
        else:
            print("DOESN'T COMPUTE!")
            return "scene"

class Money(Scene):
    def enter(self):
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
            return "loser"
        elif choice == "No":
            print(textwrap.dedent("""
            "No money no honey".
            All debts must be paid."""))
            return "loser"
        else:
            print("DOESN'T COMPUTE!")
            return "oligarch"

class FirstElection(Scene):
    pass

class SecondElection(Scene):
    pass

class Revolution(Scene):
    pass

class Loser(Scene):
    jokes = [
        "Add insult to injury.",
        "Bite off more than you can chew.",
        "Can't judge a book by its cover.",
        "Cry over spilt milk.",
        "Curiosity killed the cat",
    ]
    def print_joke(self):
        joke = random.choice(jokes)
        print("You lose!")
        print(joke)
        exit(1)


class President(Scene):
    pass

class PremierMinistre(Scene):
    pass

class Map(object):
    scenes_dict = {
        "scene": Scene(),
        "money": Money(),
        "loser": Loser(),
        "first_election": FirstElection,
        "second_election": SecondElection,
        "revolution": Revolution(),
        "president": President(),
        "premier_ministre": PremierMinistre,
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, name_scene):
        next_step = Map.scenes_dict.get(name_scene)
        return next_step
    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def run(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('president')  # trouble
        # - i have not one last scene
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            # be sure to print out the last scene
            current_scene.enter()


a_map = Map("scene")
a_race = Engine(a_map)
a_race.run()
