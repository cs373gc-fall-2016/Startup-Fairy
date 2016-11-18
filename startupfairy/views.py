"""
Serves all the routes for the application
"""
import json
import subprocess
from collections import defaultdict
import string
import markdown2
from flask import render_template, abort, request
from flask_cors import CORS
from sqlalchemy.exc import SQLAlchemyError

from models import app, db, Company, Person, FinancialOrg, City, Index

ALT_NAMES = {
    'financialorgs': 'Financial Organizations',
    'companies': 'Companies',
    'cities': 'Cities',
    'people': 'People'
}

CORS(app)


@app.route('/')
@app.route('/index')
def index():
    """
    Serve the home/index page
    """
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    """
    :return: favicon for the website
    """
    return ""


def format_query(query_string):
    '''
        Format the query string for search so that we can
        parse the tokens easily. Here we replace the "+"
        characters with spaces, and remove all punctuation.
    '''
    query_string = query_string.replace("+", " ").lower()
    translator = str.maketrans({key: None for key in string.punctuation})
    print(query_string)
    return query_string.translate(translator)


@app.route('/find/', methods=['GET'])
def find():
    """
    a function to search the database
    :return: json object with search results
    """
    query_string = request.args.get('query')
    try:
        obj = search(query_string)
    except SQLAlchemyError:
        return render_template('noresults.html', query=query_string)
    return render_template('results.html', query=query_string, data=obj)


@app.route('/search/<query_string>', methods=['GET'])
def search(query_string='test'):
    """
    :param query_string: the string we are querying
    :return: the json of search results
    """
    # if request.method == 'GET':
        # query_string = request.args.get['query']
    query_string = format_query(query_string)
    query_words = set(query_string.split())
    # For the "and" results.
    and_model_to_words = defaultdict(lambda: defaultdict(set))
    # For the "or" results.
    or_model_to_words = defaultdict(lambda: defaultdict(set))
    # Map of the following form:
    # <model id, dictionary> where the dictionary is of the form:
    # <"type": "<model type>"
    # <"words">: "<words from our query that appear in this model>"
    for word in query_words:
        print(word)
        word_index = db.session.query(Index).filter_by(token=word).one()
        models = json.loads(word_index.models)
        if models is not None:
            for model in models:
                model_type = model["model"]
                model_id = model["id"]
                or_model_to_words[model_id]["type"] = model_type
                or_model_to_words[model_id]["words"].add(word_index.token)
    for key, value in or_model_to_words.items():
        # If this result contains ALL of the words in our search, add
        # it to the AND results.
        if query_words.issubset(value["words"]):
            and_model_to_words[key] = value
            # Cast words to list so that we can serialize with JSON.
            and_model_to_words[key]["words"] = list(
                and_model_to_words[key]["words"])
        value["words"] = list(value["words"])
    return json.dumps([and_model_to_words, or_model_to_words])


@app.route('/about')
def about():
    """
    Serve the about page
    """
    return render_template('about.html', alt_title='About')


@app.route('/category/<app_category>')
def category(app_category):
    """Render table template"""
    print("Attempting to get category %s" % app_category)
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
    print("Rendering template")
    return render_template('category.html',
                           alt_title=ALT_NAMES.get(app_category, None),
                           title=app_category, data=data)


@app.route('/category/<app_category>/<entity>')
def details(app_category, entity):
    """Serve the an entity's page"""
    if app_category == 'people':
        data = api_people(entity)
    elif app_category == 'cities':
        data = api_cities(entity)
    elif app_category == 'companies':
        data = api_companies(entity)
    elif app_category == 'financialorgs':
        data = api_financialorgs(entity)
    else:
        print("Category does not exist")
        data = ""
    parsed_data = json.loads(data)
    if 'summary' in parsed_data.keys() and parsed_data['summary'] is not None:
        parsed_data['summary'] = markdown2.markdown(parsed_data['summary'])
    if app_category == 'cities':
        parsed_data['is_city']=True
    else:
        parsed_data['is_city']=False
        location_info = {}
        city_info = json.loads(get_city_by_name(parsed_data['city']))
        if city_info is not None:
            if 'state' in city_info.keys():
                location_info['state'] = city_info['state']
            if 'region' in city_info.keys():
                location_info['region'] = city_info['region']
            if 'city_id' in city_info.keys():
                location_info['city_id'] = city_info['city_id']
        parsed_data['location'] = json.dumps(location_info)
    return render_template('details.html', data=parsed_data, category=app_category)


