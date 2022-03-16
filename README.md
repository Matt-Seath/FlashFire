# FlashFire

STATUS: CURRENTLY IN DEVELOPMENT
App: FlashFire is a web application that will reproduce behavior and features of the US stock markets, allowing users to execute orders with zero commissions through live trading functionality, or practice trading stocks without financial risk with paper trading.
Trading-Bot: FlashFire will also provide users with the option to utilise a paradigm of popular trading strategies that can be configured from the user interface to automatically execute trades on the users behalf. 
The app uses Aplacas Trade API to place orders and request historical data that is then inserted into a local sqlite database.
Created in Python, using the Flask framework.

Package dependencies:
    flask,
    flask-session,
    flask-wtf,
    requests,
    python-dotenv,
    alpaca-trade-api,
    email_validator,
    datetime

Usage:
    1: Install the latest version of Python and add to your PATH.
    2: Install package dependencies into your environment.
        -This can be achieved in your CLI by typing "pip install * ", where * is the name of the dependency you wish to install. 
    3: Configure the Alpaca API.
        -Alpacas api key and secret key are required by the app to send REST requests. Both can be obtained for free on their website.
        -Once you have obtained your keys, create a file: ".env" in the root flashfire directory.
        -Open .env using a text editor and paste the keys as values to their respective variables: "ALPACA_KEY=yourapikeyhere, ALPACA_SECRET=yoursecretkeyhere, PAPER_URL=yoururlhere"
    4: Construct the database.
        -Initialize the database by running the following cli command while in the root flashfire directory: "flask init-db"
        -Populate the database with: "python scripts/update_stocks.py", followed by: "python scripts/update_prices.py"
    5: Run flask from the CLI with: "flask run"

------------------PACKAGE TREE--------------------------

    FLASHFIRE
    ├───env
    ├───scripts
    │   ├───update_prices.py
    │   └───update_stocks.py
    ├───flashfire
    │   ├───static
    │   │   ├───css
    │   │   │   ├───bootstrap.css
    │   │   │   └───styles.css
    │   │   ├───js
    │   │   │   └───bootstrap.bundle.js
    │   │   └───images
    │   │       └───.ico and .svg files
    │   ├───templates
    │   │   ├───auth
    │   │   │   ├───change_password.html
    │   │   │   ├───login.html
    │   │   │   └───register.html
    │   │   ├───platform
    │   │   │   ├───index.html
    │   │   │   ├───portfolio.html
    │   │   │   ├───quote.html
    │   │   │   ├───settings.html
    │   │   │   ├───trading.html
    │   │   │   └───watchlist.html
    │   │   └───base.html
    │   ├───__init__.py
    │   ├───auth.py
    │   ├───db.py
    │   ├───forms.py
    │   ├───queries.py
    │   ├───platform.py
    │   └───schema.sql
    ├───.flaskenv
    ├───.gitignore
    ├───MANIFEST.in
    ├───README.md
    └───setup.py


--------------------------------------------------



















