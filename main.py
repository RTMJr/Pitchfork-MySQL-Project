import mysql.connector
import config
from pitchfork_classes import *

mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
)

db = Database(mydb)

db.create_database()
db.use_database()

db.create_table()
db.show_tables()





