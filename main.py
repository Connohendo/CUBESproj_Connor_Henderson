from database import db_functions
from api import api_functions
from gui import gui_functions


# Very modular main function wow
def main():
    data = api_functions.get_wufoo_data()
    db_functions.database_creation('wufoo_db.db', 'entries')
    db_functions.insert_db('wufoo_db.db', 'entries', data)
    # db_functions.print_db()
    display_data = gui_functions.get_test_data()
    gui_functions.display_data(display_data)


if __name__ == "__main__":
    main()
