import time
from messages import HealthMessage, ResponseMessage, OrderMessage, ResponseCode, Bread, Drinks, Meat, Milk, Veggies, BreadType, MeatType
import serialize as sz


# DEMO: Serializes and deserializes a message
def main():
    # cm = ResponseMessage(ResponseCode.OK, "Order Placed")
    cm = OrderMessage()
    # cm = HealthMessage()

    print("Message contents before serialization:\n")
    cm.dump()

    # Serialize message
    start_time = time.time()
    buf = sz.serialize(cm)
    end_time = time.time()
    print("\nSerialization took {} secs".format(end_time - start_time))

    # Deserialize message
    start_time = time.time()
    cm = sz.deserialize(buf, cm.type)  # Need to pass type in to deserialize
    end_time = time.time()
    print("Deserialization took {} secs\n".format(end_time - start_time))

    print("Message contents after serialization:\n")
    cm.dump()


if __name__ == '__main__':
    main()
