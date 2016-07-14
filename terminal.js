var terminal = {

  baseUrl: "http://localhost:5000/",
  /* List of the current stack of dirs */
  dirStack: [""],
  /* The input dom element */
  stdin: document.getElementById("stdin"),
  /* The entire terminal element */
  element: document.getElementById("terminal"),
  /* The element currently reflecting the input */
  activeInputElement: document.getElementById("input-display-init"),
  /* The cursor element */
  cursor: "",

  setup: function() {
    stdin.addEventListener("keypress", terminal.handleKeyPress);
    stdin.addEventListener("keydown", terminal.handleTabPress);
    stdin.addEventListener("input", terminal.handleInputChange);
    window.addEventListener("mouseup", terminal.handleMouseUp);
    var cursorElement = document.getElementById("terminal-cursor");
    terminal.cursor = new Cursor(cursorElement);
    terminal.resultsForExpression("", function(response) {
      console.log("have response");
      result = JSON.parse(response);
      terminal.dirStack = result.dirstack;
      document.getElementById("stdin-1").innerHTML = terminal.prompt();
    });
  },

  httpGet: function(url, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      console.log("state change");
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
        console.log("done");
        callback(xmlHttp.responseText);
      }
    }
    xmlHttp.open("GET", url, true); // true for asynchronous
    xmlHttp.send(null);
  },

  /**
   * Perform async GET request for the result of doing command at path.
   * @param {string} url - The base url with no query parameters
   * @param {string} path - The current absolute path of the user in the file system
   * @param {string} expression - The expression to be executed as a command
   */
  getWithPathExpression: function(url, path, expression, callback) {
    fullUrl = url + "?path=" + path + "&expr=" + expression;
    console.log(url);
    terminal.httpGet(fullUrl, callback);
  },

  /**
   * combine dirStack into a path.
   */
  pathFromDirStack: function() {
    return terminal.dirStack.join("/");
  },

  /**
   * generate a prompt.
   */
  prompt: function() {
    return terminal.pathFromDirStack() + " $ ";
  },

  /**
   * @access public
   * Submit the current expression, and pass the output to callback.
   */
  resultsForExpression: function(expression, callback) {
    var url = terminal.baseUrl;
    terminal.getWithPathExpression(url, terminal.pathFromDirStack(), expression,
      callback);
  },

  /**
   * @access public
   * Get the results of performing an autofill tab from the current directory.
   */
   resultsForTab: function(callback) {
     var tokens = terminal.stdin.value.split(" ");
     var incomplete = tokens[tokens.length - 1];
     var url = terminal.baseUrl + "tab"
     terminal.getWithPathExpression(url, terminal.pathFromDirStack(),
      incomplete, callback);
   },

  /**
   * If the key pressed is the enter key, submit the contents of input.
   */
  handleKeyPress: function(event) {
    console.log("hi");
    if (event.keyCode == 13) { // enter
      terminal.resultsForExpression(stdin.value, function(response) {
        result = JSON.parse(response);
        terminal.dirStack = result.dirstack;
        terminal.dom.addLine(result.evaluated);
        window.scrollTo(0, document.body.scrollHeight);
      });
    }
  },

  handleTabPress: function(event) {
    if (event.keyCode == 9) { // tab
      terminal.resultsForTab(function(response) {
        result = JSON.parse(response);
        terminal.dom.addToInput(result.result);
      });
      event.preventDefault();
      return false;
    }
  },

  /**
   * Update content of input display
   */
  handleInputChange: function(event) {
    terminal.dom.setInputDisplay(stdin.value);
  },

  /**
   * Focus on the input.
   */
  handleMouseUp: function(e) {
    terminal.stdin.focus();
  },

  /**
   * A subclass that handles dom element creation.
   */
  dom: {
    addLine: function(content) {
      stdin.value = "";
      var cursor = terminal.element.removeChild(terminal.cursor.element);

      lineBreak = document.createElement("br");
      terminal.element.appendChild(lineBreak);

      output = document.createElement("pre");
      output.innerHTML = content;
      terminal.element.appendChild(output);

      prompt = document.createElement("code");
      prompt.innerHTML = terminal.prompt();
      terminal.element.appendChild(prompt);

      activeDisplay = document.createElement("code");
      terminal.activeInputElement = activeDisplay;
      terminal.element.appendChild(activeDisplay);

      terminal.element.appendChild(cursor);
    },
    setInputDisplay: function(content) {
      terminal.activeInputElement.innerHTML = content;
    },
    addToInput: function(content) {
      terminal.stdin.value += content;
      terminal.activeInputElement.innerHTML += content;
    },
  },

}

var Cursor = function(element) {
  this.element = element;
  this.on = true;
  element.style.transition = "all 0.1s";
  var myself = this;
  // this.interval = setInterval(function() {
  //   myself.updateBlinkState();
  // }, 400);
}
Cursor.prototype.updateBlinkState = function() {
  if (this.on) {
    this.element.style.opacity = "0";
    this.on = false;
  } else {
    this.element.style.opacity = "1";
    this.on = true;
  }
}

terminal.setup();
