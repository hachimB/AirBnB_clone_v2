#!/usr/bin/python3
"""Module documentation"""
from fabric.api import local, run, put, env
from datetime import datetime
import os


env.hosts = ['100.25.200.71', '54.160.97.207']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """do_deploy function"""
    if not os.path.exists(archive_path):
        return False
    try:
        archive_name = os.path.basename(archive_path)
        archive_name_without_ext = os.path.splitext(archive_name)[0]
        put(archive_path, "/tmp/{}".format(archive_name))
        run("mkdir -p /data/web_static/releases/{}".format
            (archive_name_without_ext))
        run("tar -xvf /tmp/{} -C /data/web_static/releases/{}".format
            (archive_name, archive_name_without_ext))
        run("rm  /tmp/{}".format(archive_name))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{} /data/web_static/current"
            .format(archive_name_without_ext))
        return True
    except Exception as e:
        return False
