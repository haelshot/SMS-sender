from twilio.rest import Client
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import email, smtplib, ssl
import time
from lala import providers

def iExit():
    result = messagebox.askyesno('Notification', 'Do you want to quit?')
    if result:
        root.destroy()
def send_sms(
    number,
    message,
    sender_email,
    email_password,
    subject,
    smtp_server = "smtp.gmail.com",
    smtp_port = 465
    ):  
    prov = ["AT&T", "C-Spire", "Cricket Wireless", "Consumer Cellular", "Google Project Fi", "Metro PCS", "Mint Mobile", "Page Plus", "Republic Wireless", "Sprint", "Straight Talk", "T-Mobile", "Ting", "Tracfone", "U.S. Cellular", "Verizon", "Virgin Mobile", "Xfinity Mobile"]
    for num in number:
        for provider in prov:
            receiver_email = "{}@{}".format(number,providers.get(provider).get('sms'))
            email_message = "Subject:{}\nTo:{}\n{}".format(subject,receiver_email,message)
            with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
                email.login(sender_email, email_password)
                email.sendmail(sender_email, receiver_email, email_message)

def settings():
    root4 = Toplevel()
    root4.title('Settings')
    root4.geometry('780x620+100+50')
    root4.config(bg='light grey')
    
    emailFrame = LabelFrame(root4, text='Email Address', font=('new times roman', 16), bd=5, bg='light grey')
    emailFrame.grid(row=1, column=1)
    emailField = Entry(emailFrame, bd=0, width=40)
    emailField.grid(row=0, column=0, padx=100, pady=10)
    
    passFrame = LabelFrame(root4, text='Password', font=('new times roman', 16), bd=5, bg='light grey')
    passFrame.grid(row=2, column=1)
    passField = Entry(passFrame, bd=0, width=40, show='*')
    passField.grid(row=0, column=0, padx=100, pady=10)
    def sv():
        with open('credientials.txt', 'w') as f:
            f.write(emailField.get()+ ',' + passField.get() + ',')
            f.close()
    saveBtn = Button(root4, text='Save Credentials', activebackground='cyan', command=sv).place(x=610, y=540)
    root4.mainloop()
