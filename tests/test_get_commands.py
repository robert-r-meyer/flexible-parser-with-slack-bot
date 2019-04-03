from pytest_mock import mocker

from lighthouse.get_commands import GetCommands


class TestGetCommands():
    def setup(self):
        self.api = 'NOT THE ACTUAL API INTERFACE'
        self.parser = GetCommands(self.api)

    def test_ping(self):
        assert self.parser._ping(
        ) == "This is a journey into Check Mk's get API commands."

    def test_calling_ping(self):
        assert self.parser.handle_command(
            'ping') == "This is a journey into Check Mk's get API commands."

    def test_command_block(self):
        assert [*self.parser._commands] == [
            'ping', 'help', 'all', 'host', 'services', 'alerts'
        ]
