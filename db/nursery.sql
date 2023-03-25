DROP TABLE IF EXISTS children;
DROP TABLE IF EXISTS guardians;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS staffmembers;

CREATE TABLE guardians (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_number VARCHAR(255)
);
CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE staffmembers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE children (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    allergies VARCHAR (255),
    guardian_id INT NOT NULL REFERENCES guardians(id) ON DELETE CASCADE,
    room_id INT NOT NULL REFERENCES rooms(id) ON DELETE CASCADE,
    staff_member_id INT NOT NULL REFERENCES staffmembers(id) ON DELETE CASCADE
);


