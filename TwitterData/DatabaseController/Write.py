from .Database import Database


class WriteToDatabase(Database):

    def __init__(self, db_name):
        super().__init__(db_name)

    def add_data(self, collection, data):
        post_id = self.db[collection].insert_one(data).inserted_id
        return post_id
