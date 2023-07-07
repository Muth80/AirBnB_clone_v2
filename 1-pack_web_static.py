#!/usr/bin/python3
"""
This module contains a Fabric script that generates a .tgz archive
from the contents of the web_static folder.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        The path of the archive if it was successfully generated, None otherwise.
    """
    local("mkdir -p versions")
    now = datetime.now()
    file_name = "web_static_{}.tgz".format(
        now.strftime("%Y%m%d%H%M%S")
    )
    try:
        local("tar -czvf versions/{} web_static".format(file_name))
        return "versions/{}".format(file_name)
    except Exception:
        return None
`
