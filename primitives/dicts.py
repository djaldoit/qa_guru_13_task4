# Заводим словарики

d = {
    "key": "value",
    "another": "another value"
}

user1 = {
    "name": "Vasya",
    "age": 18,
}

user2 = {
    "name": "Petya",
    "age": 20,
}

users = {
    25: user1,
    42: user2
}

print(users[42])
print(user1["name"])
print(user2["name"])


users[55] = {"name": "Oleg", "age": 25}

# Функции словарей

print("-----")
from pprint import pprint
pprint(list(users.items()))

print("-----")
users.values()
users.keys()

# print(users[50])
print(users.get(50, {"name": "default user"}))
print(users.get(42, {"name": "default user"}))
