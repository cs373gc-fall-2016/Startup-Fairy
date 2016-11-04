"""
Serves all the routes for the application
"""
import json
import requests
from os import listdir
from flask import render_template, Blueprint, abort, request
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
    if app_category == 'people':
        data = api_people()
    elif app_category == 'cities':
        data = api_cities()
    elif app_category == 'companies':
        data = api_companies()
    elif app_category == 'financialorgs':
        data = api_financialorgs()
    else:
        print("Category does not exist")
        data = []
    return render_template('category.html',
                           alt_title=ALT_NAMES.get(app_category, None),
                           title=app_category, data=data)


@public_views.route('/<app_category>/<entity>', methods=['GET'])
def details(app_category, entity):
    """
    Serve the an entity's page
    """
    data = []
    return render_template('details.html', data=data, category=app_category)


@public_views.route('/api/people', methods=['GET'])
def api_people():
    try:
        person_id = request.args.get('id')
        if person_id is None:
            data = db.session.query(Person).all()
            return json.dumps(list(map(lambda d: d.dictionary(), data)))
        else:
            data = db.session.query(Person).filter_by(
                person_id=person_id).one()
            return json.dumps(data.dictionary())
    except:
        print("Get people failed")
        abort(404)


@public_views.route('/api/companies', methods=['GET'])
def api_companies():
    try:
        company_id = request.args.get('id')
        if company_id is None:
            data = db.session.query(Company).all()
            return json.dumps(list(map(lambda d: d.dictionary(), data)))
        else:
            data = db.session.query(Company).filter_by(
                company_id=company_id).one()
            return json.dumps(data.dictionary())
    except:
        print("Get companies failed")
        abort(404)


@public_views.route('/api/financialorgs', methods=['GET'])
def api_financialorgs():
    try:
        finorg_id = request.args.get('id')
        if finorg_id is None:
            data = db.session.query(FinancialOrg).all()
            return json.dumps(list(map(lambda d: d.dictionary(), data)))
        else:
            data = db.session.query(FinancialOrg).filter_by(
                financial_org_id=finorg_id).one()
            return json.dumps(data.dictionary())
    except:
        print("Get financial orgs failed")
        abort(404)


@public_views.route('/api/cities', methods=['GET'])
def api_cities():
    try:
        city_id = request.args.get('id')
        if city_id is None:
            data = db.session.query(City).all()
            return json.dumps(list(map(lambda d: d.dictionary(), data)))
        else:
            data = db.session.query(City).filter_by(city_id=city_id).one()
            return json.dumps(data.dictionary())
    except:
        print("Get cities failed")
        abort(404)
