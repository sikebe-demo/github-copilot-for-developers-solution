-- Create the 'cats' table
CREATE TABLE cats (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    breed VARCHAR(50)
);

-- Insert random data into the 'cats' table
INSERT INTO cats (name, age, breed) VALUES ('Whiskers', 2, 'Siamese');
INSERT INTO cats (name, age, breed) VALUES ('Mittens', 3, 'Maine Coon');
INSERT INTO cats (name, age, breed) VALUES ('Shadow', 1, 'British Shorthair');
INSERT INTO cats (name, age, breed) VALUES ('Simba', 4, 'Bengal');
INSERT INTO cats (name, age, breed) VALUES ('Luna', 2, 'Persian');
INSERT INTO cats (name, age, breed) VALUES ('Oliver', 5, 'Ragdoll');
INSERT INTO cats (name, age, breed) VALUES ('Leo', 3, 'Sphynx');
INSERT INTO cats (name, age, breed) VALUES ('Bella', 1, 'Abyssinian');
INSERT INTO cats (name, age, breed) VALUES ('Charlie', 4, 'Scottish Fold');
INSERT INTO cats (name, age, breed) VALUES ('Max', 2, 'Russian Blue');
INSERT INTO cats (name, age, breed) VALUES ('Chloe', 3, 'American Shorthair');