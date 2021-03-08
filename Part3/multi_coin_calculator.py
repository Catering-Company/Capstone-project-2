# MULTI COIN CALCULATOR

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
        self.text_display.setText("Multiple Coin Calculator")
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
        
# struture similar to coinCalculator
# ask how many pennies they want to input
        self.coin_input_title = QLabel("How much do you want to input?")
        self.coin_input_title.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.coin_input_title)

        self.coin_input_box = QLineEdit(self)
        self.coin_input_box.setPlaceholderText("Enter a amount (in pence)")
        layout.addWidget(self.coin_input_box)

        self.coin_input_button = QPushButton("Submit")
        self.coin_input_button.clicked.connect(self.coin_input_button_clicked)
        layout.addWidget(self.coin_input_button)

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
        self.denom_title = QLabel("Select the denomination you would like to exclude.")
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
    
        self.denom_dropdown.activated.connect(self.deselect_coin)
        layout.addWidget(self.denom_dropdown)

# -----------------------------------------------

# spacing
        self.text_display = QLabel(self)
        self.text_display.setText("--------------------------")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.text_display)

# CALCULATE BUTTON ------------------------------

# button to calculate
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_button_clicked)
        layout.addWidget(self.calculate_button)

# ouput text
        self.calculate_text = QLabel(" ")
        self.calculate_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.calculate_text)

# SHOW WINDOW ------------------------------

# display the window
        self.setLayout(layout)

# ----------------------FUNCTIONS----------------------------

# set the denomination excluded using the dropdown menu
    def deselect_coin(self,index):
        # missing denomination stored in variables
        variables.excluded_denomination = int(self.denom_dropdown.itemData(index))

        #variables.used_denomination = variables.multi_denomination.remove(int(self.denom_dropdown.itemData(index)))
        
        # gets a list with the missing denomination = 0
        # e.g excluded_denomination = 50
        # multi_denomination =  [200, 100, 50, 20, 10]
        # missing_denom = [200, 100, 0, 20, 10]
        variables.missing_denom = variables.multi_denomination
        for j in range(len(variables.missing_denom)):
            if variables.missing_denom[j] == variables.excluded_denomination:
                variables.missing_denom[j] = 0


        #------TESTING------
        #print('Variables.multi_denomination: ' + str(variables.multi_denomination))
        #print(type(variables.multi_denomination))
        #print('Selected to exclude: ' + str(self.denom_dropdown.itemData(index)))
        #print('variables.missing_denom: ' + str(variables.missing_denom))

# button function to display if the inputted amount is valid
# calls check_input_value
# similar to function in coinCalculator
    def coin_input_button_clicked(self):
        textboxValue = self.coin_input_box.text()
        testing_value = self.check_input_value(textboxValue)
        self.calculate_text.setText("") # removes calculated text if user starts putting in new input
        if testing_value >= 0:
            self.result_input_text.setText(f"You inputted {textboxValue} " + variables.currency_config['currency_word'])
        if testing_value == -1:
            self.result_input_text.setText(f"Request denied. Entered less than the min value.")
        if testing_value == -2:
            self.result_input_text.setText(f"Request denied. Entered more than the max value.")
        if testing_value == -3:
            self.result_input_text.setText(f"Request denied. Please\nenter a number.")

    
# checks if the inputted amount is a number and within the min/ max
# if invalid, resets input to -2 so the code can knows input is invalid
# similar to function in coinCalculator
    def check_input_value(self, textboxValue):
        try:
            textboxValue = int(textboxValue)
            if int(textboxValue) < variables.min_input:
                    variables.multi_inputted_amount = -2
                    return -1
            if int(textboxValue) > variables.max_input:
                    variables.multi_inputted_amount = -2
                    return -2
        except:
            variables.multi_inputted_amount = -2
            return -3
        
        variables.multi_inputted_amount = int(textboxValue)
        #print(variables.single_inputted_amount)
        return int(textboxValue)
    
   
# calculate button function
    def calculate_button_clicked(self):
        # accesses the input amount (which should already have been validated)
        amount = variables.multi_inputted_amount
        
        # this list stores how many of each coin the user can have
        # e.g. [1, 1, 0, 3, 0] (1 £2, 1 £1, 0 50p, 3 20p, 0 10p)
        number_of_each = variables.how_many_of_each

        # iterator
        i = 0
        
        # multi_inputted_amount is initialised as -2; checks if user has entered input
        if variables.multi_inputted_amount == -2:
            self.calculate_text.setText("You haven't inputted a valid amount")
        else:
            # 'calculator'

            # as long as the amount (left) is more than 10 coins
            while amount >= 10 and i<=4:
                # sees if looking at the excluded denomination
                # in missing_denom
                # if so, moves on
                if variables.missing_denom[i] == 0:
                    i+=1

                # sees if current denomination that's being added
                # is more than the amount left
                # if so, moves on
                elif (variables.missing_denom[i] > amount):
                    i+=1

                # if the denomination can be used, add that coin to 
                # number_of_each and reduces the amount left by
                # that denomination
                else:
                    number_of_each[i] += 1
                    amount = amount - variables.missing_denom[i]

            # remainder is what's left after all these subtractions
            remainder = amount

            # prints the result
            self.calculate_text.setText(f"{variables.multi_inputted_amount} " +
                    variables.currency_config['currency_word'] + " can be converted to\n" +
                    str(number_of_each[0]) + f" {variables.currency_config['currency_major']}2 ('s)\n" +
                    str(number_of_each[1]) + f" {variables.currency_config['currency_major']}1 ('s)\n" +
                    str(number_of_each[2]) + f" 50{variables.currency_config['currency_minor']} ('s)\n" +
                    str(number_of_each[3]) + f" 20{variables.currency_config['currency_minor']} ('s)\n" +
                    str(number_of_each[4]) + f" 10{variables.currency_config['currency_minor']} ('s)\n" +
                    "With a remainder of " + str(remainder) + variables.currency_config['currency_minor'])
            
            #print(number_of_each)
            #print(remainder)

            # reinitialises the global variables 
            variables.multi_denomination = [200,100,50,20,10]
            variables.how_many_of_each = [0,0,0,0,0]

# when window closed resets the text output
    def closeEvent(self,event):
            self.calculate_text.setText("")
            self.result_input_text.setText("")
            self.coin_input_box.clear()
            variables.single_inputted_amount = -2



 
     
