from __future__ import print_function
import logging

import grpc
import TemperatureService_pb2
import TemperatureService_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = TemperatureService_pb2_grpc.TemperatureSensorServiceStub(channel)
        response = stub.GetTemperature(TemperatureService_pb2.TemperatureRequest(sensorId=0))
    print("Temperature sensor service client received: " + str(response.temperature))


if __name__ == '__main__':
    logging.basicConfig()
    run()