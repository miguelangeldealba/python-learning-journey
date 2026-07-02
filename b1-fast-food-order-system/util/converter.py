from abc import ABC, abstractmethod
from products.product import Hamburger, Soda, Drink, HappyMeal
from users.user import Cashier, Customer


class Converter(ABC):

    @abstractmethod
    def convert(self, data):
        pass

    def print(self, objects):
        for obj in objects:
            print(obj)


class ProductConverter(Converter):
    # CSV a objetos Product
    def __init__(self, product_type: str):
        self.product_type = product_type

    def convert(self, data):
        products = []

        for _, row in data.iterrows():
            id = row["id"]
            name = row["name"]
            price = float(row["price"])

            if self.product_type == "hamburger":
                product = Hamburger(id, name, price)
            elif self.product_type == "soda":
                product = Soda(id, name, price)
            elif self.product_type == "drink":
                product = Drink(id, name, price)
            elif self.product_type == "happymeal":
                product = HappyMeal(id, name, price)
            else:
                raise ValueError("Tipo de producto no válido")

            products.append(product)

        return products


class CashierConverter(Converter):
    # CSV a objetos Cashier
    def convert(self, data):
        cashiers = []

        for _, row in data.iterrows():
            dni = row["dni"]
            name = row["name"]
            age = int(row["age"])
            timetable = row["timetable"]
            salary = float(row["salary"])

            cashier = Cashier(dni, name, age, timetable, salary)
            cashiers.append(cashier)

        return cashiers


class CustomerConverter(Converter):
    # CSV a objetos Customer
    def convert(self, data):
        customers = []

        for _, row in data.iterrows():
            dni = row["dni"]
            name = row["name"]
            age = int(row["age"])
            email = row["email"]
            postal_code = row["postal_code"]

            customer = Customer(dni, name, age, email, postal_code)
            customers.append(customer)

        return customers