def homepage():
    root1 = Toplevel()
    root1.title('Home Page')
    root1.geometry('780x620+100+50')
    root1.config(bg='light grey')
    titleFrame = Frame(root1,bg='light grey')
    titleFrame.grid(row=0, column=0, padx=150, pady=20)

    titleLabel = Label(titleFrame, text='  NAS-Sender   ', image=logoImage, compound= LEFT, font=('Goudy old style', 25, 'bold'), bg='light grey')
    titleLabel.grid(row=0, column=0)
    
    Button(titleFrame,image=settingImage, bd=0, bg='white', cursor='hand2', activebackground='cyan', command=settings).grid(row=0, column=1)
    
    toLabelFrame = LabelFrame(root1, text='To (number)', font=('new times roman', 16), bd=5, bg='light grey')
    toLabelFrame.grid(row=2, column=0)

    toEntryField = Entry(toLabelFrame, bd=0, width=40)
    toEntryField.grid(row=0, column=0, padx=10, pady=10)
    totalLabel = Label(root1, font=('new times roman', 15), bg='light grey').place(x=10, y=560)
    sentLabel = Label(root1, font=('new times roman', 15), bg='light grey').place(x=100, y=560)
    def browse():
        toEntryField.config(state='readonly')
        path = filedialog.askopenfilename(title='Select number TXT file')
        if path=="":
            messagebox.showerror('Error', 'Please select a txt file')
        else:
            with open(path, 'r') as f:
                lines = f.readlines()
            aList = []
            for line in lines:
                if line != '':
                    aList.append(line[0:11])
            if len(aList) == 0:
                messagebox.showerror('Error', 'File does not have any numbers')
            else:
                toEntryField.config(state=NORMAL)
                toEntryField.insert(0, path)
                toEntryField.config(state='readonly')
        return aList
    browseButton = Button(toLabelFrame,text='Browse', image=browseImage, compound=LEFT, font=('arial', 12, 'bold'), height=35,cursor='hand2',bd=0, activebackground='cyan', command=browse).grid(row=0, column=1)
    
    toSubjectFrame = LabelFrame(root1, text='Subject', font=('new times roman', 16), bd=5, bg='light grey')
    toSubjectFrame.grid(row=3, column=0)
    
    subjectField = Entry(toSubjectFrame, bd=0, width=40)
    subjectField.grid(row=0, column=0, padx=10, pady=10)
    
    emailFrame = LabelFrame(root1, text='Compose Message', font=('new times roman', 16), bd=5, bg='light grey')
    emailFrame.grid(row=4, column=0, padx=30)
    
    emailField = Text(emailFrame, font=('new times roman', 12), height=10, width=65)
    emailField.grid(row=0, column=0,columnspan=2, padx=10, pady=10)
    
    def sendingSms():
        with open('/home/hael/Desktop/NasSMS/credientials.txt', 'r') as f:
            lines = f.read()
            lines = lines.split(',')
        if lines > 0:
            number = browse()
            send_sms(number, emailField.get(1.0, END), lines[0], lines[1], subjectField.get())
            time.sleep(30)
            messagebox.showinfo('Notification', 'Messages sent sucessfully')
        else:
            messagebox.showerror('Error', 'Please go to settings and add an email')
    
    sendButton = Button(root1,text='send', image=sendImage, compound=LEFT, font=('arial', 12, 'bold'), height=35,cursor='hand2',bd=0, activebackground='light grey', command=sendingSms).place(x=490, y=540)
    exitButton = Button(root1,text='exit', image=exitImage, compound=LEFT, font=('arial', 12, 'bold'), height=35,cursor='hand2',bd=0, activebackground='light grey', command=iExit).place(x=610, y=540)

    
    root1.mainloop()

def loginpage():
    titleFrame = Frame(root,bg='white')
    titleFrame.grid(row=0, column=0)

    titleLabel = Label(titleFrame, text='  Login/Signup   ',font=('Goudy old style', 25, 'bold'), bg='light grey')
    titleLabel.grid(row=0, column=0)
    
    loginFrame = Frame(root, bg='light grey')
    loginFrame.grid(row=2, column=0, pady=100, padx=100)
    
    loginLabel = Label(loginFrame, text='Login here', font=('new time roman', 20, 'bold'), bg='light grey')
    loginLabel.grid(row=0, column=0, pady=40, padx=40)
    signLabel = Label(loginFrame, text='SignUp here', font=('new times roman', 20, 'bold'), bg='light grey')
    signLabel.grid(row=0, column=1, pady=40, padx=40)
    
    userLogFrame = LabelFrame(loginFrame, text='username', font=('new times roman', 12), bd=5, bg='light grey')
    userLogFrame.grid(row=1, column=0)
    
    userlogField = Entry(userLogFrame, bd=0)
    userlogField.grid(row=0, column=0)
    
    userSignFrame = LabelFrame(loginFrame, text='username', font=('new times roman', 12), bd=5, bg='light grey')
    userSignFrame.grid(row=1, column=1)
    
    userSignField = Entry(userSignFrame, bd=0)
    userSignField.grid(row=0, column=0)
    
    passLogFrame = LabelFrame(loginFrame, text='password', font=('new times roman', 12), bd=5, bg='light grey')
    passLogFrame.grid(row=2, column=0)
    
    passlogField = Entry(passLogFrame, bd=0, show='*')
    passlogField.grid(row=0, column=0)
    
    passSignFrame = LabelFrame(loginFrame, text='password', font=('new times roman', 12), bd=5, bg='light grey')
    passSignFrame.grid(row=2, column=1)
    
    passSignField = Entry(passSignFrame, bd=0, show='*')
    passSignField.grid(row=0, column=0)
    limit = 4
    def checkpass():
        with open('/home/hael/Desktop/NasSMS/bin.txt') as f:
            lines = f.read()
            lines = lines.split(',')
        return lines
    lines = checkpass()
    def log():
        if len(lines) > 0:
            if userlogField.get() in lines and passlogField.get() in lines:
                selectSender()
            else:
                messagebox.showerror('Error', 'Incorrect Username or Password')
        else:
            messagebox.showerror('Error', 'Login Required')
    def save():
        if userSignField.get() == '' or passSignField.get() == '':
            messagebox.showerror('Error', 'Fill all fields')
        elif len(lines) <= limit:
            with open('bin.txt', 'a') as f:
                f.writelines(userSignField.get()+','+passSignField.get()+',')
                f.close()
                messagebox.showinfo('Infomation', 'Successfully Signed up')
            selectSender()
        else:
            messagebox.showerror('Error', 'Limit Exceeded, Login Your account')
    clickToLogin = Button(loginFrame, text='Click here to Login', font=('new times roman', 15), activebackground='cyan', command=log)
    clickToLogin.grid(row=3, column=0, pady=30, padx=40)
    
    clickTosign = Button(loginFrame, text='Click here to SignUp', font=('new times roman', 15), activebackground='cyan', command=save)
    clickTosign.grid(row=3, column=1, pady=30)
 
