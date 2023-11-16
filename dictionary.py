from typing import Dict, List


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
    "ip": "127.0.0.1",
    "programming_language": "python",
    "address": {"Street": "some street", "House Number": "some house number"},
    "languages": ["Latvian", "English", "Swedish"],
}

people = [person, person1]


def get_most_popular_language(people: List[Dict]) -> str:
    language_counts = {}
    for human in people:
        for language in human["languages"]:
            if language in language_counts:
                language_counts[language] += 1
            else:
                language_counts[language] = 1

    max_value = None
    max_key = None
    for key, value in language_counts.items():
        if max_key == None or max_value < value:
            max_value, max_key = value, key
    return max_key

    # max_value = None
    # max_key = None
    # for key, value in language_counts:
    # if max_key == None:
    #   max_value = value
    #   max_key = key
    # elif max_value < value:
    #   max_value = value
    #   max_key = key
    #

    # return max(language_counts, key=language_counts.get)


print(get_most_popular_language(people))


# create dictionary with language counts
# for person in people:
# get persons languages
# for language in languages:
# if language is new:
# add key to dictionary with language counts
# else if langauge is not new:
# add count +1 to already existing language in dictionary with language counts
