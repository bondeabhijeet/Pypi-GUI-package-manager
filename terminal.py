import tkinter as tk

# Clone of a terminal to display the status of installation or upgradation
def terminal_maker(root):
    # Color and size config
    text = tk.Text(root, highlightthickness=3, background="red",height = 10, width = 100, bg = "#000000", fg="#00FFFF", highlightbackground = "#2F4F4F")
    text.place(x=0, y=500, width=1000, height=300)

    intro = """┌──(kali㉿kali)-[~]\n└─$ """     # Beautification
    text.tag_config('warning', background="black", foreground="#FF00FF")
    text.tag_config('command', background="black", foreground="#e08009")

    text.insert(tk.END, intro, 'warning') # warning is for highlighting the text
    return text

def terminal(output, text, package_no):
    text.config(state="normal") # Interactive box (afterwards it will be set to disabled) as user should not be able to type into that area

    if package_no != 1:         # If this is not the first package
        intro = """┌──(kali㉿kali)-[~]\n└─$ """ # Beautification
        text.insert(tk.END, intro, 'warning')
    text.insert(tk.END, f"{' '.join(output.args)}\n", 'command')

    outputs = output.communicate()[0].decode('utf-8').split('\n')
    for item in outputs:        # If the package is first
        text.insert(tk.END, item)
        text.insert(tk.END, "\n")

    text.insert(tk.END, "\n")
    text.config(state="disabled")   # Disabled to prevent user from typing in the output display area
    return text