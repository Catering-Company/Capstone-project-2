import sys
import coinCalculator
import variables

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
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
        # put the sub-window here FILE_NAME.CLASS_NAME()
        self.window1 = coinCalculator.CalcWindow()
        self.window2 = AnotherWindow()
        self.window3 = AnotherWindow()
        self.window4 = AnotherWindow()
        self.window5 = AnotherWindow()


        # l is our canvas, have to add components to l using l.addWidget(...)
        l = QVBoxLayout()

# textbox at top of MainWindow
        self.text_display = QLabel(self)
        self.text_display.setText("Welcome to the Calculator")
        self.text_display.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter) # set text to centre of screen
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
        button4.clicked.connect(self.click_see_config) # button calls click_see_config function
        #button4.clicked.connect(self.toggle_window4)
        l.addWidget(button4)

        button5 = QPushButton("Set Configurations")
        button5.clicked.connect(self.toggle_window5)
        l.addWidget(button5)

        # builds window by collecting widgets added to l (I think that's how it works - Joe)
        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

#toggling which windows are displayed - needs work to make sure no 2 windows can be opened simultaneously or not depending on what we want. 

    def toggle_window1(self, checked):
        if self.window1.isVisible():
            self.window1.hide()

        else:
            self.window1.show()

    def toggle_window2(self, checked):
        if self.window2.isVisible():
            self.window2.hide()

        else:
            self.window2.show()

    def toggle_window3(self, checked):
        if self.window1.isVisible():
            self.window3.hide()

        else:
            self.window3.show()

    def toggle_window4(self, checked):
        if self.window1.isVisible():
            self.window4.hide()

        else:
            self.window4.show()

    def toggle_window5(self, checked):
        if self.window1.isVisible():
            self.window5.hide()

        else:
            self.window5.show()

    def click_see_config(self):    
        currency = variables.currency
        min_input = variables.min_input
        max_input = variables.max_input    
        self.text_display.setText("Currency: " + currency + "\nMinimum Input (pence): " +
        str(min_input) + "\nMaximum Input (pence): " + str(max_input))

    def click_see_coins(self):
        coins = variables.coins

        self.text_display.setText("We can convert to\n " + coins[0] + ", " + coins[1] + ", "+ coins[2] + ", "
        + coins[3] + " or "+ coins[4])



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
w = MainWindow()
w.show()
app.exec_()
