from datetime import datetime
import os, time
from src.entities.Temperature import Temperature

_sensorPath = '/sys/bus/w1/devices/28-01144fdb5caa/w1_slave'

class TemperatureSlave:  
            
    def ReadTemperature(self):
        temperatureFile = open(_sensorPath, 'r')
        lines = temperatureFile.readlines()
        temperatureFile.close()

        temperatureString = lines[1].find('t=')
        if temperatureString != -1 :
            tempData = lines[1][temperatureString+2:]
            tempCelsius = float(tempData) / 1000.0            
            return Temperature(datetime.now(), tempCelsius)
        raise ValueError(temperatureString)