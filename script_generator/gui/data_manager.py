import json
import copy
from typing import overload
from tkinter import ttk

class data_manager:
    __slots__=("_data",
               "_par_list",
               "_par_name_list")

    def __init__(self)->None:
        self._data = []
        self._par_list={}
        self._par_name_list = []


    def _is_float(self,s)->bool:
        try:
            float(s)
            return True
        except ValueError:
            return False

    def _is_int(self,s)->bool:
        try:
            int(s)
            return True
        except ValueError:
            return False

    def append_parameter(self,par_name:str,val:str)->None:
        if self._is_int(val):
            self._par_list[par_name] = int(val)
        elif self._is_float(val):
            self._par_list[par_name] = float(val)
        else:
            self._par_list[par_name] = val
        self._par_name_list.append(par_name)
        return

    def initialize_data(self)->None:
        temp_dict = {}
        for par_name,val in self._par_list.items():
            temp_dict[par_name]=val
        self._data.append(temp_dict)

    def delete_data(self,item_id:int)->None:
        clen = len(self._data)
        print("clen = ",clen)
        print("item_id = ",item_id)
        if clen==1:
            return
        data_temp = []
        for i in range(0,clen):
            if not i == item_id:
                data_temp.append(self._data[i])
        self._data = copy.copy(data_temp)

    def copy_data(self,item_id:int)->None:
        clen = len(self._data)
        data_copy = copy.copy(self._data)
        data_target = copy.copy(data_copy[item_id])
        if clen <= item_id+1:
            data_copy.append(data_target)
        else:
            data_copy.append({})
            data_copy[item_id+1] = data_target
            for i in range(item_id+1,clen+1):
                data_copy[i] = self._data[i-1]
        self._data = copy.copy(data_copy)

    def update_data(self,item_id_x:int,item_id_y:int,val:str)->None:
        par_name = self._par_name_list[item_id_x]
        current_val = self._data[item_id_y][par_name]
        print(self._data[item_id_y][par_name])
        print(type(current_val))
        if 'int' in str(type(current_val)):
            if self._is_int(val):
                self._data[item_id_y][par_name] = int(val)
            else:
                return
        elif 'float' in str(type(current_val)):
            if self._is_float(val):
                self._data[item_id_y][par_name] = float(val)
            else:
                return
        else:
            self._data[item_id_y][par_name] = val
        return

    def view_init(self,tree:ttk.Treeview)->None:
        columns_list=()
        for par_name in self._par_list.keys():
            columns_list += (par_name,)
        tree['columns'] = columns_list
        tree.column('#0',width=50,stretch='yes')
        tree.heading('#0',text='id')
        for par_name in self._par_name_list:
            tree.column(par_name,width=100,anchor='center')
            tree.heading(par_name,text=par_name,anchor='center')

    def view(self,tree:ttk.Treeview)->None:
        for i in tree.get_children():
            print(i)
            tree.delete(i)
        #columns_list=()
        #for par_name in self._par_list.keys():
        #    columns_list += (par_name,)
        #tree['columns'] = columns_list
        #tree.column('#0',width=50,stretch='yes')
        #tree.heading('#0',text='id')
        #for par_name in self._par_name_list:
        #    tree.column(par_name,width=100,anchor='center')
        #    tree.heading(par_name,text=par_name,anchor='center')
        iid = 0
        print(self._data)
        for par_data in self._data:
            value_list=()
            for par_name in self._par_name_list:
                value_list += (par_data[par_name],)
            tree.insert(parent="",index='end',iid=iid,values=value_list)
            iid +=1

    def script_generator(self,file_prefix:str,\
            file_suffix,template_script:list[str],\
            replace_marker:str)->None:
        num_data = len(self._data)
        for iid in range(0,num_data):
            with open(file_prefix+str(iid)+file_suffix,"w") as of:
                for text in template_script:
                    if text.count(replace_marker) == 2:
                        init = text.find(replace_marker)
                        last = text.rfind(replace_marker)
                        sliced_text = text[init+1:last]
                        if sliced_text.count(":")==1:
                            init2 = sliced_text.find(":")
                            print("126",sliced_text[:init2])
                            par_name = sliced_text[:init2]
                            par_val = self._data[iid][par_name]
                            text = text[0:init] + \
                                    str(par_val) + \
                                    text[last+1:]
                    of.write(text)

