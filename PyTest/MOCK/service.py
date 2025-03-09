import requests

database = {
    1: "MeyiGi",
    2: "MeyiGi",
    3: "MeyiGi",
}


def get_user_from_db(user_id):
    return database.get(user_id)


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    if response.status_code == 200:
        return response.json()
    
    return requests.HTTPError