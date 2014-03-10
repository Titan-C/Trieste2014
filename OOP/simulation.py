# -*- coding: utf-8 -*-
"""
@author: Oscar Najera
Starting template for tutorial
Developed for the ICTP Workshop
"""

from des_engine import Event, Simulator

class Customer(Event):
    """Represents the customer visiting the Bank"""
    def __init__(self, time):
        pass
    def execute(self, simulator):
        """Event class required action"""
        pass

class BankSimulator(Simulator):
    """Simulates the Workday of a Bank"""
    def run(self):
        """Runs simulation"""
        pass

if __name__ == "__main__":
    UBS = BankSimulator()
    UBS.run()
