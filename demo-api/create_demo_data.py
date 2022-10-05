import requests
import random

names = ["Bob", "Joe", "Harry", "Sam", "Lemon", "Gabby", "Pat", "Luca", "Trixie", "Jacob", "Pumpkin", "Smokey"]
breeds = ["Orange", "Black", "Tabby", "Shorthair"]

for i in range(10000):
    response = requests.post("http://localhost:8000/api/v1/cat/", data={
        "name": random.choices(names),
        "breed": random.choices(breeds),
        "age": random.randint(1, 18)
    })
    print(i)