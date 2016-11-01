from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app

# initialize database object
db = SQLAlchemy(app)

# helper tables for many-to-many relationships
companies = db.Table('companies',
    db.Column('person_id', db.String, db.ForeignKey('company.id')),
    db.Column('company_id', db.String, db.ForeignKey('person.id'))
)

financial_orgs = db.Table('financial_orgs',
    db.Column('company_id', db.String, db.ForeignKey('financial_org_id')),
    db.Column('financial_org_id', db.String, db.ForeignKey('company.id'))
)

class Company(db.Model):
    __tablename__ = "company"
    # set column types
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True)
    summary = db.Column(db.String, unique=True)
    #people = db.Column(db.String)
    city_id = db.Column(db.String, db.ForeignKey('city.id'))
    financial_orgs = db.relationship('FinancialOrg', secondary=financial_orgs, backref=db.backref('companies', lazy='dynamic'))
    twitter = db.Column(db.String)
    website = db.Column(db.String)
    logo_url = db.Column(db.String)

    # set column values in constructor
    #def __init__(self, name, summary, people, city, financial_orgs, twitter, website, logo_url):
    def __init__(self, name, summary, financial_orgs, twitter, website, logo_url):
        self.name = name
        self.summary = summary
        #self.people = people
        #self.city = city
        self.financial_orgs = financial_orgs
        self.twitter = twitter
        self.website = website
        self.logo_url = logo_url

    def __repr__(self):
        return '<Company %r>' % self.name

    def dictionary(self):
        """Returns a dictionary representation of the class data"""
        dict_rep = {}
        dict_rep['id'] = self.id
        dict_rep['name'] = self.name
        dict_rep['summary'] = self.summary
        #dict_rep['people'] = self.people
        #dict_rep['city'] = self.city
        dict_rep['financial_orgs'] = self.financial_orgs
        dict_rep['twitter'] = self.twitter
        dict_rep['website'] = self.website
        dict_rep['logo_url'] = self.logo_url
        return dict_rep


class FinancialOrg(db.Model):
    __tablename__ = "financial_org"
    # set the column types
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True)
    summary = db.Column(db.String, unique=True)
    city_id = db.Column(db.String, db.ForeignKey('city.id'))
    #companies = db.Column(db.String)
    twitter = db.Column(db.String)
    website = db.Column(db.String)
    logo_url = db.Column(db.String)

    # set the column values in constructor
    #def __init__(self, name, summary, city, companies, twitter, website, logo_url):
    def __init__(self, name, summary, twitter, website, logo_url):
        self.name = name
        self.summary = summary
        #self.city = city
        #self.companies = companies
        self.twitter = twitter
        self.website = website
        self.logo_url = logo_url

    def __repr__(self):
        return '<FinancialOrg %r>' % self.name

    def dictionary(self):
        """Returns a dictionary representation of the class data"""
        dict_rep = {}
        dict_rep['id'] = self.id
        dict_rep['name'] = self.name
        dict_rep['summary'] = self.summary
        #dict_rep['city'] = self.city
        #dict_rep['companies'] = self.companies
        dict_rep['twitter'] = self.twitter
        dict_rep['website'] = self.website
        dict_rep['logo_url'] = self.logo_url
        return dict_rep


class Person(db.Model):
    __tablename__ = "person"
    # set the column types
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True)
    summary = db.Column(db.String, unique=True)
    city_id = db.Column(db.String, db.ForeignKey('city.id'))
    companies = db.relationship('Company', secondary=companies, backref=db.backref('people', lazy='dynamic'))
    role = db.Column(db.String) # a person has a different role for each company; not sure how to implement this yet
    twitter = db.Column(db.String)
    logo_url = db.Column(db.String)

    # set the column values in constructor
    def __init__(self, name, summary, companies, role, twitter, logo_url):
        self.name = name
        self.summary = summary
        #self.city = city
        self.companies = companies
        self.role = role
        self.twitter = twitter
        self.logo_url = logo_url

    def __repr__(self):
        return '<Person %r>' % self.name

    def dictionary(self):
        """Returns a dictionary representation of the class data"""
        dict_rep = {}
        dict_rep['id'] = self.id
        dict_rep['name'] = self.name
        dict_rep['summary'] = self.summary
        #dict_rep['city'] = self.city
        dict_rep['companies'] = self.companies
        dict_rep['role'] = self.role
        dict_rep['twitter'] = self.twitter
        dict_rep['logo_url'] = self.logo_url
        return dict_rep


class City(db.Model):
    __tablename__ = "city"
    # set the column types
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True)
    state = db.Column(db.String)
    region = db.Column(db.String)
    companies = db.relationship('Company', backref='city', lazy='dynamic')
    financial_orgs = db.relationship('FinancialOrg', backref='city', lazy='dynamic')
    people = db.relationship('Person', backref='city', lazy='dynamic')

    # set the column values in constructor
    def __init__(self, name, state, region, companies, financial_orgs, people):
        self.name = name
        self.state = state
        self.region = region
        self.companies = companies
        self.financial_orgs = financial_orgs
        self.people = people

    def __repr__(self):
        return '<City %r>' % self.name

    def dictionary(self):
        """Returns a dictionary representation of the class data"""
        dict_rep = {}
        dict_rep['id'] = self.id
        dict_rep['name'] = self.name
        dict_rep['state'] = self.state
        dict_rep['region'] = self.region
        dict_rep['companies'] = self.companies
        dict_rep['financial_orgs'] = self.financial_orgs
        dict_rep['people'] = self.people
        return dict_rep
