# MAIN MENU

import sys
import coinCalculator
import multi_coin_calculator
import configMenu
import variables

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QDesktopWidget
)
from PyQt5 import QtCore


# template for generic sub-window
# copy this to a new file to make a new window
# change the name and remember to change it when referencing from main window
class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Let's Count Coins")
        layout.addWidget(self.label)
        self.setLayout(layout)

# class for main menu
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

# dimensions, position and window title
    def init_ui(self):
        self.resize(200, 250)
        self.center()
        self.setWindowTitle('Coin Counter 3000')
        self.show()

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move calc menus's center point to screen's center point
        qr.moveCenter(cp)

        # top left of calc menu becomes top left of window centering it
        self.move(qr.topLeft())

      
        # put the sub-window here FILE_NAME.CLASS_NAME()
        self.window1 = coinCalculator.CalcWindow()
        self.window2 = multi_coin_calculator.CalcWindow()
        self.window3 = AnotherWindow()
        self.window4 = AnotherWindow()
        self.window5 = configMenu.ConfigWindow()


        # l is our canvas, have to add components to l using l.addWidget(...)
        l = QVBoxLayout()

# textbox at top of MainWindow
        self.text_display = QLabel("Label",self)
        self.text_display.setText("Welcome to the Calculator")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) 
        # set text to centre of screen
        self.text_display.setStyleSheet("color: white; border: 3px solid white; border-radius: 8px; padding: 6px; ")  
        l.addWidget(self.text_display)


# buttons on MainWindow
        button1 = QPushButton("Single Coin Calculator")
        button1.clicked.connect(self.toggle_window1)
        l.addWidget(button1)

        button2 = QPushButton("Multiple Coin Calculator")
        button2.clicked.connect(self.toggle_window2)
        l.addWidget(button2)

        button3 = QPushButton("Display Available Coins")
        button3.clicked.connect(self.click_see_coins)
        #button3.clicked.connect(self.toggle_window3)
        l.addWidget(button3)

        button4 = QPushButton("Display Configurations")
        button4.clicked.connect(self.click_see_config) # button calls click_see_config 
        #function button4.clicked.connect(self.toggle_window4)
        l.addWidget(button4)

        button5 = QPushButton("Set Configurations")
        button5.clicked.connect(self.toggle_window5)
        l.addWidget(button5)

        clearButton = QPushButton("Clear")
        clearButton.clicked.connect(self.clearText)
        l.addWidget(clearButton)
        # builds window by collecting widgets added to l 
        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

# toggling which windows are displayed - needs work to make sure no 2 windows 
# can be opened simultaneously or not depending on what we want. 

# --------- OPENING WINDOWS --------------------

    def toggle_window1(self, checked):
        if self.window1.isVisible():
            self.window1.hide()

        else:
            # when single calculator is opened
            # text box needs to say 'cents'
            # dropdown needs to be in correct currency
            # all windows are made when main menu is run, so these need to be changed when 
            # sub-window is opened
            self.window1.show()
            self.window1.coin_input_box.setPlaceholderText(f"Enter an amount (in {variables.currency_config['currency_word']})")
            for i in range(len(variables.coins)):
                value = int(variables.coins_value[i])
                index = self.window1.denom_dropdown.findData(value)
                self.window1.denom_dropdown.setItemText(index, variables.coins[i])


    def toggle_window2(self, checked):
        if self.window2.isVisible():
            self.window2.hide()

        else:
            # needs to do the same as window1 (see comments for toggle_window1)
            self.window2.show()
            self.window2.coin_input_box.setPlaceholderText(f"Enter an amount (in {variables.currency_config['currency_word']})")
            for i in range(len(variables.coins)):
                value = int(variables.coins_value[i])
                index = self.window2.denom_dropdown.findData(value)
                self.window2.denom_dropdown.setItemText(index, variables.coins[i])


    def toggle_window3(self, checked):
        if self.window3.isVisible():
            self.window3.hide()

        else:
            self.window3.show()

    def toggle_window4(self, checked):
        if self.window4.isVisible():
            self.window4.hide()

        else:
            self.window4.show()

    def toggle_window5(self, checked):
        if self.window5.isVisible():
            self.window5.hide()

        else:
            self.window5.show()

# ---------------- MAIN MENU FUNCTIONS -------------------

# Outputs current configuration when 'Display Configurations' button pressed 
    def click_see_config(self):    
        curr = variables.currency_config["currency"]
        curr_word = variables.currency_config["currency_word"]

        #currency = variables.currency
        min_input = variables.min_input
        max_input = variables.max_input    
        self.text_display.setText("Currency: " + curr + f"\nMinimum Input ({curr_word}): " +
        str(min_input) + f"\nMaximum Input ({curr_word}): " + str(max_input))

# Outputs available coins when 'Display Available Coins' button pressed 
    def click_see_coins(self):
        coins = variables.coins
        #print(coins)
        self.text_display.setText("We can convert to\n " + coins[0] + ", " 
        + coins[1] + ", "+ coins[2] + ", "+ coins[3] + " or "+ coins[4])
    
# Resets top textbox when 'Clear' button pressed
    def clearText(self):
        self.text_display.setText("Welcome to the Calculator")

# when main menu closed, all windows close
    def closeEvent(self,event):
        app.quit()



# main coin runs from here 

# EDIT - variables are no stored in variables.py so need to be referenced as variables.blah
# define defaults here
# I think if these variables are to be changed in a GUI function needs to be
#---- def function(self)
#----   global variable
#----   variable = 7

#currency = 'GBP'
#min_input = 0
#max_input = 10000
#coins = ['£2','£1','50p','20p','10p']

# initialise GUI and display
app = QApplication(sys.argv)

#CSS style sheet 

style = """
QLabel{
    color: white;
    font-size: 15px;
    font-family: verdana ;
    font-weight: bold;
}

QPushButton{
    color: black;
    background: #daf4f5 ;
    border-radius: 8px;
    padding: 6px;
    }

QMainWindow {
    background: #1c2d30;
}

CalcWindow {
    background: #1c2d30;

}

ConfigWindow { 
    background: #1c2d30;
}

QLineEdit {
    border-radius: 8px;
    padding: 4px;
}

"""
app.setStyleSheet(style)


w = MainWindow()
w.show()
app.exec_()
