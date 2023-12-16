# User story:

```
STRAIGHT UP

As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter

HARDER

As a Maker
So that only I can post messages on Chitter as me
I want to log in to Chitter

As a Maker
So that I can avoid others posting messages on Chitter as me
I want to log out of Chitter

ADVANCED

As a Maker
So that I can stay constantly tapped in to the shouty box of Chitter
I want to receive an email if I am tagged in a Peep
```

## Additional Notes

- You don't have to be logged in to see the peeps.
- Users sign up to chitter with their email, password, name and a username (e.g.
  samm@makersacademy.com, password123, Sam Morgan, sjmog).
- The username and email are unique.
- Peeps (posts to chitter) have the name of the user and their user handle.
- Your README should indicate the technologies used, and give instructions on
  how to install and run the tests.

# Requirements:

## Data requirements:

- user (email, password, name and username)
- peep( message, datetime, foreign key to user)

## Functionality requirements:

### 'Straight up' sprint:

- User related:
  - Create database, model and model repository
  - create forms to sign up
- Peep replated:
  - Create database, model and model repository
  - Create page to view all
  - Create page to create peep

# Table Names:

User:

| Record | Properties                         |
| ------ | ---------------------------------- |
| users  | email, password, name and username |

Peeps:

| Record | Properties                         |
| ------ | ---------------------------------- |
| peeps  | message, created_datetime, user_id |

# Column Types:

Table: users
id : SERIAL
email : text UNIQUE
password : text
name : text
username : text UNIQUE

Table: peeps
id : SERIAL
message : text UNIQUE
created_datetime : date
user_id : int FOREIGN KEY

# SQL:

```SQL
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS user_id_seq;

CREATE SEQUENCE IF NOT EXISTS user_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE
);

INSERT INTO users (email, password, name, username)
VALUES
  ('alice.smith@example.com', 'password', 'Alice Smith', 'alicesmith_23'),
  ('bob.johnson@example.com', 'password', 'Bob Johnson', 'bobjohn89'),
  ('elena.garcia@example.com', 'password', 'Elena Garcia', 'elenagarcia23'),
  ('maxwell.lee@example.com', 'password', 'Maxwell Lee', 'maxwell_l'),
  ('sophie.patel@example.com', 'password', 'Sophie Patel', 'sophiep_123');

DROP TABLE IF EXISTS peeps CASCADE;
DROP SEQUENCE IF EXISTS peeps_id_seq;

CREATE SEQUENCE IF NOT EXISTS peeps_id_seq;
CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    message VARCHAR(255),
    date_created TIMESTAMP,
    user_id int,
    constraint fk_user FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE
);

INSERT INTO peeps (message, date_created, user_id)
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
```

# Design Route Signature

Request:

- POST /albums

With body parameters:

- title=Voyage
- release_year=2022
- artist_id=2

Expected response (200 OK)

- (No content)

**_ Challenge exercise _**

Request:

- GET /artists

Expected response (200 OK)

- Pixies, ABBA, Taylor Swift, Nina Simone

Request:

- POST /artists

With body parameters:

- name=Wild nothing
- genre=Indie

Expected response (200 OK)

- (No content)

Then subsequent request:

- GET /artists

Expected response (200 OK)

- Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
