-- param dbname
USE sampleapp;

CREATE TABLE IF NOT EXISTS sampleapp.camel_db_version (
	version int,
	PRIMARY KEY(version)
);

DROP FUNCTION IF EXISTS sampleapp.camel_check_version;
DELIMITER $$
CREATE FUNCTION sampleapp.camel_check_version(version INT) RETURNS INT
    BEGIN
    RETURN version = (SELECT * FROM camel_db_version);
END $$
DELIMITER ;


DROP FUNCTION IF EXISTS sampleapp.camel_update_version;
DELIMITER $$
CREATE FUNCTION sampleapp.camel_update_version(currentVersion INT, newVersion INT) RETURNS INT
    BEGIN
	IF (SELECT camel_check_version(currentVersion) = 1) THEN
		UPDATE camel_db_version SET version = newVersion;
		RETURN 1;
	ELSE
		RETURN 0;
	END IF;
END $$
DELIMITER ;

DROP FUNCTION IF EXISTS sampleapp.camel_get_schema_version;
DELIMITER $$
CREATE FUNCTION sampleapp.camel_get_schema_version() RETURNS INT
	BEGIN
	    DECLARE result INT;
	    SELECT version INTO result FROM camel_db_version;
	    RETURN result;
	END $$
DELIMITER ;


-- SET default version
DELETE FROM camel_db_version;
INSERT INTO camel_db_version(version) VALUES (
	1
);
