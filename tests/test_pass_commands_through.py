import json

import pytest

from lighthouse.format import FormatFor
from lighthouse.master_control_program import MasterControlProgram


class TestCommandPassing():
    def setup(self):
        self.parser = MasterControlProgram()

    def test_ping(self):
        assert self.parser._ping() == "End of Line."

    def test_calling_ping(self):
        assert self.parser.handle_command('ping') == 'End of Line.'

    def test_command_block(self):
        assert [*self.parser._commands] == ['ping', 'help', 'cmk']

    def test_pass_through(self):
        response = self.parser.handle_command('cmk ping')
        assert response == 'This is a journey into Check Mk.'

    def test_pass_through_nope(self):
        """
        Pass Check MK command subcommands to CheckMkCommand processor
        nope should be passed to checkmk and return help block
        """
        block = self.parser.handle_command('cmk nope')

        completed_block = '\r\n'.join([
            "Sorry I don't understand the command: `nope`. " +
            "No arguments were passed. " +
            "Currently Check Mk supports the following commands:",
            "ping",
            "help",
            "get",
            "host",
            "downtime",
        ])

        assert block == completed_block

        # assert set(block.split(' ')) - set(completed_block.split(' ')) == set(
        # [])

    def test_pass_through_ping(self):
        """
        Pass Check MK command subcommands to CheckMkCommand processor
        `ping` should be passed to checkmk and return the ping result
        """
        block = self.parser.handle_command('cmk ping')

        assert block == 'This is a journey into Check Mk.'

    @pytest.mark.vcr()
    def test_pass_through_get_all(self):
        """
        Pass Check MK command subcommands to CheckMkCommand processor
        `get all` should be passed to checkmk and return the get all hosts
        from GetCommands processor
        """
        block = self.parser.handle_command('cmk get all')

        expected = {
            "gewrjd1dv": {
                "attributes": {},
                "hostname": "gewrjd1dv",
                "path": "tests"
            },
            "gewrpp1dv": {
                "attributes": {},
                "hostname": "gewrpp1dv",
                "path": "tests"
            }
        }

        formated_block = FormatFor.slack_json_as_code_blob(expected)
        assert block == formated_block

    @pytest.mark.vcr()
    def test_pass_through_get_host(self):
        """
        Pass Check MK command subcommands to CheckMkCommand processor
        `get all` should be passed to checkmk and return the get all hosts
        from GetCommands processor
        """
        block = self.parser.handle_command('cmk get host my-host')

        assert block == 'Check_MK exception: No such host'
