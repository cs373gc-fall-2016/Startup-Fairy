"""
Serves all the routes for the application
"""
import json
from os import listdir
from flask import render_template
from app import app

ALT_NAMES = {
    'financialorgs': 'Financial Organizations',
    'companies': 'Companies',
    'cities': 'Cities',
    'people': 'People'

}


@app.route('/')
@app.route('/index')
def index():
    """
    Serve the home/index page
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """
    Serve the about page
    """
    return render_template('about.html', title='About')


@app.route('/<category>')
def category(app_category):
    """Render table template"""
    filepath = "static/data/%s" % (app_category)
    data = []
    for filename in listdir(filepath):
        with open("%s/%s" % (filepath, filename), 'r') as json_data:
            category_obj = json.load(json_data)
            data.append(category_obj)
    return render_template('category.html',
                           alt_title=ALT_NAMES.get(app_category, None),
                           title=category, data=data)


@app.route('/<category>/<entity>')
def details(app_category, entity):
    """
    Serve the an entity's page
    """
    filename = "static/data/%s/%s.json" % (app_category, entity)
    with open(filename, 'r') as json_data:
        data = json.load(json_data)
    return render_template('details.html', data=data, category=app_category)
