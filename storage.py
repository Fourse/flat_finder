class Storage:
    def __init__(self):
        self.storage = []

    def update_storage(self, url):
        self.storage.append(url)

    def get_storage(self):
        return self.storage.copy()


class User:
    def __init__(self):
        self.storage = Storage()

    def set_star(self, url):
        self.storage.update_storage(url)

    def get_stared(self):
        return self.storage.get_storage()