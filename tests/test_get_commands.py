from lighthouse.get_commands import GetCommands


class TestGetCommands():
    def setup(self):
        self.parser = GetCommands()

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

    # # @pytest.mark.vcr()
    # def test_add_host_with_folder(self):
    #     """
    #     TODO: Add VCR when adding actual calls to checkmk

    #     `host add my-host folder-name`
    #     should be passed to checkmk and return successfully
    #     """
    #     block = self.parser.handle_command('add my-host folder-name')
    #     assert block == 'TODO: Add Host name from CheckMk my-host folder-name'

    # # @pytest.mark.vcr()
    # def test_edit_host_with_ipaddress(self):
    #     """
    #     TODO: Add VCR when adding actual calls to checkmk

    #     `` should be passed to checkmk and return the get all hosts
    #     from GetCommands processor
    #     """
    #     block = self.parser.handle_command('edit my-host-name ipaddress')

    #     assert block == (
    #         'TODO: Edit Host name from CheckMk my-host-name ipaddress')
