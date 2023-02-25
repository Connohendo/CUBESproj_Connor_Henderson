import sqlite3
from api import api_functions
from database import db_functions


# test that the api call is properly getting data from wuffo
def test_api_data_received():
    data = api_functions.get_wufoo_data()
    assert len(data) == 10


# test that the database functions are properly creating databases/tables and filling them with test data properly
def test_database():
    db_connection = sqlite3.connect('pytest_db.db')
    db_cursor = db_connection.cursor()

    db_functions.database_creation('pytest_db.db', 'test')
    data = [{"EntryId": "1",
             "Field5": "Mr.",
             "Field6": "Test",
             "Field7": "Man",
             "Field8": "Tester",
             "Field11": "Testers Anon org",
             "Field10": "testers@aol.com",
             "Field9": "wetest.com",
             "Field12": "8000337357",
             "Field113": "Course Project",
             "Field114": "Guest Speaker",
             "Field115": "Site Visit",
             "Field116": "Job Shadow",
             "Field117": "Internships",
             "Field118": "Career Panel",
             "Field119": "Networking Event",
             "Field213": "Summer 2022",
             "Field214": "",
             "Field215": "",
             "Field216": "",
             "Field217": "Other",
             "Field313": "Yes",
             "DateCreated": "right now",
             "CreatedBy": "testers",
             "DateUpdated": "today",
             "Updatedby": ""}]

    db_functions.insert_db('pytest_db.db', 'test', data)

    db_cursor.execute("SELECT * FROM test")
    rows = db_cursor.fetchall()
    assert len(rows) == 1
    assert rows[0] == (
        ('1',
         'Mr.',
         'Test',
         'Man',
         'Tester',
         'Testers Anon org',
         'testers@aol.com',
         'wetest.com',
         '8000337357',
         'Summer 2022, , , , Other',
         'Yes',
         'Course Project, Guest Speaker, Site Visit, Job Shadow, Internships, Career '
         'Panel, Networking Event',
         'right now',
         'testers',
         'today',
         '')
    )
