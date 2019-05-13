import logging

from lighthouse.master_control_program import MasterControlProgram


class Event:
    """
    Event calls MasterControlProgram as the entry point.
    MCP handles parsing, calling, and sub params. View MCP for further details
    """

    def __init__(self, bot):
        self.bot = bot
        self.command = MasterControlProgram()

    def _handle_event(self, user, command, channel):
        if command and channel:
            logging.debug(
                "Received command: %s in channel: %s from user %s",
                command,
                channel,
                user,
            )

            response = self.command.handle_user_command(user, command)
            self.bot.web_slack_client.api_call(
                "chat.postMessage", channel=channel, text=response, as_user=True
            )
