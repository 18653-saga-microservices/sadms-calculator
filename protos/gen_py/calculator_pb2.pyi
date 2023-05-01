from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ["first_number", "second_number"]
    FIRST_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SECOND_NUMBER_FIELD_NUMBER: _ClassVar[int]
    first_number: int
    second_number: int
    def __init__(self, first_number: _Optional[int] = ..., second_number: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["result", "status"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    result: int
    status: Status
    def __init__(self, result: _Optional[int] = ..., status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["code", "message"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
