from lighthouse.master_control_program import MasterControlProgram


class TestCommandMasterControl():
    def setup(self):
        self.parser = MasterControlProgram()

    def test_ping(self):
        assert self.parser._ping() == "End of Line."

    def test_command_block(self):
        assert [*self.parser._commands], ['cmk', 'ping', 'help']

    def test_help(self):
        block = self.parser._help()
        completed_block = '\r\n'.join([
            "Currently %s supports the following commands:" %
            self.parser._command_name, "ping", "help", "cmk"
        ])

        assert block == completed_block

    def test_handle_command(self):
        block = self.parser.handle_command('ping')
        expected_block = 'End of Line.'
        assert block == expected_block

    def test_handle_command_help(self):
        """
        Verifying that the use of bad commands causes the help block
        to be returned with the list of commands
        """
        block = self.parser.handle_command('stay on course')

        for check in ['Currently', 'ping', 'help']:
            assert check in block

    def test_handler_user_command(self):
        block = self.parser.handle_user_command('Darkligther', 'ping')

        for check in ['Darkligther', 'End of Line']:
            assert check in block

    def test_handle_command_ping(self):
        block = self.parser.handle_command('ping')

        assert block == 'End of Line.'
