DROP TABLE IF EXISTS dane_osobowe;
CREATE TABLE dane_osobowe
(
	Nr_ucznia INTEGER PRIMARY KEY,
	Dzien INTEGER NOT NULL,
	Miesiac INTEGER NOT NULL,
	Rok INTEGER NOT NULL,
	Miejsce_urodzenia TEXT 30,
	Wojewodztwo TEXT 30
);

DROP TABLE IF EXISTS nazwiska;
CREATE TABLE nazwiska
(
	Nr_ucznia INTEGER FOREIGN KEY,
	Nazwisko TEXT 25,
	Imie1 TEXT 20,
	Imie2 TEXT 20 DEFAULT NULL,
	FOREIGN KEY (Nr_ucznia) REFERENCES dane_osobowe(Nr_ucznia)
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny
(
	Nr_ucznia INTEGER FOREIGN KEY,
	Zachowanie TEXT 15,
	Rel_Ety INTEGER,
	Jpol INTEGER,
	Jang INTEGER,
	Jniem INTEGER,
	Matematyka INTEGER,
	Historia INTEGER,
	Geografia INTEGER,
	Biologia INTEGER,
	Fizyka INTEGER,
	Chemia INTEGER,
	Technika INTEGER,
	Informatyka INTEGER,
	Plastyka INTEGER,
	PO INTEGER,
	WF TEXT,
	FOREIGN KEY (Nr_ucznia) REFERENCES dane_osobowe(Nr_ucznia)
);