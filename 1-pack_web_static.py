#!/usr/bin/python3
"""Module documentation"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """do_pack function"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    local(f"tar -czvf versions/web_static_{date}.tar.gz web_static")

