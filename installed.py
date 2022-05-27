import os

from sympy import li

def get_installed():
    os.system("pip freeze > installed.txt")

def clean():
    installed_libraries = []
    with open('installed.txt', 'r') as f:
        data = f.read()
    
    for item in data.strip().split("\n"):
        installed_libraries.append(item.split("==")[0])
    return installed_libraries

def clean_version():
    installed_libraries = []
    with open('installed.txt', 'r') as f:
        data = f.read()
    
    for item in data.strip().split("\n"):
        installed_libraries.append(item.split("=="))
        # installed_libraries.append({item.split("==")[0], item.split("==")[1]})
    return installed_libraries
