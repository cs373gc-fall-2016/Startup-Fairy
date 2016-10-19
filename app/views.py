from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/category')
def category():
	"""Render table template"""
	return render_template('category.html',title='Category')

@app.route('/details/<entity>')
def show_user_profile(entity):
    return render_template('details.html', 
    	title=entity,
    	name=entity,
    	tagline='Meow meow meow meow. I eat tuna',
    	twitter='discoverdowning',
    	image='http://i.imgur.com/IpZGW1j.jpg')