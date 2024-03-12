#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
        class for the command interpreter
    """
    prompt = '(hbnb) '

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, line):
        """ method to handle default """
        commands = ["all", "show", "destroy", "update", "create", "count"]
        args = line.split(".")
        cmnd = args[1].split("(")
        if len(args) < 2:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if cmnd[0] not in commands:
            print("** command doesn't exist **")
            print(cmnd)
            return
        if cmnd[0] in commands:
            if cmnd[0] == "destroy" or cmnd[0] == "show":
                self.onecmd(cmnd[0] + " " + args[0] + " " + cmnd[1][1:-2])
                return
            if cmnd[0] == "update":
                atr = " ".join([i[1:-1] for i in cmnd[1][0:-1].split(", ")])
                self.onecmd(cmnd[0] + " " + args[0] + " " + atr)
                return
            else:
                self.onecmd(cmnd + " " + args[0])

        else:
            print("*** Unknown syntax: {}".format(line))

    def do_count(self, line):
        """ method to handle count """
        count = 0
        for k, v in models.storage.all().items():
            if line in k:
                count += 1
        print(count)

    def do_create(self, line):
        """ method to handle create """
        if not line:
            print("** class name missing **")
            return
        try:
            new_inst = eval(line)()
            new_inst.save()
            print(new_inst.id)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ method to handle show """
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        try:
            key = args[0] + "." + args[1]
            print(models.storage.all()[key])
        except Exception as e:
            print("** no instance found **")

    def do_destroy(self, line):
        """ method to handle destroy """
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        try:
            key = args[0] + "." + args[1]
            del models.storage.all()[key]
            models.storage.save()
        except Exception as e:
            print("** no instance found **")

    def do_all(self, line):
        """ method to handle all """
        a = line.split()
        if not line:
            print([str(v) for k, v in models.storage.all().items()])
            return
        if a[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        print([str(v) for k, v in models.storage.all().items() if a[0] in k])

    def do_update(self, line):
        """ method to handle update """
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = args[0] + "." + args[1]
        try:
            setattr(models.storage.all()[key], args[2], args[3])
            models.storage.all()[key].save()
        except Exception as e:
            print("** no instance found **")

    def emptyline(self):
        """ method to handle empty lines """
        return

    def do_quit(self, line):
        """ method to handle quiting """
        return True

    def do_EOF(self, line):
        """ method to handle EOF """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
