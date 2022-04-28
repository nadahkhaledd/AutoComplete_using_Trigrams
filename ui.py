import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

from assigmentnlp import output


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Auto complete')
        self.init_ui()

        self.show()

    def init_ui(self):
        layout = QVBoxLayout()
        title = QLabel('Auto Complete ')
        # title.setFont(QFont('helvetica', 14))
        # title.setAlignment(QtCore.Qt.AlignCenter)
        search_input = QLineEdit()
        result = QLabel('')

        button = QPushButton('search')
        # button.setStyleSheet("background-color : green")
        # button.setFixedSize(90, 25)

        button.clicked.connect(self.get_results)
        button.setAutoDefault(True)
        search_input.returnPressed.connect(button.click)

        layout.addWidget(title)
        layout.addWidget(search_input)
        layout.addWidget(button)
        layout.addWidget(result)

        self.setLayout(layout)

    def get_results(self):
        input = self.search_input.text()
        out = output(input)
        self.result.setText(out)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
