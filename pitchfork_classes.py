class Database:
    def __init__(self, mydb):
        self.mydb = mydb
        self.mycursor = mydb.cursor()

    def create_database(self):
        self.mycursor.execute("CREATE DATABASE pitchfork")

    def delete_database(self):
        self.mycursor.execute("DROP DATABASE IF EXISTS \'pitchfork\'")
        
    def show_database(self): 
        self.mycursor.execute("SHOW DATABASES LIKE \'pitchfork\'")

        for x in self.mycursor:
            print(x)
