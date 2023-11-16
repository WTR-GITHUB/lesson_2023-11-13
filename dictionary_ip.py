person = {
    "name": "Vytautas",
    "surname": "Sluckas",
    "ip": "127.0.0.1",
    "programming_language": "python",
    "address": {"Street": "some street", "House Number": "some house number"},
    "languages": ["Lithuanian", "English", "Norwegian"],
}

person1 = {
    "name": "Tomas",
    "surname": "BLABLABA",
    "ip": "162.2.0.2",
    "programming_language": "python",
    "address": {"Street": "some street", "House Number": "some house number"},
    "languages": ["Latvian", "English", "Swedish"],
}

person2 = {
    "name": "Tom",
    "surname": "Edison",
    "ip": "127.2.0.1",
    "programming_language": "python",
    "address": {"Street": "some street", "House Number": "some house number"},
    "languages": ["Latvian", "English", "Swedish"],
}


people = [person, person1, person2]

print([human for human in people if human.get("ip").split(".")[1] == "2"])
