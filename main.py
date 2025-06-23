import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class HalfCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HalfCalc")
        self.setFixedSize(300, 400)
        self.setStyleSheet("""
            QWidget {
                background-color: #1b1b1b;
                color: #f2f2f2;
                font-family: "MS Gothic", monospace;
                font-size: 18px;
            }
            QLineEdit {
                background-color: #2a2a2a;
                border: 3px double #FF6A00;
                color: #f2f2f2;
                padding: 10px;
                font-size: 24px;
            }
            QPushButton {
                background-color: #2a2a2a;
                border: 1px solid #FF6A00;
                color: #FF6A00;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
                color: #ffffff;
            }
        """)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C']
        ]

        grid = QGridLayout()
        for row, row_data in enumerate(buttons):
            for col, key in enumerate(row_data):
                btn = QPushButton(key)
                btn.clicked.connect(lambda _, k=key: self.on_click(k))
                grid.addWidget(btn, row, col)
        layout.addLayout(grid)
        self.setLayout(layout)

    def on_click(self, key):
        if key == 'C':
            self.display.clear()
        elif key == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + key)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = HalfCalc()
    calc.show()
    sys.exit(app.exec_())
