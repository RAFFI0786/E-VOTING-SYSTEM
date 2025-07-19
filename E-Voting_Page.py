from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import mysql.connector
import cv2
import face_recognition
import PIL.Image
import PIL.ImageTk
from time import sleep

root = tk.Tk()
root.title("Face Recognition Voting System")
root.geometry("925x500+300+200")
root.config(bg='#fff')
win_logo = PhotoImage(file="Image/poll.png")
root.iconphoto(win_logo, win_logo)
root.resizable(False, False)
login_icon = PhotoImage(file='Image/login.png')
passshow_icon = PhotoImage(file='Image/eye.png')
passhide_icon = PhotoImage(file='Image/hide.png')

db = mysql.connector.connect(host='localhost',
                                   port=3306,
                                   database='vote_details',
                                   user='root',
                                   password='')
cursor = db.cursor()

password_mode = True

login_photo = tk.Label(root, image=login_icon, bg='white')
login_photo.place(x=30, y=30)

login_frame = tk.Frame(root, width=350, height=420, bg='white')
signup_frame = tk.Frame(root, width=350, height=420, bg='white')

def change_signin():

    def voting_poll(name_of_person, aadhar_id):
            
            def update_Vote():
                already_vote = 0

                if vote.get() == 1:
                    BJP_Vote_1 = messagebox.askyesno("Verification", "Are you ready to poll your vote for BJP?")
                    if BJP_Vote_1:
                        BJP_Vote_2 = messagebox.askyesno("Second Verification",
                                                         "Are you damn sure to submit your vote for BJP?")
                        if BJP_Vote_2:
                            with open("Election_Database.txt", "r+") as f:
                                vote_value = f.readlines()
                                total_vote = len(vote_value)
                                for i in range(total_vote):
                                    if vote_value[i] == f"{name_of_person}\n":
                                        already_vote = 1
                            with open("Election_Database.txt", "a+") as f:
                                if already_vote == 0:
                                    print(f"Successfully, {name_of_person} voted for BJP")
                                    f.write(f'{name_of_person}\n')
                                    f.write('voted for BJP\n')
                                    messagebox.showinfo("Success",
                                                        f"{name_of_person} Successfully voted for BJP")
                                    print("Voting Polled Successfully ...")
                                else:
                                    messagebox.showwarning("Warning", f"{name_of_person} already voted ...")
                                    print(
                                        f"{name_of_person} already polled vote in the mentioned candidates ...")
                elif vote.get() == 2:
                    Congress_Vote_1 = messagebox.askyesno("Verification", "Are you ready to poll your vote for Congress?")
                    if Congress_Vote_1:
                        Congress_Vote_2 = messagebox.askyesno("Second Verification",
                                                              "Are you damn sure to submit your vote for Congress?")
                        if Congress_Vote_2:
                            with open("Election_Database.txt", "r+") as f:
                                vote_value = f.readlines()
                                total_vote = len(vote_value)
                                for i in range(total_vote):
                                    if vote_value[i] == f"{name_of_person}\n":
                                        already_vote = 1
                            with open("Election_Database.txt", "a+") as f:
                                if already_vote == 0:
                                    print(f"Successfully, {name_of_person} voted for Congress")
                                    f.write(f'{name_of_person}\n')
                                    f.write('voted for Congress\n')
                                    messagebox.showinfo("Success",
                                                        f"{name_of_person} Successfully voted for Congress")
                                    print("Voting Polled Successfully ...")
                                else:
                                    messagebox.showwarning("Warning", f"{name_of_person} already voted ...")
                                    print(
                                        f"{name_of_person} already polled vote in the mentioned candidates ...")
                elif vote.get() == 3:
                    ADMK_Vote_1 = messagebox.askyesno("Verification", "Are you ready to poll your vote for ADMK?")
                    if ADMK_Vote_1:
                        ADMK_Vote_2 = messagebox.askyesno("Second Verification",
                                                          "Are you damn sure to submit your vote for ADMK?")
                        if ADMK_Vote_2:
                            with open("Election_Database.txt", "r+") as f:
                                vote_value = f.readlines()
                                total_vote = len(vote_value)
                                for i in range(total_vote):
                                    if vote_value[i] == f"{name_of_person}\n":
                                        already_vote = 1
                            with open("Election_Database.txt", "a+") as f:
                                if already_vote == 0:
                                    print(f"Successfully, {name_of_person} voted for ADMK")
                                    f.write(f'{name_of_person}\n')
                                    f.write('voted for ADMK\n')
                                    messagebox.showinfo("Success",
                                                        f"{name_of_person} Successfully voted for ADMK")
                                    print("Voting Polled Successfully ...")
                                else:
                                    messagebox.showwarning("Warning", f"{name_of_person} already voted ...")
                                    print(
                                        f"{name_of_person} already polled vote in the mentioned candidates ...")
                elif vote.get() == 4:
                    DMK_Vote_1 = messagebox.askyesno("Verification", "Are you ready to poll your vote for DMK?")
                    if DMK_Vote_1:
                        DMK_Vote_2 = messagebox.askyesno("Second Verification",
                                                         "Are you damn sure to submit your vote for DMK?")
                        if DMK_Vote_2:
                            with open("Election_Database.txt", "r+") as f:
                                vote_value = f.readlines()
                                print(vote_value)
                                total_vote = len(vote_value)
                                for i in range(total_vote):
                                    if vote_value[i] == f"{name_of_person}\n":
                                        already = 1
                            with open("Election_Database.txt", "a+") as f:
                                if already == 0:
                                    f.write(f'{name_of_person}\n')
                                    f.write('voted for DMK\n')
                                    print("Voting Polled Successfully ...")
                                else:
                                    messagebox.showwarning("Warning", f"{name_of_person} already voted")
                                    print(
                                        f"{name_of_person} already polled vote in the mentioned candidates ...")
                else:
                    messagebox.showerror("Empty Poll",
                                         f"{name_of_person}, You are not selected any candidate from the list")
                    print("Some Problem Occurs ...")

            vote_window = Tk()
            vote_window.title("Face Recognition Voting System")
            win_logo = PhotoImage(file="Image/poll.png")
            vote_window.iconphoto(win_logo, win_logo)
            vote_window.geometry("720x480")
            vote_window.config(bg="gray")
            vote_window.resizable(False, False)

            bg_img = PIL.Image.open('Image/back.png').resize((720, 480))
            bg_img = PIL.ImageTk.PhotoImage(bg_img)
            background_img = Label(vote_window, image=bg_img)
            background_img.pack()

            project_title = Label(vote_window, text="FACE RECOGNITION VOTING SYSTEM",
                                  font=('poppins', 18, 'bold'))
            project_title.config(bg='#d5d9db')
            project_title.place(x=50, y=15)

            login_details = Label(vote_window, text=f"Welcome, {name_of_person}\n({aadhar_id})",
                                  font=('poppins', 8, 'bold'))
            login_details.config(bg='#d5d9db')
            login_details.place(x=550, y=10)

            question_lable = Label(vote_window,
                                   text="Who do you want to vote in below mentioned parties ...")
            question_lable.config(bg='#d5d9db', font=('poppins', 13))
            question_lable.place(x=30, y=100)

            vote = IntVar()
            bjp = PIL.Image.open('Image/BJP.png')
            bjp = PIL.ImageTk.PhotoImage(bjp)
            option1_symbol = Label(vote_window, image=bjp, bg="#d5d9db")
            option1_symbol.place(x=240, y=140)
            option1 = Radiobutton(vote_window, text="BJP", variable=vote, value="1", cursor='hand2')
            option1.config(bg="#d5d9db", font=('Arial', 15), activebackground="#d5d9db")
            option1.place(x=120, y=150)

            congress = PIL.Image.open('Image/Congress.jpg').resize((40, 40))
            congress = PIL.ImageTk.PhotoImage(congress)
            option2_symbol = Label(vote_window, image=congress, bg="#d5d9db")
            option2_symbol.place(x=245, y=200)
            option2 = Radiobutton(vote_window, text="Congress", variable=vote, value="2",
                                  cursor='hand2')
            option2.config(bg="#d5d9db", font=('Arial', 15), activebackground="#d5d9db")
            option2.place(x=120, y=205)

            admk = PIL.Image.open('Image/ADMK.jpg').resize((40, 40))
            admk = PIL.ImageTk.PhotoImage(admk)
            option3_symbol = Label(vote_window, image=admk, bg="#d5d9db")
            option3_symbol.place(x=245, y=256)
            option3 = Radiobutton(vote_window, text="ADMK", variable=vote, value="3",
                                  cursor='hand2')
            option3.config(bg="#d5d9db", font=('Arial', 15), activebackground="#d5d9db")
            option3.place(x=120, y=260)

            dmk = PIL.Image.open('Image/DMK.png').resize((40, 40))
            dmk = PIL.ImageTk.PhotoImage(dmk)
            option4_symbol = Label(vote_window, image=dmk, bg="#d5d9db")
            option4_symbol.place(x=245, y=313)
            option4 = Radiobutton(vote_window, text="DMK", variable=vote, value="4", cursor='hand2')
            option4.config(bg="#d5d9db", font=('Arial', 15), activebackground="#d5d9db")
            option4.place(x=120, y=315)

            final_vote = Button(vote_window, text="Poll Vote", command=update_Vote)
            final_vote.config(font=('Arial', 15, 'bold'), width=20, height=1, bg='black',
                              fg='white', activebackground='black', activeforeground='white')
            final_vote.place(x=80, y=390)

            vote_window.mainloop()

    signup_frame.place_forget()
    login_frame.place(x=480, y=70)

    login_head = tk.Label(login_frame, text='Voter Login Page', fg='#57a1f8', bg='white',
                          font=('Microsoft YaHei UI Light', 23, 'bold'))
    login_head.place(x=45, y=5)

    def signin():
        aadhar_id = login_user_entry.get()
        password = login_pass_entry.get()

        if aadhar_id == 'Aadhaar ID' or password == 'Password':
            messagebox.showwarning("Warning", "Please enter missing Aadhaar ID or Password !!!")

        else:
            cursor.execute("select * from voter_content where aadhar_id = %s and password = %s",
                           [(aadhar_id), (password)])
            user_details = cursor.fetchall()

            if user_details:
                username = user_details[0][0]
                messagebox.showinfo("Login Successfully", "Welcome " + username + " !")
                root.destroy()

                # Capture video from default camera
                webcam_video_stream = cv2.VideoCapture(0)
                check = 0

                # Load samples and retrieve 128 face encodings for each
                face_1 = face_recognition.load_image_file('dataset/01.jpg')
                face_1_encodings = face_recognition.face_encodings(face_1)[0]
                face_1_name = 'Madan Raj'

                face_2 = face_recognition.load_image_file('dataset/02.jpg')
                face_2_encodings = face_recognition.face_encodings(face_2)[0]
                face_2_name = 'Raffi'

                face_3 = face_recognition.load_image_file('dataset/03.jpg')
                face_3_encodings = face_recognition.face_encodings(face_3)[0]
                face_3_name = 'Vignesh'

                face_4 = face_recognition.load_image_file('dataset/04.jpg')
                face_4_encodings = face_recognition.face_encodings(face_4)[0]
                face_4_name = 'Sarma'

                # Save encodings and corresponding labels to separate arrays in same order
                known_face_encodings = [face_1_encodings, face_2_encodings, face_3_encodings, face_4_encodings]
                known_face_names = [face_1_name, face_2_name, face_3_name, face_4_name]

                # Initialize arrays for face locations, encodings, and names
                all_face_locations = []
                all_face_encodings = []
                all_face_names = []

                # Loop through each video frame until user exits
                while True:
                    ret, current_frame = webcam_video_stream.read()

                    # Let's use a smaller version (0.25x) of the image for faster processing
                    scale_factor = 4
                    current_frame_small = cv2.resize(
                        current_frame, (0, 0), fx=1 / scale_factor, fy=1 / scale_factor)

                    # Find total number of faces, encodings, set names to empty
                    all_face_locations = face_recognition.face_locations(
                        current_frame_small, number_of_times_to_upsample=2, model='hog')

                    all_face_encodings = face_recognition.face_encodings(current_frame_small, all_face_locations)

                    # Iterate through each face location and encoding in our test image
                    for current_face_location, current_face_encoding in zip(all_face_locations, all_face_encodings):

                        # Splitting up tuple of face location
                        top_pos, right_pos, bottom_pos, left_pos = current_face_location

                        # Correct positions based on scale factor
                        top_pos *= scale_factor
                        right_pos *= scale_factor
                        bottom_pos *= scale_factor
                        left_pos *= scale_factor

                        # Now we'll slice our image array to isolate the faces
                        current_face_image = current_frame[top_pos: bottom_pos,
                                             left_pos:right_pos]

                        # Compare to known faces to check for matches
                        all_matches = face_recognition.compare_faces(
                            known_face_encodings, current_face_encoding)

                        # Initialize name string as unknown face
                        name_of_person = 'Unknown Person'

                        # Check if all_matches isn't empty
                        # If yes get the index number corresponding to the face in the first index
                        if True in all_matches:
                            first_match_index = all_matches.index(True)
                            name_of_person = known_face_names[first_match_index]

                        # Draw rectangle around face
                        cv2.rectangle(current_frame, (left_pos, top_pos),
                                      (right_pos, bottom_pos), (255, 0, 255), 2)

                        # Write corresponding name below face
                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(current_frame, name_of_person, (left_pos,
                                                                    bottom_pos + 20), font, 0.8, (0, 0, 255), 2)

                    # Display image with rectangle and text
                    cv2.imshow('Face Recognition Analysis', current_frame)

                    # Press 'Spacebar' key to exit loop
                    if cv2.waitKey(1) == ord(' '):
                        if name_of_person == "Unknown Person":
                            print("Unknown Person identified, You are not allowed to vote ...")
                            messagebox.showerror("Malfunction Occured",
                                                 "Unknown Person identified, You are not allowed to vote ...")
                            break
                        else:
                            print(f"{name_of_person} identified Successfully, You are redirected to vote page ...")
                            user_decision = messagebox.askokcancel("Face Recognition Voting",
                                                                   f"{name_of_person} identified Successfully, Do you ready to vote or not ?")
                            if username == name_of_person:
                                if user_decision:
                                    webcam_video_stream.release()
                                    cv2.destroyAllWindows()
                                    print("Voting Program Executing ...")
                                    sleep(2)
                                    voting_poll(name_of_person, aadhar_id)
                                    break
                                else:
                                    print("Exit Program Executing ...")
                                    sleep(2)
                                    continue
                            else:
                                messagebox.showerror("Malpractise", "Person identified not match with Database, So you are allowed to vote ...")
                                cv2.destroyAllWindows()
                                print("Exit Program Executing ...")
            else:
                messagebox.showerror("Login Error", "Aadhaar ID or Password is Incorrect, Please try again ...")

    def user_on_enter(e):
        login_user_entry.config(font=('Arial', 11))
        login_user_entry.delete(0, 'end')

    def user_on_leave(e):
        login_username = login_user_entry.get()
        if login_username == '':
            login_user_entry.insert(0, 'Aadhaar ID')

    login_user_entry = tk.Entry(login_frame, width=25, fg='black', border=0, bg='white',
                          font=('Microsoft YaHei UI Light', 11))
    login_user_entry.place(x=30, y=80)
    login_user_entry.insert(0, 'Aadhaar ID')
    login_user_entry.bind('<FocusIn>', user_on_enter)
    login_user_entry.bind('<FocusOut>', user_on_leave)

    tk.Frame(login_frame, width=295, height=2, bg='black').place(x=25, y=107)

    def pass_on_enter(e):
        login_pass_entry.delete(0, 'end')
        login_pass_entry.config(show='*', font=('Arial', 11))
        login_pass_show.config(image=passhide_icon)

    def pass_on_leave(e):
        login_pass_entry.config(show='')
        login_pass_show.config(fg='#fff', image='')
        login_password = login_pass_entry.get()
        if login_password == '':
            login_pass_entry.insert(0, 'Password')

    def passshow():
        global password_mode

        if password_mode:
            login_pass_show.config(image=passshow_icon)
            login_pass_entry.config(show='')
            password_mode = False
        else:
            login_pass_show.config(image=passhide_icon)
            login_pass_entry.config(show='*')
            password_mode = True

    login_pass_entry = tk.Entry(login_frame, width=25, fg='black', border=0, bg='white',
                          font=('Microsoft YaHei UI Light', 11))
    login_pass_entry.place(x=30, y=150)
    login_pass_entry.insert(0, 'Password')
    login_pass_entry.bind('<FocusIn>', pass_on_enter)
    login_pass_entry.bind('<FocusOut>', pass_on_leave)

    login_pass_show = tk.Button(login_frame, image='', border=0, bg='#fff', activebackground='#fff', command=passshow)
    login_pass_show.place(x=280, y=135, width=50, height=50)

    tk.Frame(login_frame, width=295, height=2, bg='black').place(x=25, y=177)

    login_login_btn = tk.Button(login_frame, width=42, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,
                          command=signin)
    login_login_btn.place(x=25, y=225)

    signup_label = tk.Label(login_frame, text="Don't have an account?", fg='black', bg='white',
                            font=('Microsoft YaHei UI Light', 9))
    signup_label.place(x=75, y=280)

    signup_btn = tk.Button(login_frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                           activebackground='white', activeforeground='#57a1f8', command=change_signup)
    signup_btn.place(x=215, y=280)

