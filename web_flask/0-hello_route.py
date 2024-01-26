#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)

# Comment out or remove this line:
# app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
  """Print web"""
  return 'Hello HBNB!'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)

