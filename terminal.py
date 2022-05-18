import tkinter as tk

def terminal_maker(root):
    text = tk.Text(root, height = 10, width = 100, bg = "#000000", fg="#00FFFF")
    text.place(x=5, y=500, width=1000, height=300)
    intro = """┌──(kali㉿kali)-[~]\n└─$ """
    text.tag_config('warning', background="black", foreground="#FF00FF")
    text.tag_config('command', background="black", foreground="#e08009")
    # text.tag_config('warning', background="black", foreground="#e08009")
    text.insert(tk.END, intro, 'warning')
    return text

def terminal(output, text, package_no):
    text.config(state="normal")

    if package_no != 1:
        intro = """┌──(kali㉿kali)-[~]\n└─$ """
        text.insert(tk.END, intro, 'warning')
    text.insert(tk.END, f"{' '.join(output.args)}\n", 'command')

    outputs = output.communicate()[0].decode('utf-8').split('\n')
    for item in outputs:
        text.insert(tk.END, item)
        text.insert(tk.END, "\n")

    text.insert(tk.END, "\n")
    text.config(state="disabled")
    return text
    
