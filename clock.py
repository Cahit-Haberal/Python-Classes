import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


class digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self): 
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 300, 300, 100)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("font-size: 100px;""font-family: Arial;""color: light;")
        self.setStyleSheet("background-color: black;")            
        
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
         
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
        
        
def main():
    app = QApplication(sys.argv)
    clock = digital_clock()
    clock.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()