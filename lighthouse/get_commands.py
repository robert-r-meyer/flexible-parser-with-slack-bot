from lighthouse.check_mk_base_command import CheckMkBaseCommand


class GetCommands(CheckMkBaseCommand):
    def __init__(self):
        super().__init__()
        self._check = 'This is a journey into Check Mk\'s get API commands.'
        self._command_name = 'Check Mk Get API'

        # # Add additional command functions and parsers here
        self._commands.update({
            'all': self.all_hosts,
            'host': self.single_host,
            'services': self.discover_services,
            'alerts': self.alerts
        })

    def all_hosts(self):
        return self._api.all_hosts()

    def single_host(self, host_name):
        return self._api.host(host_name)

    def discover_services(self):
        return self._api.discover_all_services()

    def alerts(self):
        return self._api.get_alerts()
