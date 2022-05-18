import requests
from bs4 import BeautifulSoup
import json
import time
import os
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import installed as INST
import subprocess
import sys
import terminal as TER

class App:
    def __init__(self):
        self.fetch_list = "https://pypi.org/simple/"
        self.fetched_data = "fetched_html.html"
        self.stark = {}
        self.storage = "storage.json"
        
        self.root = tk.Tk()
        self.root.title("Pip manager - GUI")
        self.root.geometry("1000x800")
        self.root.configure(bg="white")
        self.style = ThemedStyle(self.root)
        self.style.theme_use('adapta')
        self.text = TER.terminal_maker(self.root)
        self.package_no = 0
        
    def darkmd(self):
        self.style.theme_use("equilux")
        
        bg = self.style.lookup('TLabel', 'background')
        fg = self.style.lookup('TLabel', 'foreground')
        self.root.configure(bg=self.style.lookup('TLabel', 'background'))
        self.style.configure('TButton', foreground="white", highlightthickness=5, highlightbackground='#3E4149', highlightforeground="white", activebackground="black")
        self.style.configure('TLabel', foreground="white", highlightthickness=5, highlightbackground='#3E4149', highlightforeground="white", activebackground="black")
                
    def fetch(self):
        response = requests.get(self.fetch_list).text
        print("Request completed")
        with open(self.fetched_data, 'w') as f:
            f.write(response)
        self.json_maker()
        print("JSON file created")
    
    def json_maker(self):
        print("Creating JSON file")
        with open(self.fetched_data, 'r') as f:
            self.html_data = f.read()
        
        tags = BeautifulSoup(self.html_data, 'lxml').find_all('a')

        with open(self.storage, 'w') as f:
            for tag in tags:
                self.stark[f"{tag.text}"] = ""
            json.dump(self.stark, f)

        with open(self.storage, 'r') as f:
            self.all_repos = json.load(f).keys()
            # print(all_repos)
    
    def get_value(self, i):
        INST.get_installed()
        if self.str_match[i] in INST.clean():
            print("Present")
            self.package_no = self.package_no + 1
            install_args = ['pip', 'install', f'{self.str_match[i]}']
            # output = subprocess.Popen( install_args, stdout=subprocess.PIPE ).communicate()[0]
            output = subprocess.Popen( install_args, stdout=subprocess.PIPE )

            # output = subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{self.str_match}'])
            self.text = TER.terminal(output, self.text, self.package_no)

            # os.system(f"pip uninstall {self.str_match[i]}")
            # print("Uninstall complete")
            # os.system(f"pip install {self.str_match[i]}")
            # print(f"Installed {self.str_match[i]}")
            
    
    def index(self, No_of_butt):
        self.variable = tk.StringVar()
        for i in range(No_of_butt):
            lab = ttk.Label(self.root, text=str(i+1) + "\t" + self.str_match[i])
            lab.place(x=15, y=80+(i*40), width=600, height=25)

            butt = ttk.Button(self.root, text="Install", command=lambda i=i: self.get_value(i))
            butt.place(x=600, y=80+(i*40), width=120, height=30)

    def search(self):
        query = self.entr.get()
        with open(self.storage, 'r') as f:
            self.all_repos = json.load(f).keys()
        self.str_match = [s for s in self.all_repos if s.startswith(query)]
        # str_match = [s for s in self.all_repos if s.__contains__(query)]
        print(self.str_match[:10])
        if len(self.str_match) > 10:
            self.index(10)
        else:
            self.index(len(self.str_match))
    
    def gui(self):
        lab = ttk.Label(self.root,text="Search")
        lab.place(x=5, y=5, width=120, height=25)
        self.entr = ttk.Entry(self.root)
        self.entr.place(x = 70, y = 5, width=600, height=25 )

        butt = ttk.Button(self.root, text="Search Index", command=self.search)
        butt.place(x=700, y=5, width=120, height=25)

        bt_darkmd = ttk.Button(self.root, text="Darkmode", command=self.darkmd)
        bt_darkmd.place(x=880, y=5, width=120, height=25)

        self.root.mainloop()

f = App()
f.gui()
