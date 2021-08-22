
import tkinter as tk
from tkinter.constants import END
from tkinter import messagebox as mb

hostfile = "C:\Windows\System32\drivers\etc\hosts"
localhost = '127.0.0.1'

def Response():
    result = myText.get()
    displayText.configure(state='normal')
    displayText.insert(END, result +",")
    displayText.configure(state='disabled')
    User_input.delete(0,END)


def getSiteFromTextAndBlock():
    global sites
    sites = [x.strip()for x in displayText.get("1.0", END).split(",")]
    try:
        with open(hostfile, "r+") as file:
            content = file.read()
            for site in sites:
                if site in content:
                    pass
                else:
                    file.write("\n"+ localhost + " " + site)
            mb.showinfo(title="info", message="all sites blocked")
    except:
        mb.showinfo(title="Exception", message="error")

def unblockAll():
    with open(hostfile, "r+") as file:
        contents=file.readlines()
        file.seek(0)
        for content in contents:
            if not any(website in content for website in sites):
                file.write(content)
        file.truncate()
        displayText.configure(state='normal')
        displayText.delete('1.0', END)
        displayText.configure(state="disabled")
        mb.showinfo(title="unblocke websites", message="Done")

root=tk.Tk()
root.title("Website-blocker")
root.geometry("400x500")

myText= tk.StringVar()
root.resizable(False,False)

User_input=tk.Entry(root, textvariable=myText, width=50)
User_input.place(x=40, y=370)
addButton = tk.Button(root, text="Add to list", command=Response, bg='green', height=2, width=10).place(x=250,y=420)
blockButton = tk.Button(root, text="block-site", command=getSiteFromTextAndBlock, bg="red", height=2, width=10 ).place(x=150, y=420)
unblockButton = tk.Button(root, text="unblock sites", command=unblockAll, bg="blue", height=2, width=10).place(x=50, y=420)
displayText = tk.Text(root, height=20, width=40)
displayText.pack()
displayText.configure(state="disabled")

root.mainloop()