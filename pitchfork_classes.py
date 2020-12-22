class Database:
    def __init__(self, mydb):
        self.mydb = mydb
        self.mycursor = mydb.cursor()

    def create_database(self):
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS pitchfork")

    def delete_database(self):
        self.mycursor.execute("DROP DATABASE IF EXISTS pitchfork")
        
    def show_database(self): 
        self.mycursor.execute("SHOW DATABASES LIKE \'pitchfork\'")

        for x in self.mycursor:
            print(x)

    def use_database(self):
        self.mycursor.execute("USE pitchfork")

    def create_table(self):
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS reviews (name VARCHAR(255), album VARCHAR(255), label VARCHAR(255), score FLOAT(3, 1))")

    def show_tables(self):
        self.mycursor.execute("SHOW TABLES")

        for x in self.mycursor:
            print(x)
