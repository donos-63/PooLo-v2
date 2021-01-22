from legumes.vegetable import Vegetable


class Carrot(Vegetable):

    def __init__(self) -> None:
        super().__init__('carrot')

    def grow(self, number=0) -> None:
        self.nb_seeds = number