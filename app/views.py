import json
from flask import render_template
from app import app
from os import listdir

ALT_NAMES = {
    'financialorgs': 'Financial Organizations',
    'companies': 'Companies',
    'cities': 'Cities',
    'people': 'People'

}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/<category>')
def category(category):
    """Render table template"""
    filepath = "static/data/%s" % (category)
    data = []
    for file in listdir(filepath):
        with open("%s/%s" % (filepath, file), 'r') as json_data:
            category_obj = json.load(json_data)
            data.append(category_obj)
    return render_template('category.html', alt_title=ALT_NAMES.get(category, None), title=category, data=data)


@app.route('/<category>/<entity>')
def details(category, entity):
    filename = "static/data/%s/%s.json" % (category, entity)
    with open(filename, 'r') as json_data:
        data = json.load(json_data)
    return render_template('details.html', data=data, category=category)
