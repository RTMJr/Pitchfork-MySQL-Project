import mysql.connector
import config
from app_lib import *

mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
)

def main():
    db = Database(mydb)
    db.create_database()
    db.use_database()
    db.create_table()

    r = Review(config.app_name, config.user_token)
    album = str(input("Enter album name: "))
    review = r.request_review(album)

    if len(review) > 0:
        db.insert_into_database(review)

if __name__ == "__main__":
    main()
