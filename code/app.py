from flask import Flask, render_template, request

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/user')
def user():
   return render_template('user.html')

@app.route('/admin')
def admin():
   return 'admin'

if __name__ == '__main__':
   app.run(debug = True)