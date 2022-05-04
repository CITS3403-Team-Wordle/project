from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/index')
def index():
    return '<h1>This is index page</h1>'
    
@app.route('/user_test/<name>')
def user_test(name):
    return render_template('user_test.html', name=name)
