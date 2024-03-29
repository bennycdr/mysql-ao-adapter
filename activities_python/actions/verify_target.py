"""Module for the sample adapter classes."""

from ..common.action_support.base import BaseAction
from ..pythonutils.models.MySQL_target import MySQLTarget
from ..pythonutils.models.MySQL_user import MySQLUser
from ..pythonutils.mysql_adapter import MySQLAdapter
from ..pythonutils.mysql_error import MySQLError
from ..common.action_support.base import raise_action_error


class VerifyTargetQuery(BaseAction):
    """Sample Class for verifying target."""

    def invoke(self, data, context):
        """Invoke this action class. """
        self.logger.info('Invoked VerifyTargetQuery')

        # Put your code here to get/parse some adapter properties.
        # Sample:
        target = TemplateTarget(data)
        user = TemplateUser(data)
        adapter = TemplateAdapter(target, self.logger)

        try:
            # Verify target here: (check password/token/etc , try to connect).
            # Sample:
            adapter.get_auth_token(user, self.proxies)

            return {
                'verified': True,
            }
        except TemplateError as e:
            self.logger.error("Failed to verify target. Status=%s, Response=%s", e.status_code, e.response)
            raise_action_error(400, e)
