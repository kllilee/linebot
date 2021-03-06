from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World!"

@app.route('/<username>')
def show_hello(username):
   return 'Hello {}'.format(username)

if __name__ == '__main__':
   app.run(debug=True)