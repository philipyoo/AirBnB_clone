#!/usr/bin/python3
import cmd


class ConsoleShell(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, args):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, args):
        """Ctrl + D to exit program"""
        print("")
        return True

if __name__ == '__main__':
    ConsoleShell().cmdloop()
