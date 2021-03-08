# GUI CONFIGURATION SUB MENU

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QComboBox,
    QLineEdit
)
from PyQt5 import QtCore
import variables
import sys


# class for config menu
class ConfigWindow(QWidget):
    def __init__(self):
        super().__init__()
        # l is our canvas, have to add components to l using l.addWidget(...)
        l = QVBoxLayout()

# sub menu title at top of window plus styling
        self.text_display = QLabel(self)
        self.text_display.setText("Calculator Configuration Menu")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        self.text_display.setStyleSheet("border: 3px solid white; border-radius: 8px; padding: 6px; ")  
        l.addWidget(self.text_display)

#----------------------------------

# spacing
        self.text_display = QLabel(self)
        self.text_display.setText("-----------------")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.text_display)

# CHANGE CURRENCY ---------------------------------

# currency title
        self.text_display2 = QLabel("Change Currency")
        self.text_display2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.text_display2)


# currency buttons and labels
        self.pounds_button = QPushButton("Pounds Sterling")
        self.pounds_button.clicked.connect(self.pounds_button_clicked)
        l.addWidget(self.pounds_button)

        self.dollars_button = QPushButton("US Dollars")
        self.dollars_button.clicked.connect(self.dollars_button_clicked)
        l.addWidget(self.dollars_button)
        
        #self.currency_value_label = QLabel("Currency: " + variables.currency)
        #self.currency_value_label = QLabel(f"Currency: {variables.currency_config['currency']}")
        self.currency_value_label = QLabel("")
        self.currency_value_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        l.addWidget(self.currency_value_label)

#----------------------------------

# spacing
        self.text_display = QLabel(self)
        self.text_display.setText("-----------------")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.text_display)


# CHANGE MINIMUM VALUE --------------------
        self.min_value_title = QLabel("Minimum Coin Value")
        self.min_value_title.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.min_value_title)


        self.min_value_box = QLineEdit(self)
        self.min_value_box.setPlaceholderText("Enter a minimum value")
        l.addWidget(self.min_value_box)


        self.change_min_button = QPushButton("Change minimum value")
        self.change_min_button.clicked.connect(self.min_value_button_clicked)
        l.addWidget(self.change_min_button)


        self.result_min_text = QLabel("Result: ")
        self.result_min_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.result_min_text)

        
        self.min_value_label = QLabel(" \n ")
        self.min_value_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.min_value_label)

# ---------------------------------

# spacing

        self.min_text = QLabel("-----------------")
        self.min_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.min_text)


# CHANGE MAXIMUM VALUE -----------------------

        self.max_value_title = QLabel("Maximum Coin Value")
        self.max_value_title.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.max_value_title)


        self.max_value_box = QLineEdit(self)
        self.max_value_box.setPlaceholderText("Enter a maximum value")
        l.addWidget(self.max_value_box)


        self.change_max_button = QPushButton("Change maximum value")
        self.change_max_button.clicked.connect(self.max_value_button_clicked)
        l.addWidget(self.change_max_button)


        self.result_max_text = QLabel("Result: ")
        self.result_max_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.result_max_text)

        
        self.max_value_label = QLabel(" \n ")
        self.max_value_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        l.addWidget(self.max_value_label)

# ------------------------------------

# display all widgets
        self.setLayout(l)


# ----------------------FUNCTIONS----------------------------   

# sets global variables when 'Pounds Sterling' button pressed
    def pounds_button_clicked(self):
        #variables.currency = "GBP"

        variables.currency_config["currency"] = "GBP"
        variables.currency_config["currency_major"] = "£"
        variables.currency_config["currency_minor"] = "p"
        variables.currency_config["currency_word"] = "pence"

        variables.coins = [f'{variables.currency_config["currency_major"]}2',
                        f'{variables.currency_config["currency_major"]}1',
                        f'50{variables.currency_config["currency_minor"]}',
                        f'20{variables.currency_config["currency_minor"]}',
                        f'10{variables.currency_config["currency_minor"]}']

        # prints confirmation of change
        self.currency_value_label.setText("Currency: " + variables.currency_config["currency"])

