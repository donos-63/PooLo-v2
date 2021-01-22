from garden import Garden
from gardener import Gardener
from jardiland_factory import jardilandFactory
from jardiland_product import JardilandProduct

g = Gardener() #instance de classe
t = jardilandFactory.give_me_seeds(JardilandProduct.Carrot) #factory
g.add(t) #injection
p = jardilandFactory.give_me_seeds(JardilandProduct.Pickle)
p.grow(8)
g.add(p)

print(g.nb_seeds) #8 graines / affecté au jardinier (pas de sens)
#print(g.nb_seeds()) #aurait été plus logique de comprendre
print(Garden.nb_seeds) #8 graines / variable de classe

