#!/usr/bin/python3
# 1-pack_web_static.py
"""
Fabfile to generates a .tgz archive from the contents of web_static
"""
from fabric.operations import local
from datetime import datetime as d


def do_pack():
    """ generates a .tgz archive """
    name = "versions/web_static_" + str(d.now().year)
    name += str(d.now().month) + str(d.now().day) + str(d.now().hour)
    name += str(d.now().minute) + str(d.now().second) + ".tgz"
    a = local("mkdir -p versions; tar -cvzf \"{}\" web_static".format(name))

    if a.failed:
        return None
    else:
        return name
