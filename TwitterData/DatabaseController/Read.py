from .Database import Database


class ReadFromDatabase(Database):

    def __init__(self, db_name):
        super().__init__(db_name)

    def read_raw_data(self, collection):
        return self.db[collection].find()

    def read_filtered_data(self, collection, data, filter):
        pass
