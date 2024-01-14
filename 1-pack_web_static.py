#!/usr/bin/python3
"""Module documentation"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """do_pack function"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{date}"
    local("mkdir -p versions")
    arch = local(f"tar -czvf {archive_path}.tgz web_static")
    if arch.failed:
        return None
    else:
        return archive_path
