# class Calculator:
#     def __init__(self) -> None:
#         print("Testas")
    
#     def add_two_numbers(self, numb_a:int, numb_b: int) -> int:
#         return numb_a + numb_b
    
#     def divide_two_numbers(self, numb_a:int, numb_b: int) -> int:
#         return numb_a / numb_b

#     def multiply_two_numbers(self, numb_a:int, numb_b: int) -> int:
#         return numb_a * numb_b

#     def substract_two_numbers(self, numb_a:int, numb_b: int) -> int:
#         return numb_a - numb_b



# calc = Calculator()
# calc_2 = Calculator()

# print(calc =)

# print(calc.add_two_numbers(5, 2))
# print(calc.divide_two_numbers())

class People:
    def __init__(self, name: str, surname: str) -> None:
        self.n = name
        self.surname = surname

    def get_name_and_surname(self) -> str:
        return self.n + " " + self.surname

if __name__ == "__main__":
        
    person = People(name="Saulius", surname="Anusas")

    print(person.n)
    print(person.get_name_and_surname())

