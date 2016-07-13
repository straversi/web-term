#
# command.py
# created by Steven Traversi
# (c) Steven Traversi 2016
#

class Command:

    def __init__(self, name, function):
        """Define a command called name, which takes arguments written as those
        in *args. Running this command runs the block function, which should
        accept the arglist *args.
        """
        self.name = name
        self.function = function

    def run(self, directory, *args):
        """Run this command from directory, with arguments listed in args."""
        return self.function(directory, *args)
