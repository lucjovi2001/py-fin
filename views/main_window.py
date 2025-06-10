from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from ui.header import HeaderWidget
from ui.transaction_entry import TransactionEntryWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("PyFin")
        self.resize(720, 720)

        self.__header = HeaderWidget("Home")

        self.__transaction_input = TransactionEntryWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.__header)
        layout.addWidget(self.__transaction_input, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addStretch(1)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
