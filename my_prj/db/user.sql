CREATE DATABASE prj_db;
USE prj_db;

CREATE TABLE user (
  id int unsigned NOT NULL AUTO_INCREMENT,
  first_name varchar(50) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO user(id, first_name) VALUES(1, "Kent");
