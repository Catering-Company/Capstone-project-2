# FUNCTIONALITY TESTING FOR GUI SUB-MENU


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel


# Gets the user to input a new minimum amount of coins that the user can enter 
# into the Coin Calulator and Mutiple Coin Calculator. There are restrictions
# in place to prevent the user from entering:
# - Any non-integer.
# - A min value less than 0.
# - A min value greater than or equal to 10000.
# - A min value greater than the current max value.
#  If any of the above happens then min_coin_value returns a negative integer and
# min_value_button_clicked will print 'Request denied'.
def min_coin_value(textboxValue):
    try:
        textboxValue = int(textboxValue)
        if int(textboxValue) < 0:
            return -1
        if int(textboxValue) >= 10000:
            return -2
        if int(textboxValue) > int(config["max_coin_value"]):
            return -3           
    except:
        return -4
    return int(textboxValue)


# Gets the user to input a new maximum amount of coins that the user can enter 
# into the Coin Calulator and Mutiple Coin Calculator. There are restrictions
# in place to prevent the user from entering:
# - Any non-integer.
# - A max value less than 0.
# - A max value greater than 10000.
# - A max value less than the current min value. 
#  If any of the above happens then min_coin_value returns a negative integer and 
# max_value_button_clicked will print 'Request denied'.
def max_coin_value(textboxValue):
    try:
        textboxValue = int(textboxValue)
        if int(textboxValue) < 0:
            return -1
        if int(textboxValue) > 10000:
            return -2
        if int(textboxValue) < int(config["min_coin_value"]):  
            return -3
    except:
        return -4
    return int(textboxValue)


def window():
   # Note: app is used to only to write app.exec_() at the end of this function.
   # Not sure why this is necessary but I'll look into it.
   app = QApplication([])

   # This is used in order to define a new widget (e.g. button or textbox).
   # To define a new widget, write Qwidget_name(widget), where widget_name
   # is the name of the widget (e.g. pounds_button = QPushButton(widget))
   widget = QWidget()
   

   #======================= FUNCTIONS FOR BUTTONS ========================
   def pounds_button_clicked():
      config["currency"] = "POUNDS STERLING"
      currency_value_label.setText("Your currency is set to Pounds Sterling.")
      print(config)

   def dollars_button_clicked():
      config["currency"] = "US DOLLARS"
      currency_value_label.setText("Your currency is set to US Dollars.")
      print(config)   

   def min_value_button_clicked():
      textboxValue = min_value_box.text()
      testing_value = min_coin_value(textboxValue)
      if testing_value >= 0:
         config["min_coin_value"] = textboxValue
         min_value_label.setText(f"Result: The minimum coin value has been changed to {textboxValue}.")
      if testing_value == -1:
          min_value_label.setText(f"Result: Request denied. The minimum must be at least 0.")
      if testing_value == -2:
         min_value_label.setText(f"Result: Request denied. The minimum coin value must be below 10000.")
      if testing_value == -3:
         min_value_label.setText(f"Result: Request denied. That is larger than the maximum coin amount!")
      if testing_value == -4:
         min_value_label.setText(f"Result: Request denied. Please enter a number.")
      print(testing_value)
      print(textboxValue)
      print(config)

   def max_value_button_clicked():
      textboxValue = max_value_box.text()
      testing_value = max_coin_value(textboxValue)
      if testing_value >= 0:
         config["max_coin_value"] = textboxValue
         max_value_label.setText(f"Result: The maximum coin value has been changed to {textboxValue}.")
      if testing_value == -1:
          max_value_label.setText(f"Result: Request denied. The maximum cannot be below 0!")
      if testing_value == -2:
         max_value_label.setText(f"Result: Request denied. The maximum coin value must be below 10000.")
      if testing_value == -3:
         max_value_label.setText(f"Result: Request denied. That is smaller than the minimum coin amount!")
      if testing_value == -4:
         max_value_label.setText(f"Result: Request denied. Please enter a number.")
         print(textboxValue)
      print(config)

   #=================================================================

#========== CURRENCY BUTTONS AND LABELS ===============
   pounds_button = QPushButton(widget)
   pounds_button.setText("Pounds Sterling")
   pounds_button.move(100,200)
   pounds_button.clicked.connect(pounds_button_clicked)

   dollars_button = QPushButton(widget)
   dollars_button.setText("US Dollars")
   dollars_button.move(400,200)
   dollars_button.clicked.connect(dollars_button_clicked)

   currency_value_label = QLabel(widget)
   currency_value_label.move(180,240)
   currency_value_label.setFixedSize(450, 20)
   currency_value_label.setText(f"Your currency is set to {config['currency'].title()}.")

#======================================================


#============= COIN VALUE BUTTONS AND LABELS===========
   min_value_box = QLineEdit(widget)
   min_value_box.resize(250, 20)
   min_value_box.setPlaceholderText("Enter a minimum value")
   min_value_box.move(100,300)

   min_value_button = QPushButton(widget)
   min_value_button.setText("Change min value")
   min_value_button.move(350, 300)
   min_value_button.clicked.connect(min_value_button_clicked)

   min_value_label = QLabel(widget)
   min_value_label.move(100,340)
   min_value_label.setFixedSize(450, 20)
   min_value_label.setText("Result:")
   

   max_value_box = QLineEdit(widget)
   max_value_box.resize(250, 20)
   max_value_box.setPlaceholderText("Enter a maximum value")
   max_value_box.move(100,380)

   max_value_button = QPushButton(widget)
   max_value_button.setText("Change max value")
   max_value_button.move(350, 380)
   max_value_button.clicked.connect(max_value_button_clicked)

   max_value_label = QLabel(widget)
   max_value_label.move(100,420)
   max_value_label.setFixedSize(450, 20)
   max_value_label.setText("Result:")

#==========================================================


   # Fixes the size of the window
   widget.setFixedSize(600, 480)
   # Names the window
   widget.setWindowTitle("Sub Menu")
   # Allows the widgets to show up
   widget.show()


   # I don't know why this is necessary but it is
   app.exec_()


# Program configurations
config = {
    "currency": "POUNDS STERLING",
    "min_coin_value": 0,
    "max_coin_value": 10000,
}


window()