from examples.nested_commands.nested_commands import FirstLevel


class TestCommandBase():
    def setup(self):
        self.parser = FirstLevel()

    def test_ping(self):
        """
        Make sure that the underlying code responds with the _check values
        """
        assert self.parser._ping() == "First Level Ping"

    def test_command_block(self):
        """
        Makes sure that the commands we expect are returned in the commands
        """
        assert self.parser._commands.keys(), [
            'ping', 'help', 'second', 'biggs'
        ]

    def test_help(self):
        """
        Checking the values returned by asking for help or error
        """
        block = self.parser._help()
        completed_block = '\r\n'.join([
            "Currently First Level Commands supports the following commands:",
            'ping', 'help', 'second', 'biggs'
        ])

        assert block == completed_block

    def test_handle_command(self):
        """
        Validate that the commands passed into the system are handled by
        command components
        """
        block = self.parser.handle_command('ping')
        expected_block = 'First Level Ping'
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


class TestNestedCommands():
    def setup(self):
        self.parser = FirstLevel()

    def test_handle_command(self):
        """
        Validate that the commands passed into the system are handled by
        command components
        """
        block = self.parser.handle_command('biggs')
        expected_block = 'Darklighter'
        assert block == expected_block

    def test_handle_command_help(self):
        """
        Verifying that the use of bad commands causes the help block
        to be returned with the list of commands
        """
        block = self.parser.handle_command('second not a command')

        for check in ['Currently', 'ping', 'help']:
            assert check in block

    def test_get_biggs_name(self):
        """
        When calling the handle command, with the arguments of second luke,
        i should get a value
        """

        block = self.parser.handle_command('second Luke')
        expected_block = 'Skywalker'
        assert block == expected_block
