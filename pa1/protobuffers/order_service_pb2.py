# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13order_service.proto\x12\x05order\" \n\x0cOrderRequest\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t\" \n\rOrderResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2G\n\x0cOrderService\x12\x37\n\nPlaceOrder\x12\x13.order.OrderRequest\x1a\x14.order.OrderResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'order_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ORDERREQUEST']._serialized_start=30
  _globals['_ORDERREQUEST']._serialized_end=62
  _globals['_ORDERRESPONSE']._serialized_start=64
  _globals['_ORDERRESPONSE']._serialized_end=96
  _globals['_ORDERSERVICE']._serialized_start=98
  _globals['_ORDERSERVICE']._serialized_end=169
# @@protoc_insertion_point(module_scope)