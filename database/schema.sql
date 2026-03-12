CREATE DATABASE wildvision;

USE wildvision;

CREATE TABLE detections(

id INT AUTO_INCREMENT PRIMARY KEY,

filename VARCHAR(255),

predicted_class VARCHAR(100),

confidence FLOAT,

image_path VARCHAR(255),

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);