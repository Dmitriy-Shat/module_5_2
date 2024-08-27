class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    def __str__(self):
        return (f'{self.name}, количество этажей {self.number_of_floors}')

    def __len__(self):
        return self.number_of_floors


Korp1 = House('Волга', 15)
Korp2 = House('Долг', 7)
print(str(Korp1))
print(str(Korp2))
print(len(Korp1))
print(len(Korp2))