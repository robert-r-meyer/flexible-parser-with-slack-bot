from lighthouse.command import Command


class DowntimeCommands(Command):
    def __init__(self, api):
        super().__init__()

        self._check = 'This is a journey into Check Mk\'s downtime API commands.'
        self._command_name = 'Check Mk downtime API'
        self._api = api

        # Add additional command functions and parsers here
        self._commands.update({
            'historical': self.get_historical_downtimes,
            'set': self.set_downtime,
            'all': self.get_all_downtimes,
            'comments': self.get_comments,
            'alerts': self.get_alerts,
        })

    def get_historical_downtimes(self):
        return self.safe_call_as_json(self._api.view_historical_downtimes)

    def set_downtime(self, host_name, message, downTime=120):
        return self.safe_call_as_json(self._api.set_downtime, host_name,
                                      message, downTime)

    def get_all_downtimes(self):
        return self.safe_call_as_json(self._api.get_all_downtimes)

    def get_alerts(self):
        return self.safe_call_as_json(self._api.get_alerts)

    def get_comments(self):
        return self.safe_call_as_json(self._api.get_comments)
