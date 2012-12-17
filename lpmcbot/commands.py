import random

from lpmcbot.commander import registerCommand


class Command(object):
    """The base command class. All commands should subclass this."""

    onlyDirected = True
    caseSensitive = False
    regex = ''

    def __call__(self, commander, options):
        pass

@registerCommand
class FriendlyCommand(Command):

    regex = 'hello|hi|hey'

    def __init__(self):
        self.greetings = ['Hello', 'Hi', 'Hey']

    def __call__(self, commander, options):
        commander.say('{0} {1[user]}'
            .format(random.choice(self.greetings), options))
