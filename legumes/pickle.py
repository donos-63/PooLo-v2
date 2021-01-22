from legumes.vegetable import Vegetable


class Pickle(Vegetable):

    def __init__(self):
        super().__init__('pickle')

    def grow(self, number=0) -> None:
        self.nb_seeds = number