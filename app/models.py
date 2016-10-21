from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app

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
    def __init__(name, summary, people, city, financial_orgs, twitter, website):
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
        dictRep = {}
        dictRep['name'] = self.name
        dictRep['summary'] = self.summary
        dictRep['people'] = self.people
        dictRep['city'] = self.city
        dictRep['financial_orgs'] = self.financial_orgs
        dictRep['twitter'] = self.twitter
        dictRep['website'] = self.website
        return dictRep


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
    def __init__(name, summary, city, companies, twitter, website):
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
        dictRep = {}
        dictRep['name'] = self.name
        dictRep['summary'] = self.summary
        dictRep['city'] = self.city
        dictRep['companies'] = self.companies
        dictRep['twitter'] = self.twitter
        dictRep['website'] = self.website
        return dictRep


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
    def __init__(name, summary, city, companies, role, twitter):
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
        dictRep = {}
        dictRep['name'] = self.name
        dictRep['summary'] = self.summary
        dictRep['city'] = self.city
        dictRep['companies'] = self.companies
        dictRep['role'] = self.role
        dictRep['twitter'] = self.twitter
        return dictRep


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
    def __init__(name, state, country, companies, financial_orgs, people):
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
        dictRep = {}
        dictRep['name'] = self.name
        dictRep['state'] = self.state
        dictRep['country'] = self.country
        dictRep['companies'] = self.companies
        dictRep['financial_orgs'] = self.financial_orgs
        dictRep['people'] = self.people
        return dictRep
