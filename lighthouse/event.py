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

    def wait_for_event(self):
        """
        Entry point for commands from slack.
        Reads from slack and handles splitting of arguments.
        Submission of commands transitions to MCP for handling
        """
        events = self.bot.slack_client.rtm_read()

        for event in events:
            logging.debug(event)
            self._parse_event(event)

    def _parse_event(self, event):
        if event and 'text' in event and self.bot.bot_id in event['text']:
            self._handle_event(
                event['user'], event['text'].split(
                    self.bot.bot_id)[1].strip().lower(), event['channel'])

    def _handle_event(self, user, command, channel):
        if command and channel:
            logging.debug("Received command: %s in channel: %s from user %s",
                          command, channel, user)

            response = self.command.handle_user_command(user, command)
            self.bot.slack_client.api_call(
                "chat.postMessage",
                channel=channel,
                text=response,
                as_user=True)
