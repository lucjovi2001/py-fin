from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QComboBox,
    QDoubleSpinBox,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
)

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
        self.__description_entry.setMinimumWidth(160)
        self.__description_entry.setMaxLength(32)

        self.__amount_entry = QDoubleSpinBox()
        self.__amount_entry.setPrefix("$")
        self.__amount_entry.setDecimals(2)
        self.__amount_entry.setRange(0, 1_000_000_000)
        self.__amount_entry.setSingleStep(1.00)

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

    def __clear_entry_inputs(self):
        self.__description_entry.clear()
        self.__amount_entry.clear()
        self.__amount_entry.setValue(0.00)
        self.__type_dropdown.setCurrentText("Expense")

    def bind_transaction_add_button(self, callback):
        self.__add_button.clicked.connect(callback)

    def get_entry_inputs(self):
        description = self.__description_entry.text().strip()
        amount = self.__amount_entry.text()
        month = self.__month_dropdown.currentText()
        type = self.__type_dropdown.currentText().lower()
        self.__clear_entry_inputs()

        return (description, amount, month, type)
