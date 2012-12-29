import sys

from twisted.words.protocols import irc
from twisted.internet import protocol, reactor

from lpmcbot import commands
from lpmcbot.commander import CommanderFactory

try:
    from config import CONFIG
else ImportError:
    print "Config file not found."
    quit()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        chan = sys.argv[1]
    else:
        try:
            chan = CONFIG['channel']
        except KeyError:
            print "No channel present in config file!"
            quit()

    if len(sys.argv) > 2:
        nickname = sys.argv[2]
    else:
        try:
            nickname = CONFIG['nickname']
        except KeyError:
            print "No nickname present in config file!"
            quit()

    try:
        server = CONFIG['server']
    except KeyError:
        server = 'irc.freenode.net'

    try:
        port = int(CONFIG['port'])
    except KeyError:
        port = 6667

    reactor.connectTCP(server, port, CommanderFactory(chan, nickname))
    reactor.run()
