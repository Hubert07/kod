DROP TABLE IF EXISTS dane_kilent;
CREATE TABLE dane_kilent
(
	IDKlient INTEGER PRIMARY KEY AUTOINCREMENT,
	Imię_Klienta TEXT (20),
	Nazwisko_Klienta TEXT (25),
	Adres TEXT (70),
	Kod_pocztowy TEXT (6)
	Miasto TEXT (30)
	Wojewodztwo TEXT (35)
)

DROP TABLE IF EXISTS detale_zamowienia;
CREATE TABLE detale_zamowienia
(
	Numer_zamowienia INTEGER,
	Kod_zamowienia INTEGER PRIMARY KEY AUTOINCREMENT,

)

DROP TABLE IF EXISTS miasta;
CREATE TABLE miasta
(
)

DROP TABLE IF EXISTS miasta;
CREATE TABLE miasta
(
)

















id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
	nazwa_miasta TEXT (30),
	nazwa_wojewodztwa TEXT (35)
);

DROP TABLE IF EXISTS powierzchnia;
CREATE TABLE powierzchnia
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	powierzchnia_miasta DECIMAL,
	powierzchnia_zieleni DECIMAL,
	data_aktualizacji DATE,
	id_miasta INTEGER,
	FOREIGN KEY (id_miasta) REFERENCES miasta(id_miasta)
);

DROP TABLE IF EXISTS dane_gus;
CREATE TABLE dane_gus
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	liczba_mieszkancow INTEGER,
	liczba_kobiet INTEGER,
	grupa_wiekowa TEXT (15),
	data_aktualizacji DATE,
	id_miasta INTEGER,
	FOREIGN KEY (id_miasta) REFERENCES miasta(id_miasta)