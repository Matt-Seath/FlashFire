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
    no_trades INTEGER NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stocks (id)
);

CREATE TABLE IF NOT EXISTS latestTrade (
    id INTEGER PRIMARY KEY,
    stock_id INTEGER NOT NULL,
    time TEXT NOT NULL,
    price NUMERIC NOT NULL,
    size NUMERIC NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stocks (id)
);

CREATE TABLE IF NOT EXISTS latestQuote (
    id INTEGER PRIMARY KEY,
    stock_id INTEGER NOT NULL,
    time TEXT NOT NULL,
    askPrice NUMERIC NOT NULL,
    askSize NUMERIC,
    bidPrice NUMERIC NOT NULL,
    bidSize NUMERIC NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stocks (id)
);


-- CREATE UNIQUE INDEX username_idx ON users (username);
-- CREATE UNIQUE INDEX stocks_idx ON stocks (symbol);
-- CREATE UNIQUE INDEX stockHistory_idx ON stockHistory (stock_id);
-- CREATE UNIQUE INDEX keys_idx ON dataKeys (keys);