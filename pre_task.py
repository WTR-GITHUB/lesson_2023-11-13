# kdhflkjashlgfashdlfkjahlskjfgaklsjdhfgaskljh ;lakdshfvklashlofg has;lassldkfhlask hfl alkjsdjsdfh;lksaejfl sadlkjdfjlsk jfasl;dkdfh llkad;lkfj  lalksjflkasdjfl ;als;kdsdjfllk sajdflaksj gl


class Car:
    def __init__(self, model: str, made_date: int, engine_cap: float) -> None:
        self.model = model
        self.date = made_date
        self.cap = engine_cap

    def get_cars_name(self) -> str:
        return self.model


sister = Car(name="Laime", sister_age=34)

print(Car.get_cars_name())
