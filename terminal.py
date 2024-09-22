import customtkinter as tk

# Clone of a terminal to display the status of installation or upgradation
def terminal_maker(root):
    # Color and size config
    text = tk.CTkTextbox(root, border_width=3,height = 300, width = 1100, bg_color="#000000",  border_color="#2F4F4F")
    text.place(x=0, y=500)

    intro = """┌──(kali㉿kali)-[~]\n└─$ """     # Beautification

    text.insert(tk.END, intro)
    return text

def terminal(output, text, package_no):
    text.configure(state="normal") # Interactive box (afterwards it will be set to disabled) as user should not be able to type into that area

    if package_no != 1:         # If this is not the first package
        intro = """┌──(kali㉿kali)-[~]\n└─$ """ # Beautification
        text.insert(tk.END, intro)
    text.insert(tk.END, f"{' '.join(output.args)}\n")

    outputs = output.communicate()[0].decode('utf-8').split('\n')
    for item in outputs:        # If the package is first
        text.insert(tk.END, item)
        text.insert(tk.END, "\n")

    text.insert(tk.END, "\n")
    text.configure(state="disabled")   # Disabled to prevent user from typing in the output display area
    return text
