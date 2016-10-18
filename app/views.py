from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
                           title='Home')

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/table')
def table():
	"""Render table template"""
	return render_template('table.html',title='table')