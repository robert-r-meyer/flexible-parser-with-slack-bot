from lighthouse.command import Command


class SimpleCommand(Command):
    def __init__(self):
        super().__init__()

        # Set the response of the Command parser to `ping`
        self._check = 'Simple Command Parser Response'

        # Set the command's response name
        self._command_name = 'Simple Commands'

        # Add a simple command
        self._commands.update({'biggs': self.biggs_name})

    def biggs_name(self):
        """
        This returns nested array of comments in csv
        """
        return (['one', 'hello', 'world'],['two', 'three', 'four'])
