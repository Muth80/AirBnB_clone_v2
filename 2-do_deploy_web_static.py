#!/usr/bin/python3
"""
This module contains a Fabric script that distributes an archive to
web servers using the do_deploy function.
"""

from fabric.api import *
from os.path import exists


env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'


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

        print('New version deployed!')
        return True
    except Exception:
        return False

