from sqlalchemy.types import String
from sqlalchemy import create_engine
import models
from models import db
import json
from collections import defaultdict
import string
# engine = create_engine('postgresql://localhost/startup_fairy')

# NOTE: startup_fairy is a database created on my local computer
# NOTE: pip installed psycopg2

JSON_DUMP_DIR = "static/data/db_dump/"
COMPANIES_FILENAME = "companies.json"
PEOPLE_FILENAME = "people.json"
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

def remove_punctuation(value):
    translator = str.maketrans({key: None for key in string.punctuation})
    return value.translate(translator)

def main():
    people = parse_people()
    companies = parse_companies()
    cities = parse_cities()
    finorgs = parse_finorgs()
    # inverted index
    # map <search token (word), list<model IDS>
    id_set = defaultdict(set)
    index = defaultdict(list)
    for person in people:
        person_dict = person.dictionary()
        person_id = person_dict["person_id"]
        for key, value in person_dict.items():
            if value is not None:
                parsed_value = remove_punctuation(value)
                for word in parsed_value:
                    if person_id not in id_set[word]:
                        id_set[word].add(person_id)
                        index[word].append({"model": "person", "id": person_id})
    for company in companies:
        company_dict = company.dictionary()
        company_id = company_dict["company_id"]
        for key, value in company_dict.items():
            if value is not None:
                parsed_value = remove_punctuation(value)
                for word in parsed_value:
                    if company_id not in id_set[word]:
                        id_set[word].add(company_id)
                        index[word].append({"model": "company", "id": company_id})
    for city in cities:
        city_dict = city.dictionary()
        city_id = city_dict["city_id"]
        for key, value in city_dict.items():
            if value is not None:
                parsed_value = remove_punctuation(value)
                for word in parsed_value:
                    if city_id not in id_set[word]:
                        id_set[word].add(city_id)
                        index[word].append({"model": "city", "id": city_id})
    for finorg in finorgs:
        finorg_dict = finorg.dictionary()
        finorg_id = finorg_dict["financial_org_id"]
        for key, value in finorg_dict.items():
            if value is not None:
                parsed_value = remove_punctuation(value)
                for word in parsed_value:
                    if finorg_id not in id_set[word]:
                        id_set[word].add(finorg_id)
                        index[word].append({"model": "financial_org", "id": finorg_id})
    for token, ids in index.items():
        new_index = models.Index(token, json.dumps(list(ids)))
        #db.session.add(new_index)
        print(str(token)+" "+str(json.dumps(list(ids))))
    #db.session.commit()
if __name__ == '__main__':
    main()
