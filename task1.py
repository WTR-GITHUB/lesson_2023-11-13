from typing import Union


class Family:
    def __init__(
        self,
        sister_name: str,
        father_name: str,
        mother_name: str,
        brother_name: str,
        sister_age: int,
        father_age: int,
        mother_age: int,
        brother_age: int,
    ) -> None:
        self.sister_name = sister_name
        self.father_name = father_name
        self.mother_name = mother_name
        self.brother_name = brother_name
        self.sister_age = sister_age
        self.father_age = father_age
        self.mother_age = mother_age
        self.brother_age = brother_age

    def family_data(self) -> dict:
        try:
            family_dictionary = {
                self.sister_name: self.sister_age,
                self.father_name: self.father_age,
                self.mother_name: self.mother_age,
                self.brother_name: self.brother_age,
            }
            return family_dictionary
        except Exception as err:
            print(err)

    def sum_family_members_ages(self) -> int:
        return self.sister_age + self.brother_age + self.mother_age + self.father_age

    def sort_family_data_by_age(self) -> list:
        return sorted(self.family_data().items(), key=lambda age: age[1])


family_data = Family(
    sister_name="Laime",
    father_name="Alfonsas",
    mother_name="Rima",
    brother_name="Darius",
    sister_age=34,
    father_age=67,
    mother_age=65,
    brother_age=42,
)

print(family_data.family_data())
print(family_data.sister_name)
print(family_data.brother_name)
print(family_data.mother_name)
print(family_data.father_name)
print(family_data.sum_family_members_ages())
print(family_data.sort_family_data_by_age())
