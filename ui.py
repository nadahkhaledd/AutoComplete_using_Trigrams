import sys

from PyQt5.QtWidgets import *

from assigmentnlp import output


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Auto complete')
        self.init_ui()
        self.setBaseSize(1800, 900)

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.title = QLabel('Auto Complete ')
        self.search_input = QLineEdit()
        self.result = QLabel('')
        self.button = QPushButton('search')

        self.button.clicked.connect(self.get_results)
        self.button.setAutoDefault(True)
        self.search_input.returnPressed.connect(self.button.click)

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.search_input)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.result)

        self.setLayout(self.layout)

        self.show()

    def get_results(self):
        input = self.search_input.text()
        out = output(input)
        self.result.setText(out)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
