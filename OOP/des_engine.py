# -*- coding: utf-8 -*-
"""
@author: Oscar Najera
Simple Discrete Event Simulation Engine
Developed for the ICTP Workshop
"""
from bisect import insort

class Event(object):
    """Base Event class"""

    def __init__(self, time):
        self.time = time

    def __lt__(self, other):
        return self.time < other.time


class EventsList(object):
    """Ordered set that runs whole event simulation"""

    def __init__(self):
        self.orderedlist = []

    def insert(self, event):
        """Includes new event in simulation"""
        if isinstance(event, Event):
            if self.orderedlist != []:
                insort(self.orderedlist, event)
            else:
                self.orderedlist.append(event)

    def getfirst(self):
        """Returns next event in line"""
        return self.orderedlist.pop(0)


class Simulator(object):
    """Main class that goes time stepping"""

    def __init__(self):
        self.time = 0
        self.events = EventsList()

    def insert(self, event):
        """Inserts new event into simulation"""
        self.events.insert(event)

    def do_all_events(self):
        """Iterates over the entire events list"""
        while len(self.events.orderedlist) > 0:
            event = self.events.getfirst()
            self.time = event.time
            event.execute(self)
