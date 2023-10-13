from dataclasses import dataclass
from enum import Enum, IntEnum


class DispenserStatus(IntEnum):
    OPTIMAL = 1
    PARTIAL = 2
    BLOCKAGE = 3


class GeneralStatus(IntEnum):
    GOOD = 1
    BAD = 2


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
        dispenser: DispenserStatus = DispenserStatus.OPTIMAL
        icemaker: int = 97  # efficiency percentage, e.g., 90 for 90%
        lightbulb: GeneralStatus = GeneralStatus.GOOD
        fridge_temp: int = 23
        freezer_temp: int = -150
        sensor_status: GeneralStatus = GeneralStatus.BAD
        # You can add additional fields here, for example:
        motor_status: str = "RUNNING"  # just an example, can be anything relevant

        def __repr__(self):
            return f'  dispenser: {self.dispenser.name}\n' \
                   f'  icemaker: {self.icemaker}\n' \
                   f'  lightbulb: {self.lightbulb.name}\n' \
                   f'  fridge_temp: {self.fridge_temp}\n' \
                   f'  freezer_temp: {self.freezer_temp}\n' \
                   f'  sensor_status: {self.sensor_status.name}\n' \
                   f'  motor_status: {self.motor_status}'

    """ Native representation for HEALTH message """
    contents: HealthContents  # Using the 'Contents' dataclass as an attribute
    type: str = "HEALTH"

    def __init__(self):
        self.contents = self.HealthContents()

    def __repr__(self):
        return f'Type: {self.type}\n' \
               f'Contents:\n' \
               f'{self.contents}'


class Veggies:
    def __init__(self, tomato: float, cucumber: float):
        self.tomato = tomato
        self.cucumber = cucumber

    def __repr__(self):
        return f'    tomato: {self.tomato}\n' \
               f'    cucumber: {self.cucumber}'


class Cans:
    def __init__(self, coke: int):
        self.coke = coke

    def __repr__(self):
        return f'      coke: {self.coke}'


class Bottles:
    def __init__(self, sprite: int):
        self.sprite = sprite

    def __repr__(self):
        return f'      sprite: {self.sprite}'


class Drinks:
    def __init__(self, cans: Cans = Cans(2), bottles: Bottles = Bottles(3)):
        self.cans = cans
        self.bottles = bottles

    def __repr__(self):
        return f'    cans:\n{self.cans}\n' \
               f'    bottles:\n{self.bottles}'


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

    def __str__(self):
        return f'Type: {self.type}\n' \
               f'Contents:\n' \
               f'  Veggies:\n{self.contents.veggies}\n' \
               f'  Drinks:\n{self.contents.drinks}\n' \
               f'  Milk: {self.contents.milk}\n' \
               f'  Bread: {self.contents.bread}\n' \
               f'  Meat: {self.contents.meat}'


@dataclass
class ResponseMessage:
    """ Native representation for RESPONSE message """
    code: ResponseCode
    contents: str  # e.g., "Order Placed", "You are Healthy", "Bad Request"
    type: str = "RESPONSE"

    def __str__(self):
        return f'Type: {self.type}\n' \
               f'Code: {self.code}\n' \
               f'Contents: {self.contents}'
