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
PEOPLE_FILENAME = "people_sample.json"
FINORGS_FILENAME = "finorgs.json"
CITIES_FILENAME = "cities.json"


def parse_companies():
    f = open(JSON_DUMP_DIR + COMPANIES_FILENAME, "r")
    companies = json.loads(f.read())
    companies_list = []
    for company_dict in companies:
        website = company_dict['website']
        city = company_dict['city']
        name = company_dict['name']
        twitter = company_dict['twitter']
        summary = company_dict['summary']
        logo_url = company_dict['logo_url']
        company_id = company_dict['id']
        people = json.dumps(company_dict['people'])
        financial_orgs = json.dumps(company_dict['financial_orgs'])
        c = models.Company(company_id, name, summary, people, city, financial_orgs, twitter, website, logo_url)
        companies_list += [c]
    return companies_list


def parse_people():
    f = open(JSON_DUMP_DIR + PEOPLE_FILENAME, "r")
    people_json = json.loads(f.read())
    people_list = []
    for people_dict in people_json:
        city = people_dict['city']
        name = people_dict['name']
        twitter = people_dict['twitter']
        summary = people_dict['summary']
        logo_url = people_dict['logo_url']
        person_id = people_dict['id']
        companies_and_roles = people_dict['companies']
        roles = []
        companies = []
        for c in companies_and_roles:
            roles += [c['role']]
            companies += [[c['name'], c['id']]]
        p = models.Person(person_id, name, summary, city, json.dumps(companies), json.dumps(roles), twitter, logo_url)
        people_list += [p]
    return people_list


def parse_finorgs():
    f = open(JSON_DUMP_DIR + FINORGS_FILENAME, "r")
    finorg_json = json.loads(f.read())
    finorg_list = []
    for finorg_dict in finorg_json:
        website = finorg_dict['website']
        city = finorg_dict['city']
        name = finorg_dict['name']
        twitter = finorg_dict['twitter']
        summary = finorg_dict['summary']
        logo_url = finorg_dict['logo_url']
        finorg_id = finorg_dict['id']
        companies = json.dumps(finorg_dict['companies'])
        fin = models.FinancialOrg(finorg_id, name, summary, city, companies, twitter, website, logo_url)
        finorg_list += [fin]
    return finorg_list

def parse_cities():
    f = open(JSON_DUMP_DIR + CITIES_FILENAME, "r")
    cities = json.loads(f.read())
    cities_list = []
    city_id = 0
    for cities_dict in cities:
        name = cities_dict['name']
        people = json.dumps(cities_dict['people'])
        region = cities_dict['region']
        financial_orgs = json.dumps(cities_dict['financial_orgs'])
        companies = json.dumps(cities_dict['companies'])
        state = cities_dict['state']
        city = models.City(str(city_id), name, state, region, companies, financial_orgs, people)
        city_id += 1
        cities_list += [city]
    return cities_list

def main():
    people = parse_people()

    # companies = parse_companies()
    # cities = parse_cities()
    # finorgs = parse_finorgs()
    # for person in people:
    #     db.session.add(person)
    # for company in companies:
    #     db.session.add(company)
    # for city in cities:
    #     db.session.add(city)
    # for finorg in finorgs:
    #     db.session.add(finorg)
    # db.session.commit()

if __name__ == '__main__':
    main()
