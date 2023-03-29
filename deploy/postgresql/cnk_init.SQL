CREATE TABLE user (
    id integer,
    surname text NOT NULL,
    address text,
);

CREATE TABLE items (
    id integer,
    name text NOT NULL,
    price decimal(6,2) NOT NULL
);
