DROP TABLE IF EXISTS tbOrders;
CREATE TABLE tbOrders
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	customers_id INTEGER,
	subscription_id INTEGER,
	purchase_date DATE,
	FOREIGN KEY (customers_id) REFERENCES tbCustomers(id),
	FOREIGN KEY (subscription_id) REFERENCES tbSubscription(id)
);

DROP TABLE IF EXISTS tbCustomers;
CREATE TABLE tbCustomers
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	adress TEXT NOT NULL
);

DROP TABLE IF EXISTS tbSubscription;
CREATE TABLE tbSubscription
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT NOT NULL,
	price_per_month INTEGER,
	subscription_length
);