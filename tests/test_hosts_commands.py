import pytest

from lighthouse.host_commands import HostCommands


class TestCommandPassing():
    def setup(self):
        self.api = 'NOT THE ACTUAL API INTERFACE'
        self.parser = HostCommands(self.api)

    def test_ping(self):
        assert self.parser._ping(
        ) == "This is a journey into Check Mk's host API commands."

    def test_calling_ping(self):
        assert self.parser.handle_command(
            'ping') == "This is a journey into Check Mk's host API commands."

    def test_command_block(self):
        assert [*self.parser._commands] == ['ping', 'help', 'add', 'edit']

    @pytest.mark.skip('Implementation Pending')
    def test_add_host_with_folder(self):
        """
        TODO: Add VCR when adding actual calls to checkmk

        `host add my-host folder-name`
        should be passed to checkmk and return successfully
        """
        block = self.parser.handle_command('add my-host folder-name')
        assert block == 'TODO: Add Host name from CheckMk my-host folder-name'

    @pytest.mark.skip('Pending Implementation')
    def test_edit_host_with_ipaddress(self):
        """
        TODO: Add VCR when adding actual calls to checkmk

        `` should be passed to checkmk and return the get all hosts
        from GetCommands processor
        """
        block = self.parser.handle_command('edit my-host-name ipaddress')

        assert block == (
            'TODO: Edit Host name from CheckMk my-host-name ipaddress')
