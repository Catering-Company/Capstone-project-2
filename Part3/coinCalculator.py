from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QComboBox
)
from PyQt5 import QtCore

import variables

class CalcWindow(QWidget):
    coin_to_use = 200
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Let's Count Coins")
        layout.addWidget(self.label)
        

        #button1 = QPushButton("Edit Config")
        #button1.clicked.connect(self.editConfig)
        #layout.addWidget(button1)
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("£2", 200)
        self.comboBox.addItem("£1", 100)
        self.comboBox.addItem("50p",  50)
        self.comboBox.addItem("20p", 20)
        self.comboBox.addItem("10p", 10)
    
        self.comboBox.activated.connect(self.select_coin)
        layout.addWidget(self.comboBox)


        self.setLayout(layout)

# this is a test for editing variables between windows        
#    def editConfig(self):
#        variables.min_input = 19

    def select_coin(self,index):
        print(self.comboBox.itemData(index))