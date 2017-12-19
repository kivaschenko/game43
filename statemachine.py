class StateMachine(object):
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name_state, handler, end_state=0):
        name_state = name_state.upper()
        print("added name_state:".format(name_state))  #  check adding name_state
        # Assign the input handler value to key name_state in dictionary self.handlers
        self.handlers[name_state] = handler
        print("current handlers dict is:", self.handlers)  # check handlers dictionary
        # if current handler is last
        if end_state:
            self.endStates.append(name_state)
            print("added end_state:", name_state)

    def set_start(self, name_state):
        self.startState = name_state.upper()
        print("self.startState", self.startState)

    def run(self, choice):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            raise InitializationError("at least one state must be an end_state")

        while True:
            (newState, choice) = handler(choice)
            if newState.upper() in self.endStates:
                print("reached", newState)
                break
            else:
                handler = self.handlers[newState.upper()]
