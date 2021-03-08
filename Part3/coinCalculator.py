# SINGLE COIN CALCULATOR

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


class CalcWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

# TITLE -----------------------------------------

# sub menu title at top of window 

        self.text_display = QLabel(self)
        self.text_display.setText("Single Coin Calculator")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        self.text_display.setStyleSheet("border: 3px solid white; border-radius: 8px; padding: 6px; ")  
        layout.addWidget(self.text_display)

# -----------------------------------------------

# spacing
        self.text_display = QLabel(self)
        self.text_display.setText("--------------------------")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.text_display)
     
# COIN INPUT -----------------------------------

# ask how many pennies they want to input
# text label
        self.coin_input_title = QLabel("How much do you want to input?")
        self.coin_input_title.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.coin_input_title)

# input text box
        self.coin_input_box = QLineEdit(self)
        #print(variables.currency_config['currency_word'])
        
        layout.addWidget(self.coin_input_box)

# button to submit choice
        self.coin_input_button = QPushButton("Submit")
        self.coin_input_button.clicked.connect(self.coin_input_button_clicked)
        layout.addWidget(self.coin_input_button)

# result text box
        self.result_input_text = QLabel(" ")
        self.result_input_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.result_input_text)

# -----------------------------------------------

# spacing
        self.text_display = QLabel(self)
        self.text_display.setText("--------------------------")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.text_display)


# COIN DENOMINATION CHOICE ----------------------

# dropdown menu for coin denomination choice
        self.denom_title = QLabel("Select the denomination you would like.")
        self.denom_title.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.denom_title)

        self.denom_dropdown = QComboBox(self)
        # first argument displayed
        # second argument used to set denomination

        self.denom_dropdown.addItem("£2", 200)
        self.denom_dropdown.addItem("£1", 100)
        self.denom_dropdown.addItem("50p", 50)
        self.denom_dropdown.addItem("20p", 20)
        self.denom_dropdown.addItem("10p", 10)
    
        self.denom_dropdown.activated.connect(self.select_coin)
        layout.addWidget(self.denom_dropdown)
    
# -----------------------------------------------

# spacing
        self.text_display = QLabel(self)
        self.text_display.setText("--------------------------")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.text_display)

# CALCULATE BUTTON ------------------------------
# button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_button_clicked)
        layout.addWidget(self.calculate_button)

# output text box
        self.calculate_text = QLabel(" ")
        self.calculate_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.calculate_text)

# SHOW WINDOW ------------------------------

# display the window
        self.setLayout(layout)


# TESTING CODE
    #def editConfig(self):
    #    variables.min_input = 19



# ----------------------FUNCTIONS----------------------------

# set the denomination using the dropdown menu
    def select_coin(self,index):
        variables.single_denomination = int(self.denom_dropdown.itemData(index))

        #---TESTING---
        #print(variables.single_denomination)
        #print(type(variables.single_denomination))
        #print(self.denom_dropdown.itemData(index))

# button function to display if the inputted amount is valid
# calls check_input_value
    def coin_input_button_clicked(self):
        # accesses the user input, stores as local variable
        textboxValue = self.coin_input_box.text()

        # calls check_input_value function to test what was inputted
        testing_value = self.check_input_value(textboxValue)

        # removes calculated text if user starts putting in new input
        self.calculate_text.setText("") 

        if testing_value >= 0:
            self.result_input_text.setText(f"You inputted {textboxValue} " + variables.currency_config["currency_word"])
        if testing_value == -1:
            self.result_input_text.setText(f"Request denied. Entered less \nthan the min value.")
        if testing_value == -2:
            self.result_input_text.setText(f"Request denied. Entered more \nthan the max value.")
        if testing_value == -3:
            self.result_input_text.setText(f"Request denied. Please\nenter a number.")
 
# checks if the inputted amount is a number and within the min/ max
# returns negative numbers if input is invalid
# coin_input_button_clicked will then print error message
# otherwise positive, valid input is returned

    def check_input_value(self, textboxValue):
        try:
                # gets user input; stores locally
                # and tries to cast to int
            textboxValue = int(textboxValue)

            # if input is less than set minimum
            if int(textboxValue) < variables.min_input:
                    variables.single_inputted_amount = -1
                    return -1

                # if input is more than set maximum
            if int(textboxValue) > variables.max_input:
                    variables.single_inputted_amount = -1
                    return -2
        except:
                # if input can't be converted to integer
            variables.single_inputted_amount = -1
            return -3
    
        variables.single_inputted_amount = int(textboxValue)
        #print(variables.single_inputted_amount)
        return int(textboxValue)

# calculate button function
# displays the result
    def calculate_button_clicked(self):
        # accesses the inputs (which should already have been validated)
        amount = variables.single_inputted_amount
        denom = variables.single_denomination

        # gets the string value of the denomination (200 = '£2')
        # using the constant global variables
        index = variables.coins_value.index(denom)
        denom_str = variables.coins[index]

        # single_inputted_amount is initialised as -1; checks if user has entered input
        if variables.single_inputted_amount == -1:
            self.calculate_text.setText("You haven't inputted a valid amount")
        else:
            # 'calculator'
            # gets floor division result of inputted amount
            # divided by the chosen denomination
            number_of_denom = amount//denom

            # gets modulus of amount/ division -> remainder
            remainder = amount%denom

            # prints the result
            self.calculate_text.setText(str(number_of_denom) + " " + denom_str 
            + " ('s) and a remainder of " + str(remainder)
            + " " + variables.currency_config['currency_word'])

# when window closes; resets the calculator
    def closeEvent(self,event):
        self.calculate_text.setText("")
        self.result_input_text.setText("")
        self.coin_input_box.clear()
        variables.single_inputted_amount = -1
        #self.coin_input_box.setPlaceholderText(f"Enter an amount (in {variables.currency_config['currency_word']})")


    