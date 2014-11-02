-- PARAM user, password, dbname

CREATE USER 'sampleuser'@'localhost' IDENTIFIED BY '12345';
 GRANT ALL PRIVILEGES ON sampleapp.* TO 'sampleuser'@'localhost' IDENTIFIED BY '12345';
 GRANT SELECT ON mysql.proc TO 'sampleuser'@'localhost' IDENTIFIED BY '12345';