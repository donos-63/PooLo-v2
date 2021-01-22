from legumes.vegetable import Vegetable


class Garden():

    MAX_SIZE = 30
    nb_seeds = 0

    def __init__(self) -> None:
        self.__garden = []

    def _plant(self, legume : Vegetable, quantity : int) -> None:
        if len(self.__garden) + quantity > Garden.MAX_SIZE:
            raise Exception("No more place")

        self.__garden.append(legume)
        Garden.nb_seeds += legume.nb_seeds

    def add_legume(self, legume: Vegetable) -> None:
        self._plant(legume, legume.nb_seeds)

    def get_empty_slots(self) -> int:
        return Garden.MAX_SIZE - len(self.__garden)

    def see_all(self):
        while self.__garden:
            yield self.__garden
        

