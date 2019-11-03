import uuid

# Representing a single temperature measurement with:
# An ID (UUID), a Value (float) and a TimeStamp (timestamp) 
class Temperature():   
    # constructor:
    def __init__(self, timeStamp, temperatureValue, itemId=None):
        self.TimeStamp = timeStamp
        self.Value = temperatureValue
        if(itemId == None):
            self.Id = uuid.UUID(int=0)
        else:
            self.Id = itemId