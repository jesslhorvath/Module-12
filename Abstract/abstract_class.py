"""
Programs: abstract_class.py, driver.py
Author: Jessie Horvath
Modified: 4/24/22

The purpose of this program is to create an abstract class and subclasses,
create instances of the classes and call methods to ensure the
parent class methods were overriden.
"""

from abc import ABC, abstractmethod

class Rider(ABC):
    def __init__(self, ride, rider):
        self.ride_type = ride
        self.rider = rider

    def ride(self):
        pass

    def riders(self):
        pass


class Bicycle(Rider):
    def __init__(self):
        self.ride_type = "Human powered, not enclosed"
        self.rider = "1 or 2 if tandem or daredevil"

    def ride(self):
        return str(self.ride_type)
    
    def riders(self):
        return str(self.rider)

class Motorcycle(Rider):
    def __init__(self):
        self.ride_type = "Engine powered, not enclosed"
        self.rider = "1 or 2"

    def ride(self):
        return str(self.ride_type)
    
    def riders(self):
        return str(self.rider)

class Car(Rider):
    def __init__(self):
        self.ride_type = "Engine powered, enclosed"
        self.rider = "1 plus comfortably"

    def ride(self):
        return str(self.ride_type)

    def riders(self):
        return str(self.rider)
