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
    return output + "<p>Done! Check your console.</p>"
  else:
    file = open("index.html", "r")
    output = file.read()
    return output

def run():
  app.run(host="0.0.0.0", port=443)

server = Thread(target=run)
server.start()
os.system("clear")