import sqlite3
import PySide6.QtWidgets
import sys
from gui import window


def display_data(data: list):
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    my_window = window.Comp490DemoWindow(data)
    my_window
    sys.exit(qt_app.exec())


def get_test_data() -> list[dict]:
    db_connection = sqlite3.connect('wufoo_db.db')
    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM entries")
    rows = db_cursor.fetchall()

    final_data_list = []
    for row in rows:
        entryid = row[0]
        title = row[1]
        f_name = row[2]
        l_name = row[3]
        Org_title = row[4]
        Org = row[5]
        Email = row[6]
        website = row[7]
        p_num = row[8]
        Time_period = row[9]
        perms = row[10]
        Opportunities = row[11]
        date_created = row[12]
        created_by = row[13]
        date_updated = row[14]
        updated_by = row[15]

        record = {"EntryId": entryid, "Title": title, "First_name": f_name,
                  "Last_name": l_name, "Org_title": Org_title, "Org": Org, "Email": Email, "Website": website,
                  "Phone_number": p_num, "Time_period": Time_period, "Permissions": perms,
                  "Opportunities": Opportunities, "Date_created": date_created, "Created_by": created_by,
                  "Date_updated": date_updated, "Updated_by": updated_by}
        final_data_list.append(record)
    return final_data_list


# def get_key(value: dict):
#     return value["median_income"]
