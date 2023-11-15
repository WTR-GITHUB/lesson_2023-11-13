class Country:
    def __init__(self, country: str, area: int, population: int) -> None:
        self.country = country
        self.area = area
        self.population = population

    def is_big(self) -> bool:
        if self.area > 20000000 or self.population > 3000000:
            return True
        else:
            return False

    def compare_pd(self, other_country: "Country") -> str:
        if self.population / self.area > other_country.population / other_country.area:
            return f"{self.country} has a bigger population density than {other_country.country}"
        else:
            return f"{self.country} has a smaller population density than {other_country.country}"


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big())
print(andorra.is_big())
print(andorra.compare_pd(australia))
print(australia.compare_pd(andorra))
