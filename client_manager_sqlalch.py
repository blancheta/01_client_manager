from pprint import pprint
from rich.console import Console
from rich.table import Table
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
# from sqlalchemy.ext.declarative import declarative_base It's deprecated. Now it belongs to sqlalchemy.orm.
from sqlalchemy.orm import sessionmaker, declarative_base

'''we create Base, which will return a class - to inherit from; the base for our first class (Client):'''
Base = declarative_base()


class Client(Base):
    __tablename__ = "clients"
    id = Column("id", Integer, primary_key=True, autoincrement=True) # VEZI CE E CU autoincrement!!!!
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    address = Column("address", String)
    total_spent = Column("total_spent", Integer, default=0) # vezi CE E CU default=0

    '''we define a constructor'''

    def __init__(self, id, first, last, address, total_spent=0):
        self.id = id
        self.firstname = first
        self.lastname = last
        self.address = address
        self.total_spent = total_spent

    def __repr__(self):
        return f"({self.id}) {self.firstname} {self.lastname} ({self.address}, {self.total_spent})"


engine = create_engine("sqlite:///mydb_client_manager.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# results = session.query(Client).all()


def view_clients(clients):
    if clients:
        table = Table(title='Clients', show_lines=True, min_width=100)

        table.add_column("ID", justify='right', style='cyan')
        table.add_column("First Name", justify='center', style='magenta')
        table.add_column("Last Name", justify='center', style='magenta')
        table.add_column("Address", justify='center', style='magenta')
        table.add_column("Total Amount Spent $", justify='right', style='green')

        for client in clients:
            table.add_row(str(client['ID']), str(client['First Name']), str(client['Last Name']),
                          str(client['Address']), str(client['Total Amount Spent']))

        console = Console()
        console.print(table)

        print("\nClient List:")
        pprint(clients, width=30)
    else:
        print("No clients found.")
    print()


def add_client(clients):
    client = {}
    while True:
        try:
            client['ID'] = int(input("Enter client ID number: "))
        except ValueError:
            print("Invalid option. Please enter a number.")
        else:
            break

    while True:
        client['First Name'] = input("Enter client's first name: ").title()
        if client['First Name'] == '' or client['First Name'].isdigit():
            print("Invalid option. Please enter a name.")
        else:
            break

    while True:
        client['Last Name'] = input("Enter client's last name: ").title()
        if client['Last Name'] == '' or client['Last Name'].isdigit():
            print("Invalid option. Please enter a name.")
        else:
            break

    while True:
        client['Address'] = input("Enter client address: ").title()
        if client['Address'] == '' or client['Address'].isdigit():
            print("Invalid option. Please enter an address.")
        else:
            break

    while True:
        try:
            client['Total Amount Spent'] = int(input("Enter total amount spent: "))
        except ValueError:
            print("Invalid option. Please enter a number.")
        else:
            break
    clients.append(client)

    # client = Client(client['ID'], client['First Name'], client['Last Name'], client['Address'], client['Total Amount Spent'])
    id = client["ID"]
    first = client["First Name"]
    last = client["Last Name"]
    address = client["Address"]
    total_spent = client["Total Amount Spent"]

    client = Client(id, first, last, address, total_spent)


    session.add(client)
    session.commit()

    print()
    print("Client added successfully!\n")


def find_client_by_id(clients, client_id):
    for client in clients:
        if client['ID'] == int(client_id):

            return client
    return None


def edit_client(clients):
    print(clients)
    client_id = input("Enter client ID to edit: ")
    client = find_client_by_id(clients, client_id)

    if client:
        print("\nClient Details:")
        print("ID:", client['ID'])
        print("First Name:", client['First Name'])
        print("Last Name:", client['Last Name'])
        print("Address:", client['Address'])
        print("Total Amount Spent:", client['Total Amount Spent'])

        new_client_id = input("\nEnter updated client ID (press Enter to keep current): ")
        if new_client_id:
            client['ID'] = new_client_id

        new_client_first_name = input("Enter updated client first name (press Enter to keep current): ").title()
        if new_client_first_name:
            client['First Name'] = new_client_first_name

        new_client_last_name = input("Enter updated client last name (press Enter to keep current): ").title()
        if new_client_last_name:
            client['Last Name'] = new_client_last_name

        new_client_address = input("Enter updated client address (press Enter to keep current): ").title()
        if new_client_address:
            client['Address'] = new_client_address

        while True:
            new_amount_spent = input("Enter updated total amount spent (press Enter to keep current): ")
            if new_amount_spent == '':
                break
            elif new_amount_spent.isdigit():
                client["Total Amount Spent"] = new_amount_spent
                break
            else:
                print("Invalid option. Please enter a number.")

        print("Client details updated successfully!")
    else:
        print("Client not found.")
    print()

def delete_client(clients):
    client_id = input("Enter client ID to delete: ")
    client = find_client_by_id(clients, client_id)
    if client:
        clients.remove(client)
        print("Client deleted successfully!")
    else:
        print("Client not found.")
    print()


def main():
    clients = []

    while True:
        print("*" * 29)
        print("Welcome to ClientManager v1.0")
        print("*" * 29)

        prompt = """
Select the number of your choice to display screen:   
    [1] - Print my clients
    [2] - Add a client
    [3] - Edit a client
    [4] - Delete a client
    [5] - Exit
"""
        choice = input(prompt)

        if choice == '1':
            view_clients(clients)
        elif choice == '2':
            add_client(clients)
        elif choice == '3':
            edit_client(clients)
        elif choice == '4':
            delete_client(clients)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


