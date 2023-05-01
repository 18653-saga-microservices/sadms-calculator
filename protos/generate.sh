#!/bin/bash

declare -a services=("proto")

for SERVICE in "${services[@]}"; do
    DESTDIR='gen_py'
    mkdir -p $DESTDIR
    python3 -m grpc_tools.protoc \
        --proto_path=$SERVICE/ \
        --python_out=$DESTDIR \
        --pyi_out=$DESTDIR \
        --grpc_python_out=$DESTDIR \
        $SERVICE/*.proto
done