def twilio():
    root7 = Toplevel()
    root7.title('Home Page')
    root7.geometry('780x620+100+50')
    root7.config(bg='light grey')
    titleFrame = Frame(root7,bg='light grey')
    titleFrame.grid(row=0, column=0, padx=150, pady=20)

    titleLabel = Label(titleFrame, text='  NAS-Sender   ', image=logoImage, compound= LEFT, font=('Goudy old style', 25, 'bold'), bg='light grey')
    titleLabel.grid(row=0, column=0)
    def settingsT():
        root0 = Toplevel()
        root0.title('Settings')
        root0.geometry('780x620+100+50')
        root0.config(bg='light grey')    
        emailFrame = LabelFrame(root0, text='account sid', font=('new times roman', 16), bd=5, bg='light grey')
        emailFrame.grid(row=1, column=1)
        emailField = Entry(emailFrame, bd=0, width=40)
        emailField.grid(row=0, column=0, padx=100, pady=10)
       
        passFrame = LabelFrame(root0, text='authentication token', font=('new times roman', 16), bd=5, bg='light grey')
        passFrame.grid(row=2, column=1)
        passField = Entry(passFrame, bd=0, width=40)
        passField.grid(row=0, column=0, padx=100, pady=10)
        
        numFrame = LabelFrame(root0, text='Twilio Number', font=('new times roman', 16), bd=5, bg='light grey')
        numFrame.grid(row=3, column=1)
        numField = Entry(numFrame, bd=0, width=40)
        numField.grid(row=0, column=0, padx=100, pady=10)
        
        def svc():
            with open('twilio.txt', 'w') as f:
                f.write(emailField.get()+ ',' + passField.get() + ',' + numField.get() + ',')
                f.close()
        saveBtn = Button(root0, text='Save Credentials', activebackground='cyan', command=svc).place(x=610, y=540)
        root0.mainloop()
    Button(titleFrame,image=settingImage, bd=0, bg='white', cursor='hand2', activebackground='cyan', command=settingsT).grid(row=0, column=1)
    
    toLabelFrame = LabelFrame(root7, text='To (number)', font=('new times roman', 16), bd=5, bg='light grey')
    toLabelFrame.grid(row=2, column=0)

    toEntryField = Entry(toLabelFrame, bd=0, width=40)
    toEntryField.grid(row=0, column=0, padx=10, pady=10)

    def browse():
        toEntryField.config(state='readonly')
        path = filedialog.askopenfilename(title='Select number TXT file')
        if path=="":
            messagebox.showerror('Error', 'Please select a txt file')
        else:
            with open(path, 'r') as f:
                lines = f.readlines()
            aList = []
            for line in lines:
                if line != '':
                    aList.append(line[0:11])
            if len(aList) == 0:
                messagebox.showerror('Error', 'File does not have any numbers')
            else:
                toEntryField.config(state=NORMAL)
                toEntryField.insert(0, path)
                toEntryField.config(state='readonly')
        return aList
    emailFrame = LabelFrame(root7, text='Compose Message', font=('new times roman', 16), bd=5, bg='light grey')
    emailFrame.grid(row=4, column=0, padx=30)
    
    emailField = Text(emailFrame, font=('new times roman', 12), height=10, width=65)
    emailField.grid(row=0, column=0,columnspan=2, padx=10, pady=10)
    def sendTwilio():
        with open('/home/hael/Desktop/NasSMS/twilio.txt', 'r') as f:
            lines = f.read()
            lines = lines.split(',')
        if lines > 0:
            num = browse()
            account_sid = lines[0]
            auth_token = lines[1]
            client = Client(account_sid, auth_token)
            for number in num:
                message = client.messages.create(from_= lines[2],body =emailField.get(1.0, END),to = number)
            time.sleep(30)
            messagebox.showinfo('Notification', 'Message sent successfully')
        else:
            messagebox.showerror('Error', 'Please go to settings and add an email')
    browseButton = Button(toLabelFrame,text='Browse', image=browseImage, compound=LEFT, font=('arial', 12, 'bold'), height=35,cursor='hand2',bd=0, activebackground='cyan', command=browse).grid(row=0, column=1)

    sendButton = Button(root7,text='send', image=sendImage, compound=LEFT, font=('arial', 12, 'bold'), height=35,cursor='hand2',bd=0, activebackground='light grey', command=sendTwilio).place(x=490, y=540)
    exitButton = Button(root7,text='exit', image=exitImage, compound=LEFT, font=('arial', 12, 'bold'), height=35,cursor='hand2',bd=0, activebackground='light grey', command=iExit).place(x=610, y=540)

    root7.mainloop()
