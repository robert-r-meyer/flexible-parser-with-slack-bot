import logging
from inspect import signature

from lighthouse.format import FormatFor

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
        self._commands = {"ping": self._ping, "help": self._help}
        self._check = 'This is a journey into sound.'
        self.response = None
        self._command_name = 'Command'

    def handle_command(self, command='help'):
        """
        Entry point to commands
        """

        # Grab primary command request
        # Stash rest of arguments for future use
        pass_through_commands = command.split(' ')
        primary_command = pass_through_commands.pop(0)
        string_parsed_commands = (' ').join(pass_through_commands).split('\"')

        logging.debug('Primary Command %s' % primary_command)
        logging.debug('Pass through commands %s' % pass_through_commands)

        # Check if the command asked for is in the list of commands we know

        if primary_command in self._commands:
            exec_command = self._commands[primary_command]

            # if there are no additional arguments passed,
            # execute the command and return the result

            if not pass_through_commands:
                print('No pass through, execute directly')

                if callable(exec_command):
                    return exec_command()
                else:
                    pass_through_commands = ['help']

            # Verify that the exec_command here is a method.
            # if it is a method, check for arg length to match

            if hasattr(exec_command, 'handle_command'):
                # this is a secondary command parser in its own right.
                # In this case, call the handle command method and start all
                # this again on its own parser.

                return self._commands[primary_command].handle_command(
                    ' '.join(pass_through_commands))

            # Inspect the method and determine the number of arguments
            # the method takes

            method_signature = len(signature(exec_command).parameters)

            # if the method has the same number of arguments as the number of
            # additional arguments passed to the command, execute the
            # command with those arguments

            if method_signature == len(string_parsed_commands):
                logging.debug('pass through match command sig')
                logging.debug((' ').join(string_parsed_commands))

                return exec_command(*string_parsed_commands)

        # Otherwise, this isn't a subparser,
        # and we didn't find a command with the correct number of arguments
        # so we will show the help text and return out of the command handler

        return ' '.join([
            "Sorry I don't understand the command: `%s`." % primary_command,
            self.__help_text_args(string_parsed_commands),
            self._help()
        ])

    def __help_text_args(self, args):
        if not ' '.join(args).strip():
            return "No arguments were passed."

        return (' ').join(["with the args of: ", "`", *args, "`"])

    def _ping(self):
        return self._check

    def _help(self):
        """
        Blank response of help concatenating currently supported commands
        """

        response = ("Currently %s supports the following commands:" %
                    self._command_name)

        return "\r\n".join([response] + [*self._commands])

    def safe_call_as_json(self, function, *args):
        try:
            blob = function(args)

            return FormatFor.slack_json_as_code_blob(blob)
        except Exception as inst:
            return inst
