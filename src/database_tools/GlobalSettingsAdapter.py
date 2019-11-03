import psycopg2
import uuid

class GlobalSettingsAdapter():

    # constructor:
    def __init__(self):
        self.__tableName = "settings"  
        
    # private methods:
    def __GetConnection(self):
        connection = psycopg2.connect(
            user = "pi",
            password = "dev",
            host = "localhost",
            port = "5432",
            database = "temp_pi_db")
        return connection

    def __ExecuteReturningStatement(self, statement):
        try:
            connection = self.__GetConnection()
            cursor = connection.cursor()  
            cursor.execute(statement)    
            results = cursor.fetchall()
            return results 

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed") 

    # public methods:  

    def GetIsStoringEnabled(self):
        statement = "SELECT isenabled FROM " + self.__tableName + " WHERE setting='storingData';"
        result = self.__ExecuteReturningStatement(statement)        
        return result
        

    def SetIsStoringEnabled(self, value):
        try:            
            connection = self.__GetConnection()
            cursor = connection.cursor()
            query = """UPDATE """ + self.__tableName + """ SET ISENABLED = '%s' WHERE SETTING='storingData'; """           
            cursor.execute(query, (value,))           
            connection.commit() 

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")