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

    def add_host(self,
                 hostname,
                 folder='/',
                 ipaddress=None,
                 alias=None,
                 tags=None,
                 **custom_attrs):

        return self.safe_call_as_json(self._api.add_host, hostname, folder,
                                      ipaddress, alias, tags, **custom_attrs)

    def edit_host(self, host_name, unset_attributes=None, **custom):
        return self.safe_call_as_json(
            self._api.edit_host(host_name, unset_attributes, **custom))
