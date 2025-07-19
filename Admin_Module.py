from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import PIL.Image
import PIL.ImageTk

admin_window = Tk()
admin_window.title("Face Recognition Voting System")
admin_window.geometry("720x480")
admin_window.config(bg='white')
admin_window.resizable(False, False)

admin_image = PhotoImage(file='Image/admin.png')

def Total_Poll():
    BJP_Poll = 0
    Congress_Poll = 0
    ADMK_Poll = 0
    DMK_Poll = 0

    with open("Election_database.txt", 'r+') as f:
        poll_list = f.readlines()
        for i in poll_list:
            if "voted for BJP" in i:
                BJP_Poll += 1
            if "voted for Congress" in i:
                Congress_Poll += 1
            if "voted for ADMK" in i:
                ADMK_Poll += 1
            if "voted for DMK" in i:
                DMK_Poll += 1

    BJP_count.config(text=BJP_Poll)
    Congress_count.config(text=Congress_Poll)
    ADMK_count.config(text=ADMK_Poll)
    DMK_count.config(text=DMK_Poll)

admin_label = Label(admin_window, text="Admin Module - Total Poll Vote Count",
                                    font=('poppins', 20, 'bold'), bg='white', fg="#de5f3c")
admin_label.place(x=108, y=30)

admin_logo = Label(admin_window, image=admin_image, bg='white')
admin_logo.place(x=10, y=80)

BJP_lable = Label(admin_window, text="BJP", font=('poppins', 18, 'bold'), bg='white', fg="#ad444c")
BJP_lable.place(x=420, y=110)

arrow_1 = Label(admin_window, text="=>", font=('poppins', 18, 'bold'), bg='white', fg="#ad444c")
arrow_1.place(x=560, y=110)

BJP_count = Label(admin_window, text='0', font=('poppins', 18, 'bold'), bg='white', fg="#ad444c")
BJP_count.place(x=640, y=108)

Congress_lable = Label(admin_window, text="Congress", font=('poppins', 18, 'bold'), bg='white', fg="#ad444c")
Congress_lable.place(x=420, y=160)

arrow_2 = Label(admin_window, text="=>", font=('poppins', 18, 'bold'), bg='white', fg="#ad444c")
arrow_2.place(x=560, y=160)

Congress_count = Label(admin_window, text='0', font=('poppins', 18, 'bold'), bg='white', fg="#ad444c")
Congress_count.place(x=640, y=158)

ADMK_lable = Label(admin_window, text="ADMK", font=('poppins', 18, 'bold'), bg='white', fg="#ad444c")
ADMK_lable.place(x=420, y=210)

arrow_3 = Label(admin_window, text="=>", font=('poppins', 18, 'bold'), bg='white', fg="#ad444c")
arrow_3.place(x=560, y=210)

ADMK_count = Label(admin_window, text='0', font=('poppins', 18, 'bold'), bg='white', fg="#ad444c")
ADMK_count.place(x=640, y=208)

DMK_lable = Label(admin_window, text="DMK", font=('poppins', 18, 'bold'), bg='white', fg="#ad444c")
DMK_lable.place(x=420, y=260)

arrow_4 = Label(admin_window, text="=>", font=('poppins', 18, 'bold'), bg='white', fg="#ad444c")
arrow_4.place(x=560, y=260)

DMK_count = Label(admin_window, text='0', font=('poppins', 18, 'bold'), bg='white', fg="#ad444c")
DMK_count.place(x=640, y=258)

refresh_count = Button(admin_window, text="Refresh Poll", font=('poppins', 16, 'bold'), command=Total_Poll)
refresh_count.config(width=18, height=1, bg='black', fg='white', activebackground="black", activeforeground='white')
refresh_count.place(x=420, y=320)

admin_window.mainloop()
