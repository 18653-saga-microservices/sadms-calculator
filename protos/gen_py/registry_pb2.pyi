from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegistryRequest(_message.Message):
    __slots__ = ["serviceAddress", "serviceName", "servicePort"]
    SERVICEADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERVICENAME_FIELD_NUMBER: _ClassVar[int]
    SERVICEPORT_FIELD_NUMBER: _ClassVar[int]
    serviceAddress: str
    serviceName: str
    servicePort: int
    def __init__(self, serviceName: _Optional[str] = ..., serviceAddress: _Optional[str] = ..., servicePort: _Optional[int] = ...) -> None: ...

class RegistryResponse(_message.Message):
    __slots__ = ["serviceName", "status"]
    SERVICENAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    serviceName: str
    status: Status
    def __init__(self, serviceName: _Optional[str] = ..., status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["code", "message"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
