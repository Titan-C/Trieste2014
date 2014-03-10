# -*- coding: utf-8 -*-
"""
@author: Oscar Najera
Tutorial implementation initial solution
Developed for the ICTP Workshop
"""
from des_engine import Event, Simulator
from numpy.random import exponential

class Customer(object):
    """Contains the customer visiting the Bank"""

    def __init__(self, time):
        self.time = time

    def __repr__(self):
        return str(self.time)


class Queue(object):
    """Waiting Queue in the Bank"""

    server = None

    def __init__(self):
        self.customers = []

    def __gt__(self, other):
        return len(self.customers) > other


    def insert(self, simulator, customer):
        """Queues arriving customer directly to server if free,
           or puts customer in waiting queue"""
        if self.server.isfree():
            self.server.insert(simulator, customer)
        else:
            self.customers.append(customer)

    def nextcustomer(self):
        """Takes out the first in line customer"""
        return self.customers.pop(0)


class NewArrival(Event):
    """Simulates the arrival of customers"""

    queue = None

    def __init__(self, time, maxtime):
        self.time = time
        self.maxtime = maxtime

    def execute(self, simulator):
        """Generates new customer at given time"""
        print 'new customer at t= ' + str(self.time)
        customer = Customer(simulator.time)
        self.queue.insert(simulator, customer)
        self.time += exponential(4)
        if self.time < self.maxtime:
            simulator.insert(self)


class Server(Event):
    """Simulates the cashier"""

    queue = None

    def __init__(self):
        self.customerserved = None
        self.time = 0

    def isfree(self):
        """Test if server is free to receive customer in line"""
        if self.customerserved == None:
            return True

    def insert(self, simulator, customer):
        """Takes customer"""
        if self.customerserved != None:
            print 'Already busy with a customer'
        self.customerserved = customer
        print 'receiving customer[', customer, '] at t=', simulator.time
        self.time = simulator.time + 2.5
        simulator.insert(self)

    def execute(self, simulator):
        """Completes serving customer and takes new one if waiting"""
        print 'served customer[', self.customerserved, '] at t=', self.time
        self.customerserved = None
        if self.queue > 0:
            self.insert(simulator, self.queue.nextcustomer())


class BankSimulator(Simulator):
    """Simulates the Workday of a Bank"""

    def run(self):
        """Runs simulation"""
        newarrival = NewArrival(0, 30)
        queue = Queue()
        server = Server()

        newarrival.queue = queue
        queue.server = server
        server.queue = queue

        self.insert(newarrival)
        self.do_all_events()


if __name__ == "__main__":
    UBS = BankSimulator()
    UBS.run()
