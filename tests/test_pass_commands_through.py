import json
from unittest.mock import MagicMock

import check_mk_web_api
import pytest

from lighthouse.format import FormatFor
from lighthouse.master_control_program import MasterControlProgram

# from pytest_mock import mocker


class TestCommandPassing:
    def setup(self):
        self.parser = MasterControlProgram()

    def test_ping(self):
        assert self.parser._ping() == "End of Line."

    def test_calling_ping(self):
        assert self.parser.handle_command("ping") == "End of Line."

    def test_command_block(self):
        assert [*self.parser._commands] == ["ping", "help", "cmk"]

    def test_pass_through(self):
        response = self.parser.handle_command("cmk ping")
        assert response == "This is a journey into Check Mk."

    def test_pass_through_nope(self):
        """
        Pass Check MK command subcommands to CheckMkCommand processor
        nope should be passed to checkmk and return help block
        """
        block = self.parser.handle_command("cmk nope")

        completed_block = "\r\n".join([
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

    def test_pass_through_ping(self):
        """
        Pass Check MK command subcommands to CheckMkCommand processor
        `ping` should be passed to checkmk and return the ping result
        """
        block = self.parser.handle_command("cmk ping")

        assert block == "This is a journey into Check Mk."

    def test_pass_through_get_all(self, mocker):
        """
        Pass Check MK command subcommands to CheckMkCommand processor
        `get all` should be passed to checkmk and return the get all hosts
        from GetCommands processor
        """

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
            },
        }

        get_all_hosts = mocker.patch.object(
            check_mk_web_api.web_api.WebApi,
            "get_all_hosts",
            autospec=True,
            return_value=expected,
        )

        block = self.parser.handle_command("cmk get all")
        formatted_block = FormatFor.slack_json_as_code_blob(expected)
        assert block == formatted_block

        # Assert parser calls to get all hosts on web api package
        get_all_hosts.assert_called_once()

    def test_pass_through_get_host(self, mocker):
        """
        Pass Check MK command subcommands to CheckMkCommand processor
        `get all` should be passed to checkmk and return the get all hosts
        from GetCommands processor
        """
        expected = {"expected": True}

        get_host = mocker.patch.object(
            check_mk_web_api.web_api.WebApi,
            "get_host",
            autospec=True,
            return_value=expected,
        )

        block = self.parser.handle_command("cmk get host my-host")
        formatted_block = FormatFor.slack_json_as_code_blob(expected)
        assert block == formatted_block
        get_host.assert_called_once()
