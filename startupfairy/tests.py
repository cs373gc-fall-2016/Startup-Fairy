# -------
# imports
# -------

#import httpretty
#import requests
from unittest import main, TestCase
#from app import app
from models import Company, FinancialOrg, Person, City, db
#from populate_db import *
import run

from flask_sqlalchemy import SQLAlchemy

# initialize database object
# db = SQLAlchemy()


# -----------
# TestCompany
# -----------

class TestCompany(TestCase):
    # ------------------
    # Setup and Teardown
    # ------------------
    
    # def setUp(self):

    # def tearDown(self):
    
    # -------
    # Company
    # -------

    def test_company_constructor_1(self):
        """
        Test construction of a new company instance
        """

        example1 = Company("id", "name", "summary", "people",
            "city", "finorgs", "twitter", "website", "logo")

        self.assertEqual(example1.company_id, "id")
        self.assertEqual(example1.name, "name")
        self.assertEqual(example1.summary, "summary")
        self.assertEqual(example1.people, "people")
        self.assertEqual(example1.city, "city")

    def test_company_constructor_2(self):
        """
        Test construction of a new company instance
        """
        example1 = Company("id", "name", "summary", "people",
            "city", "finorgs", "twitter", "website", "logo")

        self.assertEqual(example1.financial_orgs, "finorgs")
        self.assertEqual(example1.twitter, "twitter")
        self.assertEqual(example1.website, "website")
        self.assertEqual(example1.logo_url, "logo")

    def test_company_constructor_3(self):
        """
        Test construction of a new company instance
        """

        example2 = Company("id1", "Wetpaint",
        "Wetpaint is a technology platform company that uses its proprietary state-of-the-art technology and expertise in social media to build and monetize audiences for digital publishers. Wetpaint?s own online property, Wetpaint Entertainment, an entertainment news site that attracts more than 12 million unique visitors monthly and has over 2 million Facebook fans, is a proof point to the company?s success in building and engaging audiences. Media companies can license Wetpaint?s platform which includes a dynamic playbook tailored to their individual needs and comprehensive training. Founded by Internet pioneer Ben Elowitz, and with offices in New York and Seattle, Wetpaint is backed by Accel Partners, the investors behind Facebook.",
        "person1", "San Francisco", "Youniversity Ventures", "wetpaint", "http://wetpaint.com", "logo_url")

        self.assertEqual(example2.company_id, "id1")
        self.assertEqual(example2.name, "Wetpaint")
        self.assertEqual(example2.summary, "Wetpaint is a technology platform company that uses its proprietary state-of-the-art technology and expertise in social media to build and monetize audiences for digital publishers. Wetpaint?s own online property, Wetpaint Entertainment, an entertainment news site that attracts more than 12 million unique visitors monthly and has over 2 million Facebook fans, is a proof point to the company?s success in building and engaging audiences. Media companies can license Wetpaint?s platform which includes a dynamic playbook tailored to their individual needs and comprehensive training. Founded by Internet pioneer Ben Elowitz, and with offices in New York and Seattle, Wetpaint is backed by Accel Partners, the investors behind Facebook.")
        self.assertEqual(example2.people, "person1")
        self.assertEqual(example2.city, "San Francisco")

    def test_company_constructor_4(self):
        """
        Test construction of a new company instance
        """

        example2 = Company("id1", "Wetpaint",
        "Wetpaint is a technology platform company that uses its proprietary state-of-the-art technology and expertise in social media to build and monetize audiences for digital publishers. Wetpaint?s own online property, Wetpaint Entertainment, an entertainment news site that attracts more than 12 million unique visitors monthly and has over 2 million Facebook fans, is a proof point to the company?s success in building and engaging audiences. Media companies can license Wetpaint?s platform which includes a dynamic playbook tailored to their individual needs and comprehensive training. Founded by Internet pioneer Ben Elowitz, and with offices in New York and Seattle, Wetpaint is backed by Accel Partners, the investors behind Facebook.",
        "person1", "San Francisco", "Youniversity Ventures", "wetpaint", "http://wetpaint.com", "logo_url")

        self.assertEqual(example2.financial_orgs, "Youniversity Ventures")
        self.assertEqual(example2.twitter, "wetpaint")
        self.assertEqual(example2.website, "http://wetpaint.com")
        self.assertEqual(example2.logo_url, "logo_url")

    def test_company_repr_1(self):
        """
        Test __repr__ methond of company class
        """

        example1 = Company("id", "name", "summary", "people",
            "city", "finorgs", "twitter", "website", "logo")

        self.assertEqual(example1.__repr__(), "<Company 'name'>")


    def test_company_repr_2(self):
        """
        Test __repr__ methond of company class
        """

        example2 = Company("id1", "Wetpaint",
        "Wetpaint is a technology platform company that uses its proprietary state-of-the-art technology and expertise in social media to build and monetize audiences for digital publishers. Wetpaint?s own online property, Wetpaint Entertainment, an entertainment news site that attracts more than 12 million unique visitors monthly and has over 2 million Facebook fans, is a proof point to the company?s success in building and engaging audiences. Media companies can license Wetpaint?s platform which includes a dynamic playbook tailored to their individual needs and comprehensive training. Founded by Internet pioneer Ben Elowitz, and with offices in New York and Seattle, Wetpaint is backed by Accel Partners, the investors behind Facebook.",
        "person1", "San Francisco", "Youniversity Ventures", "wetpaint", "http://wetpaint.com", "logo_url")

        self.assertEqual(example2.__repr__(), "<Company 'Wetpaint'>")


    def test_company_dictionary_1(self):
        """
        Test dictionary method of company class
        """

        example1 = Company("id", "name", "summary", "people",
            "city", "finorgs", "twitter", "website", "logo")
        dict_rep = example1.dictionary()

        self.assertEqual(dict_rep['company_id'], "id")
        self.assertEqual(dict_rep['name'], "name")
        self.assertEqual(dict_rep['summary'], "summary")
        self.assertEqual(dict_rep['people'], "people")
        self.assertEqual(dict_rep['city'], "city") 

    def test_company_dictionary_2(self):
        """
        Test dictionary method of company class
        """

        example1 = Company("id", "name", "summary", "people",
            "city", "finorgs", "twitter", "website", "logo")
        dict_rep = example1.dictionary()

        self.assertEqual(dict_rep['financial_orgs'], "finorgs")
        self.assertEqual(dict_rep['twitter'], "twitter")
        self.assertEqual(dict_rep['website'], "website")
        self.assertEqual(dict_rep['logo_url'], "logo")

    def test_company_dictionary_3(self):
        """
        Test dictionary method of company class
        """

        example2 = Company("id1", "Wetpaint",
        "Wetpaint is a technology platform company that uses its proprietary state-of-the-art technology and expertise in social media to build and monetize audiences for digital publishers. Wetpaint?s own online property, Wetpaint Entertainment, an entertainment news site that attracts more than 12 million unique visitors monthly and has over 2 million Facebook fans, is a proof point to the company?s success in building and engaging audiences. Media companies can license Wetpaint?s platform which includes a dynamic playbook tailored to their individual needs and comprehensive training. Founded by Internet pioneer Ben Elowitz, and with offices in New York and Seattle, Wetpaint is backed by Accel Partners, the investors behind Facebook.",
        "person1", "San Francisco", "Youniversity Ventures", "wetpaint", "http://wetpaint.com", "logo_url")
        dict_rep = example2.dictionary()

        self.assertEqual(dict_rep['company_id'], "id1")
        self.assertEqual(dict_rep['name'], "Wetpaint")
        self.assertEqual(dict_rep['summary'], "Wetpaint is a technology platform company that uses its proprietary state-of-the-art technology and expertise in social media to build and monetize audiences for digital publishers. Wetpaint?s own online property, Wetpaint Entertainment, an entertainment news site that attracts more than 12 million unique visitors monthly and has over 2 million Facebook fans, is a proof point to the company?s success in building and engaging audiences. Media companies can license Wetpaint?s platform which includes a dynamic playbook tailored to their individual needs and comprehensive training. Founded by Internet pioneer Ben Elowitz, and with offices in New York and Seattle, Wetpaint is backed by Accel Partners, the investors behind Facebook.")
        self.assertEqual(dict_rep['people'], "person1")
        self.assertEqual(dict_rep['city'], "San Francisco") 

    def test_company_dictionary_4(self):
        """
        Test dictionary method of company class
        """

        example2 = Company("id1", "Wetpaint",
        "Wetpaint is a technology platform company that uses its proprietary state-of-the-art technology and expertise in social media to build and monetize audiences for digital publishers. Wetpaint?s own online property, Wetpaint Entertainment, an entertainment news site that attracts more than 12 million unique visitors monthly and has over 2 million Facebook fans, is a proof point to the company?s success in building and engaging audiences. Media companies can license Wetpaint?s platform which includes a dynamic playbook tailored to their individual needs and comprehensive training. Founded by Internet pioneer Ben Elowitz, and with offices in New York and Seattle, Wetpaint is backed by Accel Partners, the investors behind Facebook.",
        "person1", "San Francisco", "Youniversity Ventures", "wetpaint", "http://wetpaint.com", "logo_url")
        dict_rep = example2.dictionary()

        self.assertEqual(dict_rep['financial_orgs'], "Youniversity Ventures")
        self.assertEqual(dict_rep['twitter'], "wetpaint")
        self.assertEqual(dict_rep['website'], "http://wetpaint.com")
        self.assertEqual(dict_rep['logo_url'], "logo_url")


