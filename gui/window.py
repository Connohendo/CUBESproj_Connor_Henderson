from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox
from gui import secondwindow


class Comp490DemoWindow(QWidget):
    def __init__(self, data_to_show):
        super().__init__()
        self.data = data_to_show
        self.list_control = None
        self.setup_window()
        self.data_window = None

    def setup_window(self):
        self.setWindowTitle("CUBES Submissions")
        display_list = QListWidget(self)
        self.list_control = display_list
        self.put_data_in_list(self.data)
        display_list.resize(400, 350)
        display_list.currentItemChanged.connect(self.demo_list_item_selected)
        self.setGeometry(300, 100, 400, 500)
        quit_button = QPushButton("Quit Now", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(300, 400)
        # comp490_demo_button = QPushButton("Push me for Demo", self)
        # comp490_demo_button.move(100, 400)
        # comp490_demo_button.clicked.connect(self.do_something_to_demo)
        self.show()

    def put_data_in_list(self, data: list[dict]):
        print(" here is the data\n", data)
        for item in data:
            display_text = f"{item['EntryId']}\t\t{item['Title']}\t\t{item['First_name']}\t\t{item['Last_name']}" \
                           f"\t\t{item['Org_title']}\t\t{item['Org']}\t\t{item['Email']}" \
                           f"\t\t{item['Website']}\t\t{item['Phone_number']}\t\t{item['Time_period']}" \
                           f"\t\t{item['Permissions']}\t\t{item['Opportunities']}\t\t{item['Date_created']}" \
                           f"\t\t{item['Created_by']}\t\t{item['Date_updated']}\t\t{item['Updated_by']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)
            list_item

    # def do_something_to_demo(self):
    #     message_box = QMessageBox(self)
    #     message_box.setText("You just pushed the button - imagine database work here")
    #     message_box.setWindowTitle("Comp490 Demo")
    #     message_box.show()

    def find_full_data_record(self, entryid: str):
        for info in self.data:
            if info["EntryId"] == entryid:
                return info

    def demo_list_item_selected(self, current: QListWidgetItem, previous: QListWidgetItem):
        selected_data = current.data(0)  # the data function has a 'role' choose 0 unless you extended QListWidgetItem
        state_name = selected_data.split("\t")[0]  # split on tab and take the first resulting entry
        full_record = self.find_full_data_record(state_name)
        print(full_record)
        self.data_window = secondwindow.Comp490DataDemoWindow(full_record)
        self.data_window.show()
