#!/usr/bin/python3
"""
Unittests for the console module.
"""
import unittest
import sys
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    def setUp(self):
        """Redirect stdout."""
        sys.stdout = StringIO()

    def tearDown(self):
        """Restore stdout."""
        sys.stdout = sys.__stdout__

    def test_create(self):
        """Test the create command."""
        console = HBNBCommand()

        # Test create with valid arguments
        console.onecmd('create BaseModel')
        output = sys.stdout.getvalue().strip()
        self.assertTrue(output)

        # Test create with invalid class name
        console.onecmd('create InvalidClass')
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

        # Test create with invalid arguments
        console.onecmd('create BaseModel invalid_arg')
        output = sys.stdout.getvalue().strip()
        self.assertFalse(output)

        # Test create with different data types
        console.onecmd('create BaseModel name="Test Name" value=10.5 count=3')
        output = sys.stdout.getvalue().strip()
        self.assertTrue(output)

    def test_quit(self):
        """Test the quit command."""
        console = HBNBCommand()

        self.assertTrue(console.onecmd('quit'))

    def test_EOF(self):
        """Test the EOF command."""
        console = HBNBCommand()

        self.assertTrue(console.onecmd('EOF'))


if __name__ == '__main__':
    unittest.main()

