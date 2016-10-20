#!flask/bin/python
from app import app
from os import environ
if environ.get('production', False):
	app.run(debug=True,host='0.0.0.0',port=80)
else:
	app.run(debug=True,host='0.0.0.0')
