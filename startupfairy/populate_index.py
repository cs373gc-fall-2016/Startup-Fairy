from sqlalchemy.types import String
from sqlalchemy import create_engine
import models
from models import db
import json
from collections import defaultdict
import string
import populate_db


# engine = create_engine('postgresql://localhost/startup_fairy')

# NOTE: startup_fairy is a database created on my local computer
# NOTE: pip installed psycopg2

def remove_punctuation(value):
    translator = str.maketrans({key: None for key in string.punctuation})
    return value.translate(translator)


def main():
    populate_db.collect_ids()
    people = populate_db.parse_people()
    companies = populate_db.parse_companies()
    cities = populate_db.parse_cities()
    finorgs = populate_db.parse_finorgs()
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
                for word in parsed_value.split():
                    word = word.lower()
                    if person_id not in id_set[word]:
                        id_set[word].add(person_id)
                        index[word].append({"model": "person", "id": person_id})
    for company in companies:
        company_dict = company.dictionary()
        company_id = company_dict["company_id"]
        for key, value in company_dict.items():
            if value is not None:
                parsed_value = remove_punctuation(value)
                for word in parsed_value.split():
                    word = word.lower()
                    if company_id not in id_set[word]:
                        id_set[word].add(company_id)
                        index[word].append({"model": "company", "id": company_id})
    for city in cities:
        city_dict = city.dictionary()
        city_id = city_dict["city_id"]
        for key, value in city_dict.items():
            if value is not None:
                parsed_value = remove_punctuation(value)
                for word in parsed_value.split():
                    word = word.lower()
                    if city_id not in id_set[word]:
                        id_set[word].add(city_id)
                        index[word].append({"model": "city", "id": city_id})
    for finorg in finorgs:
        finorg_dict = finorg.dictionary()
        finorg_id = finorg_dict["financial_org_id"]
        for key, value in finorg_dict.items():
            if value is not None:
                parsed_value = remove_punctuation(value)
                for word in parsed_value.split():
                    word = word.lower()
                    if finorg_id not in id_set[word]:
                        id_set[word].add(finorg_id)
                        index[word].append({"model": "financial_org", "id": finorg_id})
    for token, ids in index.items():
        new_index = models.Index(token, json.dumps(list(ids)))
        db.session.add(new_index)
        # print(str(token))
    db.session.commit()


if __name__ == '__main__':
    main()
