from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddRequest(_message.Message):
    __slots__ = ["operand1", "operand2"]
    OPERAND1_FIELD_NUMBER: _ClassVar[int]
    OPERAND2_FIELD_NUMBER: _ClassVar[int]
    operand1: int
    operand2: int
    def __init__(self, operand1: _Optional[int] = ..., operand2: _Optional[int] = ...) -> None: ...

class AddResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class MultiplyRequest(_message.Message):
    __slots__ = ["operand1", "operand2"]
    OPERAND1_FIELD_NUMBER: _ClassVar[int]
    OPERAND2_FIELD_NUMBER: _ClassVar[int]
    operand1: int
    operand2: int
    def __init__(self, operand1: _Optional[int] = ..., operand2: _Optional[int] = ...) -> None: ...

class MultiplyResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...
