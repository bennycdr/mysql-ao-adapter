"""Module for the adapter target classes. """
import pymysql.cursors

from activities_python.pythonutils.utils import check_input_params
from activities_python.pythonutils.utils import get_optional_value


class MySQLTarget(object):
    """Class representing the adapter target. """

    HOST = "host"
    CHARSET="charset"
    DB="db"

    def fill_host(self, data):
        """Set the target host. """
        check_input_params(data, self.HOST)
        self.host = data[self.HOST]

    def fill_charset(self, data):
        """Set the target charset, or use a default if not provided. """
        self.charset = get_optional_value(data, self.CHARSET, "utf8mb4")
        self.charset = self.charset or "utf8mb4"

    def fill_db(self, data):
        """Set the target DB. """
        check_input_params(data, self.DB)
        self.db = data[self.DB]

    def __init__(self, data):
        self.fill_host(data)
        self.fill_db(data)
        self.fill_charset(data)
        self.cursor = pymysql.cursors.DictCursor

    def get_params(self):
        return {
            'host': self.host,
            'db': self.db,
            'charset': self.charset,
            'cursor': self.cursor
        }
