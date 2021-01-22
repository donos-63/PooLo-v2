from legumes.vegetable import Vegetable


class Tomato(Vegetable):
       
    def __init__(self) -> None:
        super().__init__('tomato')

    def grow(self, number=0) -> None:
        self.nb_seeds = number

    