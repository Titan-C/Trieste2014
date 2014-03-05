# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 00:15:39 2014

@author: oscar
"""

class Customer(object):
    """Represents a customer in the Bank"""

    def __init__(self, count, t):
        self.name = count
        self.task = 12
        print str(self.name) + ' arrived at t =' + str(t)


class Server(object):
    """Represents chashier"""
    def __init__(self, identifier):
        self.isfree = True
        self.name = identifier
        print "cashier " + str(self.name) + " is free at t=0"

class Queue(object):
    """Holds the customers in the queue.
       Customers are server in a first come first served basis"""
    def __init__(self):
        self.queue = []
    def size(self):
        return len(self.queue)
    def add_customer(self, customer):
        """Queues customer to the queue"""
        self.queue.append(customer)

    def serve_customer(self):
        """Releases customer from the queue to be served by cashier"""
        return self.queue.pop(0)

class Bank(object):
    """Time iterator for simulation"""
    def __init__(self, cashiers):
        self.time = 0
        self.cashiers = [Server(i) for i in range(cashiers)]
        self.queue = Queue()
        print 'The bank opens at t=' + str(self.time) +' with:\n', \
                str(len(self.cashiers)) + ' cashiers\n', \
                str(self.queue.size())  + ' customers'

    def add_customer(self, customer):
        """Adds customer to Bank queue"""
        self.queue.add_customer(customer)
        print str(self.queue.size()) + 'customers in line'

    def workday(self,working_minutes):
        """Performs the time stepping for simulating a
           workday at the bank"""
           
        while self.time < working_minutes:
            try:
                

def main():
    """Executes simulation"""
    ubs = Bank(2)
    
    ubs.add_customer(Customer('mark', 2))
    
    ubs.workday(60*8)
    


if __name__ == "__main__":
    main()
