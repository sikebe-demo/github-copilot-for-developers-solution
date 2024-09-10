-- catsテーブルの作成
CREATE TABLE cats (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    breed VARCHAR(50)
);

-- データの挿入
INSERT INTO cats (name, age, breed) VALUES ('Mittens', 2, 'Siamese');
INSERT INTO cats (name, age, breed) VALUES ('Whiskers', 3, 'Maine Coon');
INSERT INTO cats (name, age, breed) VALUES ('Shadow', 1, 'British Shorthair');
INSERT INTO cats (name, age, breed) VALUES ('Luna', 4, 'Persian');
INSERT INTO cats (name, age, breed) VALUES ('Simba', 5, 'Bengal');
INSERT INTO cats (name, age, breed) VALUES ('Chloe', 2, 'Sphynx');
INSERT INTO cats (name, age, breed) VALUES ('Oliver', 3, 'Ragdoll');
INSERT INTO cats (name, age, breed) VALUES ('Leo', 1, 'Scottish Fold');
INSERT INTO cats (name, age, breed) VALUES ('Bella', 4, 'Abyssinian');
INSERT INTO cats (name, age, breed) VALUES ('Max', 5, 'Birman');