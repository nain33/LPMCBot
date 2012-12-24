LPMCBot
=======

LPMCBot is an IRC Bot designed to be easy for new programmers to get
involved in open source projects.

Recently LPMCBot was re-written by [Chance](http://github.com/ecnahc515/) using
[Twisted][twisted]. If you have questions please join
our [IRC channel][irc] on freenode: [#lpmc][irc].

Things LPMCBot aims to be
----
- A learning platform.
- A project with the ability to grow.
- Something fun.

Things LPMCBot doesn't aim to be
----
- An ultra irc bot that will order you pizza.
- Something new.
- Perfect.

The goal with LPMCBot is to allow anyone to get involved with a project and
learn important new skills such as working with revision control systems such
as git, and how to contribute to a project using these tools.

Setup
----
Set up for LPMCBot is fairly easy. The only dependencies are Python 2.7+ and
[Twisted][twisted]. Set up instructions will be with
[pip](http://pypi.python.org/pypi/pip). Pip is a python package installer and
if you do not already have it, it should be easily available through most
package managers.

For those that want to install dependencies inside the project instead of 
globally, you will need to install [virtualenv](http://pypi.python.org/pypi/virtualenv)

###Installation
After you have cloned/forked the repo, issue the following commands.

####Global install
```
cd LPMCBot/
pip install -r requirements.txt
cp config.py.dist config.py
python main.py
```
####Local install with virtualenv
```
cd LPMCBot/
virtualenv venv --distribute
source venv/bin/activate
pip install -r requirements.txt
cp config.py.dist config.py
python main.py
```
####Command line arguments at startup
LPMCBot also supports passing the channel and nick at startup which overrides the
default config file settings. For instance, to start the bot in channel #Test 
with nick TestBot, you would type
```
python main.py '#Test' 'Testbot'
```
 
You can tweak the settings in your config file as necessary. If you wish to add
additional configuration settings for a feature, simply add the field in
config.py.dist for when you wish to have the changes merged in.


How to Contribute
----
Contributing to [LPMCBot][repo] is easy.

1. [Fork](https://help.github.com/articles/fork-a-repo) the [bot][fork].
2. Make some [changes](http://git-scm.com/book/en/Git-Basics-Recording-Changes-to-the-Repository),
   and commit them.
3. Send a [pull request](https://help.github.com/articles/using-pull-requests)
   and someone will take a look at the code. If it looks good and ready to add
   to the main repo we'll merge it in.
4. Huzzah, your change is now a part of our project, and you've contributed to
   an open source project.

If you need help, please join our [IRC Channel][irc] on the freenode server: [#lpmc][irc]


[irc]: http://webchat.freenode.net/?channels=lpmc&uio=d4 "Freenode web chat"
[twisted]: http://twistedmatrix.com/trac/
[fork]: https://github.com/LearnProgramming/LPMCBot/fork_select
[repo]: https://github.com/LearnProgramming/LPMCBot

