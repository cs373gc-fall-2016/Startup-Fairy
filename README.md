# StartupFairy
IMD 4

[Apiary Docs](http://docs.startupfairy.apiary.io/)
[Travis](https://travis-ci.org/cs373gc-fall-2016/Startup-Fairy)

### Setup 
Pretty much follows [this](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) tutorial.

1. `pip install virtualenv` - install virtualenv
2. `virtualenv flaskapp` - create your virtualenv
3. `source flaskapp/bin/activate` - you are now inside your virtualenv
4. `pip install flask flask-login flask-sqlalchemy sqlalchemy-migrate flask-whooshalchemy flask-wtf flask-babel guess_language flipflop coverage pylint autopep8` - installs stuff needed to run flask
5. `npm install`
6. `bower install`

### Development
Run `python run.py`, you will be able to see the site at `localhost:5000`
