import mysql.connector
import config
from pitchfork_classes import *

mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password
)

db = Database(mydb)

db.show_database()
