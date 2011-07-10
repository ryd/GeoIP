USE geoip;

CREATE TABLE blocks (
    startIpNum INT(15) UNSIGNED NOT NULL,
    endIpNum INT(10) UNSIGNED NOT NULL,
    locId INT(15) UNSIGNED NOT NULL
);

create unique index blocks_01 on blocks (startIpNum asc, endIpNum desc);
create unique index blocks_02 on blocks (startIpNum desc, endIpNum asc);
 
CREATE TABLE location (
    locId INT(15) UNSIGNED NOT NULL,
    country VARCHAR(2) NOT NULL,
    region VARCHAR(2) NOT NULL,
    city VARCHAR(45) NOT NULL,
    postalCode VARCHAR(10) NOT NULL,
    latitude VARCHAR(10) NOT NULL,
    longitude VARCHAR(10) NOT NULL,
    metroCode INT(5) UNSIGNED NOT NULL,
    areaCode INT(5) UNSIGNED NOT NULL
);

create unique index location_01 on location (locId asc);
