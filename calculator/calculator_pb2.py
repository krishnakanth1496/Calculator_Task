# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x63\x61lculator.proto\"\'\n\x0f\x41\x64\x64itionRequest\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x02\"\x1d\n\x10\x41\x64\x64itionResponse\x12\t\n\x01\x63\x18\x01 \x01(\x02\"+\n\x13SubstractionRequest\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x02\"!\n\x14SubstractionResponse\x12\t\n\x01\x63\x18\x01 \x01(\x02\"-\n\x15MultiplicationRequest\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x02\"#\n\x16MultiplicationResponse\x12\t\n\x01\x63\x18\x01 \x01(\x02\"\'\n\x0f\x44ivisionRequest\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x02\"\x1d\n\x10\x44ivisionResponse\x12\t\n\x01\x63\x18\x01 \x01(\x02\x32=\n\x08\x41\x64\x64ition\x12\x31\n\x08\x41\x64\x64ition\x12\x10.AdditionRequest\x1a\x11.AdditionResponse\"\x00\x32M\n\x0cSubstraction\x12=\n\x0cSubstraction\x12\x14.SubstractionRequest\x1a\x15.SubstractionResponse\"\x00\x32U\n\x0eMultiplication\x12\x43\n\x0eMultiplication\x12\x16.MultiplicationRequest\x1a\x17.MultiplicationResponse\"\x00\x32=\n\x08\x44ivision\x12\x31\n\x08\x44ivision\x12\x10.DivisionRequest\x1a\x11.DivisionResponse\"\x00\x62\x06proto3'
)




_ADDITIONREQUEST = _descriptor.Descriptor(
  name='AdditionRequest',
  full_name='AdditionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='AdditionRequest.a', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='AdditionRequest.b', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=59,
)


_ADDITIONRESPONSE = _descriptor.Descriptor(
  name='AdditionResponse',
  full_name='AdditionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='c', full_name='AdditionResponse.c', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=90,
)


_SUBSTRACTIONREQUEST = _descriptor.Descriptor(
  name='SubstractionRequest',
  full_name='SubstractionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='SubstractionRequest.a', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='SubstractionRequest.b', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=135,
)


_SUBSTRACTIONRESPONSE = _descriptor.Descriptor(
  name='SubstractionResponse',
  full_name='SubstractionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='c', full_name='SubstractionResponse.c', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=170,
)


_MULTIPLICATIONREQUEST = _descriptor.Descriptor(
  name='MultiplicationRequest',
  full_name='MultiplicationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='MultiplicationRequest.a', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='MultiplicationRequest.b', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=217,
)


_MULTIPLICATIONRESPONSE = _descriptor.Descriptor(
  name='MultiplicationResponse',
  full_name='MultiplicationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='c', full_name='MultiplicationResponse.c', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=254,
)


_DIVISIONREQUEST = _descriptor.Descriptor(
  name='DivisionRequest',
  full_name='DivisionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='DivisionRequest.a', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='DivisionRequest.b', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=295,
)


_DIVISIONRESPONSE = _descriptor.Descriptor(
  name='DivisionResponse',
  full_name='DivisionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='c', full_name='DivisionResponse.c', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=326,
)

DESCRIPTOR.message_types_by_name['AdditionRequest'] = _ADDITIONREQUEST
DESCRIPTOR.message_types_by_name['AdditionResponse'] = _ADDITIONRESPONSE
DESCRIPTOR.message_types_by_name['SubstractionRequest'] = _SUBSTRACTIONREQUEST
DESCRIPTOR.message_types_by_name['SubstractionResponse'] = _SUBSTRACTIONRESPONSE
DESCRIPTOR.message_types_by_name['MultiplicationRequest'] = _MULTIPLICATIONREQUEST
DESCRIPTOR.message_types_by_name['MultiplicationResponse'] = _MULTIPLICATIONRESPONSE
DESCRIPTOR.message_types_by_name['DivisionRequest'] = _DIVISIONREQUEST
DESCRIPTOR.message_types_by_name['DivisionResponse'] = _DIVISIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdditionRequest = _reflection.GeneratedProtocolMessageType('AdditionRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDITIONREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:AdditionRequest)
  })
