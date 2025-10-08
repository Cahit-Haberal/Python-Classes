import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QButtonGroup
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.result_show = QLineEdit(self)
        self.submit_button = QPushButton("=",self)
        
        self.plus_sign = QPushButton("+", self)
        self.minus_sign = QPushButton("-", self)
        self.product_sign = QPushButton("*", self)
        self.division_sign = QPushButton("/", self)
        
        self.zero = QPushButton("0", self)
        self.one = QPushButton("1", self)
        self.two = QPushButton("2", self)
        self.three = QPushButton("3", self)
        self.four = QPushButton("4", self)
        self.five = QPushButton("5", self)
        self.six = QPushButton("6", self)
        self.seven = QPushButton("7", self)
        self.eight = QPushButton("8", self)
        self.nine = QPushButton("9", self)
        
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("CALCULATOR")
        self.setGeometry(500, 300, 300, 300)
        self.setFixedSize(270,430)
        
        self.setStyleSheet("""QPushButton{
            font-size: 20px;
            padding: 20px;}
        QLineEdit{
            font-size: 24px;
            padding: 5px;}""")
        
        
        self.result_show.setPlaceholderText("Enter...")
    
        
        result_hbox = QHBoxLayout()
        result_hbox.addWidget(self.result_show)
        result_hbox.addWidget(self.submit_button)
        result_hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_show.setFixedWidth(165)
        self.result_show.setFixedHeight(65)
        self.submit_button.setFixedWidth(55)
        
        numbers_vbox = QVBoxLayout()
        
        row1 = QHBoxLayout()
        
        row1.addWidget(self.one)
        row1.addWidget(self.two)
        row1.addWidget(self.three)
        row1.addWidget(self.minus_sign)
        
        row2 = QHBoxLayout()
               
        row2.addWidget(self.four)
        row2.addWidget(self.five)
        row2.addWidget(self.six)
        row2.addWidget(self.product_sign)
        
        row3 = QHBoxLayout()
               
        row3.addWidget(self.seven)
        row3.addWidget(self.eight)
        row3.addWidget(self.nine)
        row3.addWidget(self.plus_sign)
        
        row4 = QHBoxLayout()
        
        row4.addWidget(self.zero)
        row4.addWidget(self.division_sign)
        self.zero.setFixedWidth(165)
        
        numbers_vbox.addLayout(row1)
        numbers_vbox.addLayout(row2)
        numbers_vbox.addLayout(row3)
        numbers_vbox.addLayout(row4)
        numbers_vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        main_vbox = QVBoxLayout()
        
        main_vbox.addLayout(result_hbox)
        main_vbox.addLayout(numbers_vbox)
        
        main_vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)        
        
        self.setLayout(main_vbox)
        
        self.zero.clicked.connect(self.button_0)
        self.one.clicked.connect(self.button_1)
        self.two.clicked.connect(self.button_2)
        self.three.clicked.connect(self.button_3)
        self.four.clicked.connect(self.button_4)
        self.five.clicked.connect(self.button_5)
        self.six.clicked.connect(self.button_6)
        self.seven.clicked.connect(self.button_7)
        self.eight.clicked.connect(self.button_8)
        self.nine.clicked.connect(self.button_9)
        
        self.plus_sign.clicked.connect(self.button_plus)
        self.minus_sign.clicked.connect(self.button_minus)
        self.product_sign.clicked.connect(self.button_pro)
        self.division_sign.clicked.connect(self.button_div)
        self.submit_button.clicked.connect(self.button_eq)
    
        
    def button_0(self):
        current = self.result_show.text()
        self.result_show.setText(current + "0")
        
    def button_1(self):
        current = self.result_show.text()
        self.result_show.setText(current + "1")
        
    def button_2(self):
        current = self.result_show.text()
        self.result_show.setText(current + "2")

    def button_3(self):
        current = self.result_show.text()
        self.result_show.setText(current + "3")

    def button_4(self):
        current = self.result_show.text()
        self.result_show.setText(current + "4")
        
    def button_5(self):
        current = self.result_show.text()
        self.result_show.setText(current + "5")
        
    def button_6(self):
        current = self.result_show.text()
        self.result_show.setText(current + "6")

    def button_7(self):
        current = self.result_show.text()
        self.result_show.setText(current + "7")

    def button_8(self):
        current = self.result_show.text()
        self.result_show.setText(current + "8")
        
    def button_9(self):
        current = self.result_show.text()
        self.result_show.setText(current + "9")
        
    def button_plus(self):
        current = self.result_show.text()
        self.result_show.setText(current + "+")
        
    def button_minus(self):
        current = self.result_show.text()
        self.result_show.setText(current + "-")
        
    def button_pro(self):
        current = self.result_show.text()
        self.result_show.setText(current + "*")

    def button_div(self):
        current = self.result_show.text()
        self.result_show.setText(current + "/")
        
    def button_eq(self):
        current = self.result_show.text()
        temp2, total = 0, 0
        
        temp = ""
        nums = []
        operator = []
        for i in current:
            if i.isdigit():
                temp += i
            else:
                nums.append(temp)
                operator.append(i)
                temp = ""
        nums.append(temp)

        while "*" in operator or "/" in operator:
            temp4 = 0
            temp3 = 0
            for i in operator:
                if i == "*":
                    temp4 = float(nums[operator.index(i)]) * float(nums[operator.index(i) + 1])
                    nums[temp3] = temp4
                    print(nums)
                    print(operator)
                    nums.pop(temp3 + 1)
                    operator.pop(temp3)
                    print(nums)
                    print(operator)
                    break
                elif i == "/":
                    temp4 = float(nums[operator.index(i)]) / float(nums[operator.index(i) + 1])
                    nums[temp3] = temp4
                    nums.pop(temp3 + 1)
                    operator.pop(temp3)
                    break
                temp3 += 1

        for i in operator:
                
            if i == "+":
                if temp2 == 0:
                    total += float(nums[operator.index(i)]) + float(nums[operator.index(i) + 1])
                else:
                    total += float(nums[temp2 + 1])
            elif i == "-":
                if temp2 == 0:
                    total += float(nums[operator.index(i)]) - float(nums[operator.index(i) + 1])
                else:
                    total -= float(nums[temp2 + 1])
            temp2 += 1
            
        if temp2 == 0:
            total = float(nums[0]) 
        self.result_show.setText(f"{total}")

        operator.clear()


def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()