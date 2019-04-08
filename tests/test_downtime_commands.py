from unittest.mock import Mock

import pytest
from pytest_mock import mocker

from lighthouse.downtime_commands import DowntimeCommands
from lighthouse.format import FormatFor


class TestDowntimeCommands():
    def setup(self):
        self.api = Mock()
        self.parser = DowntimeCommands(self.api)

    def test_ping(self):
        assert self.parser._ping(
        ) == "This is a journey into Check Mk's downtime API commands."

    def test_calling_ping(self):
        assert self.parser.handle_command(
            'ping'
        ) == "This is a journey into Check Mk's downtime API commands."

    def test_return_of_all_downtime(self):
        """
        `downtime all`
        should be passed to checkmk and return successfully
        """
        self.parser.handle_command('all')

        # Assert call without arguments
        self.api.get_all_downtimes.assert_called_with((), )

    def test_set_downtime(self):
        """
        `downtime set <hostname> <message> <hours>`

        should be passed to checkmk and set downtime on the server
        """
        self.parser.handle_command(
            'set sewrndb26.mgmt.taketwo.online "down me!" 120')
        self.api.set_downtime.assert_called_with(
            ('sewrndb26.mgmt.taketwo.online', '120', 'down me!'), )

    def test_get_alerts(self):
        self.parser.handle_command('alerts')
        self.api.get_alerts.assert_called_with((), )

    def test_historical_downtimes(self):
        self.parser.handle_command('historical')
        self.api.view_historical_downtimes.assert_called_with((), )

    def test_get_comments(self):
        self.parser.handle_command('comments')
        self.api.get_comments.assert_called_with((), )
