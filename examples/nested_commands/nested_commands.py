from lighthouse.command import Command


class FirstLevel(Command):
    def __init__(self):
        super().__init__()

        # Set the response of the parser to `ping`
        self._check = 'First Level Ping'

        # Set the command's response name
        self._command_name = 'First Level Commands'

        # Add additional command Parsers
        self._commands.update({
            'second': SecondLevel(),
            'biggs': self.biggs_name
        })

    def biggs_name(self):
        return 'Darklighter'


class SecondLevel(Command):
    def __init__(self):
        super().__init__()

        # Set the response of the parser to `ping`
        self._check = 'Second Level Ping'

        # Set the command's response name
        self._command_name = 'Second Level Commands'

        # Adding a command in the second level command handler
        self._commands.update({'Luke': self.luke_name})

    def luke_name(self):
        return 'Skywalker'
