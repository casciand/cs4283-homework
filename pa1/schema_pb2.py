# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cschema.proto\x12\x08messages\"\xc2\x02\n\rHealthMessage\x12\x31\n\tdispenser\x18\x01 \x01(\x0e\x32\x19.messages.DispenserStatusH\x00\x88\x01\x01\x12\x15\n\x08icemaker\x18\x02 \x01(\rH\x01\x88\x01\x01\x12(\n\tlightbulb\x18\x03 \x01(\x0e\x32\x10.messages.StatusH\x02\x88\x01\x01\x12\x18\n\x0b\x66ridge_temp\x18\x04 \x01(\rH\x03\x88\x01\x01\x12\x19\n\x0c\x66reezer_temp\x18\x05 \x01(\rH\x04\x88\x01\x01\x12,\n\rsensor_status\x18\x06 \x01(\x0e\x32\x10.messages.StatusH\x05\x88\x01\x01\x42\x0c\n\n_dispenserB\x0b\n\t_icemakerB\x0c\n\n_lightbulbB\x0e\n\x0c_fridge_tempB\x0f\n\r_freezer_tempB\x10\n\x0e_sensor_status\"\x90\x08\n\rOrderContents\x12\x35\n\x07veggies\x18\x01 \x01(\x0b\x32\x1f.messages.OrderContents.VeggiesH\x00\x88\x01\x01\x12\x33\n\x06\x64rinks\x18\x02 \x01(\x0b\x32\x1e.messages.OrderContents.DrinksH\x01\x88\x01\x01\x12*\n\x04milk\x18\x03 \x03(\x0b\x32\x1c.messages.OrderContents.Milk\x12,\n\x05\x62read\x18\x04 \x03(\x0b\x32\x1d.messages.OrderContents.Bread\x12*\n\x04meat\x18\x05 \x03(\x0b\x32\x1c.messages.OrderContents.Meat\x1aM\n\x07Veggies\x12\x13\n\x06tomato\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x15\n\x08\x63ucumber\x18\x02 \x01(\x02H\x01\x88\x01\x01\x42\t\n\x07_tomatoB\x0b\n\t_cucumber\x1a\xe2\x01\n\x06\x44rinks\x12\x36\n\x04\x63\x61ns\x18\x01 \x01(\x0b\x32#.messages.OrderContents.Drinks.CansH\x00\x88\x01\x01\x12<\n\x07\x62ottles\x18\x02 \x01(\x0b\x32&.messages.OrderContents.Drinks.BottlesH\x01\x88\x01\x01\x1a\"\n\x04\x43\x61ns\x12\x11\n\x04\x63oke\x18\x01 \x01(\x05H\x00\x88\x01\x01\x42\x07\n\x05_coke\x1a)\n\x07\x42ottles\x12\x13\n\x06sprite\x18\x01 \x01(\x05H\x00\x88\x01\x01\x42\t\n\x07_spriteB\x07\n\x05_cansB\n\n\x08_bottles\x1a\x8e\x01\n\x04Milk\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32%.messages.OrderContents.Milk.MilkTypeH\x00\x88\x01\x01\x12\x15\n\x08quantity\x18\x02 \x01(\x02H\x01\x88\x01\x01\"\x1f\n\x08MilkType\x12\t\n\x05WHOLE\x10\x00\x12\x08\n\x04SKIM\x10\x01\x42\x07\n\x05_typeB\x0b\n\t_quantity\x1a\x93\x01\n\x05\x42read\x12:\n\x04type\x18\x01 \x01(\x0e\x32\'.messages.OrderContents.Bread.BreadTypeH\x00\x88\x01\x01\x12\x15\n\x08quantity\x18\x02 \x01(\x02H\x01\x88\x01\x01\"!\n\tBreadType\x12\t\n\x05WHITE\x10\x00\x12\t\n\x05WHEAT\x10\x01\x42\x07\n\x05_typeB\x0b\n\t_quantity\x1a\x9a\x01\n\x04Meat\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32%.messages.OrderContents.Meat.MeatTypeH\x00\x88\x01\x01\x12\x15\n\x08quantity\x18\x02 \x01(\x02H\x01\x88\x01\x01\"+\n\x08MeatType\x12\x08\n\x04\x42\x45\x45\x46\x10\x00\x12\x0b\n\x07\x43HICKEN\x10\x01\x12\x08\n\x04PORK\x10\x02\x42\x07\n\x05_typeB\x0b\n\t_quantityB\n\n\x08_veggiesB\t\n\x07_drinks\"`\n\x05Order\x12\x11\n\x04type\x18\x01 \x01(\tH\x00\x88\x01\x01\x12.\n\x08\x63ontents\x18\x02 \x01(\x0b\x32\x17.messages.OrderContentsH\x01\x88\x01\x01\x42\x07\n\x05_typeB\x0b\n\t_contents\"d\n\x08Response\x12+\n\x04\x63ode\x18\x07 \x01(\x0e\x32\x18.messages.ResponseStatusH\x00\x88\x01\x01\x12\x15\n\x08\x63ontents\x18\x08 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_codeB\x0b\n\t_contents*9\n\x0f\x44ispenserStatus\x12\x0b\n\x07OPTIMAL\x10\x00\x12\x0b\n\x07PARTIAL\x10\x01\x12\x0c\n\x08\x42LOCKAGE\x10\x02*\x1b\n\x06Status\x12\x08\n\x04GOOD\x10\x00\x12\x07\n\x03\x42\x41\x44\x10\x01*)\n\x0eResponseStatus\x12\x06\n\x02OK\x10\x00\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x01\x32?\n\x0cOrderService\x12/\n\x06method\x12\x0f.messages.Order\x1a\x12.messages.Response\"\x00\x32H\n\rHealthService\x12\x37\n\x06method\x12\x17.messages.HealthMessage\x1a\x12.messages.Response\"\x00\x62\x06proto3')

