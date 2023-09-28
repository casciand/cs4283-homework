import schema_pb2 as schema


# DEMO: Serializes and deserializes a message
def main():
    # Define message
    order = schema.Order()
    order.type = 'ORDER'

    order.contents.veggies.tomato = 2.2
    order.contents.veggies.cucumber = 1.8
    order.contents.drinks.cans.coke = 2
    order.contents.drinks.bottles.sprite = 1

    milk = order.contents.milk.add()
    milk.type = order.contents.Milk.WHOLE
    milk.quantity = 3.89
    milk = order.contents.milk.add()
    milk.type = order.contents.Milk.SKIM
    milk.quantity = 2.3

    bread = order.contents.bread.add()
    bread.type = order.contents.Bread.WHEAT
    bread.quantity = 3.89

    meat = order.contents.meat.add()
    meat.type = order.contents.Meat.CHICKEN
    meat.quantity = 3.89

    print("Original message:")
    print(order)

    # Serialize message
    serialized = order.SerializeToString()
    print("\nSerialized message:")
    print(serialized)

    # Deserialize message
    deserialized = schema.Order()
    deserialized.ParseFromString(serialized)
    print("\nDeserialized message:")
    print(deserialized)


if __name__ == '__main__':
    main()
