from tkinter import *
import tkinter as tk
from tkinter import ttk
from numpy import pad
from ttkthemes import ThemedStyle
from tkinter.ttk import Progressbar
import installed as INST
import requests
import time
import subprocess

start = time.time()
INST.get_installed()
installed_libs = INST.clean_version()
update_len = 100/(len((installed_libs)))

root = Tk()
style = ThemedStyle(root)
style.theme_use("adapta")
text = tk.Text(root)

root["bg"] = "white"

sess = requests.Session()
update_required = []

lab = ttk.Label(root, text=f"Updates")
lab.pack(padx=20, pady=10)

def upgrade_lib(i):
    print(i)
    install_args = ['pip', 'install', '--upgrade' , f'{i}']
    labe.configure(text=f"Status: updating {i}")
    output = subprocess.Popen( install_args, stdout=subprocess.PIPE )
    labe.configure(text=f"Status: upgraded {i}")
    print(output)

def step():
    for lib in installed_libs:
        
        root.update_idletasks()
        pb1['value'] += update_len
        lab.configure(text=f"{lib[0]}")
        try:
            latest_version = sess.get(f'https://pypi.org/pypi/{lib[0]}/json').json()['info']['version']
            if lib[1] == latest_version:
                print(f"{lib[0]} Latest version")
            else:
                update_required.append(lib[0])
                print(f"{lib[0]} update required")
        except:
            print(f"Skipped {lib[0]}")

    with open('update.txt', 'w') as f:
        for i in update_required:
            f.write(f"{i}\n")
    print(update_required)

    for lib in update_required:
        button = ttk.Button(text=f"Update", command=lambda i=lib: upgrade_lib(i))
        text.window_create("end", window=button)
        text.insert("end", f"\t{lib}\n")
    # time.sleep(0.2)

print(time.time() - start)

pb1 = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
pb1.pack(expand=True)

ttk.Button(root, text='Start', command=step).pack(pady=5)
labe = ttk.Label(root, text=f"Status:")
labe.pack(padx=20, pady=10)

text.pack(side="left")
sb = ttk.Scrollbar(root, command=text.yview)
sb.pack(side="right", fill=Y)
text.configure(yscrollcommand=sb.set)

mainloop()