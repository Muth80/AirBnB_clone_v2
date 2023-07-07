#!/usr/bin/python3
"""
This module contains a Fabric script that creates and distributes an
archive to web servers using the deploy function.
"""

from fabric.api import *
from fabric.contrib.files import exists
from datetime import datetime


env.hosts = ['100.26.157.96', '54.160.71.55']
env.user = 'ubuntu'
env.key_filename = 'https://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@github.com/Muth80/alx-system_engineering-devops.git'


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


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path: The path of the archive to deploy.

    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        file_no_ext = file_name.split('.')[0]
        path_no_ext = '/data/web_static/releases/{}'.format(file_no_ext)

        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Uncompress the archive to /data/web_static/releases/ directory
        run('mkdir -p {}'.format(path_no_ext))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, path_no_ext))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(file_name))

        # Move files from web_static/ to the new path
        run('mv {}/web_static/* {}'.format(path_no_ext, path_no_ext))

        # Delete the web_static/ folder
        run('rm -rf {}/web_static'.format(path_no_ext))

        # Delete the existing symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(path_no_ext))

        return True
    except Exception:
        return False


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

