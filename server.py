#
# server.py
# created by Steven Traversi
# (c) Steven Traversi 2016
#

from flask import Flask, jsonify
from flask import request
app = Flask(__name__)
from cross_domain_decorator import crossdomain
from user_definitions import root, commands

def tokenize(expression):
    """ Break a string into a command and its arguments, and return
    them both.
    """
    tokens = expression.split()
    return tokens[0], tokens[1:]


@app.route("/")
@crossdomain(origin='*')
def hello():
    response = {'dirstack':[root.name],
               'evaluated':'Command not found'}
    if request.args.get("expr") and request.args.get("path"):
        expr = request.args.get("expr")
        path = request.args.get("path")
        cmd, args = tokenize(expr)
        # First request should just be to get root path.
        if path == "":
            response['evaluated'] = ""
        elif cmd == "cd":
            response['evaluated'] = ""
            current_dir = root.get_dir("/".join(path.split("/")[1:]))
            dirstack = current_dir.get_dir(args[0]).absolute_path().split("/")
            response['dirstack'] = dirstack
        elif cmd in commands:
            # Remove root
            from_dir = root.get_dir("/".join(path.split("/")[1:]))
            response['evaluated'] = commands[cmd].run(from_dir, *args)
            response['dirstack'] = path.split("/")
    return jsonify(**response)

@app.route("/tab")
@crossdomain(origin='*')
def tab():
    response = {'result':''}
    if request.args.get("expr") and request.args.get("path"):
        expr = request.args.get("expr")
        path = request.args.get("path")
        current_dir = root.get_dir("/".join(path.split("/")[1:]))
        search_results = [name for name in current_dir.contents if name.startswith(expr)]
        if len(search_results) == 1:
            response['result'] = search_results[0][len(expr):]
    return jsonify(**response)

if __name__ == "__main__":
    app.run()
