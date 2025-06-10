from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QComboBox, QHBoxLayout, QLineEdit, QPushButton, QWidget

MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

TYPES = ["Expense", "Income"]


class TransactionEntryWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.__init_ui()

    def __init_ui(self):
        self.__description_entry = QLineEdit()
        self.__description_entry.setPlaceholderText("Description")
        self.__description_entry.setMaxLength(32)

        self.__amount_entry = QLineEdit()
        self.__amount_entry.setPlaceholderText("Amount (USD)")

        self.__month_dropdown = QComboBox()
        self.__month_dropdown.addItems(MONTHS)

        self.__type_dropdown = QComboBox()
        self.__type_dropdown.addItems(TYPES)

        self.__add_button = QPushButton("Add")

        entry_layout = QHBoxLayout()
        entry_layout.addWidget(self.__description_entry)
        entry_layout.addWidget(self.__amount_entry)
        entry_layout.addWidget(self.__month_dropdown)
        entry_layout.addWidget(self.__type_dropdown)
        entry_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout = QHBoxLayout()
        layout.addLayout(entry_layout)
        layout.addStretch(1)
        layout.addWidget(self.__add_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)
