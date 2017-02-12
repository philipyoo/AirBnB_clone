import unittest, sys, io
from contextlib import contextmanager
from models import *
from datetime import datetime
from console import ConsoleShell

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class Test_Console(unittest.TestCase):
    """
    Test the console
    """

    def setUp(self):
        self.cli = ConsoleShell()

        test_args = {'updated_at': datetime(2017, 2, 11, 23, 48, 34, 339879),
                     'id': 'd3da85f2-499c-43cb-b33d-3d7935bc808c',
                     'created_at': datetime(2017, 2, 11, 23, 48, 34, 339743)}
        self.model = BaseModel(test_args)

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.cli.do_quit(self.cli)

    def test_show_correct(self):
        with captured_output() as (out, err):
            self.cli.do_show("BaseModel d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertFalse("2017-2-11 23:48:34.339879" in output)
        self.assertTrue('2017-02-11 23:48:34.339743' in output)

    def test_show_error_no_args(self):
        with captured_output() as (out, err):
            self.cli.do_show('')
        output = out.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_show_error_missing_arg(self):
        with captured_output() as (out, err):
            self.cli.do_show("BaseModel")
        output = out.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_create(self):
        with captured_output() as (out, err):
            self.cli.do_create('')
        output = out.getvalue().strip()
        self.assertEqual(output, "Usage: create BaseModel")

        with captured_output() as (out, err):
            self.cli.do_create("BaseModel")
        output = out.getvalue().strip()

        with captured_output() as (out, err):
            self.cli.do_show("BaseModel {}".format(output))
        output2 = out.getvalue().strip()
        self.assertTrue(output in output2)




if __name__ == "__main__":
    unittest.main()
