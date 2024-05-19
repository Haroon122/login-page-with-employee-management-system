from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter
import mysql.connector
from register import Register

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Login Page")
        self.reset_pass_window = None


 #================veriables================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_cPassword=StringVar()
        self.var_nwPassword=StringVar()



        # =========background frame============
        main_frm = Frame(self.root, bg="white", width=1350, height=700)
        main_frm.place(x=0, y=0)

        # =============login image============
        login_img = Image.open(r"E:\python projects\login with employe managment system\data\login.jpg")
        login_img = login_img.resize((700,500), Image.LANCZOS)
        self.login_photo = ImageTk.PhotoImage(login_img)
        lbl_L = Label(main_frm, bg="white", image=self.login_photo)
        lbl_L.place(x=100,y=70,width=700,height=500)
        
        # =========login frame============
        login_frm = Frame(main_frm, bg="white", width=350, height=350)
        login_frm.place(x=880, y=100)

        # =============top heading================
        heading = Label(login_frm, text="sign in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=100, y=5)

        # ===============sign in button======================
        s_btn = Button(login_frm,command=self.login_pg, width=39, pady=7, text="sign in", bg="#57a1f8", fg="white", border=0, cursor="hand2")
        s_btn.place(x=35, y=204)

        # =============sign up button=================
        s_up = Button(login_frm,activebackground="white",command=self.signUP, text="sign up", border=0, bg="white", fg="#57a1f8", cursor="hand2")
        s_up.place(x=220, y=270)

        # =============forget button=================
        f_up = Button(login_frm,command=self.forget_pass,activebackground="white", text="Forget password ", border=0, bg="white", fg="#57a1f8", cursor="hand2")
        f_up.place(x=133, y=305)        

        # ==============dont account label=================
        Ac_lbl = Label(login_frm, text="Don't have an account?", fg="black", bg="white",font=("Microsoft YaHei UI Light", 9))         
        Ac_lbl.place(x=75, y=270)


        # =============line 1 email frame=============
        line_frm = Frame(login_frm, width=295, height=2, bg="black")
        line_frm.place(x=25, y=107)

        # =============line 2 password frame=============
        line1_frm = Frame(login_frm, width=295, height=2, bg="black")
        line1_frm.place(x=25, y=177)

        # ==========user entry box=============
        self.user = Entry(login_frm, width=25, fg="black", bg="white", border=0, font=("Microsoft YaHei UI Light", 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, "Email")
        self.user.bind("<FocusIn>", self.on_enter)
        self.user.bind("<FocusOut>", self.on_leave)

        # ==========password entry box=============
        self.passw = Entry(login_frm, width=25, fg="black", bg="white", border=0, font=("Microsoft YaHei UI Light", 11))
        self.passw.place(x=30, y=150)
        self.passw.insert(0, "Password")
        self.passw.bind("<FocusIn>", self.on_enter)
        self.passw.bind("<FocusOut>", self.on_leave)

    def on_enter(self, event):
        if event.widget == self.user:
            self.user.delete(0, "end")
        elif event.widget == self.passw:
            self.passw.delete(0, "end")

    def on_leave(self, event):
        name = event.widget.get()
        if name == "":
            if event.widget == self.user:
                self.user.insert(0, "Email")
            elif event.widget == self.passw:
                self.passw.insert(0, "Password")


# ===============LOGIN WORKING=============
    def login_pg(self):
        E_mail = self.user.get()
        password = self.passw.get()

        if E_mail == "admin" and password == "123":
            messagebox.showinfo("Successful", "Successful login", parent=self.root)
        elif E_mail == "" or password == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="h@Roon#123Abc", database="login_page")
            curr = conn.cursor()
            curr.execute("SELECT * FROM register WHERE email=%s AND password=%s", (E_mail, password))
            row = curr.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid User Name or Password", parent=self.root)
            else:
                open_main = messagebox.askyesno("Access", "Access only admin", parent=self.root)
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = employe(self.new_window)
                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()

#================================Reset Password==================================            
    def forget_pass(self):
        if self.user.get() == "":
            messagebox.showerror("Error", "Please Enter the Email to Reset Password",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="h@Roon#123Abc", database="login_page")
            curr = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s"
            values = (self.user.get(),)
            curr.execute(query, values)
            row = curr.fetchone()

            if row is None:
                messagebox.showerror("Error", "Email Address not found. Please Enter a Valid Email Address",parent=self.root)
            else:
                conn.close()
                self.reset_pass_window = Toplevel(self.root)
                self.reset_pass_window.title("Forget Password")
                self.reset_pass_window.geometry("400x500+880+100")

                frm2 = Frame(self.reset_pass_window, bg="white")
                frm2.place(x=0, y=0, width=400, height=450)

                l = Label(self.reset_pass_window, text="Forget Password", bg="white", fg="#57a1f8",
                          font=("times new roman", 18, "bold"))
                l.place(x=0, y=0, relwidth=1)

                # Security Question
                Q2_lbl = Label(self.reset_pass_window, text="Select Security Questions", font=("roboto", 11, "bold"),
                               bg="white", fg="black")
                Q2_lbl.place(x=100, y=55)

                Q2_comb = ttk.Combobox(self.reset_pass_window, textvariable=self.var_securityQ, width=23,
                                       font=("Microsoft YaHei UI Light", 11), state="readonly")
                Q2_comb["values"] = ("Select Question", "Best Friend", "Primary School Name", "Born Date")
                Q2_comb.current(0)
                Q2_comb.place(x=100, y=85)

                # Security Answer
                A_lbl = Label(self.reset_pass_window, text="Security Answer", font=("roboto", 11, "bold"),
                              bg="white", fg="black")
                A_lbl.place(x=100, y=120)

                a1_entr = Entry(self.reset_pass_window, textvariable=self.var_securityA, bd=2, relief="ridge", width=25,
                                font=("Microsoft YaHei UI Light", 11))
                a1_entr.place(x=100, y=145)

                # New Password
                nw_lbl = Label(self.reset_pass_window, text="New Password", font=("roboto", 11, "bold"),
                               bg="white", fg="black")
                nw_lbl.place(x=100, y=205)

                nw_entr = Entry(self.reset_pass_window, textvariable=self.var_nwPassword, bd=2, relief="ridge", width=25,
                                font=("Microsoft YaHei UI Light", 11))
                nw_entr.place(x=100, y=235)

                # Reset Button
                btn = Button(self.reset_pass_window, command=self.reset_pass, width=15, text="Reset", fg="white",
                             bg="#57a1f8", border=0, font=("Microsoft YaHei UI Light", 15))
                btn.place(x=120, y=280)

    def reset_pass(self):
        if self.var_securityQ.get() == "Select Question":
            messagebox.showerror("Error", "Please Select Security Question",parent=self.reset_pass_window)
        elif self.var_securityA.get() == "":
            messagebox.showerror("Error", "Please enter security Answer",parent=self.reset_pass_window)
        elif self.var_nwPassword.get() == "":
            messagebox.showerror("Error", "Please enter the new password",parent=self.reset_pass_window)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="h@Roon#123Abc",
                                           database="login_page")
            curr = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
            value = (self.user.get(), self.var_securityQ.get(), self.var_securityA.get())
            curr.execute(query, value)
            row = curr.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please Enter the correct answer",parent=self.reset_pass_window)
            else:
                query = "UPDATE register SET password=%s WHERE email=%s"
                value = (self.var_nwPassword.get(), self.user.get())
                curr.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, please login with the new password !!!",parent=self.reset_pass_window)
                # Clear the entry fields
                self.var_securityQ.set("Select Question")
                self.var_securityA.set("")
                self.var_nwPassword.set("")
                # Destroy the reset password window
                self.reset_pass_window.destroy()

    
    def signUP(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


#########################################################################################
class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Registration Form")
        self.root.resizable(False,False)

    #================veriables================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_cPassword=StringVar()

    #=============main back frame==============
        bk_frm=Frame(self.root,bg="white")
        bk_frm.place(x=0,y=0,width=1350,height=700)

    #===============register image============
        img=Image.open(r"E:\python projects\login with employe managment system\data\register.jpg")
        img=img.resize((600,450),Image.LANCZOS)
        self.photo=ImageTk.PhotoImage(img)
        lbl=Label(bk_frm,image=self.photo)
        lbl.place(x=50, y=70, width=600, height=450)

    #======================register frame================
        R_frm=Frame(bk_frm,bg="white")
        R_frm.place(x=700,y=70,width=600,height=500)

    #=========1st label register here===========
        Tp_lbl=Label(R_frm,text="REGISTER HERE",font=("times new roman", 23, "bold"),bg="white",fg="#57a1f8")
        Tp_lbl.place(x=10,y=5)

    #=========2nd label name===========
        N_lbl=Label(R_frm,text="First Name",font=("roboto", 11, "bold"),bg="white",fg="black")
        N_lbl.place(x=10,y=80)

    #=========3rd label last name===========
        L_lbl=Label(R_frm,text="Last Name",font=("roboto", 11, "bold"),bg="white",fg="black")
        L_lbl.place(x=300,y=80)

    #=========4th label contact no===========
        L_lbl=Label(R_frm,text="Contact No",font=("roboto", 11, "bold"),bg="white",fg="black")
        L_lbl.place(x=10,y=150)

    #=========5th label email===========
        E_lbl=Label(R_frm,text="Email",font=("roboto", 11, "bold"),bg="white",fg="black")
        E_lbl.place(x=300,y=150)

    #=========6th seacurity quation===========
        Q_lbl=Label(R_frm,text="Select Security Questions",font=("roboto", 11, "bold"),bg="white",fg="black")
        Q_lbl.place(x=10,y=220)

    #=========7th seacurity Answer===========
        A_lbl=Label(R_frm,text="Security Answer",font=("roboto", 11, "bold"),bg="white",fg="black")
        A_lbl.place(x=300,y=220)

    #=========8th Password===========
        p_lbl=Label(R_frm,text="Password",font=("roboto", 11, "bold"),bg="white",fg="black")
        p_lbl.place(x=10,y=290)

    #=========9th Confirm Password===========
        cp_lbl=Label(R_frm,text="Confirm Password",font=("roboto", 11, "bold"),bg="white",fg="black")
        cp_lbl.place(x=300,y=290)


        self.var_check=IntVar()
    #==========terms condition check box========
        c_box=Checkbutton(R_frm,variable=self.var_check,activebackground="white",text="I Agree The Terms & Conditions",font=("roboto", 11, "bold"),bg="white",fg="black",onvalue=1,offvalue=0)
        c_box.place(x=10,y=365)

    #==========1 name entry box===============
        n_entr=Entry(R_frm,bd=2,textvariable=self.var_fname,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        n_entr.place(x=10,y=110)

    #==========2 last name entry box===============
        l_entr=Entry(R_frm,bd=2,textvariable=self.var_lname,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        l_entr.place(x=300,y=110)

    #==========3 contact entry box===============
        c_entr=Entry(R_frm,bd=2,textvariable=self.var_contact,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        c_entr.place(x=10,y=180)

    #==========4 email entry box===============
        e_entr=Entry(R_frm,bd=2,textvariable=self.var_email,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        e_entr.place(x=300,y=180)

    #=========5 S_Q combobox====================
        Q_comb=ttk.Combobox(R_frm,textvariable=self.var_securityQ,width=23,font=("Microsoft YaHei UI Light",11),state="readonly")
        Q_comb["values"]=("Select Question","Best Friend","Primary School Name","Born Date")
        Q_comb.current(0)
        Q_comb.place(x=10,y=253)

    #==========6 s_answer box===============
        a_entr=Entry(R_frm,bd=2,textvariable=self.var_securityA,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        a_entr.place(x=300,y=253)

    #==========7 password box===============
        p_entr=Entry(R_frm,bd=2,textvariable=self.var_password,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        p_entr.place(x=10,y=320)

    #==========8 confirm password box===============
        cp_entr=Entry(R_frm,textvariable=self.var_cPassword,bd=2,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        cp_entr.place(x=300,y=320)

    #============REGISTER BUTTON================
        R_btn=Button(R_frm,command=self.registerr,width=25,pady=6,text="Register Now",font=("Microsoft YaHei UI Light",10),bg="#57a1f8",fg="white",border=0,cursor="hand2")
        R_btn.place(x=10,y=400)

    #============login BUTTON================
        R_btn=Button(R_frm,command=self.login_rtn,width=25,pady=6,text="Login",font=("Microsoft YaHei UI Light",10),bg="#57a1f8",fg="white",border=0,cursor="hand2")
        R_btn.place(x=300,y=400)

    def login_rtn(self):
        self.root.destroy()


    #====================working=============================
    
    def registerr(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select Question" or self.var_securityA.get()=="" or self.var_password.get()=="":
            messagebox.showerror("Error","All Fields are required", parent=self.root)
        elif self.var_password.get()!=self.var_cPassword.get():
            messagebox.showerror("Error","Password & Confirm Password must be same", parent=self.root)
        elif self.var_check.get()== 0:
            messagebox.showerror("Error","please agree terms & condition", parent=self.root)
        else:
            try:               
                conn = mysql.connector.connect(host="localhost", user="root", password="h@Roon#123Abc", database="login_page")
                curr = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.var_email.get(),)
                curr.execute(query, value)
                row = curr.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists. Please try another email.", parent=self.root)
                else:
                        # Insert the new user into the database
                    query = "INSERT INTO register (first_name, last_name, contact_no, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    values = (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_password.get()
                    )
                    curr.execute(query, values)

                        # Commit the changes and close the connection
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Successful", "Registration Successful", parent=self.root)
                    self.clear_fields()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

    def clear_fields(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_securityQ.set("Select Question")
        self.var_securityA.set("")
        self.var_password.set("")
        self.var_cPassword.set("")

#########################################################################################
class employe():
    def __init__(self,root):
        self.root=root
        self.root.config(bg="white")
        self.root.geometry("1350x680+0+0")
        self.root.title("Employe managment system")

      #=================veriables====================
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_deginition=StringVar()
        self.var_mail=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_Id_Type=StringVar()
        self.var_Id_prof_comb=StringVar()
        self.var_Id_prof_entry=StringVar()
        self.var_gndr=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        self.var_srch_comb=StringVar()
        self.var_srch_entry=StringVar()
 

        #back main frame
        lbl_frame1=LabelFrame(self.root,width=1320,height=670,bg="white")
        lbl_frame1.place(x=15,y=0)

        #main Title
        lbl=Label(lbl_frame1,text="EMPLOYE MANAGMENT SYSTEM",font="arial 25 bold",bg="white",fg="dark blue")
        lbl.place(x=440,y=10)


        #employe info frame
        lbl_frame=LabelFrame(self.root,text="Employe Information",fg="red",font="arial 10 bold",width=1310,height=230,bg="white")
        lbl_frame.place(x=19,y=160)

        # #student image

        img1=Image.open(r"E:\python projects\login with employe managment system\data1\imm1.jpg")
        img1=img1.resize((300,200),Image.LANCZOS)
        self.photo=ImageTk.PhotoImage(img1)

        lbl_1= Label(lbl_frame,image=self.photo)
        lbl_1.place(x=1000,y=0,height=200,width=300)


        # #employe managment top pics 1

        img2=Image.open(r"E:\python projects\login with employe managment system\data1\4380.jpg")
        img2=img2.resize((300,130),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img2)

        self.img2 = Label(lbl_frame1,image=self.photo1).place(x=100,y=50,height=130,width=300)

        # #employe managment top pics 2

        img3=Image.open(r"E:\python projects\login with employe managment system\data1\5236.jpg")
        img3=img3.resize((300,120),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img3)

        self.img2 = Label(lbl_frame1,image=self.photo2).place(x=550,y=50,height=120,width=300)

        # #employe managment top pics 3

        img4=Image.open(r"E:\python projects\login with employe managment system\data1\imgg.jpg")
        img4=img4.resize((300,130),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img4)

        self.img4 = Label(lbl_frame1,image=self.photo3).place(x=1000,y=50,height=130,width=300)



         #employe info frame table
        #lbl_frame=LabelFrame(self.root,text="Employe Information Table",fg="red",font="arial 10 bold",width=1310,height=270,bg="white")
        #lbl_frame.place(x=19,y=390)

        #employe search info
        lbl_frame=LabelFrame(self.root,text="Employe Search Information",fg="red",font="arial 8 bold",width=1310,height=70,bg="white")
        lbl_frame.place(x=19,y=390)

        #employe data information  department
        lbl_info=Label(self.root,text="Department:",font="arial 13 bold",bg="white")
        lbl_info.place(x=30,y=180)

        #employe data information designition
        lbl_info=Label(self.root,text="Designition:",font="arial 13 bold",bg="white")
        lbl_info.place(x=30,y=220)

        #employe data information Address
        lbl_info=Label(self.root,text="Address:",font="arial 13 bold",bg="white")
        lbl_info.place(x=30,y=260)

        #employe data information DOB
        lbl_info=Label(self.root,text="D-O-B:",font="arial 13 bold",bg="white")
        lbl_info.place(x=30,y=300)

        #employe data information name
        lbl_info=Label(self.root,text="Name:",font="arial 13 bold",bg="white")
        lbl_info.place(x=365,y=180)

        #employe data information mail
        lbl_info=Label(self.root,text="E.mail:",font="arial 13 bold",bg="white")
        lbl_info.place(x=365,y=220)

        #employe data information marid status
        lbl_info=Label(self.root,text="Married Status:",font="arial 13 bold",bg="white")
        lbl_info.place(x=365,y=260)

        #employe data information Date of joining
        lbl_info=Label(self.root,text="D-O-J:",font="arial 13 bold",bg="white")
        lbl_info.place(x=365,y=300)

        #employe data information gender
        lbl_info=Label(self.root,text="Gender:",font="arial 13 bold",bg="white")
        lbl_info.place(x=365,y=340)

        #employe data information phone
        lbl_info=Label(self.root,text="Phone No:",font="arial 13 bold",bg="white")
        lbl_info.place(x=695,y=180)

        #employe data information country
        lbl_info=Label(self.root,text="Country:",font="arial 13 bold",bg="white")
        lbl_info.place(x=695,y=220)

        #employe data information salary ctc
        lbl_info=Label(self.root,text="Salary (CTC):",font="arial 13 bold",bg="white")
        lbl_info.place(x=695,y=260)


        #employe info Entry box of designition
        ent=Entry(self.root,textvariable=self.var_deginition,width=20,font=20,bg="#f0f8ff")
        ent.place(x=160,y=220)

         #employe info Entry box of address
        ent=Entry(self.root,textvariable=self.var_address,width=20,font=20,bg="#f0f8ff")
        ent.place(x=160,y=260)

        
         #employe info Entry box of date of birth
        ent=Entry(self.root,textvariable=self.var_dob,width=20,font=20,bg="#f0f8ff")
        ent.place(x=160,y=300)

        #employe info Entry box of id proof
        ent=Entry(self.root,textvariable=self.var_Id_prof_entry,width=20,font=20,bg="#f0f8ff")
        ent.place(x=160,y=340)

        #employe info Entry box of name
        ent=Entry(self.root,textvariable=self.var_name,width=20,font=20,bg="#f0f8ff")
        ent.place(x=500,y=180)

        #employe info Entry box of mail
        ent=Entry(self.root,textvariable=self.var_mail,width=20,font=20,bg="#f0f8ff")
        ent.place(x=500,y=220)

        #employe info Entry box of Date of joining
        ent=Entry(self.root,textvariable=self.var_doj,width=20,font=20,bg="#f0f8ff")
        ent.place(x=500,y=300)

        #employe info Entry box of  phone
        ent=Entry(self.root,textvariable=self.var_phone,width=20,font=20,bg="#f0f8ff")
        ent.place(x=810,y=180)

        #employe info Entry box of country
        ent=Entry(self.root,textvariable=self.var_country,width=20,font=20,bg="#f0f8ff")
        ent.place(x=810,y=220)

        #employe info Entry box of salary ctc
        ent=Entry(self.root,textvariable=self.var_salary,width=20,font=20,bg="#f0f8ff")
        ent.place(x=810,y=260)

        #employe info combo_box of department
        box=ttk.Combobox(self.root,textvariable=self.var_dep,width=27,values=["Select Department","Abid Motors","Abid Filling Station","Abasia Town"],state="readonly")
        box.place(x=160,y=180)
        box.current(0)

         #employe info combo_box of ID proff
        box=ttk.Combobox(self.root,textvariable=self.var_Id_prof_comb,width=15,values=["Select ID Proff","CNIC","pasport","Drivig licince"],state="readonly")
        box.place(x=30,y=340)
        box.current(0)

         #employe info combo_box of marid status
        box=ttk.Combobox(self.root,textvariable=self.var_married,width=27,values=["Select Option","Married","Un-Married"],state="readonly")
        box.place(x=500,y=260)
        box.current(0)

         #employe info combo_box of gender
        box=ttk.Combobox(self.root,textvariable=self.var_gndr,width=27,values=["Select Option","Male","Female"],state="readonly")
        box.place(x=500,y=340)
        box.current(0)

        #employe info button of save

        btn=Button(self.root,command=self.add_data,text="save",font="arial 14 bold",fg="white",bg="dark blue")
        btn.place(x=720,y=300,width=130)

         #employe info button of update

        btn=Button(self.root,command=self.up_date,text="Update",font="arial 14 bold",fg="white",bg="dark blue")
        btn.place(x=860,y=300,width=130)

        #employe info button of delete

        btn=Button(self.root,command=self.dlt,text="Delete",font="arial 14 bold",fg="white",bg="dark blue")
        btn.place(x=720,y=345,width=130)

        #employe info button of reset

        btn=Button(self.root,command=self.rst,text="Reset",font="arial 14 bold",fg="white",bg="dark blue")
        btn.place(x=860,y=345,width=130)

        #employe table frame


        #employe search lable

        Label(self.root,text="Search By:",font="arial 14 bold",fg="white",bg="red").place(x=50,y=420)

         #employe search info combo_box
        box=ttk.Combobox(self.root,textvariable=self.var_srch_comb,width=27,font="arial 10 bold",values=["Select Option ","Phone","Name"],state="readonly")
        box.place(x=200,y=420)
        box.current(0)

        #employe info table entry of search

        Entry(self.root,textvariable=self.var_srch_entry,width=25,font=20,bg="#f0f8ff").place(x=450,y=420)

         #employe info table search button of "search" or "show all"

         #search button
        btn=Button(self.root,command=self.search_data,text="Search",font="arial 13 bold",fg="white",bg="dark blue")
        btn.place(x=720,y=415,width=130)

          #show all button
        btn=Button(self.root,command=self.fetch_data,text="Show All",font="arial 13 bold",fg="white",bg="dark blue")
        btn.place(x=860,y=415,width=130)

        #================  Employe data table ================

           #employe save frame table
        table_frame=LabelFrame(self.root,bg="darkgreen",font="arial 10 bold")
        table_frame.place(x=20,y=465,width=1310,height=200)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employe_table=ttk.Treeview(table_frame,columns=("dep","nme","degi","mail","adrs","marid","dob","doj","id_prof_comb","idprof","gndr","phn","cntry","slry",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employe_table.xview)
        scroll_y.config(command=self.employe_table.yview)

        self.employe_table.heading('dep',text="Department")
        self.employe_table.heading('nme',text="Name")
        self.employe_table.heading('degi',text="Deginition")
        self.employe_table.heading('mail',text="E.mail")
        self.employe_table.heading('adrs',text="Address")
        self.employe_table.heading('marid',text="Married")
        self.employe_table.heading('dob',text="D-O-B")
        self.employe_table.heading('doj',text="D-O-J")
        self.employe_table.heading('id_prof_comb',text="ID-proff")
        self.employe_table.heading('idprof',text="ID-No")
        self.employe_table.heading('gndr',text="Gender")
        self.employe_table.heading('phn',text="Phone No")
        self.employe_table.heading('cntry',text="Country")
        self.employe_table.heading('slry',text="Salary")

        self.employe_table['show']='headings'
        self.employe_table.column("dep",width=100)
        self.employe_table.column("nme",width=100)
        self.employe_table.column("degi",width=100)
        self.employe_table.column("mail",width=100)
        self.employe_table.column("adrs",width=100)
        self.employe_table.column("marid",width=100)
        self.employe_table.column("dob",width=100)
        self.employe_table.column("doj",width=100)
        self.employe_table.column("id_prof_comb",width=100)
        self.employe_table.column("idprof",width=100)
        self.employe_table.column("gndr",width=100)
        self.employe_table.column("phn",width=100)
        self.employe_table.column("cntry",width=100)
        self.employe_table.column("slry",width=100)
        


        self.employe_table.pack(fill=BOTH,expand=1)
        self.employe_table.bind('<ButtonRelease>', self.get_query)

        self.fetch_data()     #calling for fetch data

##############################################################################################

#======================================Add Data Query=====================================

    def add_data(self):
      if(
        self.var_dep.get()=="Select Department"
        or self.var_name.get()==""
        or self.var_deginition.get()=="" 
        or self.var_mail.get()=="" 
        or self.var_address.get()=="" 
        or self.var_married.get()=="Select Option" 
        or self.var_dob.get()=="" 
        or self.var_doj.get()=="" 
        or self.var_Id_prof_comb.get()=="Select ID Proff"
        or self.var_Id_prof_entry.get()==""
        or self.var_gndr.get()=="Select Option" 
        or self.var_phone.get()=="" 
        or self.var_country.get()=="" 
        or self.var_salary.get()==""
      ):
        messagebox.showerror("Error","All Fields are Required",parent=self.root)
      else:

        try:

          con=mysql.connector.connect(host="localhost",username="root",password="h@Roon#123Abc",database="employe")
          cur=con.cursor()

          query = ("INSERT INTO new_table SET "
                   "department=%s, "
                   "name=%s, "
                   "deginition=%s, "
                   "Email=%s, "
                   "address=%s, "
                   "married=%s, "
                   "DOB=%s, "
                   "DOJ=%s,"
                   "ID_Type=%s, "
                   "ID_No=%s, "
                   "gender=%s, "
                   "phone=%s, "
                   "country=%s, "
                   "salary=%s")
          data = (
                self.var_dep.get(),
                self.var_name.get(),
                self.var_deginition.get(),
                self.var_mail.get(),
                self.var_address.get(),
                self.var_married.get(),
                self.var_dob.get(),
                self.var_doj.get(),
                self.var_Id_prof_comb.get(),
                self.var_Id_prof_entry.get(),
                self.var_gndr.get(),
                self.var_phone.get(),
                self.var_country.get(),
                self.var_salary.get(),
          )
          cur.execute(query, data)
          con.commit()
          self.fetch_data()
          con.close()

          messagebox.showinfo("Success","Employe details Add Successfilly",parent=self.root)
        except Exception as e:
          messagebox.showerror("Error",f"Error:{str(e)}")

######################################Fetch Data########################################
    def fetch_data(self):
        try:
            con = mysql.connector.connect(host="localhost", username="root", password="h@Roon#123Abc", database="employe")
            cur = con.cursor()
            cur.execute("SELECT * FROM new_table")
            data = cur.fetchall()
            self.employe_table.delete(*self.employe_table.get_children())

            if len(data) != 0:
                for i in data:
                    self.employe_table.insert("", END, values=i)

            con.close()
        except Exception as e:
          messagebox.showerror("Error",f"Error:{str(e)}")

##############################Get Function################################

    def get_query(self,event=""):
      cursor_focus=self.employe_table.focus()
      content=self.employe_table.item(cursor_focus)
      data1=content["values"]
      self.var_dep.set(data1[0])
      self.var_name.set(data1[1])
      self.var_deginition.set(data1[2])
      self.var_mail.set(data1[3])
      self.var_address.set(data1[4])
      self.var_married.set(data1[5])
      self.var_dob.set(data1[6])
      self.var_doj.set(data1[7])
      self.var_Id_prof_comb.set(data1[8])
      self.var_Id_prof_entry.set(data1[9])
      self.var_gndr.set(data1[10])
      self.var_phone.set(data1[11])
      self.var_country.set(data1[12])
      self.var_salary.set(data1[13])      
          
#==================================update function==============================          
          
    def up_date(self):
      if(
        self.var_dep.get()=="Select Department"
        or self.var_name.get()==""
        or self.var_deginition.get()=="" 
        or self.var_mail.get()=="" 
        or self.var_address.get()=="" 
        or self.var_married.get()=="Select Option" 
        or self.var_dob.get()=="" 
        or self.var_doj.get()=="" 
        or self.var_Id_prof_comb.get()=="Select ID Proff"
        or self.var_Id_prof_entry.get()==""
        or self.var_gndr.get()=="Select Option" 
        or self.var_phone.get()=="" 
        or self.var_country.get()=="" 
        or self.var_salary.get()==""
      ):
        messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
        try:
          updt=messagebox.askyesno("update","Do you want to update!!!",parent=self.root)
          if updt>0:
            con = mysql.connector.connect(host="localhost", username="root", password="h@Roon#123Abc", database="employe")
            cur = con.cursor()

            query= (
                    "UPDATE new_table SET "
                    "department=%s, "
                    "name=%s, "
                    "deginition=%s, "
                    "Email=%s, "
                    "address=%s, "
                    "married=%s, "
                    "DOB=%s, "
                    "DOJ=%s,"
                    "ID_Type=%s, "
                    "gender=%s, "
                    "phone=%s, "
                    "country=%s, "
                    "salary=%s"
                    "WHERE ID_No=%s"

                               )

            data= (
                  self.var_dep.get(),
                  self.var_name.get(),
                  self.var_deginition.get(),
                  self.var_mail.get(),
                  self.var_address.get(),
                  self.var_married.get(),
                  self.var_dob.get(),
                  self.var_doj.get(),
                  self.var_Id_prof_comb.get(),
                  self.var_gndr.get(),
                  self.var_phone.get(),
                  self.var_country.get(),
                  self.var_salary.get(),
                  self.var_Id_prof_entry.get()

            )

            cur.execute(query, data)
            con.commit()
            self.fetch_data()
            con.close()

            messagebox.showinfo("Success", "Employe details successfully updated",parent=self.root)

          else:
                          # If the user clicks 'No', do nothing
            return
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)





# ==================================Delete Function==============================

    def dlt(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_deginition.get() == ""
            or self.var_mail.get() == ""
            or self.var_address.get() == ""
            or self.var_married.get() == "Select Option"
            or self.var_dob.get() == ""
            or self.var_doj.get() == ""
            or self.var_Id_prof_comb.get() == "Select ID Proff"
            or self.var_Id_prof_entry.get() == ""
            or self.var_gndr.get() == "Select Option"
            or self.var_phone.get() == ""
            or self.var_country.get() == ""
            or self.var_salary.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                dlt1 = messagebox.askyesno("Result", "Do you want to delete",parent=self.root)
                if dlt1:
                    con = mysql.connector.connect(
                        host="localhost", username="root", password="h@Roon#123Abc", database="employe"
                    )
                    cur = con.cursor()

                    sql = "delete from new_table where ID_No=%s "
                    val = (self.var_Id_prof_entry.get(),)
                    cur.execute(sql, val)
                    con.commit()
                    con.close()
                    self.fetch_data()

                    messagebox.showinfo("Info", "Data Deleted Successfully",parent=self.root)

                else:
                    if not dlt1:
                        return

            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")


#==================================reset function===============================

    def rst(self):
      if(
        self.var_dep.get()=="Select Department"
        or self.var_name.get()==""
        or self.var_deginition.get()=="" 
        or self.var_mail.get()=="" 
        or self.var_address.get()=="" 
        or self.var_married.get()=="Select Option" 
        or self.var_dob.get()=="" 
        or self.var_doj.get()=="" 
        or self.var_Id_prof_comb.get()=="Select ID Proff"
        or self.var_Id_prof_entry.get()==""
        or self.var_gndr.get()=="Select Option" 
        or self.var_phone.get()=="" 
        or self.var_country.get()=="" 
        or self.var_salary.get()==""
      ):   
        messagebox.showerror("Error","All fields are required",parent=self.root)
      
      self.var_dep.set("Select Department")
      self.var_name.set("")
      self.var_deginition.set("") 
      self.var_mail.set("")
      self.var_address.set("") 
      self.var_married.set("Select Option") 
      self.var_dob.set("") 
      self.var_doj.set("") 
      self.var_Id_prof_comb.set("Select ID Proff")
      self.var_Id_prof_entry.set("")
      self.var_gndr.set("Select Option") 
      self.var_phone.set("") 
      self.var_country.set("") 
      self.var_salary.set("")


#===============================search query==========================
    def search_data(self):
        if self.var_srch_comb.get() == "Select Option" or self.var_srch_entry.get() == "":
            messagebox.showerror("Error", "Select valid search criteria and enter search value.",parent=self.root)
        else:
            try:
                con = mysql.connector.connect(
                    host="localhost", username="root", password="h@Roon#123Abc", database="employe"
                )
                cur = con.cursor()

                # Modify the SQL query based on the selected search criteria
                if self.var_srch_comb.get() == "Name":
                    query = "SELECT * FROM new_table WHERE name LIKE %s"
                elif self.var_srch_comb.get() == "Phone":
                    query = "SELECT * FROM new_table WHERE phone LIKE %s"

                search_value = f"%{self.var_srch_entry.get()}%"
                cur.execute(query, (search_value,))
                data = cur.fetchall()

                self.employe_table.delete(*self.employe_table.get_children())

                if len(data) != 0:
                    for i in data:
                        self.employe_table.insert("", END, values=i)

                con.close()

            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")





if __name__ == "__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()
    
