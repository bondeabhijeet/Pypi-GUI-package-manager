# import requests
from bs4 import BeautifulSoup
import json
import customtkinter as tk
import installed as INST
import subprocess
import terminal as TER
import updates as UPDT
import fetch as FETCH
import threading

class App:
    def __init__(self):
        print("Firing up the application!")
        self.fetch_url = "https://pypi.org/simple/"        # PYPI request URL
        self.fetched_data = "fetched_html.html"             # filename for html code fetched from pypi
        self.stark = {}
        self.storage = "storage.json"                       # Json filename in which all the pip package names are stored
        
        self.root = tk.CTk()                                 # Root window for tkinter
        self.root.title("Pip manager - GUI")                # Title for the window
        self.root.geometry("1100x800")                      # Size for the window
        self.root.resizable('False', 'False')               # Non-resizable
        
        self.mode_swtich = 0                                 # dark mode = 0, Light mode = 1

        self.text = TER.terminal_maker(self.root)
        self.text.configure(state="disabled")
        self.package_no = 0                                 # Number of packages

# Implementation to create an object of updater class from updates.py file to intialize the updater menu in tkinter
    def updatess(self):
        Apps = UPDT.Updater()

# Implementation for dark mode
    def darkmd(self):
        if self.mode_swtich == 0:
            self.mode = tk.set_appearance_mode("light")
            self.mode_swtich = 1
        else:
            self.mode = tk.set_appearance_mode("dark")
            self.mode_swtich = 0

# Implementation to make request to pypi and create a json file
    def fettchh(self):
        self.refresh_json.configure(text="Refreshing...")
        self.refresh_json.configure(state="disabled")
        self.root.update()
        FETCH.fetch(self)
        self.refresh_json.configure(text="Refreshed")
        self.refresh_json.configure(state="normal")
        
    
    def get_value(self, i):
        INST.get_installed()
        if self.str_match[i] in INST.clean():
            self.butts[i].configure(text="Updating")
            self.package_no = self.package_no + 1
            install_args = ['pip', 'install', '--upgrade' , f'{self.str_match[i]}']
            # output = subprocess.Popen( install_args, stdout=subprocess.PIPE ).communicate()[0]
            output = subprocess.Popen( install_args, stdout=subprocess.PIPE )
            # output = subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{self.str_match}'])
            self.text = TER.terminal(output, self.text, self.package_no)
            self.butts[i].configure(text="Done")

            # os.system(f"pip uninstall {self.str_match[i]}")
            # print("Uninstall complete")
            # os.system(f"pip install {self.str_match[i]}")
            # print(f"Installed {self.str_match[i]}")
        else:
            print("Installing...")
            self.butts[i].configure(text="Installing")

            self.package_no = self.package_no + 1
            install_args = ['pip', 'install', f"{self.str_match[i]}"]
            output = subprocess.Popen(install_args, stdout=subprocess.PIPE)
            self.text = TER.terminal(output, self.text, self.package_no)
            self.butts[i].configure(text="Done")

            
# Creating and storing buttons and their ids for every package displayed  
    def index(self, No_of_butt):
        print("COOL")
        self.variable = tk.StringVar()
        self.butts = []                         # To store button ids for the purpose to get to know the details of the button clicked
        for i in range(No_of_butt):
            lab = tk.CTkLabel(self.root, text=str(i+1) + "\t" + self.str_match[i])        # Creating a label
            lab.place(x=15, y=80+(i*40))

            butt = tk.CTkButton(self.root, text="Install", command=lambda i=i: threading.Thread(target=self.get_value, args=(i, )).start()) # Creating a button
            self.butts.append(butt)                                                 # Appending the unique button id to the list previously made
            butt.place(x=600, y=80+(i*40))

# Function to search for 10 results for the user input query  
    def search(self, *args):
        query = self.entr.get()                                         # Fetch the query from tkinter entry
        with open(self.storage, 'r') as f:                              # Loading the keys from the json file created earlier (database fetched from pypi)
            self.all_repos = json.load(f).keys()
        self.str_match = [s for s in self.all_repos if s.startswith(query)]     # Get the results that match the characters from query
        # str_match = [s for s in self.all_repos if s.__contains__(query)]
        print(self.str_match[:10])
        if len(self.str_match) > 10:            # If number of results are more than 10 then only make 10 buttons as others are discarded
            self.index(10)
        else:
            self.index(len(self.str_match))     # If number of results are less than 10 then make number of buttons as results

# Creating the main GUI for application    
    def gui(self):
        lab = tk.CTkLabel(self.root,text="Search")    # Search Label
        lab.place(x=5, y=5)

        self.entr = tk.CTkEntry(self.root, width=620, placeholder_text="Type library name")            # Input for query
        self.root.update()
        self.entr.place(x = 70, y = 5) 
        self.entr.focus_set()                           # To make widget default to take input wihout clicking on it, after openeing the app

        butt = tk.CTkButton(self.root, text="Search Index", command=self.search)  # Search button
        butt.place(x=700, y=5)
        self.root.bind("<Return>", self.search)                                 # Bind the button with "Enter" button to search function

        bt_darkmd = tk.CTkButton(self.root, text="Darkmode", command=self.darkmd) # Dark mode button
        bt_darkmd.place(x=870, y=5)

        self.refresh_json = tk.CTkButton(self.root, text="Update List", command=lambda: threading.Thread(target=self.fettchh).start())
        self.refresh_json.place(x=870, y=400)

        update_butt = tk.CTkButton(self.root, text="Updates", command=self.updatess)# Updates tab (To be integrated)
        update_butt.place(x=870, y=460)
        self.root.mainloop()

f = App()

f.gui()
