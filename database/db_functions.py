import sqlite3


# Create a new database
def database_creation(database, table):
    try:
        # create a database connection
        db_connection = sqlite3.connect(f'{database}')
        db_cursor = db_connection.cursor()

        # create the table if it doesn't already exist
        db_cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table}
                     (Entry_Id text,
                      title text,
                      First_name text,
                      Last_name text,
                      Org_title text,
                      org text,
                      email text,
                      website text,
                      p_num text,
                      time_period text,
                      perms text,
                      opportunity text,
                      Date_Created text,
                      Created_By text,
                      Date_Updated text,
                      Updated_By text)''')

    # catch any database errors
    except sqlite3.Error as db_error:
        # print the error description
        print(f'A Database Error has occurred: {db_error}')

    # 'finally' blocks are useful when behavior in the try/except blocks is not predictable
    # The 'finally' block will run regardless of what happens in the try/except blocks.
    finally:
        # close the database connection whether an error happened or not (if a connection exists)
        if db_connection:
            db_connection.close()
            print('Database connection closed.')


# insert data from the api call into the database after first clearing any data left over
def insert_db(database, table, data):
    try:
        db_connection = sqlite3.connect(f'{database}')
        db_cursor = db_connection.cursor()

        for item in data:
            # check if entry already exists in table
            db_cursor.execute("SELECT Entry_Id FROM entries WHERE Entry_Id = ?", (item['EntryId'],))
            result = db_cursor.fetchone()
            if result is not None:
                continue

            db_cursor.execute(f"INSERT INTO {table} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                              (item['EntryId'],
                               # title
                               item.get('Field5', ''),
                               # first name
                               item.get('Field6', ''),
                               # last name
                               item.get('Field7', ''),
                               # org title
                               item.get('Field8', ''),
                               # org
                               item.get('Field11', ''),
                               # email
                               item.get('Field10', ''),
                               # website
                               item.get('Field9', ''),
                               # phone number
                               item.get('Field12', ''),
                               # Time period
                               ' '.join([item.get('Field213', ''),
                                         item.get('Field214', ''),
                                         item.get('Field215', ''),
                                         item.get('Field216', ''),
                                         item.get('Field217', '')]),
                               # perms
                               item.get('Field313', ''),
                               # opportunities
                               ' '.join([item.get('Field113', ''), item.get('Field114', ''), item.get('Field115', ''),
                                         item.get('Field116', ''), item.get('Field117', ''), item.get('Field118', ''),
                                         item.get('Field119', '')]),
                               # created
                               item.get('DateCreated', ''),
                               # created by
                               item.get('CreatedBy', ''),
                               # date updated
                               item.get('DateUpdated', ''),
                               # updated by
                               item.get('UpdatedBy', '')))

    # catch any database errors
    except sqlite3.Error as db_error:
        # print the error description
        print(f'A Database Error has occurred: {db_error}')

    # 'finally' blocks are useful when behavior in the try/except blocks is not predictable
    # The 'finally' block will run regardless of what happens in the try/except blocks.
    finally:
        db_connection.commit()
        # close the database connection whether an error happened or not (if a connection exists)
        if db_connection:
            db_connection.close()
            print('Database connection closed.')


def print_db():
    db_connection = sqlite3.connect('wufoo_db.db')
    db_cursor = db_connection.cursor()

    db_cursor.execute('SELECT * FROM entries')
    rows = db_cursor.fetchall()

    for row in rows:
        print(row)
