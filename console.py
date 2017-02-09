#!/usr/bin/python3
import cmd
from models import *


class ConsoleShell(cmd.Cmd):
    prompt = '(hbnb)'
    storage.reload()

    valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, args):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, args):
        """Ctrl + D to exit program"""
        print("")
        return True

    def do_create(self, args):
        """Create a new Basemodel"""
        args = args.split()
        if len(args) != 1:
            print("Usage: create BaseModel")
        else:
            if args[0] in valid_classes:
                new_obj = eval(args[0])()
                print(new_obj.id)
                new_obj.save()

    def do_show(self, args):
        """Usage: show BaseModel 1234-1234-1234"""
        args = args.split()
        if len(args) != 2:
            print("Usage: show BaseModel 1234-1234-1234")
            return
        all_objs = storage.all()
        for objs_id in all_objs.keys():
            if objs_id == args[1]:
                print(all_objs[objs_id])

    def do_destroy(self, args):
        """Usage: destroy BaseModel 1234-1234-1234"""
        args = args.split()
        if len(args) != 2:
            print("Usage: destroy BaseModel 1234-1234-1234")
            return
        all_objs = storage.all()
        for objs_id in all_objs.keys():
            if objs_id == args[1]:
                del all_objs[objs_id]
                break
        storage.save()

    def do_all(self, args):
        """Usage: all Basemodel or all"""
        if args[0] in valid_classes:
            all_objs = {k: v for k, v in d.items() if v["__class__"] is args[0]}
        else:
            all_objs = storage.all()

        for objs_id in all_objs.keys():
            print(all_objs[objs_id])

    def do_update(self, args):
        """Usage: update <class name> <id> <attribute name> <attribute value>"""
        args = args.split()
        if len(args) != 4:
            print("Usage: see help for update")
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if obj_id == args[1]:
                setattr(all_objs[obj_id], args[2], args[3])
        storage.save()

if __name__ == '__main__':
    ConsoleShell().cmdloop()
