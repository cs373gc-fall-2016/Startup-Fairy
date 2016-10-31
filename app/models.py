from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.__init__ import app

# initialize database object
db = SQLAlchemy(app)


class Company(db.Model):
    __tablename__ = "company"
    # set column types
    name = db.Column(db.String, unique=True, primary_key=True)
    summary = db.Column(db.String, unique=True)
    people = db.Column(db.String)
    city = db.Column(db.String)
    financial_orgs = db.Column(db.String)
    twitter = db.Column(db.String)
    website = db.Column(db.String)

    # set column values in constructor
    def __init__(self, name, summary, people, city, financial_orgs, twitter, website):
        self.name = name
        self.summary = summary
        self.people = people
        self.city = city
        self.financial_orgs = financial_orgs
        self.twitter = twitter
        self.website = website

    def __repr__(self):
        return '<Company %r>' % self.name

    def dictionary(self):
        """Returns a dictionary representation of the class data"""
        dict_rep = {}
        dict_rep['name'] = self.name
        dict_rep['summary'] = self.summary
        dict_rep['people'] = self.people
        dict_rep['city'] = self.city
        dict_rep['financial_orgs'] = self.financial_orgs
        dict_rep['twitter'] = self.twitter
        dict_rep['website'] = self.website
        return dict_rep


class FinancialOrg(db.Model):
    __tablename__ = "financial_org"
    # set the column types
    name = db.Column(db.String, unique=True, primary_key=True)
    summary = db.Column(db.String, unique=True)
    city = db.Column(db.String)
    companies = db.Column(db.String)
    twitter = db.Column(db.String)
    website = db.Column(db.String)

    # set the column values in constructor
    def __init__(self, name, summary, city, companies, twitter, website):
        self.name = name
        self.summary = summary
        self.city = city
        self.companies = companies
        self.twitter = twitter
        self.website = website

    def __repr__(self):
        return '<FinancialOrg %r>' % self.name

    def dictionary(self):
        """Returns a dictionary representation of the class data"""
        dict_rep = {}
        dict_rep['name'] = self.name
        dict_rep['summary'] = self.summary
        dict_rep['city'] = self.city
        dict_rep['companies'] = self.companies
        dict_rep['twitter'] = self.twitter
        dict_rep['website'] = self.website
        return dict_rep


class Person(db.Model):
    __tablename__ = "person"
    # set the column types
    name = db.Column(db.String, unique=True, primary_key=True)
    summary = db.Column(db.String, unique=True)
    city = db.Column(db.String)
    companies = db.Column(db.String)
    role = db.Column(db.String)
    twitter = db.Column(db.String)

    # set the column values in constructor
    def __init__(self, name, summary, city, companies, role, twitter):
        self.name = name
        self.summary = summary
        self.city = city
        self.companies = companies
        self.role = role
        self.twitter = twitter

    def __repr__(self):
        return '<Person %r>' % self.name

    def dictionary(self):
        """Returns a dictionary representation of the class data"""
        dict_rep = {}
        dict_rep['name'] = self.name
        dict_rep['summary'] = self.summary
        dict_rep['city'] = self.city
        dict_rep['companies'] = self.companies
        dict_rep['role'] = self.role
        dict_rep['twitter'] = self.twitter
        return dict_rep


class City(db.Model):
    __tablename__ = "city"
    # set the column types
    name = db.Column(db.String, unique=True, primary_key=True)
    state = db.Column(db.String)
    country = db.Column(db.String)
    companies = db.Column(db.String)
    financial_orgs = db.Column(db.String)
    people = db.Column(db.String)

    # set the column values in constructor
    def __init__(self, name, state, country, companies, financial_orgs, people):
        self.name = name
        self.state = state
        self.country = country
        self.companies = companies
        self.financial_orgs = financial_orgs
        self.people = people

    def __repr__(self):
        return '<City %r>' % self.name

    def dictionary(self):
        """Returns a dictionary representation of the class data"""
        dict_rep = {}
        dict_rep['name'] = self.name
        dict_rep['state'] = self.state
        dict_rep['country'] = self.country
        dict_rep['companies'] = self.companies
        dict_rep['financial_orgs'] = self.financial_orgs
        dict_rep['people'] = self.people
        return dict_rep
