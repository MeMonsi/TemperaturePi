from concurrent import futures
import sys 
sys.path.append('..')
from TemperatureSlave import TemperatureSlave 

import logging
import grpc
import os, time

import TemperatureService_pb2
import TemperatureService_pb2_grpc

_sensorPath = '/sys/bus/w1/devices/28-01144fdb5caa/w1_slave'

class TemperatureSensorService(TemperatureService_pb2_grpc.TemperatureSensorServiceServicer):    

    def GetTemperature(self, request, context):
        temperatureSlave = TemperatureSlave()
        temperature = temperatureSlave.ReadTemperature() 
        return TemperatureService_pb2.TemperatureReply(temperature=temperature)   


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TemperatureService_pb2_grpc.add_TemperatureSensorServiceServicer_to_server(TemperatureSensorService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
