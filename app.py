from flask import (Flask, render_template)
app = Flask(__name__)

@app.route("/")
def index():
   # return "Hello, World!"
   return render_template('index.html')




@app.route("/hola")
def hola():
   return "Hello, World!"
  


if __name__ == '__main__':
   app.run()