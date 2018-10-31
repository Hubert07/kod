DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	imie TEXT,
	nazwisko TEXT,
	plec INTEGER,
	id_klasa INTEGER,
	egz_hum INTEGER,
	egz_mat INTEGER,
	egz_jez INTEGER,
	FOREIGN KEY (id_klasa) REFERENCES klasy(id)
);

DROP TABLE IF EXISTS klasy;
CREATE TABLE klasy
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	klasa TEXT (2),
	rok_naboru INTEGER,
	rok_matury INTEGER
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	przedmiot TEXT,
	imie_naucz TEXT,
	nazwisko_naucz TEXT,
	plec_naucz INTEGER
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	datad DATE,
	id_uczen INTEGER,
	id_przedmiot INTEGER,
	ocena DECIMAL,
	FOREIGN KEY (id_uczen) REFERENCES uczniowie(id),
	FOREIGN KEY (id_przedmiot) REFERENCES przedmioty(id)
);