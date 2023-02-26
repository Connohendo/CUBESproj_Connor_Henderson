from PySide6.QtWidgets import QWidget, QLabel


class Comp490DataDemoWindow(QWidget):

    def __init__(self, data_to_show: dict):
        super().__init__()
        self.data = data_to_show
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Submission Information")
        self.setGeometry(750, 100, 1250, 400)  # put the new window next to the original one wider than it is tall
        label = QLabel(self)
        # entry id
        label.setText("Entry Id:")
        label.move(50, 50)
        entryid = QLabel(self.data['EntryId'], self)
        entryid.move(120, 50)
        # title
        label = QLabel("Title:", self)
        label.move(50, 100)
        title = QLabel(str(self.data["Title"]), self)
        title.move(90, 100)
        # first name
        label = QLabel("First Name:", self)
        label.move(140, 100)
        f_name = QLabel(str(self.data["First_name"]), self)
        f_name.move(220, 100)
        # last name
        label = QLabel("Last Name:", self)
        label.move(350, 100)
        l_name = QLabel(str(self.data["Last_name"]), self)
        l_name.move(430, 100)
        # org title
        label = QLabel("Organization Title:", self)
        label.move(550, 100)
        org_title = QLabel(str(self.data["Org_title"]), self)
        org_title.move(670, 100)
        # org
        label = QLabel("Organization:", self)
        label.move(50, 150)
        org = QLabel(str(self.data["Org"]), self)
        org.move(140, 150)
        # email
        label = QLabel("Email:", self)
        label.move(350, 150)
        email = QLabel(str(self.data["Email"]), self)
        email.move(390, 150)
        # website
        label = QLabel("Website:", self)
        label.move(630, 150)
        website = QLabel(str(self.data["Website"]), self)
        website.move(690, 150)
        # phone number
        label = QLabel("Phone #:", self)
        label.move(800, 150)
        phonenum = QLabel(str(self.data["Phone_number"]), self)
        phonenum.move(860, 150)
        # Time period
        label = QLabel("Time Period:", self)
        label.move(50, 200)
        time = QLabel(str(self.data["Time_period"]), self)
        time.move(140, 200)
        # permissions
        label = QLabel("Permissions:", self)
        label.move(50, 250)
        perms = QLabel(str(self.data["Permissions"]), self)
        perms.move(140, 250)
        # opportunities
        label = QLabel("Opportunities:", self)
        label.move(200, 250)
        opportunity = QLabel(str(self.data["Opportunities"]), self)
        opportunity.move(300, 250)
        # # date created
        # label = QLabel("Date created:", self)
        # label.move(50, 300)
        # date_created = QLabel(str(self.data["Date_created"]), self)
        # date_created.move(140, 300)
        # # date created
        # label = QLabel("Created by:", self)
        # label.move(270, 300)
        # date_created = QLabel(str(self.data["Created_by"]), self)
        # date_created.move(310, 350)
