#!/usr/bin/python3
"""
This module contains a Fabric script that deletes out-of-date archives
using the do_clean function.
"""

from fabric.api import *
from fabric.contrib.files import exists
from datetime import datetime


env.hosts = ['100.26.157.96', '54.160.71.55']
env.user = 'ubuntu'
env.key_filename = 'https://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@github.com/Muth80/alx-system_engineering-devops.git'


def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Args:
        number: The number of archives to keep (including the most recent).

    Returns:
        Nothing.
    """
    number = int(number)
    if number < 2:
        number = 1
    else:
        number += 1

    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs rm -rf --'.format(number))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf --'.format(number))


def deploy():
    """
    Creates and distributes an archive to web servers.

    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

