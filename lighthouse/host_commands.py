from lighthouse.command import Command


class HostCommands(Command):
    def __init__(self, api):
        super().__init__()
        self._check = 'This is a journey into Check Mk\'s host API commands.'
        self._command_name = 'Check Mk host API'
        self._api = api

        # # Add additional command functions and parsers here
        self._commands.update({
            'add': self.add_host,
            'edit': self.edit_host,
        })

    def add_host(self, host_name, folder_name):
        return ' '.join(
            ['TODO:', 'Add Host name from CheckMk', host_name, folder_name])

    def edit_host(self, host_name, ipaddress):
        return ' '.join(
            ['TODO:', 'Edit Host name from CheckMk', host_name, ipaddress])
