import copy
import json
import os
import subprocess
import sys
import tkinter
from tkinter.colorchooser import askcolor

import customtkinter

"""
Author: Akash Bora (Akascape)
License: MIT
Quick Guide:
This program can be used to create custom themes for customtkinter.
You can easily create and edit themes for your applications.
Customtkinter themefiles are .json files that can be used with customtkinter using the 'set_default_color_theme' method.
Example: customtkinter.set_default_color_theme("Path//my_theme.json")
A customtkinter theme has one dark and one light color attribute for each widget type and you have to choose the 2 colors for each widget type.
(You can switch between them with the 'set_appearance_mode' method)
Currently it is not possible to switch themes, so only appearance_mode can be changed.
Default reset color is "transparent" which has no color, means it take the color from the background instead.
(transparent is not supported in all widgets)
"""

class App(customtkinter.CTk):
    
    #--------------------Main Structure of the Theme File--------------------#
    
    json_data = {
                  "CTk": {
                    "fg_color": ["gray92", "gray14"]
                  },
                  "CTkToplevel": {
                    "fg_color": ["gray92", "gray14"]
                  },
                  "CTkFrame": {
                    "corner_radius": 6,
                    "border_width": 0,
                    "fg_color": ["gray86", "gray17"],
                    "top_fg_color": ["gray81", "gray20"],
                    "border_color": ["gray65", "gray28"]
                  },
                  "CTkButton": {
                    "corner_radius": 6,
                    "border_width": 0,
                    "fg_color": ["#3B8ED0", "#1F6AA5"],
                    "hover_color": ["#36719F", "#144870"],
                    "border_color": ["#3E454A", "#949A9F"],
                    "text_color": ["#DCE4EE", "#DCE4EE"],
                    "text_color_disabled": ["gray74", "gray60"]
                  },
                  "CTkLabel": {
                    "corner_radius": 0,
                    "fg_color": "transparent",
                    "text_color": ["gray10", "#DCE4EE"]
                  },
                  "CTkEntry": {
                    "corner_radius": 6,
                    "border_width": 2,
                    "fg_color": ["#F9F9FA", "#343638"],
                    "border_color": ["#979DA2", "#565B5E"],
                    "text_color":["gray10", "#DCE4EE"],
                    "placeholder_text_color": ["gray52", "gray62"]
                  },
                  "CTkCheckBox": {
                    "corner_radius": 6,
                    "border_width": 3,
                    "fg_color": ["#3B8ED0", "#1F6AA5"],
                    "border_color": ["#3E454A", "#949A9F"],
                    "hover_color": ["#3B8ED0", "#1F6AA5"],
                    "checkmark_color": ["#DCE4EE", "gray90"],
                    "text_color": ["gray10", "#DCE4EE"],
                    "text_color_disabled": ["gray60", "gray45"]
                  },
                  "CTkSwitch": {
                    "corner_radius": 1000,
                    "border_width": 3,
                    "button_length": 0,
                    "fg_color": ["#939BA2", "#4A4D50"],
                    "progress_color": ["#3B8ED0", "#1F6AA5"],
                    "button_color": ["gray36", "#D5D9DE"],
                    "button_hover_color": ["gray20", "gray100"],
                    "text_color": ["gray10", "#DCE4EE"],
                    "text_color_disabled": ["gray60", "gray45"]
                  },
                  "CTkRadioButton": {
                    "corner_radius": 1000,
                    "border_width_checked": 6,
                    "border_width_unchecked": 3,
                    "fg_color": ["#3B8ED0", "#1F6AA5"],
                    "border_color": ["#3E454A", "#949A9F"],
                    "hover_color": ["#36719F", "#144870"],
                    "text_color": ["gray10", "#DCE4EE"],
                    "text_color_disabled": ["gray60", "gray45"]
                  },
                  "CTkProgressBar": {
                    "corner_radius": 1000,
                    "border_width": 0,
                    "fg_color": ["#939BA2", "#4A4D50"],
                    "progress_color": ["#3B8ED0", "#1F6AA5"],
                    "border_color": ["gray", "gray"]
                  },
                  "CTkSlider": {
                    "corner_radius": 1000,
                    "button_corner_radius": 1000,
                    "border_width": 6,
                    "button_length": 0,
                    "fg_color": ["#939BA2", "#4A4D50"],
                    "progress_color": ["gray40", "#AAB0B5"],
                    "button_color": ["#3B8ED0", "#1F6AA5"],
                    "button_hover_color": ["#36719F", "#144870"]
                  },
                  "CTkOptionMenu": {
                    "corner_radius": 6,
                    "fg_color": ["#3B8ED0", "#1F6AA5"],
                    "button_color": ["#36719F", "#144870"],
                    "button_hover_color": ["#27577D", "#203A4F"],
                    "text_color": ["#DCE4EE", "#DCE4EE"],
                    "text_color_disabled": ["gray74", "gray60"]
                  },
                  "CTkComboBox": {
                    "corner_radius": 6,
                    "border_width": 2,
                    "fg_color": ["#F9F9FA", "#343638"],
                    "border_color": ["#979DA2", "#565B5E"],
                    "button_color": ["#979DA2", "#565B5E"],
                    "button_hover_color": ["#6E7174", "#7A848D"],
                    "text_color": ["gray10", "#DCE4EE"],
                    "text_color_disabled": ["gray50", "gray45"]
                  },
                  "CTkScrollbar": {
                    "corner_radius": 1000,
                    "border_spacing": 4,
                    "fg_color": "transparent",
                    "button_color": ["gray55", "gray41"],
                    "button_hover_color": ["gray40", "gray53"]
                  },
                  "CTkSegmentedButton": {
                    "corner_radius": 6,
                    "border_width": 2,
                    "fg_color": ["#979DA2", "gray29"],
                    "selected_color": ["#3B8ED0", "#1F6AA5"],
                    "selected_hover_color": ["#36719F", "#144870"],
                    "unselected_color": ["#979DA2", "gray29"],
                    "unselected_hover_color": ["gray70", "gray41"],
                    "text_color": ["#DCE4EE", "#DCE4EE"],
                    "text_color_disabled": ["gray74", "gray60"]
                  },
                  "CTkTextbox": {
                    "corner_radius": 6,
                    "border_width": 0,
                    "fg_color": ["#F9F9FA", "#1D1E1E"],
                    "border_color": ["#979DA2", "#565B5E"],
                    "text_color":["gray10", "#DCE4EE"],
                    "scrollbar_button_color": ["gray55", "gray41"],
                    "scrollbar_button_hover_color": ["gray40", "gray53"]
                  },
                  "CTkScrollableFrame": {
                    "label_fg_color": ["gray78", "gray23"]
                  },
                  "DropdownMenu": {
                    "fg_color": ["gray90", "gray20"],
                    "hover_color": ["gray75", "gray28"],
                    "text_color": ["gray10", "gray90"]
                  },
                  "CTkFont": {
                    "macOS": {
                      "family": "SF Display",
                      "size": 13,
                      "weight": "normal"
                    },
                    "Windows": {
                      "family": "Roboto",
                      "size": 13,
                      "weight": "normal"
                    },
                    "Linux": {
                      "family": "Roboto",
                      "size": 13,
                      "weight": "normal"
                    }
                  }
                }


    #--------------------Widget Type and Content--------------------#
    
    widgets = {'CTk':['fg_color'],
             'CTkToplevel':['fg_color'],
             'CTkFrame':['fg_color', 'top_fg_color', 'border_color'],
             'CTkButton':['fg_color','hover_color','border_color','text_color','text_color_disabled'],
             'CTkCheckBox':["fg_color", "border_color", "hover_color","checkmark_color", "text_color",
                            "text_color_disabled"],
             'CTkEntry':['fg_color','text_color','border_color','placeholder_text_color'],
             'CTkLabel':['fg_color', 'text_color'], 
             'CTkProgressBar':['fg_color','progress_color','border_color'],
             'CTkSlider':["fg_color", "progress_color", "button_color", "button_hover_color"],
             'CTkSwitch':["fg_Color", "progress_color", "button_color", "button_hover_color",
                          "text_color", "text_color_disabled"],
             'CTkOptionMenu':["fg_color", "button_color", "button_hover_color","text_color",
                              "text_color_disabled"],
             'CTkComboBox':["fg_color", "border_color", "button_color", "button_hover_color",
                            "text_color", "text_color_disabled"],
             'CTkScrollbar':["fg_color", "button_color", "button_hover_color"],
             'CTkRadioButton':["fg_color", "border_color", "hover_color", "text_color", "text_color_disabled"],
             'CTkTextbox':["fg_color", "border_color", "text_color", "scrollbar_button_color",
                           "scrollbar_button_hover_color"],
             'CTkSegmentedButton':["fg_color", "selected_color", "selected_hover_color", "unselected_color",
                                   "unselected_hover_color", "text_color", "text_color_disabled"],
             'CTkScrollableFrame':["label_fg_color"],
             'DropdownMenu':["fg_color", "hover_color", "text_color"]}

    widgetlist = [key for key in widgets] 
    current = widgetlist[0]

    for i in json_data:
        for key, value in json_data.get(i).items():
            if value=="transparent":
                json_data[i][key] = ["transparent", "transparent"]
            
    def __init__(self):
        
        #--------------------Main root Window--------------------#
        super().__init__(fg_color=customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"])
        customtkinter.set_default_color_theme("blue")
        self.title("CustomTkinter ThemeMaker")
        self.geometry("500x450")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        self.frame_info = customtkinter.CTkFrame(master=self, height=80)
        self.frame_info.grid(row=0, column=0, columnspan=6, sticky="nswe", padx=20, pady=20)
        self.frame_info.grid_columnconfigure(0, weight=1)

        self.widget_type = customtkinter.CTkLabel(master=self.frame_info, text=self.current, corner_radius=10, width=200, height=20,
                                        fg_color=("white", "gray38"))
        self.widget_type.grid(row=0, column=0, sticky="nswe", padx=80, pady=20)

        self.left_button = customtkinter.CTkButton(master=self.frame_info, text="<", width=20, height=20, corner_radius=10,
                                        fg_color=("white", "gray38"), command=self.change_mode_left, text_color=("black","white"))
        self.left_button.grid(row=0, column=0, sticky="nsw", padx=20, pady=20)

        self.right_button = customtkinter.CTkButton(master=self.frame_info, text=">", width=20, height=20, corner_radius=10,
                                        fg_color=("white", "gray38"), command=self.change_mode_right, text_color=("black","white"))
        self.right_button.grid(row=0, column=0, sticky="nse", padx=20, pady=20)

        self.menu = customtkinter.CTkOptionMenu(master=self, fg_color=("white", "gray38"), button_color=("white", "gray38"), text_color=("black","white"),
                                         height=30, values=list(self.widgets.items())[0][1], command=self.update)   
        self.menu.grid(row=1, column=0, columnspan=6, sticky="nswe", padx=20)

        self.button_light = customtkinter.CTkButton(master=self, height=100, width=200, corner_radius=10, border_color="white",
                                         text_color="grey50", border_width=2, text="Light", hover=False, command=self.change_color_light)
        self.button_light.grid(row=2, column=0, sticky="nswe", columnspan=3, padx=(20,5), pady=20)
    
        self.button_dark = customtkinter.CTkButton(master=self, height=100, width=200, corner_radius=10, border_color="white",
                                         text_color="gray80", border_width=2, text="Dark", hover=False,
                                         command=self.change_color_dark)
        self.button_dark.grid(row=2, column=3, sticky="nswe", columnspan=3, padx=(5,20), pady=20)

        self.button_load = customtkinter.CTkButton(master=self, height=40, width=110, text="Load Theme", command=self.load)
        self.button_load.grid(row=3, column=0,  columnspan=2, sticky="nswe", padx=(20,5), pady=(0,20))

        self.button_export = customtkinter.CTkButton(master=self, height=40, width=110, text="Save Theme", command=self.save)
        self.button_export.grid(row=3, column=2,  columnspan=2, sticky="nswe", padx=(5,5), pady=(0,20))
    
        self.button_reset = customtkinter.CTkButton(master=self, height=40, width=110, text="Reset", command=self.reset)
        self.button_reset.grid(row=3, column=4,  columnspan=2, sticky="nswe", padx=(5,20), pady=(0,20))
        
        self.palette = customtkinter.CTkButton(master=self, height=40, width=110, text="Color Palette", command=self.show_colors)
        self.palette.grid(row=4, column=0, columnspan=3, sticky="nswe", padx=(20,5), pady=(0,20))

        self.quick_test = customtkinter.CTkButton(master=self, height=40, width=110, text="QUICK TEST", command=self.test)
        self.quick_test.grid(row=4, column=3, columnspan=3, sticky="nswe", padx=(5,20), pady=(0,20))

        
        self.update(None)

    #--------------------App Functions--------------------#

    def change_mode_right(self):
        """ changing current widget type wih right button """
        self.widgetlist.append(self.widgetlist.pop(0))
        self.current = self.widgetlist[0]
        self.widget_type.configure(text=self.current)
        self.menu.configure(values=self.widgets[self.current])
        self.menu.set(self.widgets[self.current][0])
        self.update(self.menu.get())
         
    def change_mode_left(self):
        """ changing current widget type with left button  """
        self.widgetlist.insert(0, self.widgetlist.pop())
        self.current = self.widgetlist[0]
        self.widget_type.configure(text=self.current)
        self.menu.configure(values=self.widgets[self.current])
        self.menu.set(self.widgets[self.current][0])
        self.update(self.menu.get())

    def update(self, value):
        """ updating the widgets and their colors """
        for i in self.json_data[self.current]:
            if i==self.menu.get():
                if (self.json_data[self.current][i])[0]!="transparent":
                    self.button_light.configure(fg_color=(self.json_data[self.current][i])[0])
                else:
                    self.button_light.configure(fg_color="transparent")
                if (self.json_data[self.current][i])[1]!="transparent":    
                    self.button_dark.configure(fg_color=(self.json_data[self.current][i])[1])
                else:
                    self.button_dark.configure(fg_color="transparent")
                    
    def change_color_light(self):
        """ choosing the color for Light mode of the theme """
        default = self.button_light._apply_appearance_mode(self.button_light._fg_color)
        if default=="transparent":
            default = "white"
        color1 = askcolor(title="Choose color for "+self.menu.get()+" (Light)",
                          initialcolor=default)
        if color1[1] is not None:
            self.button_light.configure(fg_color=color1[1])
            for i in self.json_data[self.current]:
                if i==self.menu.get():
                    (self.json_data[self.current][i])[0] = color1[1]
               
    def change_color_dark(self):
        """ choosing the color for Dark mode of the theme """
        default = self.button_dark._apply_appearance_mode(self.button_dark._fg_color)
        if default=="transparent":
            default = "white"      
        color2 = askcolor(title="Choose color for "+self.menu.get()+" (Dark)",
                          initialcolor=default)
        if color2[1] is not None:
            self.button_dark.configure(fg_color=color2[1])
            for i in self.json_data[self.current]:
                if i==self.menu.get():
                    (self.json_data[self.current][i])[1] = color2[1]
      
    def save(self):
        """ exporting the theme file """
        save_file = tkinter.filedialog.asksaveasfilename(initialfile="Untitled.json", defaultextension=".json",
                                                         filetypes=[('json', ['*.json']),('All Files', '*.*')])
        try:
            export_data = copy.deepcopy(self.json_data)
            for i in export_data:
                for j in export_data[i]:
                    if export_data[i][j]==["transparent", "transparent"]:
                        export_data[i][j] = "transparent"
            if save_file:
                with open(save_file, "w") as f:
                    json.dump(export_data, f, indent=2)
                    f.close()
                tkinter.messagebox.showinfo("Exported!","Theme saved successfully!")
        except:
            tkinter.messagebox.showerror("Error!","Something went wrong!")
                       
    def load(self):
        """ load any theme file """
        global json_data
        open_json = tkinter.filedialog.askopenfilename(filetypes=[('json', ['*.json']),('All Files', '*.*')])
        try:
            if open_json:
                with open(open_json) as f:
                    self.json_data = json.load(f)
                    
            for i in self.json_data:
                for key, value in self.json_data.get(i).items():
                    if value=="transparent":
                        self.json_data[i][key] = ["transparent", "transparent"]
                        
            self.update(self.menu.get())
        except:
            tkinter.messagebox.showerror("Error!","Unable to load this theme file!")
        
    def reset(self):
        """ resetting the current colors of the widget to null (default value) """
        for i in self.json_data[self.current]:
            if i==self.menu.get():
                self.json_data[self.current][i][0] = "transparent"
                self.button_light.configure(fg_color="transparent")
                self.json_data[self.current][i][1] = "transparent"
                self.button_dark.configure(fg_color="transparent")

    def test(self):
        """ function for quickly testing the theme """
        DIRPATH = os.path.dirname(os.path.abspath(__file__))
        
        program = os.path.join(DIRPATH, "CTkExample.py")
        
        if not os.path.exists(program):
            tkinter.messagebox.showerror("Sorry!","Cannot test the theme, example program is missing!")
            return
        
        export_data = copy.deepcopy(self.json_data)
        for i in export_data:
            for j in export_data[i]:
                if export_data[i][j]==["transparent", "transparent"]:
                    export_data[i][j] = "transparent"

        with open(os.path.join(DIRPATH, "CTkTheme_test.json"), "w") as f:
            json.dump(export_data, f, indent=2)
        
        if sys.platform.startswith("win"):   
            subprocess.run(["python", program])
        else:
            subprocess.run(["python3", program])
            
    def replace_color(self, color, button, mode):
        """ replace a specific color """      
        if color=="transparent":
            default = "white"
        else:
            default = color
        new_color = askcolor(title=f"Replace this color: {color}", initialcolor=default)[1]
        if new_color is None:
            new_color = "transparent"
        if mode:
             for i in self.json_data:
                for j in self.json_data[i]:
                    if type(self.json_data[i][j]) is list:
                        if self.json_data[i][j][1]==color:
                            self.json_data[i][j][1] = new_color
                    
        else:
            for i in self.json_data:
                for j in self.json_data[i]:
                    if type(self.json_data[i][j]) is list:
                        if self.json_data[i][j][0]==color:
                            self.json_data[i][j][0] = new_color
        try: button.configure(text=new_color, fg_color=new_color)
        except: pass
        self.update(self.menu.get())
            
    def show_colors(self):
        """ show the color palette for the theme """
        toplevel = customtkinter.CTkToplevel()
        toplevel.resizable(True, True)
        toplevel.geometry("500x700")
        toplevel.title("Color Palette")
        toplevel.transient(self)
        toplevel.grab_set()
        
        frame_light = customtkinter.CTkScrollableFrame(toplevel, label_text="Light Colors")
        frame_light.pack(fill="both", expand=True, side="left", padx=(10,5), pady=10)
        
        frame_dark = customtkinter.CTkScrollableFrame(toplevel, label_text="Dark Colors")
        frame_dark.pack(fill="both", expand=True, side="right", padx=(5,10), pady=10)

        set_dark = set()
        set_light = set()
        
        for i in self.json_data:
            for j in self.json_data[i]:
                if type(self.json_data[i][j]) is list:
                    set_dark.add(self.json_data[i][j][1])
                    set_light.add(self.json_data[i][j][0])
                    
        for color in set_dark:
            button = customtkinter.CTkButton(frame_dark, text=color, fg_color=color, hover=False)
            button.configure(command=lambda x=color, y=button: self.replace_color(x, y, 1))
            button.pack(fill="x", expand=True, padx=10, pady=5)
            
        for color in set_light:
            button = customtkinter.CTkButton(frame_light, text=color, fg_color=color, hover=False)
            button.configure(command=lambda x=color, y=button: self.replace_color(x, y, 0))         
            button.pack(fill="x", expand=True, padx=10, pady=5)
             
    def on_closing(self):
        """ close the program """
        quit_ = tkinter.messagebox.askokcancel(title="Exit?", message= "Do you want to exit?")
        if quit_:
            self.destroy()
            
if __name__ == "__main__":
    app = App()
    app.mainloop()
