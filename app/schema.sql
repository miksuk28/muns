CREATE TABLE IF NOT EXISTS expenses (
    id TEXT PRIMARY KEY NOT NULL UNIQUE,
);


CREATE TABLE IF NOT EXISTS users (
    id          TEXT PRIMARY KEY NOT NULL UNIQUE,
    username    TEXT UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS items (
    id              TEXT PRIMARY KEY NOT NULL UNIQUE,
    expense_id      INTEGER NOT NULL,
    cost_bearer_id  INTEGER,
    name            TEXT    NOT NULL,
    price           INTEGER NOT NULL,

    UNIQUE(expense_id, cost_bearer_id, id),

    FOREIGN KEY (expense_id)
    REFERENCES expenses (id) ON DELETE CASCADE,

    FOREIGN KEY (cost_bearer_id)
    REFERENCES users (id)
);
