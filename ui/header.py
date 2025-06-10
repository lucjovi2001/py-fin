from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget


class HeaderWidget(QWidget):
    def __init__(self, header_text):
        super().__init__()

        self.__init_ui(header_text)

    def __init_ui(self, header_text):
        self.__header_label = QLabel(header_text)
        self.__header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.__hline = QFrame()
        self.__hline.setFrameShape(QFrame.Shape.HLine)

        layout = QVBoxLayout()
        layout.addWidget(self.__header_label, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.__hline, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addStretch(1)

        self.setLayout(layout)
