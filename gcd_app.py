from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QLineEdit, QApplication
from PyQt6.QtCore import Qt
import sys

def gcd(a, b):
    if b == 0: 
        return a
    else:
        return gcd(b, a % b)

class GCDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вычислитель НОД")
        self.resize(300, 200)
        self.initUI()

    def initUI(self):

        self.label_a = QLabel("Введите a:")
        self.label_b = QLabel("Введите b:")
        self.label_result = QLabel("НОД:")
        self.button_calculate = QPushButton("Результат")
        self.button_clear = QPushButton("Очистить")

        self.input_a = QLineEdit()
        self.input_b = QLineEdit()

        self.output_gcd = QLineEdit()
        self.output_gcd.setReadOnly(True)

        layout = QGridLayout()
        layout.addWidget(self.label_a, 0, 0)
        layout.addWidget(self.input_a, 0, 1)
        layout.addWidget(self.label_b, 1, 0)
        layout.addWidget(self.input_b, 1, 1)
        layout.addWidget(self.label_result, 2, 0)
        layout.addWidget(self.output_gcd, 2, 1)
        layout.addWidget(self.button_calculate, 3, 1)
        layout.addWidget(self.button_clear, 3, 0)

        self.setLayout(layout)

        self.button_calculate.clicked.connect(self.calculate_gcd)
        self.button_clear.clicked.connect(self.clear_input)

    def calculate_gcd(self):
        a = int(self.input_a.text())
        b = int(self.input_b.text())

        GCD = gcd(a, b)
        self.output_gcd.setText(str(GCD))

    def clear_input(self):
        self.input_a.clear()
        self.input_b.clear()
        self.output_gcd.clear()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Up:
            self.input_a.setFocus()

        elif event.key() == Qt.Key.Key_Down:
            self.input_b.setFocus()

        elif event.key() == Qt.Key.Key_Return or Qt.Key.Key_Kp_EN:
            self.calculate_gcd()

app = QApplication(sys.argv)
window = GCDApp()
window.show()

app.exec()