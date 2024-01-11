#!/usr/bin/python3
"""Module documentation"""
from fabric.api import local, task
from datetime import datetime


@task
def do_pack():
    """do_pack function"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = local(f"tar -czvf web_static_{date}.tar.gz web_static")
    local("mkdir -p versions")
    local(f"mv web_static_{date}.tar.gz versions")
    if archive.failed:
        return None
    return f"versions/web_static_{date}.tar.gz"
