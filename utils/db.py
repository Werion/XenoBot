# In making 
import mysql.connector
import os
from dotenv import load_dotenv


# db = mysql.connector.connect(
#     host=os.getenv('HOST'),
#     user=os.getenv('DB_USER'),
#     password=os.getenv('PASSWORD')
# )


db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=""
)


def get():
    print(db)


if __name__ == '__main__':
    get()