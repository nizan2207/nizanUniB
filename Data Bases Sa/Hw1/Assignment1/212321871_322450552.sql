CREATE TABLE Realtors (
    rId INTEGER PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
	tel INTEGER NOT NULL,
    years INTEGER,
	CHECK (years>=5)
);
CREATE TABLE Buyers (
    bId INTEGER PRIMARY KEY,
    name VARCHAR(10),
    address VARCHAR(255),
	tel INTEGER NOT NULL
);
CREATE TABLE Houses (
    address VARCHAR(255) PRIMARY KEY,
    type VARCHAR(255),
	size INTEGER,
    rAmount INTEGER,
	rId INTEGER,
	CHECK(Houses.type='dual' OR Houses.type='private'),
	FOREIGN KEY (rId) REFERENCES Realtors(rId)
);
CREATE TABLE Features (
    address VARCHAR(255),
    feature VARCHAR(255),
    value VARCHAR(255) UNIQUE,
	CONSTRAINT pk_features PRIMARY KEY (address, feature),
	FOREIGN KEY (address) REFERENCES Houses(address)
);
CREATE TABLE Visits (
	bId INTEGER,
    address VARCHAR(255),
    rId INTEGER,
    impression VARCHAR(255) DEFAULT 'Good',
	CONSTRAINT pk_Visits PRIMARY KEY (bId,address,rId),
	CHECK (Visits.impression='Good' OR Visits.impression='Bad'),
	FOREIGN KEY (address) REFERENCES Houses(address),
	FOREIGN KEY (bId) REFERENCES Buyers(bId) ON DELETE CASCADE,
	FOREIGN KEY (rId) REFERENCES Realtors(rId)
);
CREATE TABLE Sales (
	sId INTEGER PRIMARY KEY,
    address VARCHAR(255) NOT NULL,
    sAmount INTEGER,
    bId INTEGER,
	sdate DATE,
	FOREIGN KEY (address) REFERENCES Houses(address),
	FOREIGN KEY (bId) REFERENCES Buyers(bId) ON DELETE CASCADE
);