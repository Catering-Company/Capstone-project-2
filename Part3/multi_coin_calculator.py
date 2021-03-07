#multi coin calculator

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


#Start of GUI elements----------------------------

class CalcWindow(QWidget):
    
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

# sub menu title at top of window
        self.text_display = QLabel(self)
        self.text_display.setText("Multiple Coin Calculator")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.text_display)

# spacing
        self.text_display = QLabel(self)
        self.text_display.setText("--------------------------")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.text_display)
        
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

# spacing
        self.text_display = QLabel(self)
        self.text_display.setText("--------------------------")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.text_display)

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

# spacing
        self.text_display = QLabel(self)
        self.text_display.setText("--------------------------")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.text_display)

        # button to calculate
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_button_clicked)
        layout.addWidget(self.calculate_button)

        self.calculate_text = QLabel(" ")
        self.calculate_text.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
        layout.addWidget(self.calculate_text)

# display everything
        self.setLayout(layout)

        # -----FUNCTIONS------   


# set the denomination excluded using the dropdown menu
    def deselect_coin(self,index):

        variables.excluded_denomination = int(self.denom_dropdown.itemData(index))
        #variables.used_denomination = variables.multi_denomination.remove(int(self.denom_dropdown.itemData(index)))
        
        variables.missing_denom = variables.multi_denomination
        for j in range(len(variables.missing_denom)):
            if variables.missing_denom[j] == variables.excluded_denomination:
                variables.missing_denom[j] = 0


        #---TESTING---
        print('Variables.multi_denomination: ' + str(variables.multi_denomination))
        print(type(variables.multi_denomination))
        print('Selected to exclude: ' + str(self.denom_dropdown.itemData(index)))
        print('variables.missing_denom: ' + str(variables.missing_denom))

# button function to display if the inputted amount is valid
# calls check_input_value
    def coin_input_button_clicked(self):
        textboxValue = self.coin_input_box.text()
        testing_value = self.check_input_value(textboxValue)
        if testing_value >= 0:
            self.result_input_text.setText(f"You inputted {textboxValue} " + variables.currency_config['currency_word'])
        if testing_value == -1:
            self.result_input_text.setText(f"Request denied. Entered less than the min value.")
        if testing_value == -2:
            self.result_input_text.setText(f"Request denied. Entered more than the max value.")
        if testing_value == -3:
            self.result_input_text.setText(f"Request denied. Please\nenter a number.")

    
# checks if the inputted amount is a number and within the min/ max
    def check_input_value(self, textboxValue):
        try:
            textboxValue = int(textboxValue)
            if int(textboxValue) < variables.min_input:
                    return -1
            if int(textboxValue) > variables.max_input:
                    return -2
        except:
            variables.multi_inputted_amount = -2
            return -3
        
        variables.multi_inputted_amount = int(textboxValue)
        #print(variables.single_inputted_amount)
        return int(textboxValue)
    
   


# calculate button function
# displays the result
    def calculate_button_clicked(self):
        # accesses the inputs (which should already have been validated)
        amount = variables.multi_inputted_amount
        denom = variables.excluded_denomination
        print(denom)
        # gets the string value of the excluded denomination (200 = '£2')
        #index = variables.coins_value.index(denom)
        #denom_str = variables.coins[index]

        denom_list = variables.coins_value
        number_of_each = variables.how_many_of_each
        #denom_list[index] = 0
        i = 0

        # multi_inputted_amount is initialised as -2; checks if user has entered input
        if variables.multi_inputted_amount == -2:
            self.calculate_text.setText("You haven't inputted an amount")
        else:
            # 'calculator'
            print("i = " + str(i))
            while amount >= 10 and i<=4:
                if variables.missing_denom[i] == 0:
                    i+=1
                elif (variables.missing_denom[i] > amount):
                    i+=1
                else:
                    number_of_each[i] += 1
                    amount = amount - variables.missing_denom[i]
            remainder = amount

            self.calculate_text.setText("That can be converted to\n" +
                    str(number_of_each[0]) + f" {variables.currency_config['currency_major']}2 ('s)\n" +
                    str(number_of_each[1]) + f" {variables.currency_config['currency_major']}1 ('s)\n" +
                    str(number_of_each[2]) + f"  50{variables.currency_config['currency_minor']} ('s)\n" +
                    str(number_of_each[3]) + f" 20{variables.currency_config['currency_minor']} ('s)\n" +
                    str(number_of_each[4]) + f" 10{variables.currency_config['currency_minor']} ('s)\n" +
                    "With a remainder of " + str(remainder) + variables.currency_config['currency_minor'])
            print(number_of_each)
            print(remainder)
            variables.multi_denomination = [200,100,50,20,10]
            variables.how_many_of_each = [0,0,0,0,0]

    def closeEvent(self,event):
            self.calculate_text.setText("")
            self.result_input_text.setText("")
            self.coin_input_box.clear()
            variables.single_inputted_amount = -2



 
     
