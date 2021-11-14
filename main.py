from flask import Flask
from flask import request
from threading import Thread
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
    return output + """<p><span style="font-family: 'Trebuchet MS', Helvetica, sans-serif;">This is an example of get and post requests in Python Flask.</span></p>"""

def run():
  app.run(host="0.0.0.0", port=443)

server = Thread(target=run)
server.start()
os.system("clear")