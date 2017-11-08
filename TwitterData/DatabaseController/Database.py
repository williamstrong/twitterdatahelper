from pymongo import MongoClient
from TwitterData.DatabaseController import __credential_file__


class Database:

    def __init__(self, db_name):
        # For use with MongoDB Atlas
        with open(__credential_file__) as mongo_cred_file:
            mongo_cred = mongo_cred_file.read()
        self.client = MongoClient(mongo_cred, connect=False)
        self.db = self.client[db_name]


        # Connect to DB
        # self.client = MongoClient('localhost', 27017)
        # self.db = self.client.store_tweets

        # self.collection = self.db.tweet_collection

    def close(self):
        self.client.close()

    def create_collection(self, collection_name):
        self.db.create_collection(collection_name)

    def remove_collection(self, collection_name):
        """Dangerous, only use this if intending to permanently delete a collection."""
        self.db.drop_collection(collection_name)

    def collect_stats(self):
        # print(self.db.command("collstats", "new"))
        pass

    def collections(self):
        return self.db.collection_names()

    def search_collection_name(self, name):
        pass


if __name__ == "__main__":
    db = Database()
    db.collections()
