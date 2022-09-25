import requests
from bs4 import BeautifulSoup
import json
import tkinter as tk
from tkinter import Label, ttk
from ttkthemes import ThemedStyle
import installed as INST
import subprocess
import terminal as TER

class App:
    def __init__(self):
        self.fetch_list = "https://pypi.org/simple/"        # PYPI request URL
        self.fetched_data = "fetched_html.html"             # filename for html code fetched from pypi
        self.stark = {}
        self.storage = "storage.json"                       # Json filename in which all the pip package names are stored
        
        self.root = tk.Tk()                                 # Root window for tkinter
        self.root.title("Pip manager - GUI")                # Title for the window
        self.root.geometry("1000x800")                      # Size for the window
        self.root.resizable('False', 'False')               # Non-resizable
        self.disableDarkmd()                                # by default light mode is enabled

        # DELETE
        # self.root.configure(bg="white")
        # self.style = ThemedStyle(self.root)
        # self.style.theme_use('adapta')
        # self.text = TER.terminal_maker(self.root)
        # self.text.config(state="disabled")
        self.package_no = 0                                 # Num,ber of packages


# Implementation for dark mode using the "equilux" theme
    def darkmd(self):
        if self.dkmd == 0:
            self.style.theme_use("equilux")
            
            bg = self.style.lookup('TLabel', 'background')
            fg = self.style.lookup('TLabel', 'foreground')
            self.root.configure(bg=self.style.lookup('TLabel', 'background'))
            self.style.configure('TButton', foreground="white", highlightthickness=5, highlightbackground='#3E4149', highlightforeground="white", activebackground="black")
            self.style.configure('TLabel', foreground="white", highlightthickness=5, highlightbackground='#3E4149', highlightforeground="white", activebackground="black")
            self.style.configure('TEntry', foreground="white", selectforeground='black', selectbackground='#7FFFD4', highlightbackground='#3E4149', highlightforeground="white", activebackground="black")
            self.dkmd = 1
        else:
            self.disableDarkmd()

# Implementation for light mode using the "adapta" theme
    def disableDarkmd(self):
        self.root.configure(bg="white")
        self.style = ThemedStyle(self.root)
        self.style.theme_use('adapta')
        self.text = TER.terminal_maker(self.root)
        self.text.config(state="disabled")
        self.dkmd = 0

# Function to make a request to pypi and get all the package's names
    def fetch(self):
        response = requests.get(self.fetch_list).text   # make the request
        print("Request completed")
        with open(self.fetched_data, 'w') as f:         # write the fetched HTML code to a html file
            f.write(response)
        self.json_maker()                               # Parse the html file and create a json file
        print("JSON file created")

# Implementation to make a json file from html file    
    def json_maker(self):
        print("Creating JSON file")
        with open(self.fetched_data, 'r') as f:             # reading the html file
            self.html_data = f.read()
        
        tags = BeautifulSoup(self.html_data, 'lxml').find_all('a')  # Fetching all the "a" tags

        with open(self.storage, 'w') as f:                  # writing all the parsed results to a json file for better navigation
            for tag in tags:
                self.stark[f"{tag.text}"] = ""
            json.dump(self.stark, f)

        with open(self.storage, 'r') as f:                  # Reading the same json file and fetching all the keys into a dict
            self.all_repos = json.load(f).keys()
            # print(all_repos)
    
    def get_value(self, i):
        INST.get_installed()
        if self.str_match[i] in INST.clean():
            # print("Updating...")
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
        self.variable = tk.StringVar()
        self.butts = []                         # To store button ids for the purpose to get to know the details of the button clicked
        for i in range(No_of_butt):
            lab = ttk.Label(self.root, text=str(i+1) + "\t" + self.str_match[i])        # Creating a label
            lab.place(x=15, y=80+(i*40), width=600, height=25)

            butt = ttk.Button(self.root, text="Install", command=lambda i=i: self.get_value(i)) # Creating a button
            self.butts.append(butt)                                                 # Appending the unique button id to the list prviously made
            butt.place(x=600, y=80+(i*40), width=120, height=30)

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
        lab = ttk.Label(self.root,text="Search")    # Search Label
        lab.place(x=5, y=5, width=120, height=25)

        self.entr = ttk.Entry(self.root)            # Input for query
        self.entr.place(x = 70, y = 5, width=600, height=25 )   
        self.entr.focus()                           # To make widget default to take input wihout clicking on it, after openeing the app

        butt = ttk.Button(self.root, text="Search Index", command=self.search)  # Search button
        butt.place(x=700, y=5, width=120, height=25)
        self.root.bind("<Return>", self.search)                                 # Bind the button with "Enter" button to search function
        # butt.focus()

        bt_darkmd = ttk.Button(self.root, text="Darkmode", command=self.darkmd) # Dark mode button
        bt_darkmd.place(x=870, y=5, width=120, height=25)

        update_butt = ttk.Button(self.root, text="Updates", command=self.darkmd)# Updates tab (To be integrated)
        update_butt.place(x=870, y=460, width=120, height=25)
        self.root.mainloop()

f = App()
f.fetch()
f.gui()
