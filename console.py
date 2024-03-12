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

    # if u dont to see ugly string manipulation
    # dont look at this method
    def default(self, line):
        """ method to handle default """
        commands = ["all", "show", "destroy", "update", "create", "count"]
        args = line.split(".")
        cmnd = args[1].split("(")
        final_cmnd = ""
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
            # if the command is show or destroy
            if cmnd[0] == "destroy" or cmnd[0] == "show":
                final_cmnd = " ".join([cmnd[0], args[0], cmnd[1][1:-2]])
                self.onecmd(final_cmnd)
                return
            # if the command is update
            if cmnd[0] == "update":
                # split the arguments into the attribute and the value
                atr = cmnd[1][0:-1].split(", ")
                # if the value is a dictionary then
                if len(atr) == 2 and atr[1][0] == "{":
                    # split the dictionary into key value pairs
                    dic = atr[1][1:-1].split(": ")
                    # join the key value pairs into a string with a space
                    f_dic = " ".join([i for i in dic])
                    c_id = atr[0][1:-1]
                    # this just for the line length to be less than 80
                    final_cmnd = " ".join([cmnd[0], args[0], c_id, f_dic])
                    # call the update method with the key value pairs
                    self.onecmd(final_cmnd)
                # else just do a normal update command
                else:
                    # join the attribute and value into a string with a space
                    final_atrs = " ".join([i[1:-1] for i in atr])
                    # this just for the line length to be less than 80
                    final_cmnd = " ".join([cmnd[0], args[0], final_atrs])
                    # call the update method with the attribute and value
                    self.onecmd(final_cmnd)
                    return
            else:
                self.onecmd(cmnd[0] + " " + args[0])

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
