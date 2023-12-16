# test database connection by inserting into database, getting all records.
def test_database_connection(db_connection):
    """
    When I seed the database
    I get some records back
    """
    db_connection.seed("seeds/database_connection.sql")

    db_connection.execute(
        "INSERT INTO test_table (name) VALUES (%s)", ["second_record"]
    )

    result = db_connection.execute("SELECT * FROM test_table")

    assert result == [
        {"id": 1, "name": "first_record"},
        {"id": 2, "name": "second_record"},
    ]
