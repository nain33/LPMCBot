from twisted.words.protocols import irc
from twisted.internet import protocol, reactor

class LPMCBot(irc.IRCClient):

    @property
    def nickname(self):
        return self.factory.nickname

    def signedOn(self):
        self.join(self.factory.channel)

    def joined(self, channel):
        print "Joined %s." % (channel,)

    def privmsg(self, user, channel, msg):
        print msg

class LPMCBotFactory(protocol.ClientFactory):
    protocol = LPMCBot

    def __init__(self, channel, nickname='LPMCBot'):
        self.channel = channel
        self.nickname = nickname

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s)." % (reason,)

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)


if __name__ == '__main__':
    reactor.connectTCP('irc.freenode.net', 6667, LPMCBotFactory('#lpmc'))
    reactor.run()

