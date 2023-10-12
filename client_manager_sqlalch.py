from pprint import pprint
from rich.console import Console
from rich.table import Table
from sqlalchemy import create_engine, Column, String, Integer
# from sqlalchemy.ext.declarative import declarative_base It's deprecated. Now it belongs to sqlalchemy.orm.
from sqlalchemy.orm import sessionmaker, declarative_base

'''we create Base, which will return a class - to inherit from; the base for our first class (Client):'''
Base = declarative_base()


class Client(Base):
    __tablename__ = "clients"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    address = Column("address", String)
    total_spent = Column("total_spent", Integer, default=0)

    '''we define a constructor'''

    def __init__(self, id, first, last, address, total_spent=0):
        self.id = id
        self.firstname = first
        self.lastname = last
        self.address = address
        self.total_spent = total_spent

    def __repr__(self):
        return f"({self.id}) {self.firstname} {self.lastname} ({self.address}), ({self.total_spent})"


engine = create_engine("sqlite:///mydb_client_manager.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


def view_clients():
    clients = session.query(Client).all()

    if clients:
        table = Table(title='Clients', show_lines=True, min_width=100)

        table.add_column("ID", justify='right', style='cyan')
        table.add_column("First Name", justify='center', style='magenta')
        table.add_column("Last Name", justify='center', style='magenta')
        table.add_column("Address", justify='center', style='magenta')
        table.add_column("Total Amount Spent $", justify='right', style='green')

        for client in clients:
            table.add_row(str(client.id), str(client.firstname), str(client.lastname),
                          str(client.address), str(client.total_spent))

        console = Console()
        console.print(table)

        print("\nClient List:")
        pprint(clients, width=30)
    else:
        print()
        print("No clients found!")
    print()


def add_client():
    client = Client(id=0, first='', last='', address='', total_spent=0)

    while True:
        try:
            client.id = int(input("Enter client ID number: "))
        except ValueError:
            print("Invalid option. Please enter a number.")
        else:
            break

    while True:
        client.firstname = input("Enter client's first name: ").title()
        if client.firstname == '' or client.firstname.isdigit():
            print("Invalid option. Please enter a name.")
        else:
            break

    while True:
        client.lastname = input("Enter client's last name: ").title()
        if client.lastname == '' or client.lastname.isdigit():
            print("Invalid option. Please enter a name.")
        else:
            break

    while True:
        client.address = input("Enter client address: ").title()
        if client.address == '' or client.address.isdigit():
            print("Invalid option. Please enter an address.")
        else:
            break

    while True:
        try:
            client.total_spent = int(input("Enter total amount spent: "))
        except ValueError:
            print("Invalid option. Please enter a number.")
        else:
            break

    id = client.id
    first = client.firstname
    last = client.lastname
    address = client.address
    total_spent = client.total_spent

    client = Client(id, first, last, address, total_spent)

    session.add(client)
    session.commit()

    print()
    print("Client added successfully!\n")


def find_client_by_id():
    client_id = input("Enter client ID to look for: ")
    details = session.query(Client).filter(Client.id == client_id).first()
    if details:
        print("\n======= Client Details ======")
        print(details.id, " | ", details.firstname, " - ", details.lastname)
        print()
    else:
        return None
    return client_id


def find_client_by_lastname():
    client_lastname = input("Enter client last name to look for: ").title()
    results = session.query(Client).filter(Client.lastname == client_lastname).all()
    if results:
        print("\n======= Client(s) Details ======\n")
        for result in results:
            print(result)
            print()
    else:
        print("\nClient not found. Retry.\n")
    return client_lastname


def edit_client():
    view_clients()
    client_id = find_client_by_id()
    if client_id:
        client = session.get(Client, client_id)

        print("\nClient Details:")
        print("ID:", client.id)
        print("First Name:", client.firstname)
        print("Last Name:", client.lastname)
        print("Address:", client.address)
        print("Total Amount Spent:", client.total_spent)

        new_client_id = input("\nEnter updated client ID (press Enter to keep current): ")
        if new_client_id:
            client.id = new_client_id

        new_client_first_name = input("Enter updated client first name (press Enter to keep current): ").title()
        if new_client_first_name:
            client.firstname = new_client_first_name

        new_client_last_name = input("Enter updated client last name (press Enter to keep current): ").title()
        if new_client_last_name:
            client.lastname = new_client_last_name

        new_client_address = input("Enter updated client address (press Enter to keep current): ").title()
        if new_client_address:
            client.address = new_client_address

        while True:
            new_amount_spent = input("Enter updated total amount spent (press Enter to keep current): ")
            if new_amount_spent == '':
                break
            elif new_amount_spent.isdigit():
                client.total_spent = new_amount_spent
                break
            else:
                print("Invalid option. Please enter a number.")

        session.commit()

        print("Client details updated successfully!")
    else:
        print()
        print("Client not found!")
    print()


def delete_client():
    view_clients()
    client_id = find_client_by_id()
    if client_id:
        while True:
            client = session.get(Client, client_id)
            confirm = input("\nDo you want to delete this contact y/n? ")
            if confirm.lower() == 'y':
                session.delete(client)
                session.commit()
                print()
                print("*" * 29)
                print("Client deleted successfully!")
                print("*" * 29)
                break
            elif confirm.lower() == 'n':
                break
            else:
                print("Invalid option. Try again.")
    else:
        print()
        print("Client not found!")
    print()


def main():
    while True:
        print("*" * 29)
        print("Welcome to ClientManager v1.0")
        print("*" * 29)

        prompt = """
Select the number of your choice to display screen:   
    [1] - Print my clients
    [2] - Add a client
    [3] - Edit a client
    [4] - Get client details
    [5] - Delete a client
    [6] - Exit
"""
        choice = input(prompt)

        if choice == '1':
            view_clients()
        elif choice == '2':
            add_client()
        elif choice == '3':
            edit_client()
        elif choice == '4':
            id_or_lastname = input("Do you want by client id or by client lastname? Type 'id' or 'last': ").lower()
            if id_or_lastname == 'id':
                find_client_by_id()
            elif id_or_lastname == 'last':
                find_client_by_lastname()
            else:
                print('Invalid choice. Try again')
        elif choice == '5':
            delete_client()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

