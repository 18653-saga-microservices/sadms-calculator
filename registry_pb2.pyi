from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

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
    __slots__ = ["serviceName"]
    SERVICENAME_FIELD_NUMBER: _ClassVar[int]
    serviceName: str
    def __init__(self, serviceName: _Optional[str] = ...) -> None: ...
