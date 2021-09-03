# In making 
import mysql.connector

def connect(user, password, host, database)
    # Connect to DB
    cnx = cnx = mysql.connector.connect(user=user, password=password,
                              host=host,
                              database=database)
    cnx.close()

def get():
    # Get data from DB

if __name__ == '__main__':
    return 0