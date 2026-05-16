import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

users = []

print("===== User Details =====\n")

for user in data:
    user_info = {
        "name": user["name"],
        "email": user["email"],
        "city": user["address"]["city"]
    }

    users.append(user_info)

    print(f"Name : {user['name']}")
    print(f"Email: {user['email']}")
    print(f"City : {user['address']['city']}")
    print("------------------------")

with open("output.json", "w") as file:
    json.dump(users, file, indent=4)

print("\nData saved into output.json")
