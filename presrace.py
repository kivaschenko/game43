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
            - "I'm gonna join to the president's party!" ,
            - "I'm gonna join to opposition!" ,
            - "I'm gonna make own political party!" ,
            - "I'am gonna go by other way!"

            What the strategy you will choice?"""))
        choice = input("--> ")
        if choice == "I'm gonna join to the president's party!":
            print(textwrap.dedent("""
            You must pay 3 millions bucks for place in party!
            Look for money, bro and "jump on the bandwagon"!"""))
            return "oligarch"
        elif choice == "I'm gonna join to opposition!":
            print(textwrap.dedent("""
            Every cloud has a silver lining!
            We could do with the extra cash, Bro ))."""))
            return "opposition_leader"
        elif choice == "I'm gonna make own political party!":
            print(textwrap.dedent("""
            Actions speak louder than words!
            At the drop of a hat!"""))
            return "overseas_partners"
        elif choice == "I'am gonna go by other way!":
            print(textwrap.dedent("""
            Don't count your chickens before the eggs have hatched!
            But still need supporters..."""))
            return "radicals"
        else:
            print("DOESN'T COMPUTE!")
            return "scene"

class OwnParty(Scene):
    pass

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
        
class President(Scene):
    pass

class PremierMinistre(Scene):
    pass

class Oligarch(Scene):
    def enter(self):
        print(textwrap.dedent("""
            This a very big money, guy!
            Do you promise to service me at least 5 years
            and lobby my interests in parliament?
            Sign the contract by your blood!
            Do you sign?"""))
        choice = input("--> ")
        if choice == "Yes":
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

class OppositionLeader(Scene):
    def enter(self):
        print(textwrap.dedent("""
        To my knowledge you could not useful to opposition party.
        Good lucky!"""))
        return "loser"

class OverseasPartners(Scene):
    pass

class NorthNeighbors(Scene):
    pass

class Radicals(Scene):
    pass

class Map(object):
    scenes_dict = {
        "scene": Scene(),
        "oligarch": Oligarch(),
        "opposition_leader": OppositionLeader(),
        "overseas_partners": OverseasPartners(),
        "north_neighbors": NorthNeighbors(),
        "radicals": Radicals(),
        "loser": Loser(),
        "own_party": OwnParty(),
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




