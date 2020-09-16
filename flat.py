import requests

from abc import abstractmethod

from .storage import Storage


class Parser:

    url = None

    def __init__(self, city, undergrounds, min_price, max_price, room_count, foot_min):
        self.city = city
        self.undergrounds = undergrounds
        self.min_price = min_price
        self.max_price = max_price
        self.room_count = room_count
        self.foot_min = foot_min

    @abstractmethod
    def set_query(self):
        pass

    def _request(self):
        requests.get(self.url + self.set_query())

    def get_flat(self):
        return self._request()

    @abstractmethod
    def prepare_query(self):
        pass


class Avito(Parser):

    url = 'https://www.avito.ru/'

    def __init__(self, city, undergrounds, min_price, max_price, room_count, foot_min):
        super().__init__(city, undergrounds, min_price, max_price, room_count, foot_min)


class Cian(Parser):

    url = 'https://www.cian.ru/'

    def __init__(self, city, undergrounds, min_price, max_price, room_count, foot_min):
        super().__init__(city, undergrounds, min_price, max_price, room_count, foot_min)

    def prepare_query(self):
        # TODO prepare query from self objects
        pass


    def set_query(self):
        query = 'cat.php?currency=2&deal_type=rent&engine_version=2'

