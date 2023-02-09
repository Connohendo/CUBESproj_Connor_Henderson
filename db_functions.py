import sqlite3


def database_creation():
    try:
        # create a database connection
        db_connection = sqlite3.connect('wufoo_db.db')
        db_cursor = db_connection.cursor()

        # create the table if it doesn't already exist
        db_cursor.execute('''CREATE TABLE IF NOT EXISTS entries
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


def insert_db(data):
    try:
        db_connection = sqlite3.connect('wufoo_db.db')
        db_cursor = db_connection.cursor()

        db_cursor.execute('DELETE FROM entries')

        for item in data:
            db_cursor.execute("INSERT INTO entries VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
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
                               ', '.join([item.get('Field213', ''),
                                          item.get('Field214', ''),
                                          item.get('Field215', ''),
                                          item.get('Field216', ''),
                                          item.get('Field217', '')]),
                               # perms
                               item.get('Field313', ''),
                               # opportunities
                               ', '.join([item.get('Field113', ''), item.get('Field114', ''), item.get('Field115', ''),
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
        # close the database connection whether an error happened or not (if a connection exists)
        if db_connection:
            db_connection.close()
            print('Database connection closed.')
