from views import display_menu, choose_option, print_clients, print_add_client_message, get_input_to_add_client, \
    print_update_client_message, choose_id_to_update, display_found_client, display_client_not_found, \
    get_new_client_details, display_client_updated, print_delete_client_message, choose_id_to_delete, \
    print_client_delete_message
from models import get_clients, add_client, client_exist, update_client, delete_client


def edit_client():
    print_update_client_message()
    chosen_client_id = int(choose_id_to_update())
    if client_exist(chosen_client_id):
        display_found_client()
        for client in get_clients():
            if client["ID"] == chosen_client_id:
                new_address, new_total_spent = get_new_client_details(client["Address"], client["Total spent Â£"])
                if update_client(chosen_client_id, new_address, new_total_spent):
                    display_client_updated()
                break
    else:
        display_client_not_found()


def del_client():
    print_delete_client_message()
    chosen_client_id = int(choose_id_to_delete())
    if delete_client(chosen_client_id):
        print_client_delete_message()
    else:
        display_client_not_found()


def main():
    while True:
        display_menu()
        users_choice = choose_option()

        if users_choice == "1":
            clients_list = get_clients()
            print_clients(clients_list)

        elif users_choice == "2":
            print_add_client_message()
            add_client(get_input_to_add_client())

        elif users_choice == "3":
            edit_client()

        elif users_choice == "4":
            del_client()


if __name__ == "__main__":
    main()