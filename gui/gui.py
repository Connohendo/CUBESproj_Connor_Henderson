import sqlite3
import tkinter


class Gui(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("CUBES Project Interface")
        self.setup_window()

    def setup_window(self):
        self.button_frame = tkinter.Frame(self.master)
        self.button_frame.pack(fill='x')
        self.grab_btn = tkinter.Button(self.button_frame, text="Grab Entries", command=self.grab_entries)
        self.grab_btn.pack(side=tkinter.LEFT)
        self.update_btn = tkinter.Button(self.button_frame, text="Update Entry", command=self.update_window)
        self.update_btn.pack(side=tkinter.LEFT)
        self.add_use_btn = tkinter.Button(self.button_frame, text="Add Entry", command=self.new_user)
        self.add_use_btn.pack(side=tkinter.LEFT)
        self.paned_window = tkinter.PanedWindow(self.master, orient=tkinter.VERTICAL)
        self.paned_window.pack(fill=tkinter.BOTH, expand=1)
        self.entry_box = tkinter.Listbox(self.paned_window)
        self.entry_box.bind('<<ListboxSelect>>', lambda event=None: self.show_entry(event))
        self.paned_window.add(self.entry_box)
        self.data_frame = tkinter.Frame(self.paned_window)
        self.paned_window.add(self.data_frame)
        self.labels = []
        fields = ["Title", "First Name", "Last Name", "Organization Title", "Organization", "Email",
                  "Organization Website",
                  "Phone Number", "Time Period", "Permission", "Opportunities", "Date Created", "Created By",
                  "Date Updated", "Updated By"]
        for i, field in enumerate(fields):
            static_label = tkinter.Label(self.data_frame, text=field)
            static_label.grid(row=i, column=0, sticky="e")
            self.labels.append(static_label)

        self.entry_labels = []
        for i in range(len(fields)):
            data_label = tkinter.Label(self.data_frame, text="")
            data_label.grid(row=i, column=1, sticky="w")
            self.entry_labels.append(data_label)

    def grab_entries(self):
        db_connection = sqlite3.connect('wufoo_db.db')
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT Entry_Id, Title, First_Name, Last_Name, email FROM entries")
        data = db_cursor.fetchall()
        db_connection.close()

        self.entry_box.delete(0, tkinter.END)
        for data_label in self.entry_labels:
            data_label.config(text="")

        for item in data:
            entry = f"{item[1]} {item[2]} {item[3]}"
            self.entry_box.insert("end", entry)
            self.entry_box.configure()

    def show_entry(self, event=None):
        if event is not None and self.entry_box.curselection():
            index = self.entry_box.curselection()[0]
            entry = self.entry_box.get(index)

            db_connection = sqlite3.connect('wufoo_db.db')
            db_cursor = db_connection.cursor()
            db_cursor.execute("SELECT * FROM entries WHERE Title || ' ' || First_Name || ' ' || Last_Name = ?",
                              (entry,))
            data = db_cursor.fetchone()
            db_connection.close()

            if data is not None:
                for i, data_label in enumerate(self.entry_labels):
                    data_label.config(text=data[i + 1])

    def update_window(self):
        if not self.entry_box.curselection():
            return

        index = self.entry_box.curselection()[0]
        entry = self.entry_box.get(index)

        db_connection = sqlite3.connect('wufoo_db.db')
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT * FROM entries WHERE Title || ' ' || First_Name || ' ' || Last_Name = ?", (entry,))
        data = db_cursor.fetchone()
        db_connection.close()

        if data is None:
            return

        update_window = tkinter.Toplevel(self.master)
        update_window.title("Update Entry")

        fields = ["Title", "First Name", "Last Name", "Organization Title", "Organization", "Email",
                  "Organization Website", "Phone Number", "Time Period", "Permission", "Opportunities",
                  "Date Created", "Created By", "Date Updated", "Updated By"]
        entries = []
        for i, field in enumerate(fields):
            label = tkinter.Label(update_window, text=field)
            label.grid(row=i, column=0, sticky="e")

            entry_value = tkinter.StringVar()
            entry_value.set(data[i + 1])
            entry = tkinter.Entry(update_window, textvariable=entry_value)
            entry.grid(row=i, column=1, sticky="w")

            entries.append(entry)

        def save_entry():
            new_data = [entry.get() for entry in entries]
            new_data.append(data[0])  # add the Entry_Id to the end of the list

            db_connection = sqlite3.connect('wufoo_db.db')
            db_cursor = db_connection.cursor()
            db_cursor.execute("UPDATE entries SET Title = ?, First_Name = ?, Last_Name = ?, Org_Title = ?, "
                              "org = ?, email = ?, website = ?, p_num = ?, Time_Period = ?, "
                              "perms = ?, opportunity = ?, Date_Created = ?, Created_By = ?, Date_Updated = ?, "
                              "Updated_By = ? WHERE Entry_Id = ?",
                              tuple(new_data))
            db_connection.commit()
            db_connection.close()

            update_window.destroy()

            self.grab_entries()

        def delete_entry():
            db_connection = sqlite3.connect('wufoo_db.db')
            db_cursor = db_connection.cursor()
            db_cursor.execute("DELETE FROM entries WHERE Entry_Id = ?", (data[0],))
            db_connection.commit()
            db_connection.close()

            update_window.destroy()

            self.grab_entries()

        save_btn = tkinter.Button(update_window, text="Save", command=save_entry)
        save_btn.grid(row=len(fields), column=0, columnspan=2)

        delete_btn = tkinter.Button(update_window, text="Delete", command=delete_entry)
        delete_btn.grid(row=len(fields) + 1, column=0, columnspan=2)

        self.show_entry()

    def check_email(self, email_entry):
        email = email_entry.get()

        db_connection = sqlite3.connect('wufoo_db.db')
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT * FROM entries WHERE email = ?", (email,))
        data = db_cursor.fetchone()
        db_connection.close()

        if data is not None:
            fields = ["Title", "First Name", "Last Name", "Organization Title", "Organization",
                      "Organization Website", "Phone Number", "Time Period", "Permission", "Opportunities"]
            for i, field in enumerate(fields):
                entry_value = tkinter.StringVar(value=data[i + 2])
                app.new_user_entries[i].config(textvariable=entry_value)

    def new_user(self):
        add_entry_window = tkinter.Toplevel(self.master)
        add_entry_window.title("Add Entry")

        email_label = tkinter.Label(add_entry_window, text="Email")
        email_label.grid(row=0, column=0, sticky="e")

        email_entry_value = tkinter.StringVar()
        email_entry = tkinter.Entry(add_entry_window, textvariable=email_entry_value)
        email_entry.grid(row=0, column=1, sticky="w")
        email_entry.bind("<KeyRelease>", lambda event: self.check_email(email_entry))

        fields = ["Title", "First Name", "Last Name", "Organization Title", "Organization", "Organization Website",
                  "Phone Number", "Time Period", "Permission", "Opportunities"]
        self.new_user_entries = []
        for i, field in enumerate(fields):
            label = tkinter.Label(add_entry_window, text=field)
            label.grid(row=i + 1, column=0, sticky="e")

            entry_value = tkinter.StringVar()
            entry = tkinter.Entry(add_entry_window, textvariable=entry_value)
            entry.grid(row=i + 1, column=1, sticky="w")

            self.new_user_entries.append(entry)

        def save_user():
            email = email_entry.get().strip()
            title = self.new_user_entries[0].get().strip()
            f_name = self.new_user_entries[1].get().strip()
            l_name = self.new_user_entries[2].get().strip()
            org_title = self.new_user_entries[3].get().strip()
            org = self.new_user_entries[4].get().strip()
            org_website = self.new_user_entries[5].get().strip()
            p_num = self.new_user_entries[6].get().strip()
            time_period = self.new_user_entries[7].get().strip()
            perms = self.new_user_entries[8].get().strip()
            opportunity = self.new_user_entries[9].get().strip()

            full_name = f"{title} {f_name} {l_name}"

            db_connection = sqlite3.connect('wufoo_db')
            db_cursor = db_connection.cursor()

            db_cursor.execute("SELECT * FROM entries WHERE email = ?", (email,))
            result = db_cursor.fetchone()

            if result is not None:
                db_cursor.execute(
                    "UPDATE entries SET Title = ?, First_Name = ?, Last_Name = ?, Org_Title = ?, org = ?, "
                    "website = ?, p_num = ?, Time_Period = ?, perms = ?, opportunity = ? "
                    "WHERE email = ?",
                    (title, f_name, l_name, org_title, org, org_website, p_num, time_period,
                     perms, opportunity, email))
            else:
                db_cursor.execute("INSERT INTO entries (Title, First_Name, Last_Name, Org_Title, org, email, "
                                  "website, p_num, Time_Period, perms, opportunity) "
                                  "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                                  (title, f_name, l_name, org_title, org, email, org_website,
                                   p_num, time_period, perms, opportunity))

            db_connection.commit()
            db_connection.close()

            add_entry_window.destroy()

            app.load_data()

        save_btn = tkinter.Button(add_entry_window, text="Save", command=save_user)
        save_btn.grid(row=len(fields) + 1, column=0, columnspan=2)
