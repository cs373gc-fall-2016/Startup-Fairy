import json
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/<category>')
def category(category):
	"""Render table template"""
	return render_template('category.html',title='Category')

@app.route('/<category>/<entity>')
def details(category, entity):
	filename = "static/data/%s/%s.json" % (category, entity)
	with app.open_resource(filename) as json_data:
		data = json.load(json_data)
	return render_template('details.html', data=data)
