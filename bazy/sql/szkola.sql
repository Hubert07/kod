DROP TABLE IF EXISTS tbUczniowie;
CREATE TABLE tbUczniowie
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	imie TEXT,
	nazwisko TEXT,
	plec INTEGER,
	id_klasa INTEGER,
	egzaminHum NUMERIC NOT NULL DEFAULT 0,
	egzaminMat NUMERIC NOT NULL DEFAULT 0,
	egzaminJez NUMERIC NOT NULL DEFAULT 0,
	FOREIGN KEY (id_klasa) REFERENCES tbKlasy(id)
);

DROP TABLE IF EXISTS tbKlasy;
CREATE TABLE tbKlasy
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	klasa TEXT,
	rokNaboru INTEGER,
	rokMatury INTEGER
);

INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1A', 2017, 2020);
INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1B', 2017, 2020);
INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1C', 2017, 2020);
-- liczby nie są otoczone niczym
INSERT INTO tbUczniowie VALUES (NULL, 'Dałmian', 'Słodowy', 0, 2, 79, 80, 50);
INSERT INTO tbUczniowie VALUES (NULL, 'Hubert', 'Gajewski', 0, 1, 88, 92, 56);
INSERT INTO tbUczniowie VALUES (NULL, 'Michał', 'Rębiś', 0, 1, 90, 91, 80);
-- można pominąć wartości w () jak podamy wszysko
UPDATE tbUczniowie SET egzaminJez = 99 WHERE id = 1;