_sym_db.RegisterMessage(AdditionRequest)

AdditionResponse = _reflection.GeneratedProtocolMessageType('AdditionResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDITIONRESPONSE,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:AdditionResponse)
  })
_sym_db.RegisterMessage(AdditionResponse)

SubstractionRequest = _reflection.GeneratedProtocolMessageType('SubstractionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSTRACTIONREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:SubstractionRequest)
  })
_sym_db.RegisterMessage(SubstractionRequest)

SubstractionResponse = _reflection.GeneratedProtocolMessageType('SubstractionResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSTRACTIONRESPONSE,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:SubstractionResponse)
  })
_sym_db.RegisterMessage(SubstractionResponse)

MultiplicationRequest = _reflection.GeneratedProtocolMessageType('MultiplicationRequest', (_message.Message,), {
  'DESCRIPTOR' : _MULTIPLICATIONREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:MultiplicationRequest)
  })
_sym_db.RegisterMessage(MultiplicationRequest)

MultiplicationResponse = _reflection.GeneratedProtocolMessageType('MultiplicationResponse', (_message.Message,), {
  'DESCRIPTOR' : _MULTIPLICATIONRESPONSE,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:MultiplicationResponse)
  })
_sym_db.RegisterMessage(MultiplicationResponse)

DivisionRequest = _reflection.GeneratedProtocolMessageType('DivisionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DIVISIONREQUEST,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:DivisionRequest)
  })
_sym_db.RegisterMessage(DivisionRequest)

DivisionResponse = _reflection.GeneratedProtocolMessageType('DivisionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DIVISIONRESPONSE,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:DivisionResponse)
  })
_sym_db.RegisterMessage(DivisionResponse)



_ADDITION = _descriptor.ServiceDescriptor(
  name='Addition',
  full_name='Addition',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=328,
  serialized_end=389,
  methods=[
  _descriptor.MethodDescriptor(
    name='Addition',
    full_name='Addition.Addition',
    index=0,
    containing_service=None,
    input_type=_ADDITIONREQUEST,
    output_type=_ADDITIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADDITION)

DESCRIPTOR.services_by_name['Addition'] = _ADDITION


_SUBSTRACTION = _descriptor.ServiceDescriptor(
  name='Substraction',
  full_name='Substraction',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=391,
  serialized_end=468,
  methods=[
  _descriptor.MethodDescriptor(
    name='Substraction',
    full_name='Substraction.Substraction',
    index=0,
    containing_service=None,
    input_type=_SUBSTRACTIONREQUEST,
    output_type=_SUBSTRACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUBSTRACTION)

DESCRIPTOR.services_by_name['Substraction'] = _SUBSTRACTION


_MULTIPLICATION = _descriptor.ServiceDescriptor(
  name='Multiplication',
  full_name='Multiplication',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=470,
  serialized_end=555,
  methods=[
  _descriptor.MethodDescriptor(
    name='Multiplication',
    full_name='Multiplication.Multiplication',
    index=0,
    containing_service=None,
    input_type=_MULTIPLICATIONREQUEST,
    output_type=_MULTIPLICATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MULTIPLICATION)

DESCRIPTOR.services_by_name['Multiplication'] = _MULTIPLICATION


_DIVISION = _descriptor.ServiceDescriptor(
  name='Division',
  full_name='Division',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=557,
  serialized_end=618,
  methods=[
  _descriptor.MethodDescriptor(
    name='Division',
    full_name='Division.Division',
    index=0,
    containing_service=None,
    input_type=_DIVISIONREQUEST,
    output_type=_DIVISIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIVISION)

DESCRIPTOR.services_by_name['Division'] = _DIVISION

# @@protoc_insertion_point(module_scope)