# sets global variables when 'US Dollars' button pressed
    def dollars_button_clicked(self):
        #variables.currency = "USD"

        variables.currency_config["currency"] = "USD"
        variables.currency_config["currency_major"] = "$"
        variables.currency_config["currency_minor"] = "c"
        variables.currency_config["currency_word"] = "cents"

        variables.coins = [f'{variables.currency_config["currency_major"]}2',
                        f'{variables.currency_config["currency_major"]}1',
                        f'50{variables.currency_config["currency_minor"]}',
                        f'20{variables.currency_config["currency_minor"]}',
                        f'10{variables.currency_config["currency_minor"]}']

        # prints confirmation of change
        self.currency_value_label.setText("Currency: " + variables.currency_config["currency"])

# functionality when 'Change Minimum Value' button pressed
    def min_value_button_clicked(self):
        # accesses the user input, stores as local variable
        textboxValue = self.min_value_box.text()

        # calls min_coin_value function to test what was inputted
        testing_value = self.min_coin_value(textboxValue)

        # prints out message depending on return value of min_coin_value
        if testing_value >= 0:
                variables.min_input = int(textboxValue)
                self.min_value_label.setText(f"The minimum coin value\nis now {textboxValue}.")
        if testing_value == -1:
                self.min_value_label.setText(f"Request denied. The minnmust be at least 0.")
        if testing_value == -2:
                self.min_value_label.setText(f"Request denied. The min\nvalue must be below 10000.")
        if testing_value == -3:
                self.min_value_label.setText(f"Request denied. That is\nlarger than the max value!")
        if testing_value == -4:
                self.min_value_label.setText(f"Request denied. Please\nenter a number.")


        # Gets the user to input a new minimum amount of coins that the user can enter 
        # into the Coin Calulator and Mutiple Coin Calculator. There are restrictions
        # in place to prevent the user from entering:
        # - Any non-integer.
        # - A min value less than 0.
        # - A min value greater than or equal to 10000.
        # - A min value greater than the current max value.
        #  If any of the above happens then min_coin_value returns a negative integer and
        # min_value_button_clicked will print 'Request denied'.
    def min_coin_value(self, textboxValue):
        try:
                textboxValue = int(textboxValue)
                if int(textboxValue) < 0:
                        return -1
                if int(textboxValue) >= 10000:
                        return -2
                if int(textboxValue) > int(variables.max_input):
                        return -3           
        except:
                return -4
        return int(textboxValue)

# functionality when 'Change Maximum Value' button pressed
    def max_value_button_clicked(self):
        # accesses the user input, stores as local variable
        textboxValue = self.max_value_box.text()

        # calls max_coin_value function to test what was inputted
        testing_value = self.max_coin_value(textboxValue)

        # prints out message depending on return value of max_coin_value
        if testing_value >= 0:
                variables.max_input = int(textboxValue)
                self.max_value_label.setText(f"Result: The maximum coin\nvalue is now {textboxValue}.")
        if testing_value == -1:
                self.max_value_label.setText(f"Result: Request denied. The max\ncannot be below 0!")
        if testing_value == -2:
                self.max_value_label.setText(f"Result: Request denied. The max\nvalue must be below 10000.")
        if testing_value == -3:
                self.max_value_label.setText(f"Result: Request denied. That is\nsmaller than the min value!")
        if testing_value == -4:
                self.max_value_label.setText(f"Result: Request denied. Please\nenter a number.")


        # Gets the user to input a new maximum amount of coins that the user can enter 
        # into the Coin Calulator and Mutiple Coin Calculator. There are restrictions
        # in place to prevent the user from entering:
        # - Any non-integer.
        # - A max value less than 0.
        # - A max value greater than 10000.
        # - A max value less than the current min value. 
        #  If any of the above happens then min_coin_value returns a negative integer and 
        # max_value_button_clicked will print 'Request denied'.
    def max_coin_value(self, textboxValue):
        try:
                textboxValue = int(textboxValue)
                if int(textboxValue) < 0:
                        return -1
                if int(textboxValue) > 10000:
                        return -2
                if int(textboxValue) < int(variables.min_input):  
                        return -3
        except:
                return -4
        return int(textboxValue)

# when window closes; resets the calculator
    def closeEvent(self,event):
        self.currency_value_label.setText("")
        self.min_value_label.setText("")
        self.min_value_box.clear()
        self.max_value_label.setText("")
        self.max_value_box.clear()

