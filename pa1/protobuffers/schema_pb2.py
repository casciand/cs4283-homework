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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cschema.proto\x12\x08messages\"\x88\x04\n\x0eHealthContents\x12@\n\tdispenser\x18\x01 \x01(\x0e\x32(.messages.HealthContents.DispenserStatusH\x00\x88\x01\x01\x12\x15\n\x08icemaker\x18\x02 \x01(\rH\x01\x88\x01\x01\x12(\n\tlightbulb\x18\x03 \x01(\x0e\x32\x10.messages.StatusH\x02\x88\x01\x01\x12\x18\n\x0b\x66ridge_temp\x18\x04 \x01(\rH\x03\x88\x01\x01\x12\x19\n\x0c\x66reezer_temp\x18\x05 \x01(\rH\x04\x88\x01\x01\x12,\n\rsensor_status\x18\x06 \x01(\x0e\x32\x10.messages.StatusH\x05\x88\x01\x01\x12?\n\x0cmotor_status\x18\x07 \x01(\x0e\x32$.messages.HealthContents.MotorStatusH\x06\x88\x01\x01\"9\n\x0f\x44ispenserStatus\x12\x0b\n\x07OPTIMAL\x10\x00\x12\x0b\n\x07PARTIAL\x10\x01\x12\x0c\n\x08\x42LOCKAGE\x10\x02\"\'\n\x0bMotorStatus\x12\x0b\n\x07RUNNING\x10\x00\x12\x0b\n\x07STOPPED\x10\x01\x42\x0c\n\n_dispenserB\x0b\n\t_icemakerB\x0c\n\n_lightbulbB\x0e\n\x0c_fridge_tempB\x0f\n\r_freezer_tempB\x10\n\x0e_sensor_statusB\x0f\n\r_motor_status\"\xf7\t\n\rOrderContents\x12\x35\n\x07veggies\x18\x01 \x01(\x0b\x32\x1f.messages.OrderContents.VeggiesH\x00\x88\x01\x01\x12\x33\n\x06\x64rinks\x18\x02 \x01(\x0b\x32\x1e.messages.OrderContents.DrinksH\x01\x88\x01\x01\x12*\n\x04milk\x18\x03 \x03(\x0b\x32\x1c.messages.OrderContents.Milk\x12,\n\x05\x62read\x18\x04 \x03(\x0b\x32\x1d.messages.OrderContents.Bread\x12*\n\x04meat\x18\x05 \x03(\x0b\x32\x1c.messages.OrderContents.Meat\x1a\xb7\x01\n\x07Veggies\x12\x13\n\x06tomato\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x15\n\x08\x63ucumber\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x13\n\x06\x63\x61rrot\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x15\n\x08\x62roccoli\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12\x16\n\tasparagus\x18\x05 \x01(\x02H\x04\x88\x01\x01\x42\t\n\x07_tomatoB\x0b\n\t_cucumberB\t\n\x07_carrotB\x0b\n\t_broccoliB\x0c\n\n_asparagus\x1a\xde\x02\n\x06\x44rinks\x12\x36\n\x04\x63\x61ns\x18\x01 \x01(\x0b\x32#.messages.OrderContents.Drinks.CansH\x00\x88\x01\x01\x12<\n\x07\x62ottles\x18\x02 \x01(\x0b\x32&.messages.OrderContents.Drinks.BottlesH\x01\x88\x01\x01\x1a\\\n\x04\x43\x61ns\x12\x11\n\x04\x63oke\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\x04\x62\x65\x65r\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x12\n\x05\x66\x61nta\x18\x03 \x01(\x05H\x02\x88\x01\x01\x42\x07\n\x05_cokeB\x07\n\x05_beerB\x08\n\x06_fanta\x1ak\n\x07\x42ottles\x12\x13\n\x06sprite\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\tgingerale\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x11\n\x04wine\x18\x03 \x01(\x05H\x02\x88\x01\x01\x42\t\n\x07_spriteB\x0c\n\n_gingeraleB\x07\n\x05_wineB\x07\n\x05_cansB\n\n\x08_bottles\x1a\x8e\x01\n\x04Milk\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32%.messages.OrderContents.Milk.MilkTypeH\x00\x88\x01\x01\x12\x15\n\x08quantity\x18\x02 \x01(\x02H\x01\x88\x01\x01\"\x1f\n\x08MilkType\x12\t\n\x05WHOLE\x10\x00\x12\x08\n\x04SKIM\x10\x01\x42\x07\n\x05_typeB\x0b\n\t_quantity\x1a\x93\x01\n\x05\x42read\x12:\n\x04type\x18\x01 \x01(\x0e\x32\'.messages.OrderContents.Bread.BreadTypeH\x00\x88\x01\x01\x12\x15\n\x08quantity\x18\x02 \x01(\x02H\x01\x88\x01\x01\"!\n\tBreadType\x12\t\n\x05WHITE\x10\x00\x12\t\n\x05WHEAT\x10\x01\x42\x07\n\x05_typeB\x0b\n\t_quantity\x1a\x9a\x01\n\x04Meat\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32%.messages.OrderContents.Meat.MeatTypeH\x00\x88\x01\x01\x12\x15\n\x08quantity\x18\x02 \x01(\x02H\x01\x88\x01\x01\"+\n\x08MeatType\x12\x08\n\x04\x42\x45\x45\x46\x10\x00\x12\x0b\n\x07\x43HICKEN\x10\x01\x12\x08\n\x04PORK\x10\x02\x42\x07\n\x05_typeB\x0b\n\t_quantityB\n\n\x08_veggiesB\t\n\x07_drinks\"`\n\x05Order\x12\x11\n\x04type\x18\x01 \x01(\tH\x00\x88\x01\x01\x12.\n\x08\x63ontents\x18\x02 \x01(\x0b\x32\x17.messages.OrderContentsH\x01\x88\x01\x01\x42\x07\n\x05_typeB\x0b\n\t_contents\"b\n\x06Health\x12\x11\n\x04type\x18\x01 \x01(\tH\x00\x88\x01\x01\x12/\n\x08\x63ontents\x18\x02 \x01(\x0b\x32\x18.messages.HealthContentsH\x01\x88\x01\x01\x42\x07\n\x05_typeB\x0b\n\t_contents\"d\n\x08Response\x12+\n\x04\x63ode\x18\x07 \x01(\x0e\x32\x18.messages.ResponseStatusH\x00\x88\x01\x01\x12\x15\n\x08\x63ontents\x18\x08 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_codeB\x0b\n\t_contents*\x1b\n\x06Status\x12\x08\n\x04GOOD\x10\x00\x12\x07\n\x03\x42\x41\x44\x10\x01*)\n\x0eResponseStatus\x12\x06\n\x02OK\x10\x00\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x01\x32?\n\x0cOrderService\x12/\n\x06method\x12\x0f.messages.Order\x1a\x12.messages.Response\"\x00\x32\x41\n\rHealthService\x12\x30\n\x06method\x12\x10.messages.Health\x1a\x12.messages.Response\"\x00\x62\x06proto3')

