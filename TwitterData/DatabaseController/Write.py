from ._Database import DB


class WriteToDB(DB):

    def __init__(self):
        super().__init__()

    def add_data(self, collection, data):
        post_id = self.db[collection].insert_one(data).inserted_id
        return post_id
