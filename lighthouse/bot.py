import logging
import os
import time

from slack import RTMClient, WebClient

from configs.config_loader import ConfigLoader
from lighthouse.event import Event

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class Bot:
    """ Bot is the base unit of work
    This class allows for parser interaction between slack messages
    and underlying commands that they execute.

    Current supported systems:
    Check MK
    """

    def __init__(self):
        path = os.path.join(ROOT_DIR, "..", "config.yml")
        variables = ConfigLoader(path)

        self.web_slack_client = WebClient(variables.config["SLACK_CLIENT_TOKEN"])
        self.rtm_slack_client = RTMClient(token=variables.config["SLACK_CLIENT_TOKEN"])
        self.bot_name = variables.config["SLACK_CLIENT_NAME"]
        self.bot_id = self._get_bot_id()
        self.valid = self.valid_slack_bot()

        if self.valid:
            self.event = Event(self)
        else:
            logging.error(
                "Slack error, could not find bot by the name of " + self.bot_name
            )

    def _get_bot_id(self):
        """
        Pull ID for current bot from user list
        and returns user name
        """

        api_call = self.web_slack_client.api_call("users.list")

        if api_call.get("ok"):
            # retrieve all users so we can find our bot
            users = api_call.get("members")

            for user in users:
                if "name" in user and user.get("name") == self.bot_name:
                    return "<@" + user.get("id") + ">"

        return None

    def valid_slack_bot(self):
        """
        Private funciton to check for bot id.
        Dictates if Bot object is valid
        """

        if self.bot_id is None:
            logging.error(
                "Invalid slack bot id. Please validate SLACK_CLIENT_TOKEN "
                + "and SLACK_CLIENT_NAME."
            )

        return self.bot_id is not None
