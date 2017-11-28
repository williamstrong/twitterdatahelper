class Error(Exception):
    pass


class NoSubClass(Error):
    def __init__(self, class_name):
        self.class_name = class_name

    def __repr__(self):
        pass
