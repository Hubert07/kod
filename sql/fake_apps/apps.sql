DROP TABLE IF EXISTS apps;
CREATE TABLE apps (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT DEFAULT '',
    downloads INTEGER,
    price DECIMAL DEFAULT NULL
);