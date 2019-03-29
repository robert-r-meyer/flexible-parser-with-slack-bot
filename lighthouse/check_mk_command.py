from lighthouse import command
from lighthouse.get_commands import GetCommands
from lighthouse.host_commands import HostCommands
from lighthouse.downtime_commands import DowntimeCommands
from lighthouse.check_mk_client import CheckMkClient

class CheckMkCommand(command.Command):
    def __init__(self):
        super().__init__()

        self._check = 'This is a journey into Check Mk.'
        self._command_name = 'Check Mk'

        # Add additional command functions and parsers here
        self._commands.update({'get': GetCommands(), 'host': HostCommands(),
            'downtime': DowntimeCommands()})
