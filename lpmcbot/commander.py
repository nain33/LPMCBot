import re

from twisted.words.protocols import irc
from twisted.internet import protocol, reactor

class Commander(irc.IRCClient):

    commands = []

    @property
    def nickname(self):
        return self.factory.nickname

    def signedOn(self):
        self.join(self.factory.channel)
        print "Signed on as %s." % (self.nickname,)

    def joined(self, channel):
        print "Joined %s." % (channel,)

    def privmsg(self, user, channel, msg):

        print user, msg

        # Filter non user messages
        if not user:
            return


        directed = msg.startswith(self.nickname)
        target, msg = re.match(
            r'^(?:([a-z_\-\[\]\\^{}|`][a-z0-9_\-\[\]\\^{}|`]*)[:,] )? *(.*)$',
            msg).groups()

        user, mask = user.split('!', 1)

        comm = {
            'user': user,
            'mask': mask,
            'target': target,
            'message': msg,
            'channel': channel,
        }

        for cmd in Commander.commands:
            match = cmd.regex.match(msg)
            if match and (directed or (not cmd.onlyDirected)):
                comm.update({'groups': match.groups()})
                cmd(self, comm)

    def connectionLost(self, reason):
        reactor.stop()

    def say(self, msg):
        self.msg(self.factory.channel, msg)


class CommanderFactory(protocol.ClientFactory):
    protocol = Commander

    def __init__(self, channel, nickname='LPMCBot'):
        self.channel = channel
        self.nickname = nickname

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s). Reconnecting" % (reason,)
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)


def registerCommand(Command):
    """Registers a command with the Commander.
       Use this as a decorator to your command."""

    options = re.I if not Command.caseSensitive else None
    Command.regex = re.compile(Command.regex, options)

    Commander.commands.append(Command())
    print 'Registered', Command