_DISPENSERSTATUS = DESCRIPTOR.enum_types_by_name['DispenserStatus']
DispenserStatus = enum_type_wrapper.EnumTypeWrapper(_DISPENSERSTATUS)
_STATUS = DESCRIPTOR.enum_types_by_name['Status']
Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_RESPONSESTATUS = DESCRIPTOR.enum_types_by_name['ResponseStatus']
ResponseStatus = enum_type_wrapper.EnumTypeWrapper(_RESPONSESTATUS)
OPTIMAL = 0
PARTIAL = 1
BLOCKAGE = 2
GOOD = 0
BAD = 1
OK = 0
BAD_REQUEST = 1


_HEALTHMESSAGE = DESCRIPTOR.message_types_by_name['HealthMessage']
_ORDERCONTENTS = DESCRIPTOR.message_types_by_name['OrderContents']
_ORDERCONTENTS_VEGGIES = _ORDERCONTENTS.nested_types_by_name['Veggies']
_ORDERCONTENTS_DRINKS = _ORDERCONTENTS.nested_types_by_name['Drinks']
_ORDERCONTENTS_DRINKS_CANS = _ORDERCONTENTS_DRINKS.nested_types_by_name['Cans']
_ORDERCONTENTS_DRINKS_BOTTLES = _ORDERCONTENTS_DRINKS.nested_types_by_name['Bottles']
_ORDERCONTENTS_MILK = _ORDERCONTENTS.nested_types_by_name['Milk']
_ORDERCONTENTS_BREAD = _ORDERCONTENTS.nested_types_by_name['Bread']
_ORDERCONTENTS_MEAT = _ORDERCONTENTS.nested_types_by_name['Meat']
_ORDER = DESCRIPTOR.message_types_by_name['Order']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
_ORDERCONTENTS_MILK_MILKTYPE = _ORDERCONTENTS_MILK.enum_types_by_name['MilkType']
_ORDERCONTENTS_BREAD_BREADTYPE = _ORDERCONTENTS_BREAD.enum_types_by_name['BreadType']
_ORDERCONTENTS_MEAT_MEATTYPE = _ORDERCONTENTS_MEAT.enum_types_by_name['MeatType']
HealthMessage = _reflection.GeneratedProtocolMessageType('HealthMessage', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHMESSAGE,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:messages.HealthMessage)
  })
_sym_db.RegisterMessage(HealthMessage)

