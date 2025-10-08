import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 300, 400, 200)
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Stop Watch")
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""QPushButton, QLabel{padding: 20px;font-weight: bold;}QPushButton{font-size: 40px;font-family: Arial;}QLabel{font-size: 60px;}""")  
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
        
        
    def start(self):
        self.timer.start(10)
        
    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText("00:00:00.00")
    
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        miliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:02}"
    
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
    
def main():
    app = QApplication(sys.argv)
    Stopwatch = stopwatch()
    Stopwatch.show()
    sys.exit(app.exec_())
        


if __name__ == "__main__":
    main()
