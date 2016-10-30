# StartupFairy
IMD 4

[Apiary Docs](http://docs.startupfairy.apiary.io/)
[Travis](https://travis-ci.org/cs373gc-fall-2016/Startup-Fairy)

### Setup 
You'll need
- [Docker]()
- [Docker-compose](https://docs.docker.com/compose/install/)

Run `docker-compose up -d`. 

### Development
You'll see the app at `localhost`

### Deployment

In order to run all the nifty tools inside . With the container running, run `docker exec -it startupfairy_app_1`

### Models
* Company
  * Name
  * Summary
  * Employees
  * City
  * Investors
  * Twitter
  * Website
  
* Financial Org
  * Name
  * Summary
  * City
  * Companies invested in
  * Twitter
  * Website
 
* People
  * Name
  * Bio
  * City
  * Company
  * Role
  * Twitter
 
* City
  * Name
  * State
  * Country 
  * Companies
  * Financial Orgs
  * People

### UML Diagram

http://yuml.me/83988bfb
   
  
