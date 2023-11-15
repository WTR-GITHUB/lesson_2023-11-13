# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.


class Employee:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def join_name_and_surname(self) -> str:
        return self.name + " " + self.surname

    def make_email_addres(self) -> str:
        return self.name.lower() + "." + self.surname.lower() + "@codeacademy.lt"


person = Employee(name="Saulius", surname="Anusas")

print(person.join_name_and_surname())
print(person.make_email_addres())
