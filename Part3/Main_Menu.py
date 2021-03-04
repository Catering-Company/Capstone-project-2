import sys

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Let's Count Coins")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()
        self.window3 = AnotherWindow()
        self.window4 = AnotherWindow()
        self.window5 = AnotherWindow()

# buttons 

        l = QVBoxLayout()
        button1 = QPushButton("Single Coin Calculator")
        button1.clicked.connect(self.toggle_window1)
        l.addWidget(button1)

        button2 = QPushButton("Multiple Coin Calculator")
        button2.clicked.connect(self.toggle_window2)
        l.addWidget(button2)

        button3 = QPushButton("Display Available Coins")
        button3.clicked.connect(self.toggle_window3)
        l.addWidget(button3)

        button4 = QPushButton("Display Configurations")
        button4.clicked.connect(self.toggle_window4)
        l.addWidget(button4)

        button5 = QPushButton("Set Configurations")
        button5.clicked.connect(self.toggle_window5)
        l.addWidget(button5)

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

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