@app.route('/education')
def education():
    """
    a route to visualization of education of IDB5
    """
    return render_template('team_five.html')


@app.route('/api/people', methods=['GET'])
def api_people(entity=None):
    """
    api route for people
    :param entity: is the id of a person or None
    :return: json with results or 404
    """
    try:
        person_id = request.args.get('id')
        if entity is None and person_id is None:
            return get_all_from_category(Person)
        else:
            if entity is not None:
                data = db.session.query(Person).filter_by(
                    person_id=entity).one()
            else:
                data = db.session.query(Person).filter_by(
                    person_id=person_id).one()
            return json.dumps(data.dictionary())
    except SQLAlchemyError:
        print("Get people failed")
        abort(404)


@app.route('/api/companies', methods=['GET'])
def api_companies(entity=None):
    """
    api route for companies
    :param entity: is the id of a company or None
    :return: json with results or 404
    """
    try:
        company_id = request.args.get('id')
        if entity is None and company_id is None:
            return get_all_from_category(Company)
        else:
            if entity is not None:
                data = db.session.query(Company).filter_by(
                    company_id=entity).one()
            else:
                data = db.session.query(Company).filter_by(
                    company_id=company_id).one()
            return json.dumps(data.dictionary())
    except SQLAlchemyError:
        print("Get companies failed")
        abort(404)


@app.route('/api/financialorgs', methods=['GET'])
def api_financialorgs(entity=None):
    """
    api route for financial org
    :param entity: is the id of a financial org or None
    :return: json with results or 404
    """
    try:
        finorg_id = request.args.get('id')
        if entity is None and finorg_id is None:
            return get_all_from_category(FinancialOrg)
        else:
            if entity is not None:
                data = db.session.query(FinancialOrg).filter_by(
                    financial_org_id=entity).one()
            else:
                data = db.session.query(FinancialOrg).filter_by(
                    financial_org_id=finorg_id).one()
        return json.dumps(data.dictionary())
    except SQLAlchemyError:
        print("Get financial orgs failed")
        abort(404)

@app.route('/api/cities', methods=['GET'])
def api_cities(entity=None):
    """
    api route for cities
    :param entity: is the id of a city or None
    :return: json with results or 404
    """
    try:
        city_id = request.args.get('id')
        if entity is None and city_id is None:
            return get_all_from_category(City)
        else:
            if entity is not None:
                data = db.session.query(City).filter_by(city_id=entity).one()
            else:
                data = db.session.query(City).filter_by(city_id=city_id).one()
            return json.dumps(data.dictionary())
    except SQLAlchemyError:
        print("Get cities failed")
        abort(404)

def get_city_by_name(name):
    """
    Get city information by name. For internal use
    """
    try:
        data = db.session.query(City).filter_by(name=name).one()
        return json.dumps(data.dictionary())
    except:
        return None

def get_all_from_category(table):
    """
    Helper that gets all data from a given table
    """
    data = db.session.query(table).all()
    return json.dumps(list(map(lambda d: d.dictionary(), data)))


@app.errorhandler(404)
def page_not_found(error):
    """
    returns a 404 page
    """
    return render_template('404.html', alt_title=error, error=error)


@app.route('/run_tests')
def run_tests():
    """
    runs the tests and returns the output
    :return: the json with results
    """
    output = subprocess.getoutput("python startupfairy/tests.py")
    return json.dumps({'test_results': str(output)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
