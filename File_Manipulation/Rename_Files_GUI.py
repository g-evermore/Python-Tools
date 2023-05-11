from tkinter import *
from file_manipulator import FileManipulator

def handle_entry_click(event):
    entry_txt = entry.get()
    if entry_txt == "":
        lbl_entry.config(text="You must provide entry, first.")
    else:
        fm = FileManipulator()
        if drill_selection.get()>0:
            fm.begin(entry.get(), drill=True)
        else:
            fm.begin(entry.get())    
        lbl_entry.config(text="Done! Files are renamed.")
        entry.delete(0,END)
        

#============== MAIN ==============#

window = Tk()

frm_border = Frame(window, borderwidth=5)
banner_msg = "                   RENAME_FILES_GUI.PY                   \n"
banner_msg = banner_msg + "           Renames files within a directory           "
lbl_banner = Label(frm_border, text=banner_msg)
lbl_farewell = Label(frm_border, text="                   RENAME_FILES_GUI.PY                   ")
lbl_banner.pack()

frm_entry = Frame(frm_border, borderwidth=5, relief="groove", width=200, height=100)
lbl_entry = Label(frm_entry, text="Provide a directory path:")
entry = Entry(frm_entry, width = 40)
entry.bind('<Return>', handle_entry_click)
entry.focus()
btn_entry = Button(frm_entry,text="Rename Files",width=len("Rename Files"),bg="green",fg="white")
btn_entry.bind("<Button-1>", handle_entry_click)

drill_selection = IntVar()
ckb_drill = Checkbutton(frm_entry, text="Drill", variable=drill_selection)


lbl_entry.pack()
entry.pack()
ckb_drill.pack()
btn_entry.pack()
frm_entry.pack()

lbl_farewell.pack()
frm_border.pack()

window.mainloop()
