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


class MilkType(Enum):
    WHOLE = "WHOLE"
    SKIM = "SKIM"


class BreadType(Enum):
    WHITE = "WHITE"
    WHEAT = "WHEAT"


class MeatType(Enum):
    CHICKEN = "CHICKEN"
    BEEF = "BEEF"
    PORK = "PORK"


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
    def __init__(self, tomatoes: float, cucumbers: float):
        self.tomatoes = tomatoes
        self.cucumbers = cucumbers


class Cans:
    def __init__(self, coke: int):
        self.coke = coke


class Bottles:
    def __init__(self, sprite: int):
        self.sprite = sprite


class Drinks:
    def __init__(self, cans: Cans, bottles: Bottles):
        self.cans = cans
        self.bottles = bottles


class MilkType(IntEnum):
    OnePercent = 1
    TwoPercent = 2


@dataclass
class Milk:
    mtype: MilkType
    quantity: float


class BreadType(IntEnum):
    Wheat = 1
    White = 2


class Bread:
    type: BreadType
    quantity: float


class MeatType(IntEnum):
    Chicken = 1
    Beef = 2


class Meat:
    type: MeatType
    quantity: float


@dataclass
class OrderMessage:
    @dataclass
    class OrderContents:
        veggies: Veggies
        drinks: Drinks
        milk: List[Milk]
        bread: List[Bread]
        meat: List[Meat]

    contents: OrderContents
    type: str = 'ORDER'

    def __init__(self, contents: 'OrderMessage.OrderContents'):
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

# Example Usage:

# health_contents = HealthContents(
#     dispenser=DispenserStatus.OPTIMAL,
#     icemaker=85,
#     lightbulb=LightbulbStatus.GOOD,
#     fridge_temp=4,  # 4 degrees Celsius as an example
#     freezer_temp=-18,  # -18 degrees Celsius as an example
#     sensor_status=SensorStatus.GOOD
# )
#
# health_msg = HealthMessage(contents=health_contents)
#
# response_msg = ResponseMessage(
#     code=ResponseCode.OK,
#     contents="You are Healthy"
# )
#
# print(health_msg)
# print(response_msg)
