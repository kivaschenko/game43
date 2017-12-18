"""
*Map
 -next_situation
 -opening_situation
*Engine
 -play
*Situation
 - enter
 *Own Party
 *First Election
 *Second Election
 *Loser
 *President
 *Premier Ministre
 *Oligarch
 *Opposition Leader
 *West Partners
 *North Partners
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


class Situation(object):
    pass

class OwnParty(Situation):
    pass

class FirstElection(Situation):
    pass

class SecondElection(Situation):
    pass
    
class Revolution(Situation):
    pass
    
class Loser(Situation):
    pass
    
class President(Situation):
    pass
    
class PremierMinistre(Situation):
    pass
    
class Oligarch(Situation):
    pass
    
class OppositionLeader(Situation):
    pass
    
class WestPartners(Situation):
    pass
    
class NorthPartners(Situation):
    pass
    
class Radicals(Situation):
    pass
    
        
