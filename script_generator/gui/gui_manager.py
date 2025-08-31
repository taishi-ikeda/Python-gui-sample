import os
import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as simpledialog
import tkinter.filedialog
from . import data_manager

class gui_manager:
    __slots__=("_main_window",
               "_data_manager",
               "_template_filename",
               "_replace_maker",
               "_par_tree",
               "_pmenu",
               "_template_script")
    def __init__(self)->None:
        self._main_window = tk.Tk()
        self._replace_maker = "@"
        self._data_manager = data_manager.data_manager()
        self._pmenu = ""
        self._template_script = []
        pass

    def _delete_collumn(self,item_id:int):
        self._data_manager.delete_data(item_id)
        self._show_tree()

    def _copy_collumn(self,item_id:int):
        self._data_manager.copy_data(item_id)
        self._show_tree()

    def _select_collumn(self,event):
        if type(self._pmenu) == tk.Menu:
            self._pmenu.delete(0,tk.END)
        item_id = self._par_tree.identify_row(event.y)
        if item_id:
            self._pmenu = tk.Menu(self._main_window,tearoff=0)
            self._pmenu.add_command(label="Delete",\
                    command=lambda : self._delete_collumn(int(item_id)))
            self._pmenu.add_command(label="Copy",\
                    command=lambda : self._copy_collumn(int(item_id)))
            self._pmenu.post(event.x_root,event.y_root)

    def _change_value(self,event):
        item_id_x = self._par_tree.identify_column(event.x)
        item_id_y = self._par_tree.identify_row(event.y)
        print("item_id_x,item_id_y = ",item_id_x,item_id_y)
        if item_id_x and item_id_y:
            #tk.Tk().withdraw()
            new_value = simpledialog.askstring("Change value ?","")
            if new_value:
                self._data_manager.update_data(int(item_id_x[1:])-1,\
                                               int(item_id_y),str(new_value))
                self._show_tree()

    def _load_template_file(self)->None:
        f = open(self._template_filename,'r')
        text_list=f.readlines()
        for text in text_list:
            self._template_script.append(text)
            if text.count(self._replace_maker) == 2:
                init = text.find(self._replace_maker)
                last = text.rfind(self._replace_maker)
                sliced_text = text[init+1:last]
                if sliced_text.count(":")==1:
                    init2 = sliced_text.find(":")
                    par_name = sliced_text[:init2]
                    par_val = sliced_text[init2+1:]
                    self._data_manager.append_parameter(par_name,par_val)

    def _show_tree(self)->None:
        self._data_manager.view(self._par_tree)
        self._par_tree.pack(pady=10)

    def _generate_script(self,evnet)->None:
        output_script_name_template = simpledialog.askstring("Output file name","")
        if output_script_name_template.count(self._replace_maker) == 2:
            init = output_script_name_template.find(self._replace_maker)
            last = output_script_name_template.rfind(self._replace_maker)
            file_prefix = output_script_name_template[:init]
            file_suffix = output_script_name_template[last+1:]
            self._data_manager.script_generator(file_prefix,file_suffix,\
                self._template_script,self._replace_maker)


    def run(self)->None:
        self._main_window.title("Script Generator")
        self._main_window.geometry("1200x600")

        fTyp = [("","*")]
        iDir = os.path.abspath(os.path.dirname(__file__)) + "../"
        fname = tkinter.filedialog.askopenfilename(filetypes=fTyp,initialdir=iDir)
        self._template_filename = fname
        self._load_template_file()
        self._data_manager.initialize_data()

        self._par_tree = ttk.Treeview(self._main_window)
        self._data_manager.view_init(self._par_tree)
        self._show_tree()
        self._par_tree.bind("<Button-3>",self._select_collumn)
        self._par_tree.bind("<Button-1>",self._change_value)
        generate_buttom=tk.Button(text="generate",width=15)
        generate_buttom.bind('<Button-1>',self._generate_script)
        generate_buttom.place(relx=0.6,rely=0.9,anchor=tk.CENTER)
        self._main_window.mainloop()
