from views.main_window import MainWindow


class MainController:
    def __init__(self, model, view: MainWindow):
        self.__model = model
        self.__view = view

        self.__view.bind_transaction_add_button(self.__handle_click)

    def __handle_click(self):
        transaction = self.__view.get_entry_inputs()
        print(transaction)
