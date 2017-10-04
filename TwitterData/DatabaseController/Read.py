from ._Database import DB


class ReadFromDB(DB):

    def __init__(self):
        super().__init__()

    def read_raw_data(self, collection):
        return self.db[collection].find()

    def read_filtered_data(self, collection, data, filter):
        pass
