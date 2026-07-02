from abc import ABC, abstractmethod
from products.food_package import Wrapping, Bottle, Glass, Box


class Product(ABC):

    # Crear producto tipo + empaquetado
    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    @abstractmethod
    def type(self) -> str:
        pass

    @abstractmethod
    def foodPackage(self):
        pass


 # Productos + empaquetado

class Hamburger(Product):

    def type(self) -> str:
        return "Hamburger"

    def foodPackage(self):
        return Wrapping()



class Soda(Product):

    def type(self) -> str:
        return "Soda"

    def foodPackage(self):
        return Bottle()



class Drink(Product):

    def type(self) -> str:
        return "Drink"

    def foodPackage(self):
        return Glass()



class HappyMeal(Product):

    def type(self) -> str:
        return "HappyMeal"

    def foodPackage(self):
        return Box()