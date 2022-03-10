DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS portfolio;
DROP TABLE IF EXISTS stocks;
DROP TABLE IF EXISTS watchlist;
DROP TABLE IF EXISTS stockHistory;
DROP TABLE IF EXISTS dataKeys;

CREATE TABLE users (
    id INTEGER, 
    username TEXT NOT NULL, 
    email TEXT NOT NULL,
    hash TEXT NOT NULL, 
    cash NUMERIC NOT NULL DEFAULT 10000.00, 
    PRIMARY KEY(id)
);

CREATE TABLE portfolio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    symbol TEXT NOT NULL,
    shares INTEGER NOT NULL,
    price NUMERIC NOT NULL,
    trade TEXT NOT NULL,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE stocks (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL UNIQUE,
    company TEXT NOT NULL
);

CREATE TABLE watchlist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    symbol TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE stockHistory (
    id INTEGER PRIMARY KEY,
    stock_id INTEGER,
    date NOT NULL,
    open NOT NULL,
    high NOT NULL,
    low NOT NULL,
    close NOT NULL,
    adj_close NOT NULL,
    volume NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stocks (id)
);

CREATE TABLE dataKeys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    keys INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE UNIQUE INDEX username_idx ON users (username);
CREATE UNIQUE INDEX stocks_idx ON stocks (symbol);
CREATE UNIQUE INDEX stockHistory_idx ON stockHistory (stock_id);
CREATE UNIQUE INDEX keys_idx ON dataKeys (keys);