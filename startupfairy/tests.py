# -------
# imports
# -------

#import httpretty
#import requests
from unittest import main, TestCase
#from app import app
from models import Company, FinancialOrg, Person, City, db

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

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    # -------
    # Company
    # -------

    def test_company(self):
        """
        Test retrieval of a single company entity
        """
        example = Company("Wetpaint",
                          "Wetpaint is a technology platform company that uses its proprietary state-of-the-art technology and expertise in social media to build and monetize audiences for digital publishers. Wetpaint?s own online property, Wetpaint Entertainment, an entertainment news site that attracts more than 12 million unique visitors monthly and has over 2 million Facebook fans, is a proof point to the company?s success in building and engaging audiences. Media companies can license Wetpaint?s platform which includes a dynamic playbook tailored to their individual needs and comprehensive training. Founded by Internet pioneer Ben Elowitz, and with offices in New York and Seattle, Wetpaint is backed by Accel Partners, the investors behind Facebook.",
                          [], "San Francisco", ["Youniversity Ventures"], "airbnb", "http://airbnb.com")

        self.assertEqual(example.city, "San Francisco")
        self.assertEqual(example.twitter, "airbnb")

        db.session.add(example)
        db.session.commit()
        companies = Company.query.all()

        self.assertEqual(len(companies), 1)
        self.assertEqual(example.dictionary(), companies[1].dictionary)


# ----------------
# TestFinancialOrg
# ----------------

class TestFinancialOrg(TestCase):
    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    # ------------
    # FinancialOrg
    # ------------

    def test_financial_org(self):
        """
        Test retrival of a financial organization entity
        """
        example = FinancialOrg("Founders Fund",
                               "Founders Fund is a San Francisco based venture capital firm which invests at every stage in companies with revolutionary technologies.  The firm's five partners, Peter Thiel, Sean Parker, Ken Howery, Luke Nosek, and Brian Singerman have been founders of or early investors in numerous well-known companies such as Facebook, PayPal, Napster, and Palantir Technologies. Founders Fund was formed in 2005 and has launched four funds to date with more than $1 billion in aggregate capital under management.",
                               "San Francisco", [
                                   "Space Exploration Technologies"], "foundersfund",
                               "http://www.foundersfund.com")

        self.assertEqual(example.city, "San Francisco")
        self.assertEqual(example.twitter, "foundersfund")

        db.session.add(example)
        db.session.commit()
        financial_orgs = FinancialOrg.query.all()

        self.assertEqual(len(financial_orgs), 1)
        self.assertEqual(example.dictionary(), financial_orgs[1].dictionary)


# ----------
# TestPerson
# ----------

class TestPerson(TestCase):
    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    # ------
    # Person
    # ------

    def test_Person(self):
        """
        Test retrival of single person organization
        """
        example = Person("Brian Chesky",
                         "Brian drives Airbnb's vision, strategy and growth. Always pushing the status quo, Brian aims to disrupt the industry with ideas that change the way people live. To grasp the full impact and experience of Airbnb, Brian rid himself of an apartment and has been living in the homes of the Airbnb community since June of 2010. He is committed to assembling a passionate, top tier team to deliver on this promise. Before Airbnb, Brian ran an industrial design shop in Los Angeles; even these days he is rarely seen without a drafting pen and sketch book in hand. Brian holds a Bachelor of Fine Arts in industrial design from the Rhode Island School of Design. He believes that what sets the company apart is the access to space that would otherwise be off limits, and haunted or not, he would be honored to someday stay in the Lincoln Bedroom through the site.",
                         "", ["Airbnb"], ["Co-founder & CEO"], "bchesky")

        self.assertEqual(example.city, "")
        self.assertEqual(example.twitter, "bchesky")

        db.session.add(example)
        db.session.commit()
        people = Person.query.all()

        self.assertEqual(len(people), 1)
        self.assertEqual(example.dictionary(), people[1].dictionary)


# --------
# TestCity
# --------

class TestCity(TestCase):
    # ------------------
    # Setup and Teardown
    # ------------------

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    # ----
    # City
    # ----

    def test_city(self):
        """
        Test retrival of a single city entity
        """
        example = City("Los Angeles", "CA", "Los Angeles", [
                       "Space Exploration Technologies"], [], ["Elon Musk"])

        self.assertEqual(example.state, "CA")
        self.assertEqual(example.region, "Los Angeles")

        db.session.add(example)
        db.session.commit()
        cities = City.query.all()

        self.assertEqual(len(cities), 1)
        self.assertEqual(example.dictionary(), cities[1].dictionary)

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
