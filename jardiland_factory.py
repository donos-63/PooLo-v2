from jardiland_product import JardilandProduct
from legumes.pickle import Pickle
from legumes.tomato import Tomato
from legumes.carrot import Carrot

class jardilandFactory():

    def give_me_seeds(type : JardilandProduct):
        if type == JardilandProduct.Tomato:
            return Tomato()

        if type == JardilandProduct.Pickle:
            return Pickle()

        if type == JardilandProduct.Carrot:
            return Carrot()

        raise ValueError("bad type : " + type)