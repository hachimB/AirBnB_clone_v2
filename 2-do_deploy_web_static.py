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
        archive_name_without_ext = os.path.splitext(os.path.basename
                                                    (archive_path))[0]
        put(archive_path, "/tmp/{}".format(archive_name_without_ext))
        run("mkdir -p /data/web_static/releases/{}".format
            (archive_name_without_ext))
        run("tar -xvf /tmp/{} -C /data/web_static/releases/{}".format
            (archive_name_without_ext, archive_name_without_ext))
        run("rm -rf /tmp/{}".format(archive_name_without_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(archive_name_without_ext))
    except Exception as e:
        print(e)
        return False
    return True
