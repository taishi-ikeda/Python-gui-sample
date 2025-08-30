import tkinter as tk
from abc import ABCMeta,abstractmethod
import random

class lottery_base():
    __slots__=("_root",
               "_text_widget",
               "_mode_label")

    def __init__(self,root:tk.Tk,mode:str)->None:
        self._root=root
        self._text_widget = tk.Text(self._root,\
                                    height=1,
                                    width=30)
        self._text_widget.place(relx=0.5,rely=0.4,anchor=tk.CENTER)
        self._mode_label = tk.Label(self._root,\
                            text=mode)
        self._mode_label.place(relx=0.5,rely=0.3,anchor=tk.CENTER)
        #self._text_widget.pack()
        pass

    def has_same_number(self,rlist:list[int],v:int)->bool:
        for ele in rlist:
            if ele == v:
                return True
        return False

    @abstractmethod
    def show_widget(self)->None:
        pass

class lottery_lot6(lottery_base):
    __slots__=("_size_list",
               "_max_random_number")
    def __init__(self,root:tk.Tk)->None:
        super().__init__(root,"lot6")
        self._size_list=6
        self._max_random_number=43
        pass

    def init_widget(self)->None:
        self._text_widget.delete("1.0",tk.END)

    def execute(self)->None:
        rand_list=[]
        for i in range(0,self._size_list):
            val = random.randint(1,self._max_random_number)
            while(self.has_same_number(rand_list,val)):
                val = random.randint(1,self._max_random_number)

            rand_list.append(val)

        for val in rand_list:
            self._text_widget.insert(tk.END,str(val))
            self._text_widget.insert(tk.END,"  ")
        return

    def __del__(self):
        pass
        #self._text_widget.delete("1.0",tk.END)

class lottery_lot7(lottery_base):
    __slots__=("_size_list",
               "_max_random_number")
    def __init__(self,root:tk.Tk)->None:
        super().__init__(root,"lot7")
        self._size_list=7
        self._max_random_number=37
        pass

    def init_widget(self)->None:
        self._text_widget.delete("1.0",tk.END)

    def execute(self)->None:
        rand_list=[]
        for i in range(0,self._size_list):
            val = random.randint(1,self._max_random_number)
            while(self.has_same_number(rand_list,val)):
                val = random.randint(1,self._max_random_number)

            rand_list.append(val)

        for val in rand_list:
            self._text_widget.insert(tk.END,str(val))
            self._text_widget.insert(tk.END,"  ")
        return

    def __del__(self):
        pass
        #self._text_widget.delete("1.0",tk.END)

class lottery_minilot(lottery_base):
    __slots__=("_size_list",
               "_max_random_number")
    def __init__(self,root:tk.Tk)->None:
        super().__init__(root,"mini lot")
        self._size_list=5
        self._max_random_number=31
        pass

    def init_widget(self)->None:
        self._text_widget.delete("1.0",tk.END)

    def execute(self)->None:
        rand_list=[]
        for i in range(0,self._size_list):
            val = random.randint(1,self._max_random_number)
            while(self.has_same_number(rand_list,val)):
                val = random.randint(1,self._max_random_number)

            rand_list.append(val)

        for val in rand_list:
            self._text_widget.insert(tk.END,str(val))
            self._text_widget.insert(tk.END,"  ")
        return

    def __del__(self):
        pass
        #self._text_widget.delete("1.0",tk.END)
