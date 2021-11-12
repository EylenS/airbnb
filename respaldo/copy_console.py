#!/usr/bin/python3
"""This program contains the entry point of the command interpreter."""
import cmd
import models
from models.base_model import BaseModel
from models import storage

classList = { "BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """This class inherits the public class Cmd, to be used as the base
    class for the present interactive shell."""

    prompt = '(hbnb)'

    def do_quit(self, arg): 
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """End-Of-File marker. Exit the interpreter."""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel.
        where arg is the user input."""

        if not arg:
            print('** class name missing **')
            return

        token = arg.split(' ')
        if token[0] in classList:
            instance = classList[token[0]]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")
            return
    
    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id. Where arg is the user input"""

        if not arg:
            print('** class name missing **')
            return

        token = arg.split(' ')
        if token[0] in classList:
            if len(token) == 1:
                print('** instance id missing **')
                return
            elif len(token) == 2:
                key = token[0] + '.' + token[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print('** no instance found **')
                return
        else:
            print("** class doesn't exist **")
            return
        
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""

        if not arg:
            print('** class name missing **')
            return

        token = arg.split(' ')
        if arg[0] not in HBNBCommand.classList:
            print("** class doesn't exist **")
        elif  len(token) == 1:
                print('** instance id missing **')
        else:
            key = "{}.{}".format(token[0], token[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or
        not on the class name."""
        
        new_list = []
        arg = arg.split(' ')
        if arg == []:
            for key, isinstance in storage.all().items():
                new_list.append(isinstance.__str__())
            print(new_list)
        elif arg[0] in classList:
            for key, isinstance in storage.all().items():
                if isinstance.__class__.__name__ == arg[0]:
                    new_list.append(isinstance.__str__())
            print(new_list)
        else:
            print("** class doesn't exist**")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)."""

        token = arg.split(' ')
        new_list = storage.all()
        if token == []:
            print("** class name missing **")
        elif token[0] not in classList:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        elif len(token) == 2:
            print("** attribute name missing **")
        elif len(token) == 3:
            print("** value missing **")
        else:
            k = token[0] + "." + token[1]
            if k in new_list:
                p = new_list[k]
                setattr(p, token[2], token[3])
                storage.save()
                storage.reload()
            else:
                print("** no instance found **")
              
if __name__ == '__main__':
    HBNBCommand().cmdloop()
