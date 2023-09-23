## FlashFire - Algorithmic Trading Platform 🔥💸  

![2023-09-24_00-41](https://github.com/Matt-Seath/FlashFire/assets/100132940/1339e7aa-d58a-4a37-8add-11f9842ab5d5)

<em>Are you tired of making sensible, well-informed investment decisions and watching your money grow slowly over time? With FlashFire, you can say goodbye to all that tedious market research and analysis, and say hello to unpredictable and volatile trades that are guaranteed to keep you on the edge of your seat! FlashFires top-of-the-line, state-of-the-art, never-been-tested algorithms use cutting edge technology like random number generation and astrology to execute large, quick trades using your hard-earned cash!

## How it works:

-   Enter all your banking details and account information
-   Choose your preferred horoscope sign
-   Press the big red button labeled "IGNITE" 🔥
-   Sit back and experience an all-new level of stress as you watch your savings go up in flames!

So what are you waiting for? Download FlashFire today and start your journey towards financial ruin! 💸 </em>
<br>
<br>
## How it really works:

For those genuinely interested in my app, FlashFire is a serious full-stack algorithmic trading platform designed to automate the process of backtesting and regression analysis of stocks listed on the ASX. The system uses historical financial data scraped from Yahoo Finance for backtesting strategies and utilizes websocket API connections for live datafeeds from Interactive Brokers TWS to identify and buy into profitable trade opportunities based on a confidence rating that is produced by a dynamic series of algorithms. 
<br>
<br>

## Disclaimer:
**TO ENSURE THE APP FUNCTIONS WITHOUT GIVING UP MY PERSONAL TRADING STRATEGIES, ONLY BASIC ALGORITHMS ARE PUBLIC IN THIS REPO! SO UNLESS YOU ARE SERIOUS ABOUT LOSING MONEY, YOU SHOULD ONLY LINK PAPER ACCOUNTS TO THIS APP.**
<br>
<br>
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

1.  From a command prompt, clone the repository:

```
git clone https://github.com/Matt-Seath/FlashFire.git

```

2.  Install the required packages:

```
pip install -r requirements.txt

```

3.  Set up environment variables by running this script:

```
python manage.py setup

```
    
4.  Run migrations:
    
```
python manage.py migrate

```

7.  Start the Django development server:

```
python manage.py runserver

```

6.  In a new command prompt, "cd" into the `frontend` directory and install the required packages:

```
cd frontend
npm install

```

7.  Start the Next.js server:

```
npm run dev

```

8.  Run TWS and log into your account:


## Usage

To use the platform, simply navigate to `http://localhost:3000` in your web browser. From there, you can run backtests, perform regression analysis, and make trades using the Interactive Brokers TWS API.

## Contributing

Contributions to the project are welcome! Please follow the guidelines in the [CONTRIBUTING.md](https://chat.openai.com/CONTRIBUTING.md) file to contribute.

## License

This project is licensed under the [MIT License](https://chat.openai.com/LICENSE).
