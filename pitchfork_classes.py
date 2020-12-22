import discogs_client
import pitchfork

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
    
    def delete_table(self):
        self.mycursor.execute("DROP TABLE IF EXISTS reviews")

class Review:
    def __init__(self, app_name, user_token): 
        self.app_name = app_name
        self.user_token = user_token

    def request_review(self, album_name):
        d = discogs_client.Client(self.app_name, user_token = self.user_token)

        results = d.search(album_name, type='release')
        search_results = []
        if results.pages < 1:
            print("Could not find album.")
        else:
            artist = results[0].artists[0]
            artist_name = artist.name

            try:
                p = pitchfork.search(artist_name, album_name)
                seach_results = [artist_name, p.album(), p.label(), p.score()]
            except IndexError:
                print("Could not find album.")
                continue
            
        return search_results


            
            
