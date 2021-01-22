from abc import ABC, abstractmethod

class Vegetable(ABC):
    
    def __init__(self, name):
        self.name = name
        self.nb_seeds = 0
        print(self.name + " created")

    def __str__(self):
        self.name

    @abstractmethod
    def grow(self, number=0):
        pass
