CREATE DATABASE IF NOT EXISTS weapons_db;

USE DATABASE weapons_db;

CREATE TABLE table_name (
    id INT AUTO_INCREMENT,
    weapon_id VARCHAR(255),
    weapon_name VARCHAR(255),
    weapon_type VARCHAR(255),
    range_km INT,
    weight_kg FLOAT,
    manufacturer VARCHAR(255),
    origin_country VARCHAR(255),
    storage_location VARCHAR(255),
    year_estimated INT,
    level_risk VARCHAR(255),
    PRIMARY KEY (id)
);