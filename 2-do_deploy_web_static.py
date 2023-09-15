#!/usr/bin/python3
# 2-do_deploy_web_static.py
""" a Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy:
"""

from fabric.api import *
from datetime import datetime
from os.path import exists


# Execute remote commands on both servers
env.hosts = ['54.87.239.146', '100.25.46.30']  # <IP web-01>, <IP web-02>


def do_deploy(archive_path):
    """ distributes an archive to my web servers
    """
    if exists(archive_path) is False:
        return False  # Returns False if the file at archive_path doesnt exist
    filename = archive_path.split('/')[-1]
    # filename is <web_static_202391421957.tgz>
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    # no_tgz is </data/web_static/releases/web_static_202391421957>
    tmp = "/tmp/" + filename
    # tmp is </tmp/web_static_202391421957.tgz

    try:
        put(archive_path, "/tmp/")
        # ^ Upload the archive to the /tmp/ directory of the web server
        run("mkdir -p {}/".format(no_tgz))
        # Uncompress the archive to the folder /data/web_static/releases/
        # <archive filename without extension> on the web server
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        # ^ Delete the archive from the web server
        run("rm -rf /data/web_static/current")
        # Delete the symbolic link /data/web_static/current from the web server
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        # Create a new the symbolic link /data/web_static/current on the
        # web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        return True
    except:
        return False
