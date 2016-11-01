#!flask/bin/python
"""
Runs the flask application for display at localhost
"""
from app import app

app.run(debug=True, host='0.0.0.0', port=80)
