import flatbuffers
import Messages.HealthMessage
import Messages.HealthContents
import Messages.DispenserStatus
import Messages.GeneralStatus
import Messages.ResponseMessage
import Messages.OrderContents
import Messages.OrderMessage
import Messages.Veggies
import Messages.Drinks
import Messages.Cans
import Messages.Bottles
import Messages.Code
from messages import OrderMessage, HealthMessage, ResponseMessage, GeneralStatus, DispenserStatus, ResponseCode


def serialize_health(msg):
    builder = flatbuffers.Builder(0)

    # Must call builder to build a string
    message_type = builder.CreateString(msg.type)

    # Set lightbulb status
    if msg.contents.lightbulb == GeneralStatus.GOOD:
        lightbulb = Messages.GeneralStatus.GeneralStatus().GOOD
    else:
        lightbulb = Messages.GeneralStatus.GeneralStatus().BAD

    # Set dispenser status
    if msg.contents.dispenser == DispenserStatus.OPTIMAL:
        dispenser = Messages.DispenserStatus.DispenserStatus().OPTIMAL
    elif msg.contents.dispenser == DispenserStatus.PARTIAL:
        dispenser = Messages.DispenserStatus.DispenserStatus().PARTIAL
    else:
        dispenser = Messages.DispenserStatus.DispenserStatus().BLOCKAGE

    # Set sensor status
    if msg.contents.sensor_status == GeneralStatus.GOOD:
        sensor_status = Messages.GeneralStatus.GeneralStatus().GOOD
    else:
        sensor_status = Messages.GeneralStatus.GeneralStatus().BAD

    # Build HealthContents
    Messages.HealthContents.HealthContentsStart(builder)
    Messages.HealthContents.HealthContentsAddDispenser(builder, dispenser)
    Messages.HealthContents.AddIcemaker(builder, msg.contents.icemaker)
    Messages.HealthContents.AddLightbulb(builder, lightbulb)
    Messages.HealthContents.AddFridgeTemp(builder, msg.contents.fridge_temp)
    Messages.HealthContents.AddFreezerTemp(builder, msg.contents.freezer_temp)
    Messages.HealthContents.AddSensorStatus(builder, sensor_status)
    contents = Messages.HealthContents.HealthContentsEnd(builder)

    # Build HealthMessage
    Messages.HealthMessage.Start(builder)
    Messages.HealthMessage.AddType(builder, message_type)
    Messages.HealthMessage.AddContents(builder, contents)
    serialized_msg = Messages.HealthMessage.End(builder)

    # End the serialization process
    builder.Finish(serialized_msg)

    # Get the serialized buffer
    return builder.Output()


def serialize_order(msg):
    builder = flatbuffers.Builder(0)

    # Must call builder to build a string
    message_type = builder.CreateString(msg.type)

    veggies = Messages.Veggies.CreateVeggies(builder, msg.contents.veggies.tomatoes, msg.contents.veggies.cucumbers)
    cans = Messages.Cans.CreateCans(builder, msg.contents.drinks.cans)
    bottles = Messages.Bottles.CreateBottles(builder, msg.contents.drinks.bottles)

    Messages.Drinks.DrinksStart(builder)
    Messages.Drinks.AddCans(builder, cans)
    Messages.Drinks.AddBottles(builder, bottles)
    drinks = Messages.Drinks.DrinksEnd(builder)

    # Build OrderContents
    Messages.OrderContents.OrderContentsStart(builder)
    Messages.OrderContents.OrderContentsAddVeggies(builder, veggies)
    Messages.OrderContents.OrderContentsAddDrinks(builder, drinks)
    Messages.OrderContents.OrderContentsAddMilk(builder, msg.contents.milk)
    Messages.OrderContents.OrderContentsAddBread(builder, msg.contents.bread)
    Messages.OrderContents.OrderContentsAddMeat(builder, msg.contents.meat)
    contents = Messages.OrderContents.OrderContentsEnd(builder)

    # Build OrderMessage
    Messages.OrderMessage.Start(builder)
    Messages.OrderMessage.AddType(builder, message_type)
    Messages.OrderMessage.AddContents(builder, contents)
    serialized_msg = Messages.OrderMessage.End(builder)

    # End the serialization process
    builder.Finish(serialized_msg)

    # Get the serialized buffer
    return builder.Output()


def serialize_response(msg):
    builder = flatbuffers.Builder(0)

    # Must call builder to build a string
    message_type = builder.CreateString(msg.type)
    response = builder.CreateString(msg.contents)

    if msg.code == ResponseCode.OK:
        code = Messages.Code.Code().OK
    else:
        code = Messages.Code.Code().BAD_REQUEST

    # Build ResponseMessage
    Messages.ResponseMessage.Start(builder)
    Messages.ResponseMessage.AddType(builder, message_type)
    Messages.ResponseMessage.AddCode(builder, code)
    Messages.ResponseMessage.AddContents(builder, response)
    serialized_msg = Messages.HealthMessage.End(builder)

    # End the serialization process
    builder.Finish(serialized_msg)

    # Get the serialized buffer
    return builder.Output()


def serialize(msg):
    # Serialize based on message type
    if msg.type == 'ORDER':
        return serialize_order(msg)
    elif msg.type == 'HEALTH':
        return serialize_health(msg)
    elif msg.type == 'RESPONSE':
        return serialize_response(msg)
    else:
        raise Exception('error: unknown message type')


# Serialize message to iterable frame objects needed by zmq
def serialize_to_frames(cm):
    """ serialize into an interable format """
    # We had to do it this way because the send_serialized method of zmq under the hood
    # relies on send_multipart, which needs a list or sequence of frames. The easiest way
    # to get an iterable out of the serialized buffer is to enclose it inside []
    print("Serialize message to iterable list")
    return [serialize(cm)]


def deserialize_health(buf):
    message_packet = Messages.HealthMessage.HealthMessage.GetRootAs(buf, 0)
    contents_packet = message_packet.Contents()

    message = HealthMessage()
    message.contents.dispenser = contents_packet.Dispenser()
    message.contents.icemaker = contents_packet.Icemaker()
    message.contents.lightbulb = contents_packet.Lightbulb()
    message.contents.fridge_temp = contents_packet.FridgeTemp()
    message.contents.freezer_temp = contents_packet.FreezerTemp()
    message.contents.sensor_status = contents_packet.SensorStatus()

    return message


def deserialize_response(buf):
    message_packet = Messages.ResponseMessage.ResponseMessage.GetRootAs(buf, 0)
    return ResponseMessage(message_packet.Code(), message_packet.Contents())


# deserialize the incoming serialized structure into native data type
def deserialize(buf, message_type):
    if message_type == 'ORDER':
        pass  # return deserialize_order(buf)
    elif message_type == 'HEALTH':
        return deserialize_health(buf)
    elif message_type == 'RESPONSE':
        return deserialize_response(buf)
    else:
        raise Exception('error: unknown message type')


# deserialize from frames
def deserialize_from_frames(recvd_seq, message_type):
    """ This is invoked on list of frames by zmq """

    # For this sample code, since we send only one frame, hopefully what
    # comes out is also a single frame. If not some additional complexity will
    # need to be added.
    assert (len(recvd_seq) == 1)
    # print ("type of each elem of received seq is {}".format (type (recvd_seq[i])))
    print("received data over the wire = {}".format(recvd_seq[0]))
    cm = deserialize(recvd_seq[0], message_type)  # hand it to our deserialize method

    # assuming only one frame in the received sequence, we just send this deserialized
    # custom message
    return cm
