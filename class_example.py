import logging
from typing import Union

logging.basicConfig(
    level=logging.DEBUG,
    filename="error.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class Calculator:

    def add_two_numbers(self, numb_a: Union[float, int], numb_b: Union[float, int]) -> Union[float, int]:
        return numb_a + numb_b

    def divide_two_numbers(self, numb_a: Union[float, int], numb_b: Union[float, int]) -> Union[float, int]:
        try:
            return numb_a / numb_b
        except ZeroDivisionError as err:
            print(err)

    def multiply_two_numbers(self, numb_a: Union[float, int], numb_b: Union[float, int]) -> Union[float, int]:
        return numb_a * numb_b

    def substract_two_numbers(self, numb_a: Union[float, int], numb_b: Union[float, int]) -> Union[float, int]:
        return numb_a - numb_b


calc = Calculator()

print(calc.add_two_numbers(5, 2))
print(calc.divide_two_numbers(5, 1))
print(calc.multiply_two_numbers(5, 5))
print(calc.substract_two_numbers(7, 9))

# class People:
#     def __init__(self, name: str, surname: str) -> None:
#         self.n = name
#         self.surname = surname

#     def get_name_and_surname(self) -> str:
#         return self.n + " " + self.surname

# if __name__ == "__main__":

#     person = People(name="Saulius", surname="Anusas")

#     print(person.n)
#     print(person.get_name_and_surname())
