# -*- coding: utf-8 -*-
"""
@author: Oscar Najera
"""
from des_engine import Event, Simulator

class Customer(object):
    """Contains the customer visiting the Bank"""
    pass


class Generator(Event):
    """Simulates the arrival of customers"""

    def __init__(self, time, maxtime):
        pass

    def execute(self, simulator):
        """Generates new customer at given time"""
        pass
    
class Queue(object):
    """Waiting Queue in the Bank"""
    pass

class Server(Event):
    """Simulates the cashier"""
    pass

class BankSimulator(Simulator):
    """Simulates the Workday of a Bank"""
    def run(self):
        """Runs simulation"""
        generator = Generator(0, 30)

        self.insert(generator)
        self.do_all_events()

if __name__ == "__main__":
    UBS = BankSimulator()
    UBS.run()
