import requests

try:
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    print("\n===== User Details =====\n")

    for user in users:
        print("Name :", user["name"])
        print("Email:", user["email"])
        print("City :", user["address"]["city"])
        print("-------------------")

except Exception as error:
    print("Something went wrong!")
    print(error)