def change_signup():

    login_frame.place_forget()
    signup_frame.place(x=480, y=50)

    login_head = tk.Label(signup_frame, text='Voter Register Page', fg='#57a1f8', bg='white',
                          font=('Microsoft YaHei UI Light', 23, 'bold'))
    login_head.place(x=30, y=5)

    def signup():
        username = register_user_entry.get()
        password = register_pass_entry.get()
        aadhaar_id = register_staffid_entry.get()
        phone_no = register_phone_entry.get()

        if username == 'Voter Name' or password == 'Password' or aadhaar_id == 'Aadhaar ID' or phone_no == 'Phone Number':
            messagebox.showwarning("Warning", "Please enter missing elements to proceed voter register !!!")
        elif len(aadhaar_id) < 12 or len(aadhaar_id) > 12:
            messagebox.showerror("Aadhaar Error", "Please provide correct Aadhar ID ...")
        elif len(phone_no) < 10 or len(phone_no) > 10:
            messagebox.showerror("Phone Number Error", "Please provide Phone number correctly ...")
        else:
            cursor.execute("insert into voter_content values(%s,%s,%s,%s)", (username, aadhaar_id, phone_no, password))
            db.commit()
            messagebox.showinfo("Success", "Registered Successfully!!")

    def user_on_enter(e):
        register_user_entry.delete(0, 'end')

    def user_on_leave(e):
        register_username = register_user_entry.get()
        if register_username == '':
            register_user_entry.insert(0, 'Voter Name')

    register_user_entry = tk.Entry(signup_frame, width=25, fg='black', border=0, bg='white',
                          font=('Microsoft YaHei UI Light', 11))
    register_user_entry.place(x=30, y=80)
    register_user_entry.insert(0, 'Voter Name')
    register_user_entry.bind('<FocusIn>', user_on_enter)
    register_user_entry.bind('<FocusOut>', user_on_leave)

    tk.Frame(signup_frame, width=295, height=2, bg='black').place(x=25, y=110)

    def staffid_on_enter(e):
        register_staffid_entry.delete(0, 'end')

    def staffid_on_leave(e):
        register_staffid = register_staffid_entry.get()
        if register_staffid == '':
            register_staffid_entry.insert(0, 'Aadhaar ID')

    register_staffid_entry = tk.Entry(signup_frame, width=25, fg='black', border=0, bg='white',
                           font=('Microsoft YaHei UI Light', 11))
    register_staffid_entry.place(x=30, y=140)
    register_staffid_entry.insert(0, 'Aadhaar ID')
    register_staffid_entry.bind('<FocusIn>', staffid_on_enter)
    register_staffid_entry.bind('<FocusOut>', staffid_on_leave)

    tk.Frame(signup_frame, width=295, height=2, bg='black').place(x=25, y=170)

    def phone_on_enter(e):
        register_phone_entry.delete(0, 'end')

    def phone_on_leave(e):
        register_phone = register_phone_entry.get()
        if register_phone == '':
            register_phone_entry.insert(0, 'Phone Number')

    register_phone_entry = tk.Entry(signup_frame, width=25, fg='black', border=0, bg='white',
                           font=('Microsoft YaHei UI Light', 11))
    register_phone_entry.place(x=30, y=200)
    register_phone_entry.insert(0, 'Phone Number')
    register_phone_entry.bind('<FocusIn>', phone_on_enter)
    register_phone_entry.bind('<FocusOut>', phone_on_leave)

    tk.Frame(signup_frame, width=295, height=2, bg='black').place(x=25, y=230)

    def pass_on_enter(e):
        register_pass_entry.delete(0, 'end')
        register_pass_entry.config(show='*')
        register_pass_show.config(image=passhide_icon)

    def pass_on_leave(e):
        register_pass_entry.config(show='')
        register_pass_entry.insert(0, 'Password')
        register_pass_show.config(fg='#fff', image='')

    def passshow():
        global password_mode

        if password_mode:
            register_pass_show.config(image=passshow_icon)
            register_pass_entry.config(show='')
            password_mode = False
        else:
            register_pass_show.config(image=passhide_icon)
            register_pass_entry.config(show='*')
            password_mode = True

    register_pass_entry = tk.Entry(signup_frame, width=25, fg='black', border=0, bg='white',
                                   font=('Microsoft YaHei UI Light', 11))
    register_pass_entry.place(x=30, y=260)
    register_pass_entry.insert(0, 'Password')
    register_pass_entry.bind('<FocusIn>', pass_on_enter)
    register_pass_entry.bind('<FocusOut>', pass_on_leave)

    register_pass_show = tk.Button(signup_frame, image='', border=0, bg='#fff', activebackground='#fff',
                                   command=passshow)
    register_pass_show.place(x=280, y=250, width=50, height=50)

    tk.Frame(signup_frame, width=295, height=2, bg='black').place(x=25, y=290)

    signup_btn = tk.Button(signup_frame, width=37, pady=3, text='Sign up', bg='#57a1f8', fg='white', border=0,
                           command=signup,
                           font=('Microsoft YaHei UI Light', 10))
    signup_btn.place(x=25, y=325)

    signup_label = tk.Label(signup_frame, text="Already have an account?", fg='black', bg='white',
                            font=('Microsoft YaHei UI Light', 9))
    signup_label.place(x=65, y=375)

    signup_btn = tk.Button(signup_frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                           activebackground='white', activeforeground='#57a1f8', command=change_signin)
    signup_btn.place(x=215, y=375)

change_signin()

root.mainloop()
