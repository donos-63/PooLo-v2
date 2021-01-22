from legumes.vegetable import Vegetable
from garden import Garden

class Gardener():

    def __init__(self) -> None:
        self.nb_seeds = 0
        self._create_garden()
        print('Gardener created')

    def _create_garden(self):
        if not hasattr(self, "gardens"):
            self.gardens = []

        self.gardens.append(Garden())
        print('Garden created')


    def add(self, legume : Vegetable):
        try:
            self.gardens[-1].add_legume(legume)
            self.nb_seeds += legume.nb_seeds
            print('legume added')

        except :
            self._create_garden()
            self.add(Vegetable)

