import re

from twisted.words.protocols import irc
from twisted.internet import protocol, reactor

class Commander(irc.IRCClient):

    # Our commands will be stored in this array
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
        """This function is called when a message is sent to the bot or to a
        channel the bot is in"""

        print user, msg

        # Filter non user messages
        if not user:
            return


        directed = msg.startswith(self.nickname)
        # This regex extracts the target of a message, and the message itself,
        # where the target may not be there.
        target, msg = re.match(
            r'^(?:([a-z_\-\[\]\\^{}|`][a-z0-9_\-\[\]\\^{}|`]*)[:,] )? *(.*)$',
            msg).groups()

        # Split a users nickname and irc mask
        user, mask = user.split('!', 1)

        comm = {
            'user': user,
            'mask': mask,
            'target': target,
            'message': msg,
            'channel': channel,
        }

        # Go through each registered command and check if the command's regex
        # matches anything in our message.
        for cmd in Commander.commands:
            match = cmd.regex.match(msg)
            if match and (directed or (not cmd.onlyDirected)):
                # Store the captured values from a commands regex
                comm.update({'groups': match.groups()})
                # Pass all the values of comm to a command for use
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

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)


def registerCommand(Command):
    """Registers a command with the Commander.
       Use this as a decorator to your command."""

    options = re.I if not Command.caseSensitive else None
    Command.regex = re.compile(Command.regex, options)

    Commander.commands.append(Command())
    print 'Registered', Command

