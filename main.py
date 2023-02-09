import sys
import requests
import sqlite3
from secret import wufoo_key
from requests.auth import HTTPBasicAuth


# def main():

def get_wufoo_data() -> dict:  # comment to test workflow
    url = "https://chendro.wufoo.com/api/v3/forms/zk890sm1gnzlxu/entries/json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))

    if response.status_code != 200:
        print(f"Failed to get data, response code: {response.status_code} and error message: {response.reason}")
        sys.exit(-1)

    jsonresponse = response.json()
    print(jsonresponse['Entries'])
    return jsonresponse['Entries']


def database_creation():
    # create a database connection
    connection = sqlite3.connect('wufoo_db.db')
    cursor = connection.cursor()

    # create the table if it doesn't already exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries
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


def insert_db(data):
    connection = sqlite3.connect('wufoo_db.db')
    cursor = connection.cursor()
    for item in data:
        cursor.execute("INSERT INTO entries VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
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


def main():
    data = get_wufoo_data()
    database_creation()
    insert_db(data)


if __name__ == "__main__":
    main()
    # database_creation()
