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
    employees = db.Column(db.String)
    city = db.Column(db.String)
    investors = db.Column(db.String)
    twitter = db.Column(db.String)
    website = db.Column(db.String)
    # set column values in constructor
    def __init__(name, summary, employees, city, investors, twitter, website):
        self.name = name
        self.summary = summary
        self.employees = employees
        self.city = city
        self.investors = investors
        self.twitter = twitter
        self.website = website

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

class Person(db.Model):
    __tablename__ = "person"
    # set the column types
    name = db.Column(db.String, unique=True, primary_key=True)
    bio = db.Column(db.String, unique=True)
    location = db.Column(db.String)
    company = db.Column(db.String)
    role = db.Column(db.String)
    twitter = db.Column(db.String)
    # set the column values in constructor
    def __init__(name, bio, location, company, role, twitter):
        self.name = name
        self.bio = bio
        self.location = location
        self.company = company
        self.role = role
        self.twitter = twitter

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
