import sys 
sys.path.append('..')

import uuid
from src.database_tools.DatabaseAdapter import DatabaseAdapter
from src.entities.Temperature import Temperature	
from datetime import datetime 


class TemperatureDataService():
    # constructor:
    def __init__(self):
        self.__tableName = "temperature"
        self.__databaseAdapter = DatabaseAdapter(self.__tableName)

    # private methods:
    def __ParseTemperatureResult(self, row):        
        itemId = row[0]
        timeStamp = row[1]
        value = row[2]
        temperature = Temperature(itemId, timeStamp, value)
        return temperature
        
    
    # public methods:
    def GetById(self, itemId):
        result = self.__databaseAdapter.Select(itemId)
        temperature = self.__ParseTemperatureResult(result)
        return temperature

    def GetAll(self):
        results = self.__databaseAdapter.SelectAll()  
        temperatures = []      
        for res in results:
            temperatures.append(self.__ParseTemperatureResult(res))

        return temperatures
    
    def Save(self, temperatureItem):
        if(temperatureItem.Id == uuid.UUID(int=0)):
            itemId = uuid.uuid4()
        else:
            itemId = temperatureItem.Id
        self.__databaseAdapter.Insert((str(itemId), temperatureItem.TimeStamp, temperatureItem.Value)) 
 


           