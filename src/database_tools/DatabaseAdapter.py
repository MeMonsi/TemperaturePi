import psycopg2
import uuid

class DatabaseAdapter():

    # constructor:
    def __init__(self, tableName):
        self.__tableName = tableName  
    
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
    def SelectAll(self):
        statement = "SELECT * FROM " + self.__tableName + ";"
        return self.__ExecuteReturningStatement(statement)

    def Select(self, itemId):        
        if(isinstance(itemId, uuid.UUID)):
            statement = "SELECT * FROM " + self.__tableName + " WHERE id='" + str(itemId) + "';"
            return self.__ExecuteReturningStatement(statement)[0]
        raise TypeError(type(itemId))   

    def Insert(self, itemToInsert):
        try:
            print(itemToInsert)
            connection = self.__GetConnection()
            cursor = connection.cursor()
            query = """ INSERT INTO """ + self.__tableName + """ (ID, TIME, VALUE) VALUES (%s,%s,%s)"""            
            cursor.execute(query, itemToInsert)           
            connection.commit() 

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    print("PostgreSQL connection is closed")