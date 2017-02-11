import unittest, sys
from unittest import mock
from models import *
from console import ConsoleShell

class Test_Console(unittest.TestCase):
    """
    Test the console
    """

    def setUp(self):
        self.cli = ConsoleShell()

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.cli.do_quit(self.cli)

if __name__ == "__main__":
    unittest.main()
