# 1) Опишіть клас Вагон
# 2) Вагон повинен містити список пасажирів і дозволяти додавати пасажирів
# 3) У Вагоні може бути не більше 10 пасажирів
# 4) Під час використання функції len у вагоні я хочу бачити кількість пасажирів
# 5) Кожен вагон повинен мати номер
# 6) Опишіть об’єкт «Поїзд»
# 7) Клас повинен містити поля та метод для додавання вагонів(необхідно додати об’єкти та екземпляри класу вагонів)
# 8) В поїзді завжди є 1 вагон і це локомотив(він не приймає пасажирів)
# 9) Використовуючи len у поїзді, я хочу бачити кількість вагонів без локомотива

class Wagon:
    def __init__(self, number, passengers=None, is_locomotive=False):
        self.number = number
        self.passengers = passengers if passengers is not None else []
        self.is_locomotive = is_locomotive

    def add_passenger(self, passenger):
        if not self.is_locomotive:
            if (len(self.passengers) < 10):
                self.passengers.append(passenger)
            else:
                print("Cannot add more passengers. The wagon is full.")
        else:
            print("Locomotives cannot carry passengers.")

    def __len__(self):
        return len(self.passengers)

class Train:
    def __init__(self, locomotive):
        self.locomotive = locomotive
        self.wagons = [locomotive]

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    def __len__(self):
        return sum(1 for wagon in self.wagons if not wagon.is_locomotive)

locomotive1 = Wagon(0, is_locomotive=True)
locomotive2 = Wagon(100, is_locomotive=True)
locomotive3 = Wagon(200, is_locomotive=True)

wagon1 = Wagon(1)
wagon2 = Wagon(2)

passengers = [
    "Dmytro",
    "Denys",
    "Anna",
    "Alex",
    "Maria",
    "John",
    "Kate",
    "Mike",
    "Olga",
    "David",
    "Emma",
    "Robert",
    "Sophia",
]

for passenger in passengers:
    wagon1.add_passenger(passenger)

wagon2.add_passenger("Tom")
wagon2.add_passenger("Jack")

train = Train(locomotive1)

train.add_wagon(wagon1)
train.add_wagon(locomotive2)
train.add_wagon(wagon2)
train.add_wagon(locomotive3)

print(
    f"\nTrain information:\n"
    f"  Total objects in train: {len(train.wagons)}\n"
    f"  Passenger wagons: {len(train)}\n"
)

for wagon in train.wagons:
    if wagon.is_locomotive:
        print(
            f"Locomotive {wagon.number}:\n"
            f"  Type: Locomotive\n"
            f"  Passengers: {len(wagon)}\n"
            f"  Can carry passengers: No\n"
        )
    else:
        print(
            f"Wagon {wagon.number}:\n"
            f"  Type: Passenger wagon\n"
            f"  Passengers: {len(wagon)}\n"
            f"  Passenger list: {wagon.passengers}\n"
            f"  Can carry passengers: Yes\n"
        )
