--FlashFire Database SCHEMA--
--Initialized with GLI command: $flask init-db


CREATE TABLE IF NOT EXISTS  users (
    id INTEGER, 
    username TEXT NOT NULL, 
    email TEXT NOT NULL,
    hash TEXT NOT NULL, 
    cash NUMERIC NOT NULL DEFAULT 10000.00, 
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    is_live BOOLEAN NOT NULL DEFAULT 0,
    has_traded BOOLEAN NOT NULL DEFAULT 0,
    use_dark_theme BOOLEAN NOT NULL DEFAULT 0,
    has_watchlist BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS portfolio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    symbol TEXT NOT NULL,
    shares INTEGER NOT NULL,
    price NUMERIC NOT NULL,
    trade TEXT NOT NULL,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL UNIQUE,
    company TEXT NOT NULL,
    exchange TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS watchlist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    stock_id TEXT NOT NULL UNIQUE,
    FOREIGN KEY(user_id) REFERENCES users(id)
    FOREIGN KEY(stock_id) REFERENCES stocks(id)
);

CREATE TABLE IF NOT EXISTS stockHistory (
    id INTEGER PRIMARY KEY,
    stock_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    open NUMERIC NOT NULL,
    high NUMERIC NOT NULL,
    low NUMERIC NOT NULL,
    close NUMERIC NOT NULL,
    volume INTEGER NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stocks (id)
);

CREATE TABLE IF NOT EXISTS stockLatest (
    id INTEGER PRIMARY KEY,
    stock_id INTEGER NOT NULL,
    avgTotalVolume NUMERIC NOT NULL,
    change NUMERIC NOT NULL,
    changePercent NUMERIC NOT NULL,
    close NUMERIC NOT NULL,
    delayedPrice NUMERIC NOT NULL,
    extendedChangePercent NUMERIC NOT NULL,
    extendedPrice NUMERIC NOT NULL,
    high NUMERIC NOT NULL,
    highTime NUMERIC NOT NULL,
    iexAskPrice NUMERIC NOT NULL,
    iexAskSize NUMERIC NOT NULL,
    iexBidPrice NUMERIC NOT NULL,
    iexBidSize NUMERIC NOT NULL,
    iexClose NUMERIC NOT NULL,
    iexCloseTime NUMERIC NOT NULL,
    iexLastUpdated NUMERIC NOT NULL,
    iexMarketPercent NUMERIC NOT NULL,
    iexOpen TEXT NOT NULL,
    iexOpenTime NUMERIC NOT NULL,
    iexNUMERICtimePrice NUMERIC NOT NULL,
    iexNUMERICtimeSize NUMERIC NOT NULL,
    iexVolume NUMERIC NOT NULL,
    lastTradeTime NUMERIC NOT NULL,
    latestPrice NUMERIC NOT NULL,
    latestSource TEXT NOT NULL,
    latestTime NUMERIC NOT NULL,
    latestUpdate NUMERIC NOT NULL,
    latestVolume NUMERIC NOT NULL,
    low NUMERIC NOT NULL,
    lowTime NUMERIC NOT NULL,
    open NUMERIC NOT NULL,
    peRatio NUMERIC NOT NULL,
    previousClose NUMERIC NOT NULL,
    previousVolume NUMERIC NOT NULL,
    volume NUMERIC NOT NULL,
    week52High NUMERIC NOT NULL,
    week52Low NUMERIC NOT NULL,
    ytdChange NUMERIC NOT NULL,
    isUSMarketOpen TEXT NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stocks (id)
);


-- CREATE UNIQUE INDEX username_idx ON users (username);
-- CREATE UNIQUE INDEX stocks_idx ON stocks (symbol);
-- CREATE UNIQUE INDEX stockHistory_idx ON stockHistory (stock_id);
-- CREATE UNIQUE INDEX keys_idx ON dataKeys (keys);