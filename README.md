# sadms-calculator
An vanilla python calculator app for demoing service registration to the SAGAFramework.

# Quick Start
Install the dependencies:
```
pip install -r requirements.txt
```

Generate client/server stubs based on the proto file location at `protos/proto` folder:
```
cd protos
bash generate.sh
```

The generate stubs will be located at `protos/gen_py` folder. Update the import in calculator_pb2_grpc.py and registry_pb2_grpc.py. (It is required to perform this step because otherwise there will be import error):
```
from . import registry_pb2
from . import calculator_pb2
```
Before you start the GRPC server, make sure that the register channel is started at `RemoteSagaExample.java` in `Framework` repo. Follow the instruction there to start the SAGAFramework.

After orchestrator started, start the calculator server by running:
```
python calculator_server.py
```

# Notice
- The service protobuf file, `calculator.proto`, should be the same as the one in the `Framework\microservice-chris\src\main\proto` folder.
- The register protobuf file, `registry.proto`, should be the same as the one in `Framework\SAGAFramework\src\main\proto` folder.
## Proto file
The proto file is located at `protos/proto`.
-  `calculator.proto` defines the calculator service.
- `registry.proto` defines the registry service.


## Error code
- 0: Success
- 1: Could not connect to the registry server
- 2: Register service failed: could be the ip/port is already registered



