import sys

from PyQt6.QtWidgets import QApplication

from controllers.main_controller import MainController
from services.database import init_db
from views.main_window import MainWindow


def main():
    init_db()

    app = QApplication(sys.argv)

    window = MainWindow()

    controller = MainController("", window)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
