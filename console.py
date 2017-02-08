#!/usr/bin/python3
import cmd
from models import *


class ConsoleShell(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, args):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, args):
        """Ctrl + D to exit program"""
        print("")
        return True

    def do_create(self, args):
        """Create a new Basemodel"""
        if len(args) <= 1:
            print("Usage: create BaseModel")

    def do_show(self, args):
        pass


if __name__ == '__main__':
    ConsoleShell().cmdloop()
