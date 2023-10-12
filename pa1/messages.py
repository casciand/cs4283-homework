from typing import List, Union, Tuple
from dataclasses import dataclass, field
from enum import Enum, IntEnum


class DispenserStatus(Enum):
    OPTIMAL = "OPTIMAL"
    PARTIAL = "PARTIAL"
    BLOCKAGE = "BLOCKAGE"


class GeneralStatus(Enum):
    GOOD = "GOOD"
    BAD = "BAD"


class ResponseCode(Enum):
    OK = "OK"
    BAD_REQUEST = "BAD_REQUEST"


class MilkType(IntEnum):
    WHOLE = 1
    SKIM = 2


class BreadType(IntEnum):
    WHITE = 1
    WHEAT = 2


class MeatType(IntEnum):
    CHICKEN = 1
    BEEF = 2
    PORK = 3


@dataclass
class HealthMessage:
    class HealthContents:
        dispenser: DispenserStatus = DispenserStatus.OPTIMAL.value
        icemaker: int = 97  # efficiency percentage, e.g., 90 for 90%
        lightbulb: GeneralStatus = GeneralStatus.GOOD.value
        fridge_temp: int = 23
        freezer_temp: int = -150
        sensor_status: GeneralStatus = GeneralStatus.BAD.value
        # You can add additional fields here, for example:
        motor_status: str = "RUNNING"  # just an example, can be anything relevant

        def dump(self):
            print("  dispenser: {}".format(self.dispenser))
            print("  icemaker: {}".format(self.icemaker))
            print("  lightbulb: {}".format(self.lightbulb))
            print("  fridge_temp: {}".format(self.fridge_temp))
            print("  freezer_temp: {}".format(self.freezer_temp))
            print("  sensor_status: {}".format(self.sensor_status))
            print("  motor_status: {}".format(self.motor_status))

    """ Native representation for HEALTH message """
    contents: HealthContents  # Using the 'Contents' dataclass as an attribute
    type: str = "HEALTH"

    def __init__(self):
        self.contents = self.HealthContents()

    def dump(self):
        print("Type: {}".format(self.type))
        print("Contents:")
        self.contents.dump()


class Veggies:
    def __init__(self, tomato: float, cucumber: float):
        self.tomato = tomato
        self.cucumber = cucumber

    def __repr__(self):
        return f'\n\ttomatoes: {self.tomato}\n' \
               f'\tcucumbers: {self.cucumber}'


class Cans:
    def __init__(self, coke: int):
        self.coke = coke

    def __repr__(self):
        return f'\n\t\tcoke: {self.coke}'


class Bottles:
    def __init__(self, sprite: int):
        self.sprite = sprite

    def __repr__(self):
        return f'\n\t\tsprite: {self.sprite}'


class Drinks:
    def __init__(self, cans: Cans = Cans(2), bottles: Bottles = Bottles(3)):
        self.cans = cans
        self.bottles = bottles

    def __repr__(self):
        return f'\n\tcans: {self.cans}\n' \
               f'\tbottles: {self.bottles}'


class Milk:
    def __init__(self, type: MilkType = MilkType.WHOLE, quantity: float = 3):
        self.type = type
        self.quantity = quantity

    def __repr__(self):
        return f'({self.type}, {self.quantity})'


class Bread:
    def __init__(self, type: BreadType = BreadType.WHEAT, quantity: float = 3):
        self.type = type
        self.quantity = quantity

    def __repr__(self):
        return f'({self.type}, {self.quantity})'


class Meat:
    def __init__(self, type: MeatType = MeatType.PORK, quantity: float = 3):
        self.type = type
        self.quantity = quantity

    def __repr__(self):
        return f'({self.type}, {self.quantity})'


@dataclass
class OrderMessage:
    @dataclass
    class OrderContents:
        def __init__(self, veggies=Veggies(2, 3), drinks=Drinks(), milk=[Milk()], bread=[Bread()], meat=[Meat()]):
            self.veggies = veggies
            self.drinks = drinks
            self.milk = milk
            self.bread = bread
            self.meat = meat

    contents: OrderContents
    type: str = 'ORDER'

    def __init__(self, contents: OrderContents = OrderContents()):
        self.contents = contents
        self.type = 'ORDER'

    def dump(self):
        print("Dumping contents of Order Message:")
        print(f"  Veggies: {self.contents.veggies}")
        print(f"  Drinks: {self.contents.drinks}")
        print(f"  Milk: {self.contents.milk}")
        print(f"  Bread: {self.contents.bread}")
        print(f"  Meat: {self.contents.meat}")


@dataclass
class ResponseMessage:
    """ Native representation for RESPONSE message """
    code: ResponseCode
    contents: str  # e.g., "Order Placed", "You are Healthy", "Bad Request"
    type: str = "RESPONSE"

    def dump(self):
        print("Type: {}".format(self.type))
        print("Code: {}".format(self.code))
        print("Contents: {}".format(self.contents))