OrderContents = _reflection.GeneratedProtocolMessageType('OrderContents', (_message.Message,), {

  'Veggies' : _reflection.GeneratedProtocolMessageType('Veggies', (_message.Message,), {
    'DESCRIPTOR' : _ORDERCONTENTS_VEGGIES,
    '__module__' : 'schema_pb2'
    # @@protoc_insertion_point(class_scope:messages.OrderContents.Veggies)
    })
  ,

  'Drinks' : _reflection.GeneratedProtocolMessageType('Drinks', (_message.Message,), {

    'Cans' : _reflection.GeneratedProtocolMessageType('Cans', (_message.Message,), {
      'DESCRIPTOR' : _ORDERCONTENTS_DRINKS_CANS,
      '__module__' : 'schema_pb2'
      # @@protoc_insertion_point(class_scope:messages.OrderContents.Drinks.Cans)
      })
    ,

    'Bottles' : _reflection.GeneratedProtocolMessageType('Bottles', (_message.Message,), {
      'DESCRIPTOR' : _ORDERCONTENTS_DRINKS_BOTTLES,
      '__module__' : 'schema_pb2'
      # @@protoc_insertion_point(class_scope:messages.OrderContents.Drinks.Bottles)
      })
    ,
    'DESCRIPTOR' : _ORDERCONTENTS_DRINKS,
    '__module__' : 'schema_pb2'
    # @@protoc_insertion_point(class_scope:messages.OrderContents.Drinks)
    })
  ,

  'Milk' : _reflection.GeneratedProtocolMessageType('Milk', (_message.Message,), {
    'DESCRIPTOR' : _ORDERCONTENTS_MILK,
    '__module__' : 'schema_pb2'
    # @@protoc_insertion_point(class_scope:messages.OrderContents.Milk)
    })
  ,

  'Bread' : _reflection.GeneratedProtocolMessageType('Bread', (_message.Message,), {
    'DESCRIPTOR' : _ORDERCONTENTS_BREAD,
    '__module__' : 'schema_pb2'
    # @@protoc_insertion_point(class_scope:messages.OrderContents.Bread)
    })
  ,

  'Meat' : _reflection.GeneratedProtocolMessageType('Meat', (_message.Message,), {
    'DESCRIPTOR' : _ORDERCONTENTS_MEAT,
    '__module__' : 'schema_pb2'
    # @@protoc_insertion_point(class_scope:messages.OrderContents.Meat)
    })
  ,
  'DESCRIPTOR' : _ORDERCONTENTS,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:messages.OrderContents)
  })
_sym_db.RegisterMessage(OrderContents)
_sym_db.RegisterMessage(OrderContents.Veggies)
_sym_db.RegisterMessage(OrderContents.Drinks)
_sym_db.RegisterMessage(OrderContents.Drinks.Cans)
_sym_db.RegisterMessage(OrderContents.Drinks.Bottles)
_sym_db.RegisterMessage(OrderContents.Milk)
_sym_db.RegisterMessage(OrderContents.Bread)
_sym_db.RegisterMessage(OrderContents.Meat)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:messages.Order)
  })
_sym_db.RegisterMessage(Order)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:messages.Response)
  })
_sym_db.RegisterMessage(Response)

_ORDERSERVICE = DESCRIPTOR.services_by_name['OrderService']
_HEALTHSERVICE = DESCRIPTOR.services_by_name['HealthService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DISPENSERSTATUS._serialized_start=1594
  _DISPENSERSTATUS._serialized_end=1651
  _STATUS._serialized_start=1653
  _STATUS._serialized_end=1680
  _RESPONSESTATUS._serialized_start=1682
  _RESPONSESTATUS._serialized_end=1723
  _HEALTHMESSAGE._serialized_start=27
  _HEALTHMESSAGE._serialized_end=349
  _ORDERCONTENTS._serialized_start=352
  _ORDERCONTENTS._serialized_end=1392
  _ORDERCONTENTS_VEGGIES._serialized_start=611
  _ORDERCONTENTS_VEGGIES._serialized_end=688
  _ORDERCONTENTS_DRINKS._serialized_start=691
  _ORDERCONTENTS_DRINKS._serialized_end=917
  _ORDERCONTENTS_DRINKS_CANS._serialized_start=819
  _ORDERCONTENTS_DRINKS_CANS._serialized_end=853
  _ORDERCONTENTS_DRINKS_BOTTLES._serialized_start=855
  _ORDERCONTENTS_DRINKS_BOTTLES._serialized_end=896
  _ORDERCONTENTS_MILK._serialized_start=920
  _ORDERCONTENTS_MILK._serialized_end=1062
  _ORDERCONTENTS_MILK_MILKTYPE._serialized_start=1009
  _ORDERCONTENTS_MILK_MILKTYPE._serialized_end=1040
  _ORDERCONTENTS_BREAD._serialized_start=1065
  _ORDERCONTENTS_BREAD._serialized_end=1212
  _ORDERCONTENTS_BREAD_BREADTYPE._serialized_start=1157
  _ORDERCONTENTS_BREAD_BREADTYPE._serialized_end=1190
  _ORDERCONTENTS_MEAT._serialized_start=1215
  _ORDERCONTENTS_MEAT._serialized_end=1369
  _ORDERCONTENTS_MEAT_MEATTYPE._serialized_start=1304
  _ORDERCONTENTS_MEAT_MEATTYPE._serialized_end=1347
  _ORDER._serialized_start=1394
  _ORDER._serialized_end=1490
  _RESPONSE._serialized_start=1492
  _RESPONSE._serialized_end=1592
  _ORDERSERVICE._serialized_start=1725
  _ORDERSERVICE._serialized_end=1788
  _HEALTHSERVICE._serialized_start=1790
  _HEALTHSERVICE._serialized_end=1862
# @@protoc_insertion_point(module_scope)
