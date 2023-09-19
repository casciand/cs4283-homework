from typing import List, Union, Tuple
from dataclasses import dataclass, field
from enum import Enum


class DispenserStatus(Enum):
    OPTIMAL = "OPTIMAL"
    PARTIAL = "PARTIAL"
    BLOCKAGE = "BLOCKAGE"


class LightbulbStatus(Enum):
    GOOD = "GOOD"
    BAD = "BAD"


class SensorStatus(Enum):
    GOOD = "GOOD"
    BAD = "BAD"


class ResponseCode(Enum):
    OK = "OK"t
    BAD_REQUEST = "BAD_REQUEST"


@dataclass
class Contents:
    """ Native representation of the contents of HEALTH message """
    dispenser: DispenserStatus
    icemaker: int  # efficiency percentage, e.g., 90 for 90%
    lightbulb: LightbulbStatus
    fridge_temp: int
    freezer_temp: int
    sensor_status: SensorStatus
    # You can add additional fields here, for example:
    motor_status: str = "RUNNING"  # just an example, can be anything relevant


@dataclass
class HealthMessage:
    """ Native representation for HEALTH message """
    contents: Contents  # Using the 'Contents' dataclass as an attribute
    type: str = "HEALTH"


@dataclass
class ResponseMessage:
    """ Native representation for RESPONSE message """
    code: ResponseCode
    contents: str  # e.g., "Order Placed", "You are Healthy", "Bad Request"
    type: str = "RESPONSE"


# Example Usage:

health_contents = Contents(
    dispenser=DispenserStatus.OPTIMAL,
    icemaker=85,
    lightbulb=LightbulbStatus.GOOD,
    fridge_temp=4,  # 4 degrees Celsius as an example
    freezer_temp=-18,  # -18 degrees Celsius as an example
    sensor_status=SensorStatus.GOOD
)

health_msg = HealthMessage(contents=health_contents)

response_msg = ResponseMessage(
    code=ResponseCode.OK,
    contents="You are Healthy"
)

print(health_msg)
print(response_msg)