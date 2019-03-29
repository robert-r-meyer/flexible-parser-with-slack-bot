from lighthouse.command import Command


class TestCommandBase():
    def setup(self):
        self.parser = Command()

    def test_ping(self):
        assert self.parser._ping() == "This is a journey into sound."

    def test_command_block(self):
        assert self.parser._commands.keys(), ['ping', 'help']

    def test_help(self):
        block = self.parser._help()
        completed_block = '\r\n'.join([
            "Currently Command supports the following commands:",
            "ping",
            "help",
        ])

        assert block == completed_block

    def test_handle_command(self):
        block = self.parser.handle_command('ping')
        expected_block = 'This is a journey into sound.'
        assert block == expected_block

    def test_handle_command_help(self):
        """
        Verifying that the use of bad commands causes the help block
        to be returned with the list of commands
        """
        block = self.parser.handle_command('stay on course')

        for check in ['Currently', 'ping', 'help']:
            assert check in block
