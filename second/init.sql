CREATE TABLE uid_user_table(
    id text NOT NULL,
    token text,
    name text,
    PRIMARY KEY(id)
);
CREATE TABLE user_files(
    id text NOT NULL,
    uid text,
    file text,
    PRIMARY KEY(id)
);