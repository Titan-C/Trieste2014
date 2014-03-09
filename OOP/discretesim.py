# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 13:12:04 2014

@author: oscar
"""
import bisect

class Event(object):
    """Base class that contains event main characteristics"""
    def __init__(self, time):
        self.time = time
    def __lt__(self, other):
        return self.time < other.time
    def __eq__(self, other):
        return self.time == other.time

class Queue(object):
    """Ordered set that runs hole event simulation"""
    def __init__(self):
        self.orderedlist = []

    def insert(self, event):
        """Includes new event in simulation"""
        if isinstance(event, Event):
            if self.orderedlist != []:
                bisect.insort(self.orderedlist, event)
            else:
                self.orderedlist.append(event)

    def getfirst(self):
        """returns next event in line"""
        return self.orderedlist.pop(0)
    def remove(self, value):
        self.orderedlist.remove(value)

class Simulator(object):
    """Main class that goes time stepping"""
    def __init__(self):
        self.time = 0
        self.events = Queue()
    def insert(self, event):
        self.events.insert(event)


    def do_all_events(self):
        """Iterates over the entire events list"""
        while len(self.events.orderedlist) > 0:
            event = self.events.getfirst()
            event.execute()

class Beepsim(Simulator):
    def setup(self):
        self.insert(Beep(2))
        self.insert(Beep(4.3))
        self.do_all_events()

class Beep(Event):
    def execute(self):
        print "the time is " + str(self.time)

def main():
    """Executes simulation"""
    aa = Beepsim()
    aa.setup()

if __name__ == "__main__":
    main()
    