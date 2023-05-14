#!/usr/bin/python3
"""HBNBCommand class testing modu;e"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class Test_Console(unittest.TestCase):
    """Testing the HBNBCommand Console"""
    def test_help(self):
        """Testing the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update\n
"""

        self.assertEqual(s, f.getvalue())
    # Test cases for quit

    def test_do_quit(self):
        """Testing the quit commmand"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        # modelling what happens when someone types `quit`
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        # modelling when user types `quit anything`
        msg = f.getvalue()

        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    # Test cases for EOF
    def test_do_EOF(self):

        """Testing the EOF commmand"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        # modelling what happens when user types `quit`
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
        # modelling when user types `EOF anything`

        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)

        self.assertEqual("\n", msg)
    # Test cases for emptyline
    def test_do_emptyline(self):

        """Testing the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        # modelling what happens when user doesn't type anything
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                     \n")

        # modelling when user types lots of whitespaces & enter
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    # Test cases for do_all
    def test_do_all(self):


        """Testing the do_all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
if __name__ == "__main__":
    unittest.main()
