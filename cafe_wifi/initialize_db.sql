create table cafe(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    map_url TEXT NOT NULL UNIQUE,
    img_url TEXT NOT NULL UNIQUE,
    location TEXT NOT NULL,
    has_sockets BOOLEAN NOT NULL,
    has_toiler BOOLEAN NOT NULL,
    has_wifi BOOLEAN NOT NULL,
    can_take_calls BOOLEAN NOT NULL,
    seats TEXT,
    coffee_price TEXT
);