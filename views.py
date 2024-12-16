from typing import List


def display_menu():
    print("""
**************************
Welcome to CliManager v1.0
**************************

Select the number of your choice to display screen
[1] - Print my clients
[2] - Add a client
[3] - Update a client
[4] - Delete a client
[5] - Exit
""")


def choose_option():
    return input("pls enter you'r choose: ")


def print_clients(clients_list: List[dict]):
    for client in clients_list:
        print(client.values())


def print_add_client_message():
    print("""
    ::::::::::::::::
Add a client
****************

Select 5 to return to the menu
    """)


def get_input_to_add_client():
    user_dict = {}
    keys = ["ID", "Name", "Address", "Total spent Â£"]
    for key in keys:
        user_dict[key] = input(f"pls enter {key}: ")
    print("!! Client added !!")
    return user_dict


def print_update_client_message():
    print("""
    ::::::::::::::::
Edit a client
****************

Select 5 to return to the menu
    """)


def choose_id_to_update():
    return input("Choose an client ID for updating : ")


def display_found_client():
    print("[Client found]")


def display_client_not_found():
    print("[Client not found]")


def print_client_delete_message():
    print("Client deleted")

def get_new_client_details(current_address, current_total_spent):
    print("Let blank if no change")
    new_address = input(f"Address [{current_address}]: ")
    new_total_spent = input(f"Total spent [{current_total_spent}]: ")
    return new_address, new_total_spent


def display_client_updated():
    print("\n!! Client updated !!")


def print_delete_client_message():
    print("""
    ::::::::::::::::
Delete a client
****************
    """)


def choose_id_to_delete():
    return input("ID of the client to remove : ")
