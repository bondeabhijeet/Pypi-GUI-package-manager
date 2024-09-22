import customtkinter as tk
import installed as INST
import requests
import subprocess
import threading
# import terminal as TER

# Update class

class Updater:

    # To update a specific library/package
    def upgrade_lib(self, i, btn):
        try:
            print(i)
            self.status_label.configure(text=f"Status: updating {i}")                                   # Updating status on the label
            self.UPDroot.update_idletasks()

            btn.configure(text="Updating...", state="disabled")

            def run_upgrade():
                install_args = ['pip', 'install', '--upgrade' , i]                                          # Command line arguments
                output = subprocess.Popen( install_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE )   # Executing the command to upgrade the package/library
                stdout, stderr = output.communicate()

                if output.returncode == 0:
                    print("Command executed successfully.")
                    index_to_delete = self.update_required.index(i)
                    #self.text.delete(f"{index_to_delete}.0", f"{index_to_delete + 2}.0")
                    self.status_label.configure(text=f"Status: Processed {i}")                              # Updating the status on the label
                    btn.configure(text="Updated", state="disabled")
                else:
                    print(f"Command failed with return code: {output.returncode}")
                    print(f"Error message:\n{stderr.decode('utf-8')}")
                    self.status_label.configure(text=f"Status: Error in {i}")                               # Updating the status on the label
                    btn.configure(text="Error!!!")
                INST.get_installed()                                                                        # Updating the update.txt, a list of installed libraries  
                self.installed_libs = INST.clean_version()

            threading.Thread(target=run_upgrade).start()
        except Exception as e:
            print("Exception:", str(e))
        
        # print(output)                                                                               # Printing the output from the exectuted command


    # Checking for updates
    def CheckUpdates(self):
        self.status_label.configure(text="Scanning installed libraries")
        self.UPDroot.update_idletasks() # Update the label immediately since it gets scheduled for the next event, by default to get updated
        INST.get_installed()                    # Get the list of installed libraries
        self.installed_libs = INST.clean_version()

        self.update_len = 100/(len((self.installed_libs)))  # For creating the progress bar to display how many libraries are checked
        self.progress_bar.configure(determinate_speed = self.update_len)

        self.sess = requests.Session()            # Creating a session for the multiple requests that are going to be made to check updates of each and every package
        
        self.status_label.configure(text="Status: Checking for updates") # Updating the status on the label
        for lib in self.installed_libs:                                     # itterating through installed libraries
            
            self.UPDroot.update_idletasks()
            self.progress_bar.step()
            
            self.label_updates.configure(text=f"                {lib[0]}               ")
            try:                                                            # tring to get the latest version of the installed library
                latest_version = self.sess.get(f'https://pypi.org/pypi/{lib[0]}/json').json()['info']['version']    # Request is done using session
                if lib[1] == latest_version:            # If the installed version of library is same as latest version
                    print(f"{lib[0]} Latest version")
                else:                                   # If the version is not latest then update is required
                    self.update_required.append(lib[0]) if lib[0] not in self.update_required else None # Appending the name to a list
                    print(f"{lib[0]} update required")  
            except:                                     # If any error occurs then skip the package
                print(f"Skipped {lib[0]}")

        with open('update.txt', 'w') as f:              # Writing the list of libraries that need update to a txt file (update.txt)
            for i in self.update_required:
                f.write(f"{i}\n")
        print(self.update_required)

        if len(self.update_required) == 0:              # If all the libraries are upto date (no updates available)
            self.status_label.configure(text="Status: No updated available")
        else:                                           # If updates are available
            self.status_label.configure(text=f"     Status: Updates are available ({len(self.update_required)})     ")


        scrollable_frame = tk.CTkScrollableFrame(self.UPDroot, width=600, height=500, label_text="Avaliable Updates")
        scrollable_frame.pack()


        for i in range(len(self.update_required)):
            label_library_name = tk.CTkLabel(scrollable_frame, text=self.update_required[i])
            label_library_name.grid(row=i, column=0, padx=115, pady=5)

            self.library_update_button = tk.CTkButton(scrollable_frame, text="Update")
            self.library_update_button.configure(command=lambda j=self.update_required[i], btn=self.library_update_button: self.upgrade_lib(j, btn))
            self.library_update_button.grid(row=i, column=1, padx=5, pady=5, ipady=4)
    
    # def UpdateAll(self):
    #     print()
    #     for lib in self.update_required:
    #         install_args = ['pip', 'install', f"{lib}"]
    #         output = subprocess.Popen(install_args, stdout=subprocess.PIPE)
    #         self.text = TER.terminal(output, self.text, self.package_no)

    def __init__(self):
        self.UPDroot = tk.CTk()                              # root tkinter window
        self.UPDroot.geometry("800x800")
        
        #self.UPDroot.iconbitmap("favicon.ico")

        self.update_required = []                           # A list of all the packages that will need update (filled later on)

        self.setup_gui()
        self.UPDroot.mainloop()

    def setup_gui(self):
        self.label_updates = tk.CTkLabel(self.UPDroot, text="Updates")
        self.label_updates.pack(padx=20, pady=10)

        self.progress_bar = tk.CTkProgressBar(self.UPDroot, width=400, mode='determinate')      # Progress bar to indicate the progress of checking updates
        self.progress_bar.pack(padx=20, pady=10)                 # expand: https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method
        self.progress_bar.set(0)

        self.start_button = tk.CTkButton(self.UPDroot, text='Start', command=self.CheckUpdates)   # Button to start checking for updates
        self.start_button.pack(pady=5)

        self.status_label = tk.CTkLabel(self.UPDroot, text="Status: Idle")                        # Updating the status on the label
        self.status_label.pack(padx=20, pady=10)

# # Testing        
# app = Updater()
