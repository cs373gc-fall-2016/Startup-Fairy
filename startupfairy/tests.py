"""Tests for methods in models.py, views.py and the About page"""

# -------
# imports
# -------

from unittest import main, TestCase
from models import Company, FinancialOrg, Person, City, db

import httpretty
import requests

from views import app, index, about, category, education, page_not_found

# -----------
# TestCompany
# -----------

class TestCompany(TestCase):
    """Tests for the methods of the Company model"""

    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp(self):
        with app.test_request_context():
            db.create_all()

    def tearDown(self):
        with app.test_request_context():
            db.session.remove()

    # -------
    # Company
    # -------

    def test_company_model_1(self):
        """Test adding Company objects to and deleting Company objects from the db"""

        with app.test_request_context():
            example1 = Company("id", "name", "summary", "people",
                               "city", "finorgs", "twitter", "website", "logo")
            example2 = Company("id2", "name2", "summary2", "people2",
                               "city2", "finorgs2", "twitter2", "website2", "logo2")

            companies1 = db.session.query(Company).all()

            db.session.add(example1)
            db.session.add(example2)
            db.session.commit()
            companies2 = db.session.query(Company).all()

            self.assertTrue(example1 in companies2)
            self.assertTrue(example2 in companies2)
            self.assertEqual(len(companies2), len(companies1) + 2)

            db.session.delete(example1)
            db.session.delete(example2)
            db.session.commit()
            companies3 = db.session.query(Company).all()

            self.assertTrue(example1 not in companies3)
            self.assertTrue(example2 not in companies3)
            self.assertEqual(len(companies1), len(companies2) - 2)

    def test_company_model_2(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            example1 = Company("id", "name", "summary", "people",
                               "city", "finorgs", "twitter", "website", "logo")

            db.session.add(example1)
            db.session.commit()

            company = db.session.query(Company).filter_by(name="name").first()
            self.assertEqual(company.city, "city")
            self.assertEqual(company.twitter, "twitter")

            db.session.delete(example1)
            db.session.commit()

    def test_company_constructor_1(self):
        """Test construction of a new company instance"""

        example1 = Company("id", "name", "summary", "people",
                           "city", "finorgs", "twitter", "website", "logo")

        self.assertEqual(example1.company_id, "id")
        self.assertEqual(example1.name, "name")
        self.assertEqual(example1.summary, "summary")
        self.assertEqual(example1.people, "people")
        self.assertEqual(example1.city, "city")

    def test_company_constructor_2(self):
        """Test construction of a new company instance"""

        example1 = Company("id", "name", "summary", "people",
                           "city", "finorgs", "twitter", "website", "logo")

        self.assertEqual(example1.financial_orgs, "finorgs")
        self.assertEqual(example1.twitter, "twitter")
        self.assertEqual(example1.website, "website")
        self.assertEqual(example1.logo_url, "logo")

    def test_company_constructor_3(self):
        """Test construction of a new company instance"""

        example2 = Company("id1", "Wetpaint",
                           ("Wetpaint is a technology platform company that uses its proprietary"
                            + " state-of-the-art technology and expertise in social media to build"
                            + " and monetize audiences for digital publishers."), "person1",
                           "San Francisco", "Youniversity Ventures", "wetpaint",
                           "http://wetpaint.com", "logo_url")

        self.assertEqual(example2.company_id, "id1")
        self.assertEqual(example2.name, "Wetpaint")
        self.assertEqual(example2.summary,
                         ("Wetpaint is a technology platform company that uses its proprietary"
                          + " state-of-the-art technology and expertise in social media to build"
                          + " and monetize audiences for digital publishers."))
        self.assertEqual(example2.people, "person1")
        self.assertEqual(example2.city, "San Francisco")

    def test_company_constructor_4(self):
        """Test construction of a new company instance"""

        example2 = Company("id1", "Wetpaint",
                           ("Wetpaint is a technology platform company that uses its proprietary"
                            + " state-of-the-art technology and expertise in social media to build"
                            + " and monetize audiences for digital publishers."), "person1",
                           "San Francisco", "Youniversity Ventures", "wetpaint",
                           "http://wetpaint.com", "logo_url")

        self.assertEqual(example2.financial_orgs, "Youniversity Ventures")
        self.assertEqual(example2.twitter, "wetpaint")
        self.assertEqual(example2.website, "http://wetpaint.com")
        self.assertEqual(example2.logo_url, "logo_url")

    def test_company_repr_1(self):
        """Test __repr__ methond of company class"""

        example1 = Company("id", "name", "summary", "people",
                           "city", "finorgs", "twitter", "website", "logo")

        self.assertEqual(example1.__repr__(), "<Company 'name'>")

    def test_company_repr_2(self):
        """Test __repr__ methond of company class"""

        example2 = Company("id1", "Wetpaint",
                           ("Wetpaint is a technology platform company that uses its proprietary"
                            + " state-of-the-art technology and expertise in social media to build"
                            + " and monetize audiences for digital publishers."), "person1",
                           "San Francisco", "Youniversity Ventures", "wetpaint",
                           "http://wetpaint.com", "logo_url")

        self.assertEqual(example2.__repr__(), "<Company 'Wetpaint'>")

    def test_company_repr_3(self):
        """Test __repr__ methond of company class"""

        example3 = Company("id3", "name3", "summary3", "people3",
                           "city3", "finorgs3", "twitter3", "website3", "logo3")

        self.assertEqual(example3.__repr__(), "<Company 'name3'>")

    def test_company_dictionary_1(self):
        """Test dictionary method of company class"""

        example1 = Company("id", "name", "summary", "people",
                           "city", "finorgs", "twitter", "website", "logo")
        dict_rep = example1.dictionary()

        self.assertEqual(dict_rep['company_id'], "id")
        self.assertEqual(dict_rep['name'], "name")
        self.assertEqual(dict_rep['summary'], "summary")
        self.assertEqual(dict_rep['people'], "people")
        self.assertEqual(dict_rep['city'], "city")

    def test_company_dictionary_2(self):
        """Test dictionary method of company class"""

        example1 = Company("id", "name", "summary", "people",
                           "city", "finorgs", "twitter", "website", "logo")
        dict_rep = example1.dictionary()

        self.assertEqual(dict_rep['financial_orgs'], "finorgs")
        self.assertEqual(dict_rep['twitter'], "twitter")
        self.assertEqual(dict_rep['website'], "website")
        self.assertEqual(dict_rep['logo_url'], "logo")

    def test_company_dictionary_3(self):
        """Test dictionary method of company class"""

        example2 = Company("id1", "Wetpaint",
                           ("Wetpaint is a technology platform company that uses its proprietary"
                            + " state-of-the-art technology and expertise in social media to build"
                            + " and monetize audiences for digital publishers."), "person1",
                           "San Francisco", "Youniversity Ventures", "wetpaint",
                           "http://wetpaint.com", "logo_url")

        dict_rep = example2.dictionary()

        self.assertEqual(dict_rep['company_id'], "id1")
        self.assertEqual(dict_rep['name'], "Wetpaint")
        self.assertEqual(dict_rep['summary'],
                         ("Wetpaint is a technology platform company that uses its proprietary"
                          + " state-of-the-art technology and expertise in social media to build"
                          + " and monetize audiences for digital publishers."))
        self.assertEqual(dict_rep['people'], "person1")
        self.assertEqual(dict_rep['city'], "San Francisco")

    def test_company_dictionary_4(self):
        """Test dictionary method of company class"""

        example2 = Company("id1", "Wetpaint",
                           ("Wetpaint is a technology platform company that uses its proprietary"
                            + " state-of-the-art technology and expertise in social media to build"
                            + " and monetize audiences for digital publishers."), "person1",
                           "San Francisco", "Youniversity Ventures", "wetpaint",
                           "http://wetpaint.com", "logo_url")

        dict_rep = example2.dictionary()

        self.assertEqual(dict_rep['financial_orgs'], "Youniversity Ventures")
        self.assertEqual(dict_rep['twitter'], "wetpaint")
        self.assertEqual(dict_rep['website'], "http://wetpaint.com")
        self.assertEqual(dict_rep['logo_url'], "logo_url")


# ----------------
# TestFinancialOrg
# ----------------

class TestFinancialOrg(TestCase):
    """Tests for the methods of the Financial Organization model"""

    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp(self):
        with app.test_request_context():
            db.create_all()

    def tearDown(self):
        with app.test_request_context():
            db.session.remove()

    # ------------
    # FinancialOrg
    # ------------

    def test_financial_org_model_1(self):
        """Test adding FinancialOrg objects to and deleting FinancialOrg objects from the db"""

        with app.test_request_context():
            example1 = FinancialOrg("id", "name", "summary", "city", "companies", "twitter",
                                    "website", "logo")
            example2 = FinancialOrg("id2", "name2", "summary2", "city2", "companies2", "twitter2",
                                    "website2", "logo2")

            finorgs1 = db.session.query(FinancialOrg).all()

            db.session.add(example1)
            db.session.add(example2)
            db.session.commit()
            finorgs2 = db.session.query(FinancialOrg).all()

            self.assertTrue(example1 in finorgs2)
            self.assertTrue(example2 in finorgs2)
            self.assertEqual(len(finorgs2), len(finorgs1) + 2)

            db.session.delete(example1)
            db.session.delete(example2)
            db.session.commit()
            finorgs3 = db.session.query(FinancialOrg).all()

            self.assertTrue(example1 not in finorgs3)
            self.assertTrue(example2 not in finorgs3)
            self.assertEqual(len(finorgs3), len(finorgs2) - 2)

    def test_financial_org_model_2(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            example1 = FinancialOrg("id", "name", "summary", "city", "companies", "twitter",
                                    "website", "logo")

            db.session.add(example1)
            db.session.commit()

            finorg = db.session.query(FinancialOrg).filter_by(name="name").first()
            self.assertEqual(finorg.city, "city")
            self.assertEqual(finorg.twitter, "twitter")

            db.session.delete(example1)
            db.session.commit()

    def test_financial_org_init_1(self):
        """Test construction of a new company instance"""

        example1 = FinancialOrg("id", "name", "summary", "city", "companies", "twitter",
                                "website", "logo")

        self.assertEqual(example1.financial_org_id, "id")
        self.assertEqual(example1.name, "name")
        self.assertEqual(example1.summary, "summary")
        self.assertEqual(example1.city, "city")

    def test_financial_org_init_2(self):
        """Test construction of a new company instance"""

        example1 = FinancialOrg("id", "name", "summary", "city", "companies", "twitter",
                                "website", "logo")

        self.assertEqual(example1.companies, "companies")
        self.assertEqual(example1.twitter, "twitter")
        self.assertEqual(example1.website, "website")
        self.assertEqual(example1.logo_url, "logo")

    def test_financial_org_init_3(self):
        """Test construction of a new company instance"""

        example2 = FinancialOrg("id1", "Founders Fund",
                                ("Founders Fund is a San Francisco based venture capital firm which"
                                 + " invests at every stage in companies with revolutionary"
                                 + " technologies."),
                                "San Francisco", "Space Exploration Technologies", "foundersfund",
                                "http://www.foundersfund.com", "logo_url")

        self.assertEqual(example2.financial_org_id, "id1")
        self.assertEqual(example2.name, "Founders Fund")
        self.assertEqual(example2.summary,
                         ("Founders Fund is a San Francisco based venture capital firm which"
                          + " invests at every stage in companies with revolutionary"
                          + " technologies."))
        self.assertEqual(example2.city, "San Francisco")

    def test_financial_org_init_4(self):
        """Test construction of a new company instance"""

        example2 = FinancialOrg("id1", "Founders Fund",
                                ("Founders Fund is a San Francisco based venture capital firm which"
                                 + " invests at every stage in companies with revolutionary"
                                 + " technologies."),
                                "San Francisco", "Space Exploration Technologies", "foundersfund",
                                "http://www.foundersfund.com", "logo_url")

        self.assertEqual(example2.companies, "Space Exploration Technologies")
        self.assertEqual(example2.twitter, "foundersfund")
        self.assertEqual(example2.website, "http://www.foundersfund.com")
        self.assertEqual(example2.logo_url, "logo_url")

    def test_financial_org_repr_1(self):
        """Test __repr__ methond of company financial org"""

        example1 = FinancialOrg("id", "name", "summary", "city", "companies", "twitter",
                                "website", "logo")

        self.assertEqual(example1.__repr__(), "<FinancialOrg 'name'>")

    def test_financial_org_repr_2(self):
        """Test __repr__ methond of financial org class"""

        example2 = FinancialOrg("id1", "Founders Fund",
                                ("Founders Fund is a San Francisco based venture capital firm which"
                                 + " invests at every stage in companies with revolutionary"
                                 + " technologies."),
                                "San Francisco", "Space Exploration Technologies", "foundersfund",
                                "http://www.foundersfund.com", "logo_url")

        self.assertEqual(example2.__repr__(), "<FinancialOrg 'Founders Fund'>")

    def test_financial_org_repr_3(self):
        """Test __repr__ methond of company financial org"""

        example3 = FinancialOrg("id3", "name3", "summary3", "city3", "companies3", "twitter3",
                                "website", "logo")

        self.assertEqual(example3.__repr__(), "<FinancialOrg 'name3'>")

    def test_financial_org_dictionary_1(self):
        """Test dictionary method of financial org class"""

        example1 = FinancialOrg("id", "name", "summary", "city", "companies", "twitter",
                                "website", "logo")
        dict_rep = example1.dictionary()

        self.assertEqual(dict_rep['financial_org_id'], "id")
        self.assertEqual(dict_rep['name'], "name")
        self.assertEqual(dict_rep['summary'], "summary")
        self.assertEqual(dict_rep['city'], "city")

    def test_financial_org_dictionary_2(self):
        """Test dictionary method of company class"""

        example1 = FinancialOrg("id", "name", "summary", "city", "companies", "twitter",
                                "website", "logo")
        dict_rep = example1.dictionary()

        self.assertEqual(dict_rep['companies'], "companies")
        self.assertEqual(dict_rep['twitter'], "twitter")
        self.assertEqual(dict_rep['website'], "website")
        self.assertEqual(dict_rep['logo_url'], "logo")

    def test_financial_org_dictionary_3(self):
        """Test dictionary method of financial org class"""

        example2 = FinancialOrg("id1", "Founders Fund",
                                ("Founders Fund is a San Francisco based venture capital firm which"
                                 + " invests at every stage in companies with revolutionary"
                                 + " technologies."),
                                "San Francisco", "Space Exploration Technologies", "foundersfund",
                                "http://www.foundersfund.com", "logo_url")

        dict_rep = example2.dictionary()

        self.assertEqual(dict_rep['financial_org_id'], "id1")
        self.assertEqual(dict_rep['name'], "Founders Fund")
        self.assertEqual(dict_rep['summary'],
                         ("Founders Fund is a San Francisco based venture capital firm which"
                          + " invests at every stage in companies with revolutionary"
                          + " technologies."))
        self.assertEqual(dict_rep['city'], "San Francisco")

    def test_financial_org_dictionary_4(self):
        """Test dictionary method of company class"""

        example2 = FinancialOrg("id1", "Founders Fund",
                                ("Founders Fund is a San Francisco based venture capital firm which"
                                 + " invests at every stage in companies with revolutionary"
                                 + " technologies."),
                                "San Francisco", "Space Exploration Technologies", "foundersfund",
                                "http://www.foundersfund.com", "logo_url")

        dict_rep = example2.dictionary()

        self.assertEqual(dict_rep['companies'],
                         "Space Exploration Technologies")
        self.assertEqual(dict_rep['twitter'], "foundersfund")
        self.assertEqual(dict_rep['website'], "http://www.foundersfund.com")
        self.assertEqual(dict_rep['logo_url'], "logo_url")

# ----------
# TestPerson
# ----------


class TestPerson(TestCase):
    """Tests for the methods of the Person model"""

    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp(self):
        with app.test_request_context():
            db.create_all()

    def tearDown(self):
        with app.test_request_context():
            db.session.remove()

    # ------
    # Person
    # ------

    def test_person_model_1(self):
        """Test adding Person objects to and deleting Person objects from the db"""

        with app.test_request_context():
            example1 = Person("id1", "name1", "summary1", "city1",
                              "companies1", "role1", "twitter1", "logo_url1")
            example2 = Person("id2", "name2", "summary2", "city2",
                              "companies2", "role2", "twitter2", "logo_url2")

            people1 = db.session.query(Person).all()

            db.session.add(example1)
            db.session.add(example2)
            db.session.commit()
            people2 = db.session.query(Person).all()

            self.assertTrue(example1 in people2)
            self.assertTrue(example2 in people2)
            self.assertEqual(len(people2), len(people1) + 2)

            db.session.delete(example1)
            db.session.delete(example2)
            db.session.commit()
            people3 = db.session.query(Person).all()

            self.assertTrue(example1 not in people3)
            self.assertTrue(example2 not in people3)
            self.assertEqual(len(people1), len(people2) - 2)

    def test_person_model_2(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            example1 = Person("id1", "name1", "summary1", "city1",
                              "companies1", "role1", "twitter1", "logo_url1")

            db.session.add(example1)
            db.session.commit()

            person = db.session.query(Person).filter_by(name="name1").first()
            self.assertEqual(person.city, "city1")
            self.assertEqual(person.twitter, "twitter1")

            db.session.delete(example1)
            db.session.commit()

    def test_person_init_1(self):
        """Test construction of a Person"""

        person1 = Person("id1", "name1", "summary1", "city1",
                         "companies1", "role1", "twitter1", "logo_url1")

        self.assertIsInstance(person1, Person)
        self.assertEqual(person1.person_id, "id1")
        self.assertEqual(person1.name, "name1")
        self.assertEqual(person1.summary, "summary1")
        self.assertEqual(person1.city, "city1")
        self.assertEqual(person1.companies, "companies1")
        self.assertEqual(person1.role, "role1")
        self.assertEqual(person1.twitter, "twitter1")
        self.assertEqual(person1.logo_url, "logo_url1")

    def test_person_init_2(self):
        """Test construction of two instances of Person"""

        person1 = Person("id1", "name1", "summary1", "city1",
                         "companies1", "role1", "twitter1", "logo_url1")
        person2 = Person("id2", "name1", "summary2", "city1",
                         "companies2", "role1", "twitter2", "logo_url1")

        self.assertNotEqual(person1.person_id, person2.person_id)
        self.assertEqual(person1.name, person2.name)
        self.assertNotEqual(person1.summary, person2.summary)
        self.assertEqual(person1.city, person2.city)
        self.assertNotEqual(person1.companies, person2.companies)
        self.assertEqual(person1.role, person2.role)
        self.assertNotEqual(person1.twitter, person2.twitter)
        self.assertEqual(person1.logo_url, person2.logo_url)

    def test_person_init_3(self):
        """Test construction of a Person with more realistic information"""

        person1 = Person("p:2", "Ben Elowitz", "Ben Elowitz is co-founder and CEO of Wetpaint.",
                         "null", "Wetpaint", "CEO", "elowitz",
                         ("http://s3.amazonaws.com/crunchbase_prod_assets/assets/images/resized/"
                          + "0001/8470/18470v3-max-250x250.jpg"))

        self.assertIsInstance(person1, Person)
        self.assertEqual(person1.person_id, "p:2")
        self.assertEqual(person1.name, "Ben Elowitz")
        self.assertEqual(
            person1.summary, "Ben Elowitz is co-founder and CEO of Wetpaint.")
        self.assertEqual(person1.city, "null")
        self.assertEqual(person1.companies, "Wetpaint")
        self.assertEqual(person1.role, "CEO")
        self.assertEqual(person1.twitter, "elowitz")
        self.assertEqual(person1.logo_url, ("http://s3.amazonaws.com/crunchbase_prod_assets/assets"
                                            + "/images/resized/0001/8470/18470v3-max-250x250.jpg"))

    def test_person_repr_1(self):
        """Test the representation of an instance of a Person"""

        person1 = Person("id1", "name1", "summary1", "city1",
                         "companies1", "role1", "twitter1", "logo_url1")
        self.assertEqual(person1.__repr__(), "<Person 'name1'>")

    def test_person_repr_2(self):
        """Test the representation of an instance of a Person"""

        person2 = Person("id2", "name1", "summary2", "city1",
                         "companies2", "role1", "twitter2", "logo_url1")
        self.assertEqual(person2.__repr__(), "<Person 'name1'>")

    def test_person_repr_3(self):
        """Test the representation of an instance of a Person"""

        person1 = Person("p:2", "Ben Elowitz", "Ben Elowitz is co-founder and CEO of Wetpaint.",
                         "null", "Wetpaint", "CEO", "elowitz",
                         ("http://s3.amazonaws.com/crunchbase_prod_assets/assets/images/resized/"
                          + "0001/8470/18470v3-max-250x250.jpg"))

        self.assertEqual(person1.__repr__(), "<Person 'Ben Elowitz'>")

    def test_person_dict_1(self):
        """Test dictionary of a Person"""

        person1 = Person("id1", "name1", "summary1", "city1",
                         "companies1", "role1", "twitter1", "logo_url1")
        p1_dict = person1.dictionary()

        self.assertIsInstance(p1_dict, dict)
        self.assertEqual(p1_dict,
                         {"person_id": "id1", "name": "name1", "summary": "summary1",
                          "city": "city1", "companies": "companies1", "role": "role1",
                          "twitter": "twitter1", "logo_url": "logo_url1"})

    def test_person_dict_2(self):
        """Test dictionaries of two instances of a Person"""

        person1 = Person("id1", "name1", "summary1", "city1",
                         "companies1", "role1", "twitter1", "logo_url1")
        p1_dict = person1.dictionary()
        person2 = Person("id2", "name1", "summary2", "city1",
                         "companies2", "role1", "twitter2", "logo_url1")
        p2_dict = person2.dictionary()

        self.assertNotEqual(p1_dict["person_id"], p2_dict["person_id"])
        self.assertEqual(p1_dict["name"], p2_dict["name"])
        self.assertNotEqual(p1_dict["summary"], p2_dict["summary"])
        self.assertEqual(p1_dict["city"], p2_dict["city"])
        self.assertNotEqual(p1_dict["companies"], p2_dict["companies"])
        self.assertEqual(p1_dict["role"], p2_dict["role"])
        self.assertNotEqual(p1_dict["twitter"], p2_dict["twitter"])
        self.assertEqual(p1_dict["logo_url"], p2_dict["logo_url"])

    def test_person_dict_3(self):
        """Test dictionary of a Person with more realistic information"""

        person1 = Person("p:2", "Ben Elowitz", "Ben Elowitz is co-founder and CEO of Wetpaint.",
                         "null", "Wetpaint", "CEO", "elowitz",
                         ("http://s3.amazonaws.com/crunchbase_prod_assets/assets/images/resized/"
                          + "0001/8470/18470v3-max-250x250.jpg"))

        p1_dict = person1.dictionary()

        self.assertIsInstance(p1_dict, dict)
        self.assertEqual(p1_dict,
                         {"person_id": "p:2", "name": "Ben Elowitz",
                          "summary": "Ben Elowitz is co-founder and CEO of Wetpaint.",
                          "city": "null", "companies": "Wetpaint", "role": "CEO",
                          "twitter": "elowitz",
                          "logo_url": ("http://s3.amazonaws.com/crunchbase_prod_assets/assets/"
                                       + "images/resized/0001/8470/18470v3-max-250x250.jpg")})


# --------
# TestCity
# --------

class TestCity(TestCase):
    """Tests for the methods of the City model"""

    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp(self):
        with app.test_request_context():
            db.create_all()

    def tearDown(self):
        with app.test_request_context():
            db.session.remove()

    # ----
    # City
    # ----

    def test_city_model_1(self):
        """Test adding City objects to and deleting City objects from the db"""

        with app.test_request_context():
            example1 = City("id1", "name1", "state1", "region1",
                            "companies1", "finorgs1", "people1")
            example2 = City("id2", "name2", "state2", "region2",
                            "companies2", "finorgs2", "people2")

            cities1 = db.session.query(City).all()

            db.session.add(example1)
            db.session.add(example2)
            db.session.commit()
            cities2 = db.session.query(City).all()

            self.assertTrue(example1 in cities2)
            self.assertTrue(example2 in cities2)
            self.assertEqual(len(cities2), len(cities1) + 2)

            db.session.delete(example1)
            db.session.delete(example2)
            db.session.commit()
            cities3 = db.session.query(City).all()

            self.assertTrue(example1 not in cities3)
            self.assertTrue(example2 not in cities3)
            self.assertEqual(len(cities1), len(cities2) - 2)

    def test_city_model_2(self):
        """Test querying the database by attribute using simple keywords"""

        with app.test_request_context():
            example1 = City("id1", "name1", "state1", "region1",
                            "companies1", "finorgs1", "people1")

            db.session.add(example1)
            db.session.commit()

            city = db.session.query(City).filter_by(name="name1").first()
            self.assertEqual(city.state, "state1")
            self.assertEqual(city.region, "region1")

            db.session.delete(example1)
            db.session.commit()

    def test_city_init_1(self):
        """Tests construction of a City"""

        city1 = City("id1", "name1", "state1", "region1",
                     "companies1", "finorgs1", "people1")

        self.assertIsInstance(city1, City)
        self.assertEqual(city1.city_id, "id1")
        self.assertEqual(city1.name, "name1")
        self.assertEqual(city1.state, "state1")
        self.assertEqual(city1.region, "region1")
        self.assertEqual(city1.companies, "companies1")
        self.assertEqual(city1.financial_orgs, "finorgs1")
        self.assertEqual(city1.people, "people1")

    def test_city_init_2(self):
        """Tests construction of two instances of City"""

        city1 = City("id1", "name1", "state1", "region1",
                     "companies1", "finorgs1", "people1")
        city2 = City("id2", "name1", "state2", "region1",
                     "companies2", "finorgs1", "people2")

        self.assertNotEqual(city1.city_id, city2.city_id)
        self.assertEqual(city1.name, city2.name)
        self.assertNotEqual(city1.state, city2.state)
        self.assertEqual(city1.region, city2.region)
        self.assertNotEqual(city1.companies, city2.companies)
        self.assertEqual(city1.financial_orgs, city2.financial_orgs)
        self.assertNotEqual(city1.people, city2.people)

    def test_city_init_3(self):
        """Test construction of a City with more realistic information"""

        city1 = City("1", "Seattle", "WA", "Seattle", "Wetpaint",
                     "Vulcan Capital", "Mathias Klein")

        self.assertIsInstance(city1, City)
        self.assertEqual(city1.city_id, "1")
        self.assertEqual(city1.name, "Seattle")
        self.assertEqual(city1.state, "WA")
        self.assertEqual(city1.region, "Seattle")
        self.assertEqual(city1.companies, "Wetpaint")
        self.assertEqual(city1.financial_orgs, "Vulcan Capital")
        self.assertEqual(city1.people, "Mathias Klein")

    def test_city_repr_1(self):
        """Test the representation of an instance of a City"""

        city1 = City("id1", "name1", "state1", "region1",
                     "companies1", "finorgs1", "people1")
        self.assertEqual(city1.__repr__(), "<City 'name1'>")

    def test_city_repr_2(self):
        """Test the representation of an instance of a City"""

        city2 = City("id2", "name1", "state2", "region1",
                     "companies2", "finorgs1", "people2")
        self.assertEqual(city2.__repr__(), "<City 'name1'>")

    def test_city_repr_3(self):
        """Test the representation of an instance of a City"""

        city1 = City("1", "Seattle", "WA", "Seattle", "Wetpaint",
                     "Vulcan Capital", "Mathias Klein")
        self.assertEqual(city1.__repr__(), "<City 'Seattle'>")

    def test_city_dict_1(self):
        """Tests dictionary of a City"""

        city1 = City("id1", "name1", "state1", "region1",
                     "companies1", "finorgs1", "people1")
        c1_dict = city1.dictionary()

        self.assertIsInstance(c1_dict, dict)
        self.assertEqual(c1_dict,
                         {"city_id": "id1", "name": "name1", "state": "state1", "region": "region1",
                          "companies": "companies1", "financial_orgs": "finorgs1",
                          "people": "people1"})

    def test_city_dict_2(self):
        """Tests dictionaries of two instances of a City"""

        city1 = City("id1", "name1", "state1", "region1",
                     "companies1", "finorgs1", "people1")
        c1_dict = city1.dictionary()
        city2 = City("id2", "name1", "state2", "region1",
                     "companies2", "finorgs1", "people2")
        c2_dict = city2.dictionary()

        self.assertNotEqual(c1_dict["city_id"], c2_dict["city_id"])
        self.assertEqual(c1_dict["name"], c2_dict["name"])
        self.assertNotEqual(c1_dict["state"], c2_dict["state"])
        self.assertEqual(c1_dict["region"], c2_dict["region"])
        self.assertNotEqual(c1_dict["companies"], c2_dict["companies"])
        self.assertEqual(c1_dict["financial_orgs"], c2_dict["financial_orgs"])
        self.assertNotEqual(c1_dict["people"], c2_dict["people"])

    def test_city_dict_3(self):
        """Test dictionary of a City with more realistic information"""

        city1 = City("1", "Seattle", "WA", "Seattle", "Wetpaint",
                     "Vulcan Capital", "Mathias Klein")
        c1_dict = city1.dictionary()

        self.assertIsInstance(c1_dict, dict)
        self.assertEqual(c1_dict,
                         {"city_id": "1", "name": "Seattle", "state": "WA", "region": "Seattle",
                          "companies": "Wetpaint", "financial_orgs": "Vulcan Capital",
                          "people": "Mathias Klein"})

# -----
# About
# -----


class TestAbout(TestCase):
    """Tests for the About page"""

    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp(self):
        """About tests have no database component"""

        httpretty.enable()  # enable HTTPretty so that it will monkey patch the socket module
        httpretty.register_uri(httpretty.GET, "http://yipit.com/",
                               body="Find the best daily deals")

    def tearDown(self):
        """Disable afterwards to let other code use that socket module"""

        httpretty.disable()
        httpretty.reset()

    # -----
    # About
    # -----

    def test_about_from_index(self):
        """Test traveling from index to about page"""

        link = 'http://startupfairy.com/'
        httpretty.register_uri(httpretty.GET, link)
        response = requests.get(link)
        self.assertEqual(200, response.status_code)

        link = 'http://startupfairy.com/about'
        httpretty.register_uri(httpretty.GET, link,
                               body='[{"title": "About | Startup Fairy"}]',
                               content_type="application/json")
        response = requests.get(link)
        self.assertEqual(200, response.status_code)
        #self.assertEqual('', httpretty.last_request().body)

    def test_about_from_category(self):
        """Test traveling from a category page to about page"""

        link = 'http://startupfairy.com/companies/'
        httpretty.register_uri(httpretty.GET, link)
        response = requests.get(link)
        self.assertEqual(200, response.status_code)

        link = 'http://startupfairy.com/about'
        httpretty.register_uri(httpretty.GET, link,
                               body='[{"title": "About | Startup Fairy"}]',
                               content_type="application/json")
        response = requests.get(link)
        self.assertEqual(200, response.status_code)

    def test_about_content(self):
        """Test for specific content of about page"""

        link = 'http://startupfairy.com/about'
        httpretty.register_uri(httpretty.GET, link,
                               body='[{"title": "About | Startup Fairy"}]',
                               content_type="application/json")

        response = requests.get(link)
        self.assertEqual(200, response.status_code)

# ---------------------
# Test Views.py methods
# ---------------------


class TestViews(TestCase):

    """Test the routing used by the application"""

    def test_index_1(self):
        """Test that index renders properly"""

        with app.test_request_context():
            self.assertEqual(index() is not None, True)

    def test_about_1(self):
        """Test that about renders properly"""

        with app.test_request_context():
            self.assertEqual(about() is not None, True)

    def test_category_1(self):
        """Test that category renders properly"""

        with app.test_request_context():
            self.assertEqual(category('people') is not None, True)

    def test_category_2(self):
        """Test that category renders properly"""

        with app.test_request_context():
            self.assertEqual(category('cities') is not None, True)

    def test_category_3(self):
        """Test that category renders properly"""

        with app.test_request_context():
            self.assertEqual(category('companies') is not None, True)

    def test_category_4(self):
        """Test that category renders properly"""

        with app.test_request_context():
            self.assertEqual(category('financialorgs') is not None, True)

    def test_category_5(self):
        """Test that category renders properly"""

        with app.test_request_context():
            self.assertEqual(category('nonexistent_category') is not None, True)

    def test_education_1(self):
        """Test that education renders properly"""

        with app.test_request_context():
            self.assertEqual(education() is not None, True)

    def test_page_not_found_1(self):
        """Test that page_not_found 404 renders properly"""

        with app.test_request_context():
            self.assertEqual(page_not_found('error') is not None, True)

# ----
# main
# ----

if __name__ == "__main__":
    main()
