#!/usr/bin/python3
""" A modulel that contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import sys
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class for Console Commands"""

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """A command interpreter to exit the program with EOF or Ctrl+D"""

        return True

    def help_EOF(self):
        """Shows functionality of EndOfFile"""

        print("EOF command to exit the program")

    def emptyline(self):
        """Pressing enter doesn't execute anything"""

        pass

    def do_create(self, cName):
        '''Creates new instance of BaseModel'''

        if not cName:
            print("** class name missing **")
            return
        if cName != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            newInstance = BaseModel()
            storage.save()
            print(newInstance.id)

    def do_show(self, args):
        '''Prints the string representation of an instance'''

        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        allinstance = storage.all()
        if key in allinstance.keys():
            print(allinstance[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        '''deletes and instance and save changes to json'''

        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        allinstance = storage.all()
        if key in allinstance.keys():
            del allinstance[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        '''Prints all string representation of all
        instances based or not on the class name'''

        myLs = []
        args = args.split()
        if len(args) == 0 or (len(args) > 0 and args[0] == 'BaseModel'):
            allObj = storage.all()
            for v in allObj.values():
                myLs.append(v.__str__())
        print(myLs)

    def do_update(self, args):
        '''Updates an instance based on the class name
        and id by adding or updating attribute'''

        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        allinstance = storage.all()
        if key not in allinstance.keys():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(self, args[2], args[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
