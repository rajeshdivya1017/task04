CREATE DATABASE auth_system;

USE auth_system;

CREATE TABLE users (

    id INT PRIMARY KEY AUTO_INCREMENT,

    username VARCHAR(100) UNIQUE,

    email VARCHAR(100),

    password VARCHAR(255),

    role VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);