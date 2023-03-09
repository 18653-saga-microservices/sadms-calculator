from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ["first_number", "second_number"]
    FIRST_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SECOND_NUMBER_FIELD_NUMBER: _ClassVar[int]
    first_number: int
    second_number: int
    def __init__(self, first_number: _Optional[int] = ..., second_number: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...
