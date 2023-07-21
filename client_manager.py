def view_clients(clients):
    if clients:
        print("Client List:")
        for client in clients:
            print("ID:", client['ID'])
            print("Name:", client['Name'])
            print("Address:", client['Address'])
            print("Total Amount Spent:", client['Total Amount Spent'])
            print()
        print(clients)
    else:
        print("No clients found.")
    print()

def add_client(clients):
    client = {}
    client['ID'] = input("Enter client ID: ")
    client['Name'] = input("Enter client name: ").title()
    client['Address'] = input("Enter client address: ").title()
    while True:
        try:
            client['Total Amount Spent'] = int(input("Enter total amount spent: "))
        except ValueError:
            print("Invalid option. Please enter a number.")
        else:
            break
    clients.append(client)
    print()
    print("Client added successfully!\n")


def find_client_by_id(clients, client_id):
    for client in clients:
        if client['ID'] == client_id:

            return client
    return None


def edit_client(clients):
    print(clients)
    client_id = input("Enter client ID to edit: ")
    client = find_client_by_id(clients, client_id)

    if client:
        print("\nClient Details:")
        print("ID:", client['ID'])
        print("Name:", client['Name'])
        print("Address:", client['Address'])
        print("Total Amount Spent:", client['Total Amount Spent'])

        new_client_id = input("Enter updated client ID (press Enter to keep current): ")
        if new_client_id:
            client['ID'] = new_client_id
        new_client_name = input("Enter updated client name (press Enter to keep current): ").title()
        if new_client_name:
            client['Name'] = new_client_name
        new_client_address = input("Enter updated client address (press Enter to keep current): ").title()
        if new_client_address:
            client['Address'] = new_client_address
        new_amount_spent = input("Enter updated total amount spent (press Enter to keep current): ")
        if new_amount_spent:
            client["Total Amount Spent"] = new_amount_spent

        print("Client details updated successfully!")

    else:
        print("Client not found.")


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


