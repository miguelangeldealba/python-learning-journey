from abc import ABC, abstractmethod

# Empaquetado + material

class FoodPackage(ABC):

    @abstractmethod
    def pack(self) -> str:
        pass

    @abstractmethod
    def material(self) -> str:
        pass


class Wrapping(FoodPackage):

    def pack(self) -> str:
        return "Food Wrap Paper"

    def material(self) -> str:
        return "Aluminium"


class Bottle(FoodPackage):

    def pack(self) -> str:
        return "Bottle"

    def material(self) -> str:
        return "Plastic"


class Glass(FoodPackage):

    def pack(self) -> str:
        return "Glass"

    def material(self) -> str:
        return "Crystal"


class Box(FoodPackage):

    def pack(self) -> str:
        return "Box"

    def material(self) -> str:
        return "Cardboard"