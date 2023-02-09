import db_functions
import api_functions


def main():
    data = api_functions.get_wufoo_data()
    db_functions.database_creation()
    db_functions.insert_db(data)


if __name__ == "__main__":
    main()
