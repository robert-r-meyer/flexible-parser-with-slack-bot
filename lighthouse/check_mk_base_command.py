from lighthouse import command
from lighthouse.check_mk_client import CheckMkClient

class CheckMkBaseCommand(command.Command):
    def __init__(self):
        super().__init__()

        self._api = CheckMkClient()
