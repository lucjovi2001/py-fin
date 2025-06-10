import sys

from PyQt6.QtWidgets import QApplication

from services.database import init_db
from views.main_window import MainWindow


def main():
    init_db()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
