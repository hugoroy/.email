#!/usr/bin/python
# executes gnome-keyring-query get passwd
# and returns the output
import locale
from subprocess import Popen, PIPE
encoding = locale.getdefaultlocale()[1]
def get_password(p):
    (out, err) = Popen(["gnome-keyring-query", "get", p], stdout=PIPE).communicate()
    return out.decode(encoding).strip()
