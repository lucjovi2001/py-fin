from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from ui.header import HeaderWidget
from ui.transaction_entry import TransactionEntryWidget
from ui.transaction_scroll import TransactionScrollArea


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("PyFin")
        self.resize(720, 720)

        self.__header = HeaderWidget("Home")

        self.__transaction_entry = TransactionEntryWidget()

        self.__transaction_scroll = TransactionScrollArea()

        transactions_layout = QVBoxLayout()
        transactions_layout.addWidget(self.__transaction_entry)
        transactions_layout.addWidget(self.__transaction_scroll)
        transactions_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout = QVBoxLayout()
        layout.addWidget(self.__header)
        layout.addLayout(transactions_layout)
        layout.addStretch(1)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def bind_transaction_add_button(self, callback):
        self.__transaction_entry.bind_transaction_add_button(callback)

    def get_entry_inputs(self):
        return self.__transaction_entry.get_entry_inputs()
