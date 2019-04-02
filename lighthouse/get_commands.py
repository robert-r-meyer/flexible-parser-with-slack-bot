from lighthouse.command import Command


class GetCommands(Command):
    def __init__(self, api):
        super().__init__()
        self._check = 'This is a journey into Check Mk\'s get API commands.'
        self._command_name = 'Check Mk Get API'
        self._api = api

        # # Add additional command functions and parsers here
        self._commands.update({
            'all': self.all_hosts,
            'host': self.single_host,
            'services': self.discover_services,
            'alerts': self.alerts
        })

    def all_hosts(self):
        return self.safe_call_as_json(self._api.get_all_hosts)

    def single_host(self, hostname):
        return self.safe_call_as_json(self._api.get_host, hostname)

    def discover_host_services(self, hostname):
        return self.safe_call_as_json(self._api.discover_services, hostname)

    def discover_services(self):
        return self.safe_call_as_json(
            self._api.discover_services_for_all_hosts)

    def alerts(self):
        return self._api.get_alerts()
