CREATE TABLE IF NOT EXISTS expenses (
    id TEXT PRIMARY KEY NOT NULL UNIQUE,
);


CREATE TABLE IF NOT EXISTS users (
    id          TEXT PRIMARY KEY NOT NULL UNIQUE,
    username    TEXT UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS items (
    id              TEXT PRIMARY KEY NOT NULL UNIQUE,
    expenseId       INTEGER NOT NULL,
    costBearerId    INTEGER,
    name            TEXT    NOT NULL,
    price           INTEGER NOT NULL,

    UNIQUE(expenseId, costBearerId, id),

    FOREIGN KEY (expense_id)
    REFERENCES expenses (id) ON DELETE CASCADE,

    FOREIGN KEY (costBearerId)
    REFERENCES users (id)
);
