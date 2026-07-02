from abc import ABC, abstractmethod

class User(ABC):

    # Crear usuario
    def __init__(self, dni: str, name: str, age: int):
        self.dni = dni
        self.name = name
        self.age = age

    # Describir usuario
    @abstractmethod
    def describe(self) -> str:
        pass



class Cashier(User):

    # Crear cajero
    def __init__(self, dni: str, name: str, age: int, timetable: str, salary: float):
        super().__init__(dni, name, age)
        self.timetable = timetable
        self.salary = salary

    # Mostrar datos de cajero
    def describe(self) -> str:
        return f"Cashier - Name: {self.name}, DNI: {self.dni}, Age: {self.age}, Timetable: {self.timetable}, Salary: {self.salary}"


class Customer(User):

    # Crear cliente
    def __init__(self, dni: str, name: str, age: int, email: str, postal_code: str):
        super().__init__(dni, name, age)
        self.email = email
        self.postal_code = postal_code

    # Mostrar datos de cliente
    def describe(self) -> str:
        return f"Customer - Name: {self.name}, DNI: {self.dni}, Age: {self.age}, Email: {self.email}, Postal Code: {self.postal_code}"