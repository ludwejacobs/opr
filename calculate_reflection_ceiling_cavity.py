import math


class calculateCav:

    def __init__(self, length, width, cavityHeight, rw, cavityReflection):
        self.length = length
        self.width = width
        self.rw = rw
        self.cavityHeight = cavityHeight
        self.cavityReflection = cavityReflection


def calculateCavity(length, width, cavityHeight, reflectionWall, cavityReflection):
    length = 17
    width = 40
    reflectionWall = 4
    cavityHeight = 110
    cavityReflection = 132

    cavityIndex = (length * width) / ((length + width) * cavityHeight)

    AreaTot = (length * width) + 2 * (length * cavityHeight) + 2 * (width * cavityHeight)

    AreaCavity = length * width

    AreaWalls = 2 * (length * cavityHeight) + 2 * (width * cavityHeight)

    AreaTot = AreaCavity + AreaWalls

    AreaWallReflection = reflectionWall * AreaWalls / AreaTot

    AreaCavityReflection = cavityReflection * AreaCavity / AreaTot

    AverageReflectance = AreaWallReflection + AreaCavityReflection

    EffectiveReflectance = (cavityIndex * AverageReflectance) / (cavityIndex + (2 * (1 - AverageReflectance)))

    return EffectiveReflectance





#
calc = calculateCavity(1, 1, 1, 1, 1)
print(calc)
