from lighthouse.check_mk_command import CheckMkCommand
from lighthouse.command import Command


class MasterControlProgram(Command):
    def __init__(self):
        super().__init__()
        self._user = None
        self._commands.update({"cmk": CheckMkCommand()})
        self._check = "End of Line."
        self._command_name = "Lighthouse"

    def handle_user_command(self, user, command="help"):
        """
        MCP handles user naming.
        Takes other commands and passes them to the correct Command controller
        appends results and returns.

        All other functionality is handled by Command's `handle_command` method
        """

        self.user = user
        response = self.handle_command(command)

        return "\n".join([self.user, response])

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        if not self._user:
            self._user = "<@" + user + ">: "
