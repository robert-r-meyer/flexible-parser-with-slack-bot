from examples.simple_command.simple_command import SimpleCommand


class TestCommandBase():
    def setup(self):
        self.parser = SimpleCommand()

    def test_ping(self):
        """
        Make sure that the underlying code responds with the _check values
        """
        assert self.parser._ping() == "Simple Command Parser Response"

    def test_command_block(self):
        """
        Makes sure that the commands we expect are returned in the commands
        """
        assert self.parser._commands.keys(), ['ping', 'help', 'biggs']

    def test_help(self):
        """
        Checking the values returned by asking for help or error
        """
        block = self.parser._help()
        completed_block = '\r\n'.join([
            "Currently Simple Commands supports the following commands:",
            "ping", "help", 'biggs'
        ])

        assert block == completed_block

    def test_handle_command(self):
        """
        Validate that the commands passed into the system are handled by
        command components
        """
        block = self.parser.handle_command('ping')
        expected_block = 'Simple Command Parser Response'
        assert block == expected_block

    def test_handle_command_help(self):
        """
        Verifying that the use of bad commands causes the help block
        to be returned with the list of commands
        """
        block = self.parser.handle_command('stay on course')

        for check in ['Currently', 'ping', 'help']:
            assert check in block

    def test_get_biggs_name(self):
        """
        When calling the handle command, with the arguments of biggs,
        i should get a value
        """

        block = self.parser.handle_command('biggs')
        expected_block = 'Darklighter'
        assert block == expected_block


        


