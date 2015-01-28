from flask import Flask,url_for,render_template
from flask import request
from flask import redirect,render_template
import pickle
import random

app = Flask(__name__,static_url_path='')

@app.route('/index')
def index():
    d = pickle.load(open('links.p','rb'))
    return render_template('index.html',urls=d.values()[:10])

@app.route('/contact')
def about():
    return render_template('contact.html')

@app.route('/naren')
def naren():
    return render_template('work.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()


@app.route('/')
def root():
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run()

"""
The Coleman-Liau Readability Formula

L = sum([len[i] for i in word_tokenize(j)[:100]])


"""