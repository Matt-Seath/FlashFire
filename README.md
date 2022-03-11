# Papertrade

Papertrade is a web application that reproduces behavior and features of a stock market, so that a user may practice trading stocks without financial risk.

Created in Python, using the Flask framework.

Package dependencies:
    flask
    flask-session
    flask-wtf
    requests
    python-dotenv

Usage:
    -Install dependencies into the environment
    -Set required API_KEYs to an .env file
    -Initialize the database by running the following cli command in the root directory:   $ flask init-db
    -Run flask with:    $ flask run

------------------PACKAGE TREE--------------------------

    PAPERTRADE
    ├───env
    ├───papertrade
    │   ├───static
    │   │   ├───css
    │   │   │   ├───bootstrap.css
    │   │   │   └───styles.css
    │   │   ├───js
    │   │   │   └───bootstrap.bundle.js
    │   │   └───icons
    │   │       └───plane.ico
    │   ├───templates
    │   │   ├───auth
    │   │   │   ├───change_password.html
    │   │   │   ├───login.html
    │   │   │   └───register.html
    │   │   ├───platform
    │   │   │   ├───index.html
    │   │   │   ├───portfolio.html
    │   │   │   ├───quotes.html
    │   │   │   ├───settings.html
    │   │   │   ├───trading.html
    │   │   │   └───watchlist.html
    │   │   └───base.html
    │   ├───__init__.py
    │   ├───auth.py
    │   ├───db.py
    │   ├───forms.py
    │   ├───models.py
    │   ├───platform.py
    │   └───schema.sql
    ├───.flaskenv
    ├───.gitignore
    ├───app.py
    ├───MANIFEST.in
    ├───README.md
    └───setup.py


--------------------------------------------------



















