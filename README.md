<img src="192.png" height="32" alt="icon" style="display:inline-block;" /><h1 style="display:inline-block;">web-term</h1>

**What is it?**
It's half JavaScript, half Python, and it makes a fake, customizable terminal in your browser. It is intended to be used as a fun personal website that is easily explored by other developers who will recognize a familiar format.

**Why is it cool?**
The file system and commands are hidden on the Flask server, so an experienced developer can't dig around in the web inspector and discover all of your fun easter eggs. Make them explore! Further, you can deploy the JavaScript/HTML part on your static site host, like GitHub pages.

## Demo

(Not active yet)
[Here](http://steven.codes/terminal_demo)

## Run for development

Run `python3 server.py & python3 -m http.server` to start both the server and the webpage.

Navigate your browser to [localhost:8000/terminal.html](http://localhost:8000/terminal.html)

The server runs on port 5000 by default.

## Deploy

Upload terminal.html and terminal.js to any service that can deploy a static website. So yes, you can use [GitHub Pages!](https://pages.github.com/)

Deploy `/web_term` to a service that will deploy web applications, like [Heroku](https://community.nitrous.io/tutorials/deploying-a-flask-application-to-heroku)
