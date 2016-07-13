#
# user_definitions.py
# created by Steven Traversi
# (c) Steven Traversi 2016
#

from file_system import *
from command import *

""" Define your FileSystem here, call it 'root': """

root = Directory("~")
root.add_sub_dir("Projects")
root.add_file("About.txt", open("file_contents/About.txt").read())

""" Define your Commands here, place them in a dictionary 'commands': """

### Example command: ls ###
def func_ls(directory, *args):
    dir_list = []
    if "-a" in args:
        dir_list = [name for name in directory.contents]
    else:
        dir_list = [name for name in directory.contents if name[0] != "."]
    return "   ".join(dir_list);
cmd_ls = Command("ls", func_ls)

### Example command: cat ###
def func_cat(directory, *args):
    filename = args[0]
    return directory.contents[filename].contents
cmd_cat = Command("cat", func_cat)

commands = {}
commands["ls"] = cmd_ls
commands["cat"] = cmd_cat
