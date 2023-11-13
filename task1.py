from typing import Union


class Family:
    def __init__(
        self,
        sister: Union[str, int],
        father: Union[str, int],
        mother: Union[str, int],
        brother: Union[str, int],
    ) -> None:
        self.sister = sister
        self.father = father
        self.mother = mother
        self.brother = brother

    def create_list(self):
        data_list = [self.sister, self.father, self.mother, self.brother]
        return data_list

    def dictionary_from_two_lists(list_a: list, list_b: list) -> dict:
        dict_family = dict(zip(list_a, list_b))
        return dict_family

    def return_relative_name():
        pass

    def sum_ages(self):
        pass


family_names = Family(
    sister="Laime", father="Alfonsas", mother="Rima", brother="Darius"
)

family_members_ages = Family(sister=34, father=67, mother=65, brother=42)


print(
    Family.dictionary_from_two_lists(
        Family.create_list(family_names), Family.create_list(family_members_ages)
    )
)
print(sum(Family.create_list(family_members_ages)))
