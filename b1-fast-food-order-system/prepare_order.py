from util.file_manager import CSVFileManager
from util.converter import ProductConverter, CashierConverter, CustomerConverter
from orders.order import Order


# Buscar cajero DNI
def find_cashier_by_dni(cashiers, dni):
    dni = str(dni).strip()

    for cashier in cashiers:
        if str(cashier.dni).strip() == dni:
            return cashier

    return None


# Buscar cliente DNI
def find_customer_by_dni(customers, dni):
    dni = str(dni).strip()

    for customer in customers:
        if str(customer.dni).strip() == dni:
            return customer

    return None


# Buscar producto ID
def find_product_by_id(products, product_id):
    product_id = product_id.strip().lower()

    for product in products:
        if product.id.lower() == product_id:
            return product

    return None


# Mostrar productos
def show_products(products):
    print("\nProduct list:")
    for product in products:
        package = product.foodPackage()
        print(
            f"Product - Type: {product.type()}, "
            f"Name: {product.name}, "
            f"Id: {product.id}, "
            f"Price: {product.price}, "
            f"Wrapping: {package.pack()}, "
            f"Material: {package.material()}"
        )


# Leer CSV
cashier_data = CSVFileManager("data/cashiers.csv").read()
customer_data = CSVFileManager("data/customers.csv").read()
hamburger_data = CSVFileManager("data/hamburgers.csv").read()
soda_data = CSVFileManager("data/sodas.csv").read()
drink_data = CSVFileManager("data/drinks.csv").read()
happymeal_data = CSVFileManager("data/happyMeal.csv").read()

# Datos a objetos
cashiers = CashierConverter().convert(cashier_data)
customers = CustomerConverter().convert(customer_data)

hamburgers = ProductConverter("hamburger").convert(hamburger_data)
sodas = ProductConverter("soda").convert(soda_data)
drinks = ProductConverter("drink").convert(drink_data)
happymeals = ProductConverter("happymeal").convert(happymeal_data)

products = hamburgers + sodas + drinks + happymeals

# Mostrar cajeros
print("Cashiers:")
for cashier in cashiers:
    print(cashier.describe())

# Mostrar clientes
print("\nCustomers:")
for customer in customers:
    print(customer.describe())

# Pedir DNI cajero
cashier_dni = input("\nIntroduce cashier DNI: ")
cashier = find_cashier_by_dni(cashiers, cashier_dni)

if cashier is None:
    print("Cashier not found.")
    exit()

print(cashier.describe())

# Pedir DNI cliente
customer_dni = input("\nIntroduce customer DNI: ")
customer = find_customer_by_dni(customers, customer_dni)

if customer is None:
    print("Customer not found.")
    exit()

print(customer.describe())

# Crear pedido
order = Order(cashier, customer)

show_products(products)

# Elegir productos
while True:
    product_id = input("\nIntroduce product id: ")
    product = find_product_by_id(products, product_id)

    if product is None:
        print("Product not found.")
    else:
        package = product.foodPackage()
        print(
            f"Product - Type: {product.type()}, "
            f"Name: {product.name}, "
            f"Id: {product.id}, "
            f"Price: {product.price}, "
            f"Wrapping: {package.pack()}, "
            f"Material: {package.material()}"
        )
        order.add(product)

    another = input("Do you want to add another product? (yes/no): ").strip().lower()
    if another != "yes":
        break

# Resultado final
print("\nFinal order:")
order.show()