import os

# Base class representing a generic person
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

# Customer inherits from Person and adds banking details
class Customer(Person):
    def __init__(self, first_name, last_name, account_number, balance):
        # Using super() to reuse the initialization from the Person class
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance

    # Overriding the default string method to show the account dashboard
    def __str__(self):
        return f"CUSTOMER: {self.first_name} {self.last_name}\nAccount N°: {self.account_number}\nCurrent Balance: ${self.balance}"

    def deposit(self, amount_to_deposit):
        self.balance += amount_to_deposit
        print("\n>>> Depósito realizado con éxito.")

    def withdraw(self, amount_to_withdraw):
        # Core logic: checking if the customer has enough money before subtracting
        if self.balance >= amount_to_withdraw:
            self.balance -= amount_to_withdraw
            print("\n>>> Retiro realizado con éxito.")
        else:
            print("\n[!] Error: Saldo insuficiente.")

# Helper function to gather input and create a Customer object
def create_customer():
    # Clear the terminal for a cleaner UI
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- REGISTRO DE NUEVO CLIENTE ---")
    first_name = input("Ingrese su nombre: ")
    last_name = input("Ingrese su apellido: ")
    account = input("Ingrese su número de cuenta: ")
    
    # Using float since money can have decimals
    balance = float(input("Ingrese su saldo inicial: "))

    return Customer(first_name, last_name, account, balance)

# Main orchestrator function
def start_app():
    my_customer = create_customer()
    option = 0

    # Keep the menu running until the user types 3 to exit
    while option != 3:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("*" * 30)
        # This automatically calls the __str__ method!
        print(my_customer) 
        print("*" * 30)

        print("\nElija una opción:")
        print("1 - Depositar")
        print("2 - Retirar")
        print("3 - Salir")

        option = int(input("\nSu opción: "))

        if option == 1:
            amount = float(input("Monto a depositar: "))
            my_customer.deposit(amount)
        elif option == 2:
            amount = float(input("Monto a retirar: "))
            my_customer.withdraw(amount)
        elif option == 3:
            print("\nGracias por utilizar nuestros servicios.")

        # Pausing the loop so the user can read the success/error messages
        if option != 3:
            input("\nPresione Enter para continuar...")

# Standard Python entry point
if __name__ == '__main__':
    start_app()