_STATUS = DESCRIPTOR.enum_types_by_name['Status']
Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_RESPONSESTATUS = DESCRIPTOR.enum_types_by_name['ResponseStatus']
ResponseStatus = enum_type_wrapper.EnumTypeWrapper(_RESPONSESTATUS)
GOOD = 0
BAD = 1
OK = 0
BAD_REQUEST = 1


_HEALTHCONTENTS = DESCRIPTOR.message_types_by_name['HealthContents']
_ORDERCONTENTS = DESCRIPTOR.message_types_by_name['OrderContents']
_ORDERCONTENTS_VEGGIES = _ORDERCONTENTS.nested_types_by_name['Veggies']
_ORDERCONTENTS_DRINKS = _ORDERCONTENTS.nested_types_by_name['Drinks']
_ORDERCONTENTS_DRINKS_CANS = _ORDERCONTENTS_DRINKS.nested_types_by_name['Cans']
_ORDERCONTENTS_DRINKS_BOTTLES = _ORDERCONTENTS_DRINKS.nested_types_by_name['Bottles']
_ORDERCONTENTS_MILK = _ORDERCONTENTS.nested_types_by_name['Milk']
_ORDERCONTENTS_BREAD = _ORDERCONTENTS.nested_types_by_name['Bread']
_ORDERCONTENTS_MEAT = _ORDERCONTENTS.nested_types_by_name['Meat']
_ORDER = DESCRIPTOR.message_types_by_name['Order']
_HEALTH = DESCRIPTOR.message_types_by_name['Health']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
_HEALTHCONTENTS_DISPENSERSTATUS = _HEALTHCONTENTS.enum_types_by_name['DispenserStatus']
_HEALTHCONTENTS_MOTORSTATUS = _HEALTHCONTENTS.enum_types_by_name['MotorStatus']
_ORDERCONTENTS_MILK_MILKTYPE = _ORDERCONTENTS_MILK.enum_types_by_name['MilkType']
_ORDERCONTENTS_BREAD_BREADTYPE = _ORDERCONTENTS_BREAD.enum_types_by_name['BreadType']
_ORDERCONTENTS_MEAT_MEATTYPE = _ORDERCONTENTS_MEAT.enum_types_by_name['MeatType']
HealthContents = _reflection.GeneratedProtocolMessageType('HealthContents', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHCONTENTS,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:messages.HealthContents)
  })
