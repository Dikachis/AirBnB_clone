#!/usr/bin/python3

"""An interactive shell?"""

import cmd
import models
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)  '
    intro = "Welcome! Type ? to list commands"

    def do_EOF(self, line):
        """Exits console"""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        print("Good Bye!")
        return True

    def help_quit(self):
        """when two arguments involve"""
        print('\n'.join(["Quit command to exit the program"]))

    def emptyline(self):
        """ overwriting the emptyline method """
        return False
        # OR
        # pass

#    def do_create(self, line):
#        """Creates a new instances of a class"""
#        if line:
#            try:
#                glo_cls = globals().get(line, None)
#                obj = glo_cls()
#                obj.save()
#                print(obj.id)  # print the id
#            except Exception:
#                print("** class doesn't exist **")
#        else:
#            print("** class name missing **")

    # OR
    def do_create(self, line):
        """Create command creates a new instance of BaseModell"""
        if not line:
            print("** class name missing **")
        elif line not in storage.class_dict():
            print("** class doesn't exist **")
        else:
            new_obj = eval(line)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """print <class name> <id>"""
        arr = line.split()    # split & assign to varia

        if len(arr) < 1:
            print("** class name missing **")
        elif arr[0] not in storage.class_dict():
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[new_str])

    def do_destroy(self, line):
        """Destroy command deletes an instance based on the class name and id
        """
        arr = line.split()
        if len(arr) < 1:
            print("** class name missing **")
        elif arr[0] not in storage.class_dict():
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.all().pop(new_str)
            #    del (storage.all()[new_str])
                storage.save()

    def do_all(self, line):
        """ Print all instances in string representation """
        new_list = []

        if not line:
            for key, obj in storage.all().items():
                new_list.append(str(obj))
            print(new_list)
        elif line not in storage.class_dict():
            print("** class doesn't exist **")
        else:
            for key, obj in storage.all().items():
                if obj.__class__.__name__ == line:
                    new_list.append(str(obj))
            print(new_list)

    # def do_all(self, line):
    #    """ Print all instances in string representation """
    #    arr = line.split()
    #    if len(arr) > 0 and arr[0] not in storage.class_dict():
    #        print("** class doesn't exist **")
    #    else:
    #        new_list = []
    #        for obj in storage.all().values():
    #            if len(arr) > 0 and arr[0] == obj.__class__.__name__:
    #                new_list.append(obj.__str__())
    #            elif len(arr) == 0:
    #                new_list.append(obj.__str__())
    #        print(new_list)

    def do_update(self, line):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        usage:  update <class> <id> <attribute_name> <attribute_value> or
                <class>.update(<id>, <attribute_name>, <attribute_value>) or
                <class>.update(<id>, <dictionary>)
        """
        arr = line.split()
        if len(arr) < 1:
            print("** class name missing **")
            return
        elif arr[0] not in storage.class_dict():
            print("** class doesn't exist **")
            return
        elif len(arr) < 2:
            print("** instance id missing **")
            return
        else:
            new_dict = storage.all()
            new_str = f"{arr[0]}.{arr[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
            elif len(arr) < 3:
                print("** attribute name missing **")
                return
            elif len(arr) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_str], arr[2], arr[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
