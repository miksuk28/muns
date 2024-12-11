CREATE TABLE IF NOT EXISTS expenses (
    id TEXT PRIMARY KEY NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS users (
    id          TEXT PRIMARY KEY NOT NULL UNIQUE,
    username    TEXT UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS items (
    id              TEXT PRIMARY KEY NOT NULL UNIQUE,
    expenseId       TEXT NOT NULL,
    costBearerId    TEXT NOT NULL,
    name            TEXT    NOT NULL,
    price           INTEGER NOT NULL,

    UNIQUE(expenseId, costBearerId, name),

    FOREIGN KEY (expenseId)
    REFERENCES expenses (id) ON DELETE CASCADE,

    FOREIGN KEY (costBearerId)
    REFERENCES users (id)
);
