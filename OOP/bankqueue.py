# -*- coding: utf-8 -*-
"""
@author: Oscar Najera
"""
from des_engine import *

class Customer(object):
    """Contains the customer visiting the Bank"""
    def __init__(self, time):
        self.time = time
    def __repr__(self):
        return str(self.time)

class Queue(object):
    server = None
    def __init__(self):
        self.customers = []
    def __gt__(self, other):
        return len(self.customers) > other
    def insert(self, simulator, customer):
        if self.server.isfree():
            self.server.insert(simulator, customer)
        else:
            self.customers.append(customer)
    def nextcustomer(self):
        return self.customers.pop(0)

class Generator(Event):
    """Simulates the arrival of customers"""
    queue = None
    def execute(self, simulator):
        print 'new customer at t= ' + str(self.time)
        customer = Customer(simulator.time)
        self.queue.insert(simulator, customer)
        self.time += 2
        if self.time < 10:
            simulator.insert(self)

class Server(Event):
    """Simulates the cashier"""
    queue = None
    def __init__(self):
        self.customerserved = None

    def isfree(self):
        if self.customerserved == None:
            return True

    def insert(self, simulator, customer):
        if self.customerserved != None:
            print 'Im busy with a customer'
        self.customerserved = customer
        print 'receiving custormer['+str(customer)+'] at t= ' + str(simulator.time)
        self.time = simulator.time + 2.5
        simulator.insert(self)

    def execute(self, simulator):
        print 'served customer[' + str(self.customerserved) + '] at t= ' + str(self.time)
        self.customerserved = None
        if self.queue > 0:
            print 'hay clientes en cola'
            self.insert(simulator, self.queue.nextcustomer())

class BankSimulator(Simulator):
    """Simulates the Workday of a Bank"""
    def run(self):
        generator = Generator()
        queue = Queue()
        server = Server()

        generator.queue = queue
        queue.server = server
        server.queue = queue

        self.insert(generator)
        self.do_all_events()

if __name__ == "__main__":
    UBS = BankSimulator()
    UBS.run()
