"""Module for the sample adapter classes. """

from ..common.action_support.base import BaseAction
from ..pythonutils.models.MySQL_target import MySQLTarget
from ..pythonutils.models.MySQL_user import MySQLUser
from ..pythonutils.mysql_adapter import MySQLAdapter
from ..pythonutils.mysql_error import MySQLError
from ..common.action_support.base import raise_action_error, check_input_params


class MySQLSelect(BaseAction):
    """Sample Class to demonstrator input and output parameters."""

    def invoke(self, data, context):
        """Invoke this action class. """
        self.logger.info('Invoked MySQLSelect with Data: {}'.format(data))
        self.select_query = "select_query"
        self.return_query = "return_query"
        self.row_count = "row_count"

        check_input_params(data, self.select_query)
        sql = data[self.select_query]
        target = MySQLTarget(data)
        user = MySQLUser(data)
        adapter = MySQLAdapter(target, self.logger)
        result = {}
        try:
            connection = adapter.connect_to_mysql(user)
            with connection.cursor() as cursor:
                cursor.execute(sql)
                result[self.return_query] = cursor.fetchall()
                result[self.row_count] = len(result[self.return_query])
                self.logger.info("Returning {} to Result Engine.".format(result))
            return result
        except MySQLError as e:
            self.logger.error("Filed to verify target. Caused=%s", e.__cause__)
            self.raise_action_error('102', e.__cause__)
        finally:
            connection.close()
