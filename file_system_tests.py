#
# file-system-tests.py
# created by Steven Traversi
# (c) Steven Traversi 2016
#

from file_system import *

root = Directory("~")
root_documents = root.add_sub_dir("Documents")
root_projects = root.add_sub_dir("Projects")
root_projects.add_sub_dir("Empty")
root_projects.add_sub_dir("Empty with bash")
root_projects.add_file("bash_profile", "export $PATH")
root_projects.add_file("todo.txt", "1. eat\n2. bash\n3. sleep")
root_documents.add_file("Novel.docx", "Has the word bash in it")
root_documents.add_file("Story.pages", "Doesn't have word in it")

assert(len(root.search("bash")) == 4)
