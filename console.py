#!/usr/bin/python3
import cmd
from models import *


class ConsoleShell(cmd.Cmd):
    prompt = '(hbnb)'
    storage.reload()

    valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def emptyline(self):
        pass

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
            print(args)
            print("Usage: create BaseModel")
        else:
            if len(args) > 0 and args[0] in ConsoleShell.valid_classes:
                new_obj = eval(args[0])()
                print(new_obj.id)
                new_obj.save()
            else:
                return

    def do_show(self, args):
        """Usage: show BaseModel 1234-1234-1234"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        for objs_id in all_objs.keys():
            if objs_id == args[1]:
                print(all_objs[objs_id])
                return
        print("** no instance found **")

    def do_destroy(self, args):
        """Usage: destroy BaseModel 1234-1234-1234"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        for objs_id in all_objs.keys():
            if objs_id == args[1]:
                del all_objs[objs_id]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        """Usage: all Basemodel or all"""
        if args not in self.valid_classes and len(args) != 0:
            print("** class doesn't exist **")
            return
        elif args in ConsoleShell.valid_classes:
            all_objs = {k: v for (k, v) in storage.all().items() if isinstance(v, eval(args))}
        elif len(args) == 0:
            all_objs = storage.all()
        else:
            return
        for objs_id in all_objs.keys():
            print(all_objs[objs_id])

    def do_update(self, args):
        """Usage: update <class name> <id> <attribute name> <attribute value>"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if obj_id == args[1]:
                setattr(all_objs[obj_id], args[2], args[3])
                storage.save()
                return
        print("** no instance found **")

    def do_User(self, args):
        self.class_exec('User', args)

    def do_BaseModel(self, args):
        self.class_exec('BaseModel', args)

    def do_State(self, args):
        self.class_exec('State', args)

    def do_City(self, args):
        self.class_exec('City', args)

    def do_Amenity(self, args):
        self.class_exec('Amenity', args)

    def do_Place(self, args):
        self.class_exec('Place', args)

    def do_Review(self, args):
        self.class_exec('Review', args)

    def class_exec(self, cls_name, args):
        if args[:6] == '.all()':
            self.do_all(cls_name)
        elif args[:6] == '.show(':
            self.do_show(cls_name + ' ' + args[7:-2])
        elif args[:8] == ".count()":
            all_objs = {k: v for (k, v) in storage.all().items() if isinstance(v, eval(cls_name))}
            print(len(all_objs))
        elif args[:9] == '.destroy(':
            self.do_destroy(cls_name + ' ' + args[10:-2])
        elif args[:8] == '.update(':
            if '{' in args and '}' in args:
                new_arg = args[8:-1].split('{')
                new_arg[1] = '{' + new_arg[1]
            else:
                new_arg = args[8:-1].split(',')
            if len(new_arg) == 3:
                new_arg = " ".join(new_arg)
                new_arg = new_arg.replace("\"", "")
                new_arg = new_arg.replace("  ", " ")
                self.do_update(cls_name + ' ' + new_arg)
            elif len(new_arg) == 2:
                try:
                    dty = eval(new_arg[1])
                except:
                    return
                for j in dty.keys():
                    self.do_update(cls_name + ' ' + new_arg[0][1:-3] + ' ' + str(j) + ' ' + str(dty[j]))
        else:
            print("Not a valid command (yet)")


if __name__ == '__main__':
    ConsoleShell().cmdloop()
