# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: caffe2_legacy.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='caffe2_legacy.proto',
  package='caffe2',
  serialized_pb='\n\x13\x63\x61\x66\x66\x65\x32_legacy.proto\x12\x06\x63\x61\x66\x66\x65\x32*J\n\rLegacyPadding\x12\n\n\x06NOTSET\x10\x00\x12\t\n\x05VALID\x10\x01\x12\x08\n\x04SAME\x10\x02\x12\x18\n\x14\x43\x41\x46\x46\x45_LEGACY_POOLING\x10\x03')

_LEGACYPADDING = _descriptor.EnumDescriptor(
  name='LegacyPadding',
  full_name='caffe2.LegacyPadding',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOTSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAME', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAFFE_LEGACY_POOLING', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=31,
  serialized_end=105,
)

LegacyPadding = enum_type_wrapper.EnumTypeWrapper(_LEGACYPADDING)
NOTSET = 0
VALID = 1
SAME = 2
CAFFE_LEGACY_POOLING = 3




# @@protoc_insertion_point(module_scope)