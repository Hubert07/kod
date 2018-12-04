DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny
(
	IDucznia INTEGER,
	Ocena INTEGER,
	Data DATE,
	IDprzedmiotu INTEGER,
	FOREIGN KEY (IDprzedmiotu) REFERENCES przedmioty(IDprzedmiotu),
	FOREIGN KEY (IDucznia) REFERENCES uczniowie(IDucznia)
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty
(
	IDprzedmiotu INTEGER PRIMARY KEY,
	NazwaPrzedmiotu TEXT NOT NULL,
	Nazwisko_nauczyciela TEXT NOT NULL,
	Imie_nauczyciela TEXT NOT NULL
);

DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie
(
	IDucznia INTEGER PRIMARY KEY,
	Nazwisko TEXT NOT NULL,
	Imie TEXT NOT NULL,
	Ulica TEXT NOT NULL,
	IDklasy TEXT
);