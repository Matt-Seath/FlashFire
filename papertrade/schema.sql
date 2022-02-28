DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS portfolio;
DROP TABLE IF EXISTS watchlist;

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
    stock TEXT NOT NULL,
    symbol TEXT NOT NULL,
    shares INTEGER NOT NULL,
    price NUMERIC NOT NULL,
    trade TEXT NOT NULL,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE watchlist (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    symbol TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE UNIQUE INDEX username_idx ON users (username);