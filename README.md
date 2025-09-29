# README #

This Backend in designed using python and Alchemy ORM.
Postgres is used for the database management purpose

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Configuration
  * Clone the Repo 
  * go to the develop branch
  * create your own branch from develop 
    * Note: Do not use Master or Develop branch for development
  * create virtualenv from python version described
  * run "pip install -r requirements.txt" for the dependencies to install
  
* Dependencies
  * Python 
  * version: 3.10.13
  * Note: latest stable release at the time of configuration (1-Oct-2023)
  * Compatibility:
    * Flask
      * version: 2.3.3
      * Note: latest stable release at the time of configuration (1-Oct-2023)
    * Werkzeug
      * version: 3.0.0
      * Note: This is the compatible and latest release with Flask version. But any version greater than 2.3.6 can be used
    * Jinja2
      * version: 2.3.3
      * Note: latest stable release at the time of configuration (1-Oct-2023)
    * itsdangerous
      * version: 2.3.3
      * Note: latest stable release at the time of configuration (1-Oct-2023)
    * Click
      * version: 2.3.3
      * Note: latest stable release at the time of configuration (1-Oct-2023)
    * MarkupSafe
      * version: 2.3.3
      * Note: latest stable release at the time of configuration (1-Oct-2023)
    * Blinker
      * version: 1.6.2
      * Note: Most compatible version with Flask

* Database configuration
  * Postgres
    * version: 13.12
    * connector: sqlalchemy
      * version: 2.0.21
      * dependents: sqlalchemy.orm
        * version: 1.2.10
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact