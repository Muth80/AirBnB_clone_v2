#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """

    # create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # format the current datetime to use in the filename of our archive
    now = datetime.now()
    date_string = now.strftime("%Y%m%d%H%M%S")
    output_file = "versions/web_static_{}.tgz".format(date_string)

    print("Packing web_static to {}".format(output_file))

    # use the tar command to create a .tgz archive
    local("tar -cvzf {} web_static".format(output_file))

    print("{} packed: {} -> {}Bytes".format("web_static",
                                            output_file,
                                            local("ls -lh {}".format(output_file))))

    return output_file
```
