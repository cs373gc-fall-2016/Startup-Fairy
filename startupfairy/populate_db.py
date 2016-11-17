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

known_people = set()
known_finorgs = set()
known_companies = set()
known_cities = set()


def filter_contains(is_in, to_filter):
    return list(filter(lambda p: p[1] in is_in, to_filter))


def parse_companies(collect_ids_pass):
    f = open(JSON_DUMP_DIR + COMPANIES_FILENAME, "r")
    companies = json.loads(f.read())
    companies_list = []
    for company_dict in companies:
        company_id = company_dict['id']
        if collect_ids_pass:
            known_companies.add(company_id)
        else:
            website = company_dict['website']
            city = company_dict['city']
            if city not in known_cities:
                city = None
            name = company_dict['name']
            twitter = company_dict['twitter']
            summary = company_dict['summary']
            logo_url = company_dict['logo_url']
            people = json.dumps(filter_contains(known_people, company_dict['people']))
            financial_orgs = json.dumps(filter_contains(known_finorgs, company_dict['financial_orgs']))
            c = models.Company(company_id, name, summary, people, city, financial_orgs, twitter, website, logo_url)
            companies_list += [c]
    return companies_list


def parse_people(collect_ids_pass):
    f = open(JSON_DUMP_DIR + PEOPLE_FILENAME, "r")
    people_json = json.loads(f.read())
    people_list = []
    for people_dict in people_json:
        person_id = people_dict['id']
        if collect_ids_pass:
            known_people.add(person_id)
        else:
            city = people_dict['city']
            name = people_dict['name']
            twitter = people_dict['twitter']
            summary = people_dict['summary']
            logo_url = people_dict['logo_url']
            companies_and_roles = people_dict['companies']
            if city not in known_cities:
                city = None
            roles = []
            companies = []
            for c in companies_and_roles:
                roles += [c['role']]
                companies += [[c['name'], c['id']]]
            companies = filter_contains(known_companies, companies)
            p = models.Person(person_id, name, summary, city, json.dumps(companies), json.dumps(roles), twitter,
                              logo_url)
            people_list += [p]
    return people_list


def parse_finorgs(collect_ids_pass):
    f = open(JSON_DUMP_DIR + FINORGS_FILENAME, "r")
    finorg_json = json.loads(f.read())
    finorg_list = []
    for finorg_dict in finorg_json:
        finorg_id = finorg_dict['id']
        if collect_ids_pass:
            known_finorgs.add(finorg_id)
        else:
            website = finorg_dict['website']
            city = finorg_dict['city']
            if city not in known_cities:
                city = None
            name = finorg_dict['name']
            twitter = finorg_dict['twitter']
            summary = finorg_dict['summary']
            logo_url = finorg_dict['logo_url']
            companies = json.dumps(filter_contains(known_companies, finorg_dict['companies']))
            fin = models.FinancialOrg(finorg_id, name, summary, city, companies, twitter, website, logo_url)
            finorg_list += [fin]
    return finorg_list


def parse_cities(collect_ids_pass):
    f = open(JSON_DUMP_DIR + CITIES_FILENAME, "r")
    cities = json.loads(f.read())
    cities_list = []
    city_id = 0
    for cities_dict in cities:
        name = cities_dict['name']
        if collect_ids_pass:
            known_cities.add(name)
        else:
            people = json.dumps(filter_contains(known_people, cities_dict['people']))
            region = cities_dict['region']
            financial_orgs = json.dumps(filter_contains(known_finorgs, cities_dict['financial_orgs']))
            companies = json.dumps(filter_contains(known_companies, cities_dict['companies']))
            state = cities_dict['state']
            city = models.City(str(city_id), name, state, region, companies, financial_orgs, people)
            city_id += 1
            cities_list += [city]
    return cities_list


def main():
    parse_people(collect_ids_pass=True)
    parse_companies(collect_ids_pass=True)
    parse_finorgs(collect_ids_pass=True)
    parse_cities(collect_ids_pass=True)
    people = parse_people(collect_ids_pass=False)
    companies = parse_companies(collect_ids_pass=False)
    cities = parse_cities(collect_ids_pass=False)
    finorgs = parse_finorgs(collect_ids_pass=False)
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
