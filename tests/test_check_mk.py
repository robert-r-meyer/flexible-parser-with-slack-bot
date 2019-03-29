from lighthouse.check_mk_command import CheckMkCommand


class TestCommandCheckMk():
    def setup(self):
        self.parser = CheckMkCommand()

    def test_ping(self):
        assert self.parser._ping() == "This is a journey into Check Mk."

    def test_command_block(self):
        assert self.parser._commands.keys(), ['ping', 'help']

    def test_help(self):
        block = self.parser._help()

        completed_block = '\r\n'.join([
            "Currently %s supports the following commands:" %
            self.parser._command_name, "ping", "help", "get", "host", "downtime",
        ])

        assert block == completed_block

    def test_handle_command(self):
        block = self.parser.handle_command('ping')
        expected_block = 'This is a journey into Check Mk.'
        assert block == expected_block

    def test_handle_command_help(self):
        """
        Verifying that the use of bad commands causes the help block
        to be returned with the list of commands
        """

        block = self.parser.handle_command('stay on course')

        for check in ['Currently', 'ping', 'help']:
            assert check in block

    def test_no_arguments(self):
        """
        Verifying that the use of top level without
        arguments causes the help block
        """
        block = self.parser.handle_command('')

        for check in ['Currently', 'ping', 'help']:
            assert check in block
