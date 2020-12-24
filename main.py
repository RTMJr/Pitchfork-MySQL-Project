import mysql.connector
import config
from app_lib import *

mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
)

if __name__ == "__main__":
    main(mydb)
