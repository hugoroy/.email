
My mail user agent is [Astroid](http://github.com/astroidmail/astroid).

Behind the scenes, my email set up:

I use [offlineimap](http://www.offlineimap.org/) to sync with my email
server (running [Kolab](http://kolab.org)). My email is then indexed
with [Notmuch](http://notmuchmail.org/). Notmuch allows to tag and
search emails (among many other useful things).  I also use
[Afew](https://github.com/teythoon/afew/), which helps by bringing
some automation in email tagging (e.g. automatically tagging lists
accordingly, learning to tag email over time which is useful to fight
spam, etc.).


# Overview

    afew/	This is a tools that helps with automated 
    └─ config   tagging of emails. 

    astroid/	This is my mail user agent configuration (as a Git submodule)
    ├─ config           See https://github.com/hugoroy/.astroid
    ├─ hooks/		This is where I store astroid scripts.
    |  └─ (+x) toggle
    ├─ keybindings	This is where I customize the astroid keybindings.
    ├─ (+x) poll.sh	This script syncs imap and tags incoming email.
    ├─ searches		This is where astroid stores saved queries and search history (not in a Git repo, obviously).
    └─ ui		This is a symlink to the "ui/" directory in my customised UI branch of astroid (See <https://github.com/hugoroy/astroid/tree/ui>).

    imap/	This is where I store my synced-imap maildirs (not in this Git repo)
    ├─ ampoliros
    |	└─ ...
    └─ archives/
	└─ ...

    netrc	This is where I store login info (not in this Git repo, obviously), see
    		https://www.gnu.org/software/inetutils/manual/html_node/The-_002enetrc-file.html

		I created a symlink from ~/.netrc

    notmuch/
    ├─ hooks/		I no longer use notmuch hooks. See `astroid/poll.sh`.
    └─ notmuch-config
    
    offlineimap/
    ├─ (+x) gnome-keyring-query.py
    └─ offlineimaprc

    signatures/	This is where I store my plain-text email signatures.
    ├─ perso.signature
    └─ etc.signature
