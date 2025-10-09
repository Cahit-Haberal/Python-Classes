import sys
import requests
import math
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class Weather(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel("Enter city name:")
        self.entry = QLineEdit(self)
        self.submit = QPushButton("Get Weather",self)
        self.temperture_data = QLabel(self)
        self.symbole = QLabel(self)
        self.weather_data = QLabel(self)
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(300, 150, 300, 500)
        self.setFixedSize(300, 500)
        self.setStyleSheet("""QPushButton{padding: 15px;font-size: 30px;font-family: Arial;}QLineEdit{padding: 15px;font-size: 30px;}QLabel{font-size: 30px;font-family: Arial;}""")
        self.title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.temperture_data.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.weather_data.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.symbole.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        buttons_vbox = QVBoxLayout()

        buttons_vbox.addWidget(self.title)
        buttons_vbox.addWidget(self.entry)
        buttons_vbox.addWidget(self.submit)
        buttons_vbox.addWidget(self.temperture_data)
        buttons_vbox.addStretch()
        buttons_vbox.addWidget(self.symbole)
        buttons_vbox.addStretch()
        buttons_vbox.addWidget(self.weather_data)
        
        
        main_vbox = QHBoxLayout()
        
        main_vbox.addLayout(buttons_vbox)
        main_vbox.setAlignment(Qt.AlignmentFlag.AlignTop)        
        
        self.setLayout(main_vbox)
        
        self.submit.clicked.connect(self.submit_button)
        
    def submit_button(self):
        api_key = ""
        token = self.entry.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={token}&appid={api_key}"
         
        req = requests.get(url)
        data = req.json()
        
        print(f"{data}")
        if data["cod"] == 200:
            self.temperture_data.setText(f"{round((data['main']["temp"]) - 273)}°C/{round((data['main']["temp"]) - 273) * 1.8 + 32}°F")
            self.weather_data.setText(f"{data["weather"][0]["description"]}")
            self.print_symboles()
            
        else:
            self.temperture_data.setText(f"City not exists:\n{token}")
            self.weather_data.setText("")
        
    def print_symboles(self):
        if self.weather_data.text() == "Clouds":
            self.symbole.setText("☁")
        elif self.weather_data.text() == "Sunny" or "Clear":
            self.symbole.setText("☀️")
        elif self.weather_data.text() == "Rain":
            self.symbole.setText("⛆")
            

    
def main():
    window = QApplication(sys.argv)
    weather = Weather()
    weather.show()
    sys.exit(window.exec_())


if __name__ == "__main__":
    main()
