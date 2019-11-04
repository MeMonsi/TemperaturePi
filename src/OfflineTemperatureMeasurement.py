
from time import sleep, strftime, time
from datetime import datetime
import src.database_tools
from src.entities.Temperature import Temperature
from src.TemperatureSlave import TemperatureSlave
from src.database_tools.TemperatureDataService import TemperatureDataService
from src.database_tools.GlobalSettingsAdapter import GlobalSettingsAdapter

if __name__ == '__main__':
    slave = TemperatureSlave()
    dataService = TemperatureDataService()
    secondCounter = 0
    while secondCounter < 3600:
            temperature = slave.ReadTemperature()
            dataService.Save(temperature)
            print("Saved " + str(temperature) + "at " + str(secondCounter) + " seconds")
            secondCounter = secondCounter + 10
            sleep(10)
