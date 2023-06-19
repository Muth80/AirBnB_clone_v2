#!/usr/bin/python3
"""
This module contains the HBNBCommand class, which is the command
interpreter for the Airbnb project.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the Airbnb project.
    """
    
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'State': State, 'Place': Place}

    def do_create(self, arg):
        """
        Create a new instance of a specified class.

        Command syntax: create <Class name> <param 1> <param 2> <param 3>...
        Param syntax: <key name>=<value>
        Value syntax:
        - String: "<value>" => starts with a double quote
            - Any double quote inside the value must be escaped with a backslash \
            - All underscores _ must be replaced by spaces.
              Example: If you want to set the string My little house to the attribute name,
              your command line must be name="My_little_house"
        - Float: <unit>.<decimal> => contains a dot .
        - Integer: <number> => default case

        If any parameter doesn't fit with these requirements or can't be recognized correctly,
        it will be skipped.

        This feature is only tested with the FileStorage engine.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        kwargs = {}
        for arg in args[1:]:
            parts = arg.split('=')
            if len(parts) != 2:
                continue
            key, value = parts
            if value[0] == '"' and value[-1] == '"':
                value = value[1:-1].replace('_', ' ')
            try:
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)
            except ValueError:
                continue
            kwargs[key] = value

        new_instance = self.classes[class_name](**kwargs)
        new_instance.save()
        print(new_instance.id)

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