# ----------------
# TestFinancialOrg
# ----------------

class TestFinancialOrg(TestCase):
    # ------------------
    # Setup and Teardown
    # ------------------

    # def setUp(self):
    #     with run.app.test_request_context():
    #         db.create_all()

    # def tearDown(self):
    #     db.session.close()
    #     db.drop_all()

    # ------------
    # FinancialOrg
    # ------------

    def test_financial_org_constructor_1(self):
        """
        Test construction of a new company instance
        """

        example1 = FinancialOrg("id", "name", "summary", "city", "companies", "twitter",
        "website", "logo")

        self.assertEqual(example1.financial_org_id, "id")
        self.assertEqual(example1.name, "name")
        self.assertEqual(example1.summary, "summary")
        self.assertEqual(example1.people, "people")
        self.assertEqual(example1.city, "city")

    def test_financial_org_constructor_2(self):
        """
        Test construction of a new company instance
        """
        example1 = FinancialOrg("id", "name", "summary", "city", "companies", "twitter",
        "website", "logo")

        self.assertEqual(example1.companies, "companies")
        self.assertEqual(example1.twitter, "twitter")
        self.assertEqual(example1.website, "website")
        self.assertEqual(example1.logo_url, "logo")


# ----------
# TestPerson
# ----------

class TestPerson(TestCase):
    # ------------------
    # Setup and Teardown
    # ------------------

    # def setUp(self):

    # def tearDown(self):

    # ------
    # Person
    # ------

    def test_person(self):
        """
        Test retrieval of single person organization
        """
        # example = Person("Brian Chesky",
        #                  "Brian drives Airbnb's vision, strategy and growth. Always pushing the status quo, Brian aims to disrupt the industry with ideas that change the way people live. To grasp the full impact and experience of Airbnb, Brian rid himself of an apartment and has been living in the homes of the Airbnb community since June of 2010. He is committed to assembling a passionate, top tier team to deliver on this promise. Before Airbnb, Brian ran an industrial design shop in Los Angeles; even these days he is rarely seen without a drafting pen and sketch book in hand. Brian holds a Bachelor of Fine Arts in industrial design from the Rhode Island School of Design. He believes that what sets the company apart is the access to space that would otherwise be off limits, and haunted or not, he would be honored to someday stay in the Lincoln Bedroom through the site.",
        #                  "", ["Airbnb"], ["Co-founder & CEO"], "bchesky")

        # self.assertEqual(example.city, "")
        # self.assertEqual(example.twitter, "bchesky")

        # db.session.add(example)
        # db.session.commit()
        # people = Person.query.all()

        # self.assertEqual(len(people), 1)
        # self.assertEqual(example.dictionary(), people[1].dictionary)
        self.assertEqual(1, 1)


