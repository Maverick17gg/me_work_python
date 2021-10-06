dict = {
        "name": "Jon",
        "surname": "Smith",
        "age": 6,

    }
dict1 = {
        "name": "Bill",
        "surname": "Suns",
        "age": 20,
    }


templates = (
    "{name} {surname} закончил школу",
    "{name} {surname} скоро пойдёт в школу",
)

user = (dict, dict1)


print(templates[dict1["age"] < 7].format(name = dict1["name"], surname = dict1["surname"]))

