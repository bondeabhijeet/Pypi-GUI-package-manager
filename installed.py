import os

# To get list of all the installed libraries and write the list to a text file
def get_installed():
    os.system("pip freeze > installed.txt")

# Return a list from the text file generated by the previous function
def clean():
    installed_libraries = []
    with open('installed.txt', 'r') as f:   # Reading the data from text file
        data = f.read()
    
    for item in data.strip().split("\n"):   # Stripping the data by new line
        installed_libraries.append(item.split("==")[0]) # Selecting only the name of the package and discarding the version number installed
    return installed_libraries

# Improvising the above function
# Return a list from the text file generated by the previous function
def clean_version():
    installed_libraries = []
    with open('installed.txt', 'r') as f:   # Reading the data from text file
        data = f.read()
    
    for item in data.strip().split("\n"):   # Stripping the data by new line
        installed_libraries.append(item.split("=="))    # Selecting only the name of the package and the version number installed in a list ["Package name","Package version"]
        # installed_libraries.append({item.split("==")[0], item.split("==")[1]})
    return installed_libraries
