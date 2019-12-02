import logging
from inspect import getfullargspec, signature
from configs.config_loader import ConfigLoader

import yaml

from lighthouse.format import FormatFor

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.WARN)

# import pudb
"""
Top level module using command in order to
parse and call to sub modules
"""


class Command:
    """
    Takes commands and calls correct sub parsers
    """

    def __init__(self):
        variables = ConfigLoader("../config.yml")

        self._commands = {"ping": self._ping, "help": self._help}
        self._check = "This is a journey into sound."
        self.response = None
        self._command_name = "Command"
        self._config = variables.config
        self._csv_formatted_methods = self.__load_csv_formats()

    def __load_csv_formats(self):
        key = "FUNCTION_RETURN_FORMAT"

        if key in self._config.keys():
            return self._config[key]

        return {}

    def __get_number_of_required_arguments(self, exec_command):
        command_args = getfullargspec(exec_command)
        arg_defaults = command_args.defaults
        all_args = command_args.args

        if not all_args:
            all_args = []

        if not arg_defaults:
            arg_defaults = []

        return len(all_args) - len(arg_defaults)

    def __get_parsed_arguments(self, commands):
        commands = " ".join(commands)
        quoted_arguments = commands.partition('"')[2].partition('"')[0]
        command_args = commands.replace('"' + quoted_arguments + '"', "")
        cleaned_commands = command_args.split(" ")

        if quoted_arguments:
            cleaned_commands.append(quoted_arguments)

        cleaned_commands = list(filter(None, cleaned_commands))

        return cleaned_commands

    def __commandsNotFound(self, primary_command, string_parsed_commands):
        # This isn't a subparser,
        # and we didn't find a command with the correct number of arguments
        # so we will show the help text and return out of the command handler
        results = " ".join(
            [
                "Sorry I don't understand the command: `%s`." % primary_command,
                self.__help_text_args(string_parsed_commands),
                self._help(),
            ]
        )

        logging.debug(results)

        return results

    def __help_text_args(self, args):
        logging.debug("args", *args)

        if not (" ").join(args).strip():
            return "No arguments were passed."

        return (" ").join(["with the args of: ", "`", *args, "`"])

    def _ping(self):
        return self._check

    def _help(self):
        """
        Blank response of help concatenating currently supported commands
        """

        response = "Currently %s supports the following commands:" % self._command_name

        return "\r\n".join([response] + [*self._commands])

    def safe_call(self, function, *args):
        """
        Safe call allows for command bases to ensure that the call 
        they make will not return an error.

        This also allows for handling of csv or json results
        """
        try:
            blob = function(args)

            if function.__name__ in self._csv_formatted_methods:
                return FormatFor.slack_csv_blob(blob)

            return FormatFor.slack_json_as_code_blob(blob)
        except Exception as inst:
            return inst

    def handle_command(self, command="help"):
        """
        Entry point to commands
        """

        # Grab primary command request
        # Stash rest of arguments for future use
        pass_through_commands = command.split(" ")
        primary_command = pass_through_commands.pop(0)

        parsed_arguments = self.__get_parsed_arguments(pass_through_commands)

        logging.debug("Primary Command %s", primary_command)
        logging.debug("Pass through commands %s", parsed_arguments)

        # Check if the command asked for is in the list of commands we know

        if primary_command not in self._commands:
            return self.__commandsNotFound(primary_command, parsed_arguments)

        # Set executed commands
        exec_command = self._commands[primary_command]

        # Verify that the exec_command here is a method.
        # if it is a method, check for arg length to match

        if hasattr(exec_command, "handle_command"):
            logging.debug("recursive call to handle command %s", primary_command)
            # this is a secondary command parser in its own right.
            # In this case, call the handle command method and start all
            # this again on its own parser.

            return self._commands[primary_command].handle_command(
                " ".join(pass_through_commands)
            )

        # Inspect the method and determine the number of arguments
        # the method takes

        calling_signature = len(parsed_arguments)
        method_signature = len(signature(exec_command).parameters)
        required_signature = self.__get_number_of_required_arguments(exec_command)

        # if there are no additional arguments passed,
        # execute the command and return the result

        if not parsed_arguments and method_signature == 0:
            logging.debug("No pass through, execute directly %s", primary_command)

            if callable(exec_command):
                return exec_command()

        if method_signature == calling_signature:
            # additional arguments passed to the command, execute the
            # command with those arguments
            logging.debug("cleaned commands match command sig %s", parsed_arguments)

            return exec_command(*parsed_arguments)

        # check to see if the number of required arguments is
        # less than or equal to the number of arguments sent for the command.

        if required_signature <= calling_signature:
            # additional arguments passed to the command, execute the
            # command with those arguments
            logging.debug("cleaned commands match command sig %s", parsed_arguments)

            return exec_command(*parsed_arguments)

        return self.__commandsNotFound(primary_command, parsed_arguments)
