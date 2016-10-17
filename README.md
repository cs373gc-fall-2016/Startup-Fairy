# TBD
IMD 4

### Setup 
Pretty much follows [this](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) tutorial.

1. `pip install virtualenv` - install virtualenv
2. `virtualenv flaskapp` - create your virtualenv
3. `source flaskapp/bin/activate` - you are now inside your virtualenv
4. `pip install flask flask-login flask-seqlalchemy sqlalchemy-migrate flask-whooshalchemy flask-wtf flask-babel guess_language flipflop coverage pylint autopep8` - installs stuff needed to run flask

### Development
Run `python run.py`, you will be able to see the site at `localhost:5000`