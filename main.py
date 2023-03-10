import tkinter as tk
from api import api_functions
from database import db_functions
from gui import gui


# Very modular main function wow
def main():
    data = api_functions.get_wufoo_data()
    db_functions.database_creation('wufoo_db.db', 'entries')
    db_functions.insert_db('wufoo_db.db', 'entries', data)
    root = tk.Tk()
    root.minsize(750, 500)
    app = gui.Gui(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
