from unittest.mock import Mock

import pytest
from pytest_mock import mocker

from lighthouse.host_commands import HostCommands


class TestHostsCommands():
    def setup(self):
        self.api = Mock()
        self.parser = HostCommands(self.api)

    def test_ping(self):
        assert self.parser._ping(
        ) == "This is a journey into Check Mk's host API commands."

    def test_calling_ping(self):
        assert self.parser.handle_command(
            'ping') == "This is a journey into Check Mk's host API commands."

    @pytest.mark.skip()
    def test_command_block(self):
        assert [*self.parser._commands] == ['ping', 'help', 'add', 'edit']

    @pytest.mark.skip()
    def test_add_host_with_folder(self, mocker):
        """
        `host add my-host folder-name`
        should be passed to checkmk and return successfully
        """

        folder_host = mocker.patch(
            'lighthouse.host_commands.HostCommands.add_host',
            return_value=True,
            autospec=True)

        self.parser.handle_command('add my-host folder-name')

        assert folder_host.call_count == 1

    @pytest.mark.skip()
    def test_edit_host_with_ipaddress(self):
        """
        TODO: Add VCR when adding actual calls to checkmk

        `` should be passed to checkmk and return the get all hosts
        from GetCommands processor
        """
        block = self.parser.handle_command('edit my-host-name ipaddress')

        assert block == (
            'TODO: Edit Host name from CheckMk my-host-name ipaddress')
