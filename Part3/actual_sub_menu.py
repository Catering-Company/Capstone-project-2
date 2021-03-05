# FUNCTIONALITY TESTING FOR GUI SUB-MENU


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QMainWindow
from PyQt5 import QtCore
import sys


# class for main menu
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # l is our canvas, have to add components to l using l.addWidget(...)
        l = QVBoxLayout()



# textbox at top of MainWindow
        self.text_display = QLabel(self)
        self.text_display.setText("Sub-Menu")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.text_display)

# spacing
        self.text_display = QLabel(self)
        self.text_display.setText("-----------------")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.text_display)



# change currency title
        self.text_display2 = QLabel("Change Currency")
        self.text_display2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.text_display2)



# change currency buttons and labels
        self.pounds_button = QPushButton("Pounds Sterling")
        self.pounds_button.clicked.connect(self.pounds_button_clicked)
        l.addWidget(self.pounds_button)

        self.dollars_button = QPushButton("US Dollars")
        self.dollars_button.clicked.connect(self.dollars_button_clicked)
        l.addWidget(self.dollars_button)
        

        self.currency_value_label = QLabel(f"Currency: {config['currency'].title()}")
        self.currency_value_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        l.addWidget(self.currency_value_label)


# spacing
        self.text_display = QLabel(self)
        self.text_display.setText("-----------------")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.text_display)


#  min value--------------------
        self.min_value_title = QLabel("Minimum Coin Value")
        self.min_value_title.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.min_value_title)


        self.min_value_box = QLineEdit(self)
        self.min_value_box.setPlaceholderText("Enter a minimum value")
        l.addWidget(self.min_value_box)


        self.result_min_text = QLabel("Result: ")
        self.result_min_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.result_min_text)

        self.min_text = QLabel(" ")
        self.min_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.min_text)


        self.min_text = QLabel("-----------------")
        self.min_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.min_text)
# ---------------------------------


# max value -----------------------

        self.max_value_title = QLabel("Minimum Coin Value")
        self.max_value_title.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.max_value_title)
# ------------------------------------

        # builds window by collecting widgets added to l (I think that's how it works - Joe)
        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def click_see_config(self):        
        self.text_display.setText("Currency: " + currency + "\nMinimum Input (pence): " +
        str(min_input) + "\nMaximum Input (pence): " + str(max_input))

    def click_see_coins(self):
        self.text_display.setText("We can convert to\n " + coins[0] + ", " + coins[1] + ", "+ coins[2] + ", "
        + coins[3] + " or "+ coins[4])

    def pounds_button_clicked(self):
        config["currency"] = "POUNDS STERLING"
        self.currency_value_label.setText(f"Currency: {config['currency'].title()}")
        print(config)

    def dollars_button_clicked(self):
        config["currency"] = "US DOLLARS"
        self.currency_value_label.setText(f"Currency: {config['currency'].title()}")
        print(config)  

# Program configurations
config = {
    "currency": "POUNDS STERLING",
    "min_coin_value": 0,
    "max_coin_value": 10000,
}

# initialise GUI and display
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()