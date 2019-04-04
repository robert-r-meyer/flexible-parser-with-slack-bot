import os

from check_mk_web_api.web_api import WebApi

from configs.config_loader import ConfigLoader
from lighthouse.command import Command
from lighthouse.downtime_commands import DowntimeCommands
from lighthouse.get_commands import GetCommands
from lighthouse.host_commands import HostCommands


class CheckMkCommand(Command):
    def __init__(self):
        super().__init__()

        variables = ConfigLoader('../config.yml')

        self._api = WebApi(
            variables.config['CHECK_MK_SERVER'],
            username=variables.config['CHECK_MK_USER'],
            secret=variables.config['CHECK_MK_PASSWORD'])

        self._check = 'This is a journey into Check Mk.'
        self._command_name = 'Check Mk'

        # Add additional command functions and parsers here
        self._commands.update({
            'get': GetCommands(self._api),
            'host': HostCommands(self._api),
            'downtime': DowntimeCommands(self._api)
        })
