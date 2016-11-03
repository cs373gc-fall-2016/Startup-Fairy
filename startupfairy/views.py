"""
Serves all the routes for the application
"""
import json
from os import listdir
from flask import render_template
from flask import render_template, Blueprint
from flask import request
from models import *

public_views = Blueprint('public_views', __name__)

ALT_NAMES = {
    'financialorgs': 'Financial Organizations',
    'companies': 'Companies',
    'cities': 'Cities',
    'people': 'People'

}


@public_views.route('/')
@public_views.route('/index')
def index():
    """
    Serve the home/index page
    """
    return render_template('index.html')


@public_views.route('/about')
def about():
    """
    Serve the about page
    """
    return render_template('about.html', alt_title='About')


@public_views.route('/<app_category>', methods=['GET'])
def category(app_category):
    """Render table template"""
    filepath = "static/data/%s" % (app_category)
    data = []
    # for filename in listdir(filepath):
    # with open("%s/%s" % (filepath, filename), 'r') as json_data:
    # category_obj = json.load(json_data)
    # data.append(category_obj)
    return render_template('category.html',
                           alt_title=ALT_NAMES.get(app_category, None),
                           title=app_category, data=data)


@public_views.route('/<app_category>/<entity>', methods=['GET'])
def details(app_category, entity):
    """
    Serve the an entity's page
    """
    # filename = "static/data/%s/%s.json" % (app_category, entity)
    # with open(filename, 'r') as json_data:
    # data = json.load(json_data)
    return render_template('details.html', data=data, category=app_category)


@public_views.route('/api/people', methods=['GET'])
def api_people():
    data = db.session.query(Person).all()
    return json.dumps(list(map(lambda d: d.dictionary(), data)))

@public_views.route('/api/companies', methods=['GET'])
def api_companies():
    data = db.session.query(Company).all()
    return json.dumps(list(map(lambda d: d.dictionary(), data)))


@public_views.route('/api/cities', methods=['GET'])
def api_cities():
    data = db.session.query(City).all()
    return json.dumps(list(map(lambda d: d.dictionary(), data)))


@public_views.route('/api/financialorgs', methods=['GET'])
def api_financialorgs():
    data = db.session.query(FinancialOrg).all()
    return json.dumps(list(map(lambda d: d.dictionary(), data)))
