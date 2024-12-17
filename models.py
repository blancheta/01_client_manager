clients = [
    {
        "ID": 1,
        "Name": "omid",
        "Address": "tehran",
        "Total spent Â£": "100"
    },
    {
        "ID": 2,
        "Name": "qazal",
        "Address": "tehran",
        "Total spent Â£": "200"
    },
    {
        "ID": 3,
        "Name": "sina",
        "Address": "tehran",
        "Total spent Â£": "300"
    }
]


def get_clients():
    return clients


def add_client(client_dict: dict):
    clients.append(client_dict)


def client_exist(client_id):
    for client in clients:
        if int(client["ID"]) == int(client_id):
            return True

    return False


def update_client(client_id, new_address, new_total_spent):
    for client in clients:
        if client["ID"] == client_id:
            if new_address:
                client["Address"] = new_address
            if new_total_spent:
                client["Total spent Â£"] = new_total_spent
            return True
    return False


def delete_client(client_id):
    for client in clients:
        if client["ID"] == client_id:
            clients.remove(client)
            return True
    return False
