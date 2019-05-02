from lighthouse.command import Command
import pytest
import os

from lighthouse.format import FormatFor


class TestCommandBase:
    def setup(self):
        self.parser = Command()

    def test_ping(self):
        assert self.parser._ping() == "This is a journey into sound."

    def test_command_block(self):
        assert self.parser._commands.keys(), ["ping", "help"]

    def test_help(self):
        block = self.parser._help()
        completed_block = "\r\n".join(
            ["Currently Command supports the following commands:", "ping", "help"]
        )

        assert block == completed_block

    def test_handle_command(self):
        block = self.parser.handle_command("ping")
        expected_block = "This is a journey into sound."
        assert block == expected_block

    def test_handle_command_help(self):
        """
        Verifying that the use of bad commands causes the help block
        to be returned with the list of commands
        """
        block = self.parser.handle_command("stay on course")

        for check in ["Currently", "ping", "help"]:
            assert check in block

    @pytest.mark.skip("Unknown attempt to test not sure")
    def test_csv_configuration(self, mocker):
        expected = []

        get_host = mocker.patch.object(
            os, "get_host", autospec=True, return_value=expected
        )

        block = self.parser.handle_command("cmk get host my-host")
        formatted_block = FormatFor.slack_json_as_code_blob(expected)
        assert block == formatted_block
        get_host.assert_called_once()
