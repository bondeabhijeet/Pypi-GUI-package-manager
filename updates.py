from tkinter import *
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import installed as INST
import requests
import subprocess
# import terminal as TER

# Update class

class Updater:
    # To update a specific library/package
    def upgrade_lib(self, i):
        print(i)
        install_args = ['pip', 'install', '--upgrade' , f'{i}'] # Command line arguments
        self.statusIndicator.configure(text=f"Status: updating {i}")    # Updating status on the label
        output = subprocess.Popen( install_args, stdout=subprocess.PIPE )   # Executing the command to upgrade the package/library
        # self.statusIndicator.configure(text=f"Status: upgraded {i}")
        INST.get_installed()        # Updating the update.txt, a list of installed libraries  
        self.installed_libs = INST.clean_version()
        print(output)       # Printing the output from the exectuted command
        self.statusIndicator.configure(text=f"Status: Processed {i}")   # Updating the status on the label
        
    # Checking for updates
    def CheckUpdates(self):
        
        self.statusIndicator.configure(text="Status: Checking for updates") # Updating the status on the label
        for lib in self.installed_libs:                                     # itterating through installed libraries
            
            self.root.update_idletasks()
            self.pb1['value'] += self.update_len
            self.lab.configure(text=f"{lib[0]}")
            try:                                                            # tring to get the latest version of the installed library
                latest_version = self.sess.get(f'https://pypi.org/pypi/{lib[0]}/json').json()['info']['version']    # Request is done using session
                if lib[1] == latest_version:            # If the installed version of library is same as latest version
                    print(f"{lib[0]} Latest version")
                else:                                   # If the version is not latest then update is required
                    self.update_required.append(lib[0]) # Appending the name to a list
                    print(f"{lib[0]} update required")  
            except:                                     # If any error occurs then skip the package
                print(f"Skipped {lib[0]}")

        with open('update.txt', 'w') as f:              # Writing the list of libraries that need update to a txt file (update.txt)
            for i in self.update_required:
                f.write(f"{i}\n")
        print(self.update_required)

        if len(self.update_required) == 0:              # If all the libraries are upto date (no updates available)
            self.statusIndicator.configure(text="Status: No updated available")
        else:                                           # If updates are available
            self.statusIndicator.configure(text=f"Status: Updates are available ({len(self.update_required)})")

        for lib in self.update_required:                # Creating buttons and lables for all the packages that need to be update 
            button = ttk.Button(text=f"Update", command=lambda i=lib: self.upgrade_lib(i))  # Buttons binded with button id so as to know which button is pressed to upgrade the package
            # self.statusIndicator.configure(text=f"Status: upgraded {i}")
            self.text.window_create("end", window=button)   # Creating a window to display button and label
            self.text.insert("end", f"\t{lib}\n")           # Inserting the button and label combo inside the window created
    
    # def UpdateAll(self):
    #     print()
    #     for lib in self.update_required:
    #         install_args = ['pip', 'install', f"{lib}"]
    #         output = subprocess.Popen(install_args, stdout=subprocess.PIPE)
    #         self.text = TER.terminal(output, self.text, self.package_no)


    def __init__(self):
        INST.get_installed()                    # Get the list of installed libraries
        self.installed_libs = INST.clean_version()
        self.update_len = 100/(len((self.installed_libs)))  # For creating the progress bar to display how many libraries are checked

        self.root = Tk()                        # Root tkinter window
        self.style = ThemedStyle(self.root)     # To use themes
        self.style.theme_use("adapta")          # "adapta" theme used
        self.text = tk.Text(self.root)
        # self.text1 = TER.terminal_maker(self.root)

        self.root["bg"] = "white"               # Setting the background color to white

        self.sess = requests.Session()          # Creating a session for the multiple requests that are going to be made to check updates of each and every package
        self.update_required = []               # A list of all the packages that will need update (filled later on)

        self.lab = ttk.Label(self.root, text=f"Updates")    # Label
        self.lab.pack(padx=20, pady=10)

        self.pb1 = ttk.Progressbar(self.root, orient=HORIZONTAL, length=400, mode='determinate')    # Progress bar to indicate the progress of checking updates
        self.pb1.pack(expand=True)      # expand: https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method

        self.statusIndicator = ttk.Button(self.root, text='Start', command=self.CheckUpdates).pack(pady=5)  # Button to start checking for updates
        self.statusIndicator = ttk.Label(self.root, text=f"Status: Idle")                                   # Updating the status on the label
        self.statusIndicator.pack(padx=20, pady=10)

        # Implementation of scroll bar binding it with the list of buttons and labels
        self.text.pack(side="left")
        self.sb = ttk.Scrollbar(self.root, command=self.text.yview)
        self.sb.pack(side="right", fill=Y)
        self.text.configure(yscrollcommand=self.sb.set)

        self.root.mainloop()

# Testing        
app = Updater()
