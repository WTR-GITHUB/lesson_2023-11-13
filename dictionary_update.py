from typing import Dict

dict_one = {"a": 10, "b": 20, "c": 30}
dict_two = {"b": 200, "d": 400}


def custom_dictionary_update(
    first_dictionary: Dict, second_dictionary: Dict, overwrite: bool = True
) -> Dict:
    if overwrite == True:
        first_dictionary.update(second_dictionary)
    else:
        for key, value in second_dictionary.items():
            if key not in first_dictionary:
                first_dictionary[key] = value
    return first_dictionary


# print(custom_dictionary_update(dict_one, dict_two, False))

# d = dict_one.pop("b")
new_dict = {"d": dict_one.pop("b")}
print(dict_one)
print(new_dict)

# if overwrite == True:
#   update first dictioanry with the second one as with dictionary update method
# else:
#   do not overwrite values from the first dictionary, only add new values from the second one.
