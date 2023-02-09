import db_functions
import api_functions


def main():
    data = api_functions.get_wufoo_data()
    db_functions.database_creation('wufoo_db.db', 'entries')
    db_functions.insert_db('wufoo_db.db', 'entries', data)


if __name__ == "__main__":
    main()
