import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='t2_drw'
    )
    return connection


def token_search_notation(input_words: list):
    cnx = create_connection
    cursor = cnx.cursor()
    query = "SELECT DISTINCT d1.title FROM data d1"

    for i in range(1, len(input_words)):

        query += f" JOIN data d{i + 1} ON d1.title = d{i + 1}.title"

    query += " WHERE "

    for i, word in enumerate(input_words):

        query += f"d{i + 1}.word = '{word}'"

        if i < len(input_words) - 1:

            query += " AND "

    cursor.execute(query)
    # Fetch the results
    tuples = cursor.fetchall()

    # Convert the list of tuples to a list of lists
    results = [list(row) for row in tuples]

    # Close the database connection
    cursor.close()
    cnx.close()

    return results
