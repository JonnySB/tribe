DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS user_id_seq;

CREATE SEQUENCE IF NOT EXISTS user_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE
);


DROP TABLE IF EXISTS chants CASCADE;
DROP SEQUENCE IF EXISTS chants_id_seq;

CREATE SEQUENCE IF NOT EXISTS chants_id_seq;
CREATE TABLE chants (
    id SERIAL PRIMARY KEY,
    message VARCHAR(255),
    date_created TIMESTAMP,
    user_id int,
    constraint fk_user FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE
);

INSERT INTO users (email, password_hash, name, username)
VALUES
  ('alice.smith@example.com', 'hashed_password_placeholder', 'Alice Smith', 'alicesmith_23'),
  ('bob.johnson@example.com', 'hashed_password_placeholder', 'Bob Johnson', 'bobjohn89'),
  ('elena.garcia@example.com', 'hashed_password_placeholder', 'Elena Garcia', 'elenagarcia23'),
  ('maxwell.lee@example.com', 'hashed_password_placeholder', 'Maxwell Lee', 'maxwell_l'),
  ('sophie.patel@example.com', 'hashed_password_placeholder', 'Sophie Patel', 'sophiep_123');

INSERT INTO chants (message, date_created, user_id)
VALUES
  ('Hello!', '2023-12-01 08:30:00', 1),
  ('Feeling great today.', '2023-12-02 09:45:00', 2),
  ('Just saying hi!', '2023-12-03 10:15:00', 3),
  ('Working on a new project.', '2023-12-04 11:20:00', 4),
  ('Enjoying the weekend.', '2023-12-05 13:00:00', 5),
  ('Coding non-stop!', '2023-12-06 14:30:00', 1),
  ('Exploring new ideas.', '2023-12-07 16:00:00', 2),
  ('Learning something new every day.', '2023-12-08 18:45:00', 3),
  ('Having a productive day.', '2023-12-09 20:10:00', 4),
  ('Chasing dreams!', '2023-12-10 22:00:00', 5);