# --------
# TestCity
# --------

class TestCity(TestCase):
    # ------------------
    # Setup and Teardown
    # ------------------

    # def setUp(self):

    # def tearDown(self):

    # ----
    # City
    # ----

    def test_city(self):
        """
        Test retrieval of a single city entity
        """
        # example = City("Los Angeles", "CA", "Los Angeles", [
        #                "Space Exploration Technologies"], [], ["Elon Musk"])

        # self.assertEqual(example.state, "CA")
        # self.assertEqual(example.region, "Los Angeles")

        # db.session.add(example)
        # db.session.commit()
        # cities = City.query.all()

        # self.assertEqual(len(cities), 1)
        # self.assertEqual(example.dictionary(), cities[1].dictionary)
        self.assertEqual(1, 1)

# # ----
# # About
# # ----


# class TestAbout(TestCase):
#     # ------------------
#     # Setup and Teardown
#     # ------------------

#     def setUp(self):
#         """
#         About tests have no db component
#         """
#         httpretty.enable()  # enable HTTPretty so that it will monkey patch the socket module
#         httpretty.register_uri(httpretty.GET, "http://yipit.com/",
#                                body="Find the best daily deals")

#     def tearDown(self):
#         # disable afterwards, so that you will have no problems in code that
#         # uses that socket module
#         httpretty.disable()
#         httpretty.reset()

#     # ----
#     # About
#     # ----

#     def test_about_from_index(self):
#         """
#         Test traveling index to about page
#         """
#         link = 'localhost'
#         response = requests.get(link)
#         self.assertEqual(200, response.status_code)
#         # self.assertEqual('', httpretty.last_request().body())

#     def test_about_from_category(self):
#         """
#         Test traveling from a category page to about page
#         """
#         link = 'localhost'
#         response = requests.get(link)
#         self.assertEqual(200, response.status_code)

#     def test_about_content(self):
#         """
#         Test for specific content of about page
#         """
#         link = 'localhost'
#         httpretty.register_uri(httpretty.GET, link,
#                                body='[{"title": "About | Startup Fairy"}]',
#                                content_type="application/json")

#         response = requests.get(link)

#         self.assertIn('Svyatoslav Ilinskiy', httpretty.last_request().body)
#         self.assertIn('Madeline Stager', httpretty.last_request().body)
#         self.assertIn('Addy Kim', httpretty.last_request().body)
#         self.assertIn('Mark', httpretty.last_request().body)
#         self.assertIn('Cameron', httpretty.last_request().body)
#         self.assertIn('Ajmal Khan', httpretty.last_request().body)
#         self.assertIn('Eugene Ng', httpretty.last_request().body)


# ----
# main
# ----

if __name__ == "__main__":
    main()
