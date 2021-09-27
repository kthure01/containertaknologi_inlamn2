CREATE DATABASE prj_db;
USE prj_db;

CREATE TABLE user (
  id int unsigned NOT NULL AUTO_INCREMENT,
  name varchar(50) NOT NULL,
  age int unsigned NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO user(name, age) VALUES("Kent", 58);
