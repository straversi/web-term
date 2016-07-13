#
# file-system.py
# created by Steven Traversi
# (c) Steven Traversi 2016
#

import re

class Directory:

    def __init__(self, name):
        """Set the name of the directory and start an empty array to hold
        files and other directories.
        """
        self.name = name
        self.contents = {}

    def add_sub_dir(self, name):
        """Add a sub dir, name, of the current dir represented by root.
        Return it.
        """
        new_dir = Directory(name)
        self.contents[name] = new_dir
        new_dir.contents[".."] = self
        return new_dir

    def add_file(self, name, contents):
        """Add a file called name to the current dir. Return it."""
        new_file = File(name, contents)
        self.contents[name] = new_file
        return new_file

    def search(self, keyword):
        """Search the current directory and all of its sub directories (etc.),
        and return the relative paths of any hits. If there are no hits, return
        empty.
        """
        assert False, "Implement me"
        results = []
        for obj in self.contents:
            if re.search(keyword, obj.name):
                results.append(obj.name)
            if isinstance(obj, Directory):
                results += obj.search(keyword)
            elif isinstance(obj, File) and re.search(keyword, obj.contents):
                results.append(obj.name)
        return [self.name + "/" + sub_path for sub_path in results]

    def get_dir(self, path):
        """Get the directory relative to this directory at path.
        Example:
        self = ~/Documents
        path = Projects/Blog
        RETURN: Directory @ ~/Documents/Projects/Blog
        """
        if path == "" or path == self.name:
            return self
        dirs = path.split("/")
        for child, reference in self.contents.items():
            if isinstance(reference, Directory) and child == dirs[0]:
                return reference.get_dir("/".join(dirs[1:]))
        raise ValueError("Fix me")

    def absolute_path(self):
        if not ".." in self.contents:
            return self.name
        return self.contents[".."].absolute_path() + "/" + self.name

class File:

    def __init__(self, name, contents):
        """Set the name of the file and its contents as a string."""
        self.name = name
        self.contents = contents
