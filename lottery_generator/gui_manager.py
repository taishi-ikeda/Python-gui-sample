import tkinter as tk
from tkinter import ttk
import status_handler
import lottery_class as lc

class gui_manager:
    __slots__=("_status_handler",
               "_root",
               "_lottery")

    def __init__(self)->None:
        self._root=tk.Tk()
        self._status_handler=\
                status_handler.status_handler("lot6",\
                                              self._root)
        pass

    def execute(self,event)->None:
        self._lottery.init_widget()
        self._lottery.execute()

    def status_change(self,event,v:tk.StringVar):
        current_status = self._status_handler.get_status()
        if not current_status == v:
            self._status_handler.set_status(v)
            if self._status_handler.get_status()=="lot6":
                self._lottery = lc.lottery_lot6(self._root)
            elif self._status_handler.get_status()=="lot7":
                self._lottery = lc.lottery_lot7(self._root)
            else:
                self._lottery = lc.lottery_minilot(self._root)



    def run(self)->None:

        self._root.title("Lottery Number Generator")
        self._root.geometry("600x200")

        label=tk.Label(self._root,\
                       text="Which lottery are you interested in ?")
        label.place(relx=0.1,rely=0.1,anchor=tk.SW)

        options=["lot6","lot7","mini_lot"]
        v=tk.StringVar()
        combo = ttk.Combobox(self._root,\
                             values=options,\
                             textvariable=v,\
                             state="readonly")
        combo.bind("<<ComboboxSelected>>",\
                lambda event: self.status_change(event,combo.get()))
        combo.place(relx=0.1,rely=0.2,anchor=tk.SW)

        buttom=tk.Button(text="execute",width=15)
        buttom.bind('<Button-1>',self.execute)
        buttom.place(relx=0.5,rely=0.2,anchor=tk.SW)

        lot6 = lc.lottery_lot6(self._root)
        self._lottery = lot6
        self._lottery.show_widget()

        #txtBox=tk.Entry()
        #txtBox.configure(state="normal",width=50)
        #txtBox.pack()

        self._root.mainloop()
        self._lottery.__del__()
