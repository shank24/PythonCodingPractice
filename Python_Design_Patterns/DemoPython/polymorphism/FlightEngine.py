class Flight:
    def __init__(self,engine):
        self.engine=engine

    def startEngine(self):
        self.engine.start()

class AirbusEngine:

    def start(self):
        print('Starting Airbus Engine')

class BoeingEngine:

    def start(self):
        print('Starting Boeing Engine')

ae=AirbusEngine()
f=Flight(ae)
f.startEngine()

be=BoeingEngine()
f=Flight(be)
f.startEngine()

