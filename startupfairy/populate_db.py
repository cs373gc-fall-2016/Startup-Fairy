from sqlalchemy.types import String
from sqlalchemy import create_engine
import models
from models import db
import json

# engine = create_engine('postgresql://localhost/startup_fairy')

# NOTE: startup_fairy is a database created on my local computer
# NOTE: pip installed psycopg2

JSON_DUMP_DIR = "static/data/db_dump/"
COMPANIES_FILENAME = "companies.json"
PEOPLE_FILENAME = "people.json"
FINORGS_FILENAME = "finorgs.json"
CITIES_FILENAME = "cities.json"

_KNOWN_PEOPLE = set()
_KNOWN_FINORGS = set()
_KNOWN_COMPANIES = set()
_KNOWN_CITIES = set()

_IDS_COLLECTED = False


def filter_contains(is_in, to_filter):
    return list(filter(lambda p: p[1] in is_in, to_filter))


def check_preconditions(collect_ids_pass):
    if not _IDS_COLLECTED and not collect_ids_pass:
        raise ValueError("Have to call IDS populated before parsing")


def parse_companies(collect_ids_pass=False):
    check_preconditions(collect_ids_pass)
    f = open(JSON_DUMP_DIR + COMPANIES_FILENAME, "r")
    companies = json.loads(f.read())
    companies_list = []
    for company_dict in companies:
        company_id = company_dict['id']
        if collect_ids_pass:
            _KNOWN_COMPANIES.add(company_id)
        else:
            website = company_dict['website']
            city = company_dict['city']
            if city not in _KNOWN_CITIES:
                city = None
            name = company_dict['name']
            twitter = company_dict['twitter']
            summary = company_dict['summary']
            logo_url = company_dict['logo_url']
            people = json.dumps(filter_contains(_KNOWN_PEOPLE, company_dict['people']))
            financial_orgs = json.dumps(filter_contains(_KNOWN_FINORGS, company_dict['financial_orgs']))
            c = models.Company(company_id, name, summary, people, city, financial_orgs, twitter, website, logo_url)
            companies_list += [c]
    return companies_list


def parse_people(collect_ids_pass=False):
    check_preconditions(collect_ids_pass)
    f = open(JSON_DUMP_DIR + PEOPLE_FILENAME, "r")
    people_json = json.loads(f.read())
    people_list = []
    for people_dict in people_json:
        person_id = people_dict['id']
        if collect_ids_pass:
            _KNOWN_PEOPLE.add(person_id)
        else:
            city = people_dict['city']
            name = people_dict['name']
            twitter = people_dict['twitter']
            summary = people_dict['summary']
            logo_url = people_dict['logo_url']
            companies_and_roles = people_dict['companies']
            if city not in _KNOWN_CITIES:
                city = None
            roles = []
            companies = []
            for c in companies_and_roles:
                roles += [c['role']]
                companies += [[c['name'], c['id']]]
            companies = filter_contains(_KNOWN_COMPANIES, companies)
            p = models.Person(person_id, name, summary, city, json.dumps(companies), json.dumps(roles), twitter,
                              logo_url)
            people_list += [p]
    return people_list


def parse_finorgs(collect_ids_pass=False):
    check_preconditions(collect_ids_pass)
    f = open(JSON_DUMP_DIR + FINORGS_FILENAME, "r")
    finorg_json = json.loads(f.read())
    finorg_list = []
    for finorg_dict in finorg_json:
        finorg_id = finorg_dict['id']
        if collect_ids_pass:
            _KNOWN_FINORGS.add(finorg_id)
        else:
            website = finorg_dict['website']
            city = finorg_dict['city']
            if city not in _KNOWN_CITIES:
                city = None
            name = finorg_dict['name']
            twitter = finorg_dict['twitter']
            summary = finorg_dict['summary']
            logo_url = finorg_dict['logo_url']
            companies = json.dumps(filter_contains(_KNOWN_COMPANIES, finorg_dict['companies']))
            fin = models.FinancialOrg(finorg_id, name, summary, city, companies, twitter, website, logo_url)
            finorg_list += [fin]
    return finorg_list


def parse_cities(collect_ids_pass=False):
    check_preconditions(collect_ids_pass)
    f = open(JSON_DUMP_DIR + CITIES_FILENAME, "r")
    cities = json.loads(f.read())
    cities_list = []
    city_id = 0
    for cities_dict in cities:
        name = cities_dict['name']
        if collect_ids_pass:
            _KNOWN_CITIES.add(name)
        else:
            people = json.dumps(filter_contains(_KNOWN_PEOPLE, cities_dict['people']))
            region = cities_dict['region']
            financial_orgs = json.dumps(filter_contains(_KNOWN_FINORGS, cities_dict['financial_orgs']))
            companies = json.dumps(filter_contains(_KNOWN_COMPANIES, cities_dict['companies']))
            state = cities_dict['state']
            city = models.City(str(city_id), name, state, region, companies, financial_orgs, people)
            city_id += 1
            cities_list += [city]
    return cities_list


def collect_ids():
    parse_people(collect_ids_pass=True)
    parse_companies(collect_ids_pass=True)
    parse_finorgs(collect_ids_pass=True)
    parse_cities(collect_ids_pass=True)
    global _IDS_COLLECTED
    _IDS_COLLECTED = True


def main():
    collect_ids()
    people = parse_people()
    companies = parse_companies()
    cities = parse_cities()
    finorgs = parse_finorgs()
    for person in people:
        db.session.add(person)
    for company in companies:
        db.session.add(company)
    for city in cities:
        db.session.add(city)
    for finorg in finorgs:
        db.session.add(finorg)
    db.session.commit()


if __name__ == '__main__':
    main()