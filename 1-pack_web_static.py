#!/usr/bin/python3
"""Module documentation"""
from fabric.api import local, task
from datetime import datetime


@task
def do_pack(c):
    """do_pack function"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = c.local(f"tar -czvf web_static_{date}.tar.gz web_static")
    c.local("mkdir -p versions")
    c.local(f"mv web_static_{date}.tar.gz versions")
    if archive.ok:
        return f"versions/web_static_{date}.tar.gz"
    else:
        return None
