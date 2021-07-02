import Type
import Attack
import Stats

spez = "Special"
phys = "Physical"
status = "Status"


class Pokemon(object):
    def __init__(self, name, firstType, secondType, stats):
        self.name = name
        self.firstType = firstType
        self.secondType = secondType
        self.stats = stats

    def calculateEffecticityForPokemon(self, type):
        effect = self.firstType.calculateEffectivity(type)
        effect2 = self.secondType.calculateEffectivity(type)
        return effect * effect2


GengarBase = Stats(60, 65, 60, 130, 75, 110)
Gengar = Pokemon("Gengar", Type.Ghost, Type.Poison, GengarBase)

print(Gengar.calculateEffecticityForPokemon(Type.Ground))
