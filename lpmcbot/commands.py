from lpmcbot.commander import registerCommand


class Command(object):

    onlyDirected = True
    caseSensitive = False
    regex = ''

    def __call__(self, commander, options):
        pass

@registerCommand
class FriendlyCommand(Command):

    regex = 'hello'

    def __call__(self, commander, options):
        commander.say('Hello {0[user]}'.format(options))
