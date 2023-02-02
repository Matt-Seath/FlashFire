## FlashFire - Algorithmic Trading Platform

Hey you! Looking for a surefire way to turn your hard-earned savings into ash? Look no further than FlashFire, the algorithmic trading app that's hot, hot, hot! With its cutting-edge technology and scorching performance, FlashFire will light a fire under your portfolio and watch it burn to a crisp. Want to see your investment strategy go up in smoke? Download FlashFire today and watch the magic happen!

FlashFire achieves these feats as a full-stack algorithmic trading platform that automates the process of backtesting and regression analysis of stocks listed on the ASX. The platform uses historical financial data scraped from Yahoo Finance and live data from Interactive Brokers TWS API to find and buy into profitable trade opportunities.

## Technologies Used

-   Backend: Django
-   Frontend: Next.js
-   Broker: IBKR TWS
-   Database: MySQL

![architecture](https://user-images.githubusercontent.com/100132940/216249234-55b637ea-260a-4138-9c69-d24addc3def6.png)


## Installation Instructions

These instructions will help you to set up the project locally on your machine for development and testing purposes.

### Prerequisites
-   **Requires an active Interactive Brokers account to connect to the TWS API**
-   [Django](https://www.djangoproject.com/download/)
-   [Next.js](https://nextjs.org/docs#getting-started)
-   [Interactive Brokers TWS API](https://interactivebrokers.github.io/#tws-api-documentation)
-   [Python 3.x](https://www.python.org/downloads/)
-   [Node.js](https://nodejs.org/en/download/)

### Installing

1.  Clone the repository:

```
bashgit clone https://github.com/Matt-Seath/FlashFire.git

```

2.  Install the required packages:

```
pip install -r requirements.txt

```

3.  Set up environment variables for Interactive Brokers TWS API.
    
4.  Run migrations:
    

5.  Start the Django development server:

```
python manage.py runserver

```

6.  Change into the `frontend` directory and install the required packages:

```
bashcd frontend
npm install

```

7.  Start the Next.js development server:

## Usage

To use the platform, simply navigate to `http://localhost:3000` in your web browser. From there, you can run backtests, perform regression analysis, and make trades using the Interactive Brokers TWS API.

## Contributing

Contributions to the project are welcome! Please follow the guidelines in the [CONTRIBUTING.md](https://chat.openai.com/CONTRIBUTING.md) file to contribute.

## License

This project is licensed under the [MIT License](https://chat.openai.com/LICENSE).
