"""Module containting the template adapter classes.  """
import pymysql.cursors
import requests

from requests import ConnectionError
from requests import ConnectTimeout
from requests import HTTPError
from requests import ReadTimeout
from requests import Timeout

from activities_python.constants.basic_constants import BasicConstants
from activities_python.pythonutils.mysql_error import MySQLError
from .utils import get_proxies

class MySQLAdapter(object):
    """The Template Adapter class. """

    def __init__(self, target, logger):
        self.target = target
        self.logger = logger

    def connect_to_mysql(self, user):
        user_info = user.get_params()
        db_info = self.target.get_params()
        connection = pymysql.connect(host = db_info['host'],
                                 user=user_info['username'],
                                 password=user_info['password'],
                                 db=db_info['db'],
                                 charset=db_info['charset'],
                                 cursorclass=db_info['cursor'])
        return connection
