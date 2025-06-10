from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from ui.header_widget import HeaderWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__init_ui()

    def __init_ui(self):
        self.setWindowTitle("PyFin")
        self.resize(720, 720)

        self.__header = HeaderWidget("Home")

        layout = QVBoxLayout()
        layout.addWidget(self.__header)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
