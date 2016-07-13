# web-term (cool graphic?)

**What is it?**
It's half JavaScript, half Python, and it makes a fake, customizable terminal in your browser. It is intended to be used as a fun personal website that is easily explored by other developers in a familiar format.

**Why is it cool?**
The file system and commands are hidden on the Flask server, so an experienced developer can't dig around in the web inspector and discover all of your fun easter eggs. Make them explore! Further, you can deploy the JavaScript/HTML part on your static site host, like GitHub pages.

## Demo

[Here](http://steven.codes/terminal_demo)

## Run for development

Run `python3 -m http.server` from `/terminal`

Run `python3 server.py from `/web_term`

Navigate your browser to localhost:5000/terminal.html

## Deploy

Upload terminal.html and terminal.js to any service that can deploy a static website. So yes, you can use [GitHub Pages!](https://pages.github.com/)

Deploy `/web_term` to a service that will deploy web applications, like [Heroku](https://community.nitrous.io/tutorials/deploying-a-flask-application-to-heroku)
