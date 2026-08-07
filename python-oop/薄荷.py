class Mint:
    present_year = 2025
    def __init__(self):
        self.update()
    def create(self, coin):
        return coin(self.year)
    def update(self) -> None:
        self.year = Mint.present_year


class Coin:
    cents = None
    def __init__(self, year: int):
        self.year = year
    def worth(self) -> int:
        age = Mint.present_year - self.year
        bonus = max(0, age - 50)
        return self.cents + bonus

class Nickel(Coin):
    cents = 5
class Dime(Coin):
    cents = 10