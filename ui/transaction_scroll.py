from PyQt6.QtWidgets import QPushButton, QScrollArea, QVBoxLayout, QWidget


class TransactionScrollArea(QScrollArea):
    def __init__(self):
        super().__init__()

        self.__init_ui()

    def __init_ui(self):
        self.setMinimumHeight(120)
        self.setWidgetResizable(True)

        self.__content_widget = QWidget()

        content_layout = QVBoxLayout(self.__content_widget)

        self.setWidget(self.__content_widget)