_sym_db.RegisterMessage(HealthContents)

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

Health = _reflection.GeneratedProtocolMessageType('Health', (_message.Message,), {
  'DESCRIPTOR' : _HEALTH,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:messages.Health)
  })
_sym_db.RegisterMessage(Health)

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
  _STATUS._serialized_start=2123
  _STATUS._serialized_end=2150
  _RESPONSESTATUS._serialized_start=2152
  _RESPONSESTATUS._serialized_end=2193
  _HEALTHCONTENTS._serialized_start=27
  _HEALTHCONTENTS._serialized_end=547
  _HEALTHCONTENTS_DISPENSERSTATUS._serialized_start=340
  _HEALTHCONTENTS_DISPENSERSTATUS._serialized_end=397
  _HEALTHCONTENTS_MOTORSTATUS._serialized_start=399
  _HEALTHCONTENTS_MOTORSTATUS._serialized_end=438
  _ORDERCONTENTS._serialized_start=550
  _ORDERCONTENTS._serialized_end=1821
  _ORDERCONTENTS_VEGGIES._serialized_start=810
  _ORDERCONTENTS_VEGGIES._serialized_end=993
  _ORDERCONTENTS_DRINKS._serialized_start=996
  _ORDERCONTENTS_DRINKS._serialized_end=1346
  _ORDERCONTENTS_DRINKS_CANS._serialized_start=1124
  _ORDERCONTENTS_DRINKS_CANS._serialized_end=1216
  _ORDERCONTENTS_DRINKS_BOTTLES._serialized_start=1218
  _ORDERCONTENTS_DRINKS_BOTTLES._serialized_end=1325
  _ORDERCONTENTS_MILK._serialized_start=1349
  _ORDERCONTENTS_MILK._serialized_end=1491
  _ORDERCONTENTS_MILK_MILKTYPE._serialized_start=1438
  _ORDERCONTENTS_MILK_MILKTYPE._serialized_end=1469
  _ORDERCONTENTS_BREAD._serialized_start=1494
  _ORDERCONTENTS_BREAD._serialized_end=1641
  _ORDERCONTENTS_BREAD_BREADTYPE._serialized_start=1586
  _ORDERCONTENTS_BREAD_BREADTYPE._serialized_end=1619
  _ORDERCONTENTS_MEAT._serialized_start=1644
  _ORDERCONTENTS_MEAT._serialized_end=1798
  _ORDERCONTENTS_MEAT_MEATTYPE._serialized_start=1733
  _ORDERCONTENTS_MEAT_MEATTYPE._serialized_end=1776
  _ORDER._serialized_start=1823
  _ORDER._serialized_end=1919
  _HEALTH._serialized_start=1921
  _HEALTH._serialized_end=2019
  _RESPONSE._serialized_start=2021
  _RESPONSE._serialized_end=2121
  _ORDERSERVICE._serialized_start=2195
  _ORDERSERVICE._serialized_end=2258
  _HEALTHSERVICE._serialized_start=2260
  _HEALTHSERVICE._serialized_end=2325
# @@protoc_insertion_point(module_scope)
