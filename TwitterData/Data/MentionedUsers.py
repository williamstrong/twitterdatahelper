from ..DatabaseController.Read import ReadFromDB


class Mentioned:
    def __init__(self, name):
        self.name = name
        self._test_if_name_exist()

    def _test_if_name_exist(self):
        # If the name is a collection in the DB and is recent use it, otherwise request usertimeline from
        # TwitterController or add tweets since last_id and update name.
        pass

    def _request_from_db(self):
        pass

    def _create_list_of_users(self):
        pass

    def _create_mentions_map(self):
        pass


