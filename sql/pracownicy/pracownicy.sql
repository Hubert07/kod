DROP TABLE IF EXISTS pracownicy;
CREATE TABLE pracownicy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    nazwisko TEXT,
    kod TEXT,
    miasto_z TEXT,
    ulica TEXT,
    data_u DATE,
    miasto_u TEXT
);

DROP TABLE IF EXISTS kontakty;
CREATE TABLE kontakty (
    id_pracownika INTEGER,
    typ_k BOOLEAN,
    kontakt TEXT,
    uwagi TEXT DEFAULT NULL,
    FOREIGN KEY (id_pracownika) REFERENCES pracownicy(id)
);

DROP TABLE IF EXISTS place;
CREATE TABLE place (
    id_p INTEGER,
    id_s INTEGER,
    place DECIMAL,
    data_z DATE,
    FOREIGN KEY (id_p) REFERENCES pracownicy(id),
    FOREIGN KEY (id_s) REFERENCES stanowiska(id)
);

DROP TABLE IF EXISTS stanowiska;
CREATE TABLE stanowiska (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowisko TEXT
);