from flask import Flask
from flask import request
from threading import Thread
from stopbutton import stopbutton
import os

app = Flask('')

@app.route('/', methods=['GET', 'POST'])
def page():
  if request.method == 'POST':
    print(request.form['name'] + " said " + request.form['contents'] + "!")
    file = open("index.html", "r")
    output = file.read()
    return output + """<p><span style="font-family: 'Trebuchet MS', Helvetica, sans-serif;">Done! Check your console.</span></p>"""
  else:
    file = open("index.html", "r")
    output = file.read()
    return output + """<body data-new-gr-c-s-loaded="14.1039.0" spellcheck="false">
    <div class="container">
        <h1><span style="font-family: 'Trebuchet MS', Helvetica, sans-serif;">Get And Post Request Example</span></h1><span style='font-family: "Trebuchet MS", Helvetica, sans-serif;'><br></span>
        <form action="" method="post"><span style='font-family: "Trebuchet MS", Helvetica, sans-serif;'><input type="text" placeholder="Name" name="name" value="">&nbsp;<input type="text" placeholder="Contents" name="contents" value="">&nbsp;<input class="btn btn-default" type="submit" value="Send"><br></span></form>
    </div>
    <p><span style="font-family: 'Trebuchet MS', Helvetica, sans-serif;">This is an example of get and post requests in Python Flask.</span></p>
</body>

</html>"""

@app.errorhandler(404)
def filenotfound(e):
  return """<!DOCTYPE html>
<html>

<head>
    <title></title>
</head>

<body spellcheck="false">
    <p style="text-align: center;"><span style="font-size: 390px;">404</span></p>
    <p style="text-align: center;"><span style="font-family: 'Trebuchet MS', Helvetica, sans-serif;">File not found. Sorry!</span></p>
</body>

</html>"""

def run():
  app.run(host="0.0.0.0", port=443)

server = Thread(target=run)
server.start()
stopbutton()