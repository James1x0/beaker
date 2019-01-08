from flask import Flask, render_template

server = Flask(__name__)

@server.route('/')
def home ():
  return('Flask!')

if (__name__ == '__main__'):
  server.run(debug=True)
