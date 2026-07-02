from products.product import Product
from users.user import Cashier, Customer


class Order:

    # Pedido con cajero y cliente
    def __init__(self, cashier: Cashier, customer: Customer):
        self.cashier = cashier
        self.customer = customer
        self.products = []

    # Añadir producto a pedido
    def add(self, product: Product):
        self.products.append(product)

    # Precio total
    def calculateTotal(self) -> float:
        total = 0.0

        for product in self.products:
            total += product.price

        return total

    # Mostrar pedido
    def show(self):
        print(f"Hello: {self.customer.describe()}")
        print(f"Was attended by: {self.cashier.describe()}")

        # Mostrar productos
        for i, product in enumerate(self.products, start=1):
            print(
                f"Product {i}: Type: {product.type()}, "
                f"Name: {product.name}, "
                f"Id: {product.id}, "
                f"Price: {product.price}, "
                f"Wrapping: {product.foodPackage().pack()}, "
                f"Material: {product.foodPackage().material()}"
            )

        # Mostrar total
        print(f"Total price: {self.calculateTotal()}")