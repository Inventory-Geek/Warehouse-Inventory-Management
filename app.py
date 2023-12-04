from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def launch():
  return render_template('Home.html')

@app.route('/Signup')
def login():
  return render_template('Signup.html')

if __name__ == '__main__':
  app.run(host= '0.0.0.0', debug=True)