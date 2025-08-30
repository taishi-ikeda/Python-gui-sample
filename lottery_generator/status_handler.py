import tkinter as tk

class status_handler:
    __slots__=("_lottery_mode",
               "_root")

    def __init__(self,\
            initial_lottery_mode:tk.StringVar,
            root:tk.Tk)->None:
        self._lottery_mode=initial_lottery_mode
        self._root=root
        pass

    def get_status(self)->tk.StringVar:
        return self._lottery_mode

    def set_status(self,lottery_mode:tk.StringVar)->None:
        self._lottery_mode=lottery_mode