def selectSender(passwordCorrect=True):
    if passwordCorrect:
        root2 = Toplevel()
        root2.title('Home Page')
        root2.geometry('780x620+100+50')
        root2.config(bg='light grey')
        titleFrame = Frame(root2,bg='light grey')
        titleFrame.grid(row=0, column=0)

        titleLabel = Label(titleFrame, text='  NAS-Sender   ', image=logoImage, compound= LEFT, font=('Goudy old style', 25, 'bold'), bg='light grey')
        titleLabel.grid(row=0, column=0)

        selectFrame = Frame(root2)
        selectFrame.grid(row=1, column=0, pady=100, padx=280)

        selectLabel = Label(selectFrame, text='Select Sender', font=('new times roman', 20, 'bold')).grid(row=0, column=0)

        twilioButton = Button(selectFrame, text='Twilio', activebackground='cyan', command=twilio)
        twilioButton.grid(row=1, column=0, pady=60)

        gmailButton = Button(selectFrame, text='Gmail SMTP', activebackground='cyan', command=homepage)
        gmailButton.grid(row=2, column=0)
        root2.mainloop()
    else:
        messagebox.showinfo('Notification','Password Incorrect')

root = Tk()
root.title('Email Sender')
root.geometry('780x620+100+50')
root.config(bg='light grey')
browseImage = PhotoImage(file='/home/hael/Desktop/NasSMS/images/browse.png')
logoImage = PhotoImage(file='/home/hael/Desktop/NasSMS/images/Email_30017.png')
settingImage = PhotoImage(file='/home/hael/Desktop/NasSMS/images/settings.png')
sendImage = PhotoImage(file='/home/hael/Desktop/NasSMS/images/send.png')
exitImage = PhotoImage(file='/home/hael/Desktop/NasSMS/images/exit.png')
loginpage()
root.mainloop()