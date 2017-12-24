#!/usr/bin/env python3
#-*- coding:utf-8 -*-

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
        self.end_states = []
        self.trans = None

    def add_transition(self, transName, transition):
        self.transitions[transName] = transition


    def add_state(self, stateName, state, end_state=0):
        self.states[stateName] = state
        if end_state:
            self.end_states.append(state)
            
    def set_state(self, stateName):
        # assign previos state as current state
        self.prevState = self.curState
        # assign current state of got stateName
        # that is key to dictionary states self.curState = Start(self.FSM)
        self.curState = self.states[stateName]

    def to_transition(self, toTrans):
        """The function gets the value of toTrans, which is the name
        key in the dictionary of "self.transitions" and calls on this key
        object is a Transition object with the argument "Money".
        Returns a new class object and appends a name to it
        self.trans """
        
        # for example  if got toTans = "toMoney" then 
        # self.trans = Transition("Money")
        self.trans = self.transitions[toTrans] 

    def execute(self):
        """This engine get """
        self.curState.execute()    
        while (self.trans):           # Transition("Money")
            self.curState.exit()   # print about exit from current state
            self.trans.execute()   # execute print "Transitioning..."    
            # get the name to to_transition function from current State
            # and pass one to set_state function as stateName argument
            # for example : self.set_state("Money")
            self.set_state(self.trans.toState) 
            self.trans = None      # remove old value of trans variable
            if self.curState in self.end_states:
                break
            self.curState.execute()    # Money(self.FSM).execute() 
