CREATE DATABASE demo_db;

USE demo_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50)
);

INSERT INTO users (name, email)
VALUES ('Yogesh', 'yogesh@gmail.com');
