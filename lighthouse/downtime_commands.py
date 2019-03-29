from lighthouse.check_mk_base_command import CheckMkBaseCommand


class DowntimeCommands(CheckMkBaseCommand):
    def __init__(self):
        super().__init__()
        self._check = 'This is a journey into Check Mk\'s downtime API commands.'
        self._command_name = 'Check Mk downtime API'
        # # Add additional command functions and parsers here
        self._commands.update({
            'for': self.get_downtime,
            'set': self.set_downtime,
            'all': self.get_all_downtimes,
        })

    def get_downtime(self, host_name):
        return ' '.join(
            ['TODO:', 'get downtime CheckMk', host_name])

    def set_downtime(self, host_name, downTime=120):
        return ' '.join(
            ['TODO:', 'set Downtime for CheckMk host', host_name, downTime])

    def get_all_downtimes(self):
        return self._api.get_all_downtimes()
