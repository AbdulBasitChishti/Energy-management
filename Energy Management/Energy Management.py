from tkinter import *
import re
from sqlite3 import *
import datetime

file = Tk()
file.title("Energy Management System")
file.geometry("1400x800")
frame = Frame(file,width=1400,height=200,bg='Black').place(x=0,y=250)
Label(frame,text="Welcome to Energy Management System",font=('Times New Roman',24,'bold'),bg='Black',fg='White').place(x=380,y=300)

global dmy
dmy = datetime.datetime.now()

con = connect("DB.db")
c = con.cursor()

c.execute("CREATE TABLE IF NOT EXISTS Electric_Consumer_Info\
                   (Reference_No TEXT,Name INT, Father_Name TEXT,CNIC TEXT,\
                   Mobile_Number TEXT,Address TEXT,Date TEXT)")

c.execute("CREATE TABLE IF NOT EXISTS Electric_bills(Reference_No TEXT,Current_Reading TEXT,Previous_Reading TEXT,Total_bill TEXT,Date TEXT)")

c.execute("CREATE TABLE IF NOT EXISTS Gas_Consumer_Info\
                  (Reference_No TEXT,Name INT, Father_Name TEXT,CNIC TEXT,\
                  Mobile_Number TEXT,Address TEXT,Date TEXT)")

c.execute("CREATE TABLE IF NOT EXISTS Gas_bills(Reference_No TEXT,Current_Reading TEXT,Previous_Reading TEXT,Total_bill TEXT,Date TEXT)")

def destroy():
    file.destroy()

def proceed_1():
    frame = Frame(file,width = 1400,height = 800).place(x=0,y=100)
    Label(frame,text="Enter reference no.",font=("Arial",16)).place(x=400,y=175)
    global entry_1
    entry_1 = Entry(frame)
    entry_1.place(x=550,y=180)
    Button(frame,text="Next",font=18,command=log_in_1).place(x=300,y=300)
    Button(frame,text='Quit',command=destroy,font=18,fg="red").place(x=370,y=300)
  
    
def proceed_2():
    frame = Frame(file,width = 1400,height = 800).place(x=0,y=100)
    Label(frame,text="Enter reference no.",font=("Arial",16)).place(x=35,y=250)
    global entry_1
    entry_1 = Entry(frame)
    entry_1.place(x=290,y=255)
    
    Button(frame,text="Next",font=18,command=log_in_2).place(x=300,y=300)
    Button(frame,text='Quit',command=destroy,font=18,fg="red").place(x=370,y=300)
    
    
def options_1():
    frame = Frame(file,height=800,width=1400).place(x=0,y=100)
    Button(file,text='Quit',command=destroy,font=18,fg='red').place(x=350,y=350)
    Label(frame,text="Enter reference no.",font=("Arial",16)).place(x=15,y=150)
    
    global entry_1
    entry_1 = Entry(frame)
    entry_1.place(x=260,y=155)
    
    Button(frame,text="Next",font=18,command=log_in_1).place(x=265,y=205)
    Label(frame,text="If don't have an account,Press",font=("Arial",14)).place(x=15,y=268)
    Button(frame,text="Sign Up",font=18,command=sign_up_1).place(x=300,y=265)
    
     
def options_2():
    frame = Frame(file,height=800,width=1400).place(x=0,y=100)
    Button(file,text='Quit',command=destroy,font=18,fg='red').place(x=350,y=350)
    Label(frame,text="Enter reference no.",font=("Arial",16)).place(x=15,y=150)
    
    global entry_1
    entry_1 = Entry(frame)
    entry_1.place(x=260,y=155)
    
    
    Button(frame,text="Next",font=18,command=log_in_2).place(x=265,y=205)
    Label(frame,text="If don't have an account,Press",font=("Arial",14)).place(x=15,y=268)
    Button(frame,text="Sign Up",font=18,command=sign_up_2).place(x=300,y=265)
    
    
def log_in_1():
    global reference_no
    reference_no = entry_1.get()
    c.execute("SELECT Reference_No FROM Electric_Consumer_Info WHERE Reference_No = ?",(reference_no,))
    if c.fetchone()==None:
        Label(file,text='Invalid Input',font=("Arial",16),fg='red').place(x=400,y=205)
    else:
        frame = Frame(file,height=800,width=1400).place(x=0,y=100)
        Label(frame,text="To proceed,Click",fg='blue',font=('Times New Roman',20)).place(x=270,y=250)
        Button(file,text="Log In",font=18,command=sign_in_1).place(x=430,y=310)
        
def log_in_2():
    global reference_no
    reference_no = entry_1.get()
    c.execute("SELECT Reference_No FROM Gas_Consumer_Info WHERE Reference_No = ?",(reference_no,))
    if c.fetchone()==None:
        Label(file,text='Invalid Input',font=("Arial",16),fg='red').place(x=400,y=205)
    else:
        frame = Frame(file,height=800,width=1400).place(x=0,y=100)
        Label(frame,text="To proceed,Click",fg='blue',font=('Times New Roman',20)).place(x=270,y=250)
        Button(file,text="Log In",font=18,command=sign_in_2).place(x=430,y=310)

def sign_in_1():
    frame = Frame(file,height=800,width=1400).place(x=0,y=100)
    
    Label(frame,text="Pre-reading",font=('Arial',16)).place(x=400,y=175)
    global pre_reading_entry
    pre_reading_entry = Entry(frame)
    pre_reading_entry.place(x=600,y=180)
    
    Label(frame,text="Current_reading",font=('Arial',16)).place(x=400,y=205)
    global current_reading_entry
    current_reading_entry = Entry(frame)
    current_reading_entry.place(x=600,y=210)

    Button(frame,text='Quit',command=destroy,fg='red',font=18).place(x=600,y=365)
    Button(frame,text="Next",font=18,command=calculations_1).place(x=600,y=300)
def sign_in_2():
    frame = Frame(file,height=800,width=1400).place(x=0,y=100)
    
    Label(frame,text="Pre-reading",font=('Arial',16)).place(x=400,y=175)
    global pre_reading_entry
    pre_reading_entry = Entry(frame)
    pre_reading_entry.place(x=600,y=180)
    
    Label(frame,text="Current_reading",font=('Arial',16)).place(x=400,y=205)
    global current_reading_entry
    current_reading_entry = Entry(frame)
    current_reading_entry.place(x=600,y=210)

    Button(frame,text='Quit',command=destroy,fg='red',font=18).place(x=600,y=365)
    Button(frame,text="Next",font=18,command=calculations_2).place(x=600,y=300)

def ref_no_1():
    frame = Frame(file,width=1400,height=800).place(x=0,y=100)
    ref_file = open("counter1.txt",'r')
    r = ref_file.readlines()
    ref_file.close()
    for i in r:
        ref = int(i)
        
        ref_file = open("counter1.txt",'w')
        global reference_no
        reference_no = ref+1
        ref_file.write(str(reference_no))
        ref_file.close()
        global dmy
        dmy = datetime.datetime.now()
        date = dmy.date
        month = dmy.month
        year = dmy.year
        
        
        c.execute("INSERT INTO Electric_Consumer_Info(Reference_No,Name,Father_Name,CNIC,Mobile_Number,Address,Date)\
                   VALUES({},'{}','{}','{}','{}','{}','{}')".format(reference_no,get_3,get_7,get_4,get_5,get_6,dmy))
        
        Label(frame,text='Your reference number is {}'.format(reference_no),font=("Arial",16),fg='green').place(x=100,y=250)

        Button(frame,text='Quit',command=destroy,font=18,fg='red').place(x=400,y=330)
        Button(frame,text="Log In",command=sign_in_1,font=18).place(x=290,y=330)
        
def ref_no_2():
    frame = Frame(file,width=1400,height=800).place(x=0,y=100)
    ref_file = open("counter2.txt",'r')
    r = ref_file.readlines()
    ref_file.close()
    for i in r:
        ref = int(i)
        
        ref_file = open("counter2.txt",'w')
        global reference_no
        reference_no = ref+1
        ref_file.write(str(reference_no))
        ref_file.close()
        
        
        
        c.execute("INSERT INTO Gas_Consumer_Info(Reference_No,Name,Father_Name,CNIC,Mobile_Number,Address,Date)\
                   VALUES({},'{}','{}','{}','{}','{}','{}')".format(reference_no,get_3,get_7,get_4,get_5,get_6,dmy))
        
        Label(frame,text='Your reference number is {}'.format(reference_no),font=("Arial",16),fg='green').place(x=100,y=250)
        Button(frame,text='Quit',command=destroy,font=18,fg='red').place(x=400,y=330)
        Button(frame,text="Log In",command=sign_in_2,font=18).place(x=290,y=330)
        
def sign_up_1():
    frame = Frame(file,height=800,width=1400).place(x=0,y=100)
    
    Label(frame,text="Enter your name",font=('Arial',16)).place(x=200,y=135)
    global entry_4
    entry_4 = Entry(frame)
    entry_4.place(x=720,y=140)

    Label(frame,text="Enter your father's name",font=('Arial',16)).place(x=200,y=165)
    global entry_8
    entry_8 = Entry(frame)
    entry_8.place(x=720,y=170)
    
    Label(frame,text="Enter your CNIC",font=('Arial',16)).place(x=200,y=195)
    global entry_5
    entry_5 = Entry(frame)
    entry_5.place(x=720,y=200)
    Label(frame,text="(without hyphen or space)",fg='blue',font=('Times New Roman',12)).place(x=380,y=198)
    
    Label(frame,text="Enter your mobile no",font=('Arial',16)).place(x=200,y=225)
    global entry_6
    entry_6 = Entry(frame)
    entry_6.place(x=720,y=230)
    Label(frame,text="(without hyphen or space)",fg='blue',font=('Times New Roman',12)).place(x=415,y=230)
    
    Label(frame,text="Enter your address",font=('Arial',16)).place(x=200,y=255)
    global entry_7
    entry_7 = Entry(frame)
    entry_7.place(x=720,y=260)
    Label(frame,text="")

    Button(frame,text='Quit',command=destroy,fg='red',font=18).place(x=750,y=435)  
    Button(frame,text="Submit",font=18,command=submit_1).place(x=750,y=365)
def sign_up_2():
    frame = Frame(file,height=800,width=1400).place(x=0,y=100)
    
    Label(frame,text="Enter your name",font=('Arial',16)).place(x=200,y=135)
    global entry_4
    entry_4 = Entry(frame)
    entry_4.place(x=720,y=140)

    Label(frame,text="Enter your father's name",font=('Arial',16)).place(x=200,y=165)
    global entry_8
    entry_8 = Entry(frame)
    entry_8.place(x=720,y=170)
    
    Label(frame,text="Enter your CNIC",font=('Arial',16)).place(x=200,y=195)
    global entry_5
    entry_5 = Entry(frame)
    entry_5.place(x=720,y=200)
    Label(frame,text="(without hyphen or space)",fg='blue',font=('Times New Roman',12)).place(x=380,y=198)

    Label(frame,text="Enter your mobile no",font=('Arial',16)).place(x=200,y=225)
    global entry_6
    entry_6 = Entry(frame)
    entry_6.place(x=720,y=230)
    Label(frame,text="(without hyphen or space)",fg='blue',font=('Times New Roman',12)).place(x=415,y=230)
    
    Label(frame,text="Enter your address",font=('Arial',16)).place(x=200,y=255)
    global entry_7
    entry_7 = Entry(frame)
    entry_7.place(x=720,y=260)

    Button(frame,text='Quit',command=destroy,fg='red',font=18).place(x=750,y=435)  
    Button(frame,text="Submit",font=18,command=submit_2).place(x=750,y=365)
    
def delete_entry():
    entry_4.delete(0,END)
    entry_5.delete(0,END)
    entry_6.delete(0,END)
    entry_7.delete(0,END)
    entry_8.delete(0,END)
    
def submit_1():
    
    global get_3
    get_3 = entry_4.get()
    global get_4
    get_4 = entry_5.get()
    global get_5
    get_5 = entry_6.get()
    global get_6
    get_6 = entry_7.get()
    global get_7
    get_7 = entry_8.get()
    counter_cnic = 0
    for num in get_4:
        counter_cnic+=1
    if counter_cnic == 13:
        counter_number = 0
        for numb in get_5:
            counter_number+=1
        if counter_number == 11:
            if get_4.isnumeric() == True: 
                    c.execute("SELECT CNIC FROM Electric_Consumer_Info WHERE CNIC = ?",(get_4,))
                    count = 0
                    if c.fetchone() != None:
                        count += 1

                    if count>0:
                        Label(file,text="You already have an account,Please log in",fg='blue',font=('Arial',16)).place(x=150,y=400)
                        delete_entry()
                        Button(file,text="Log In",command=proceed_1,font=16).place(x=370,y=445)
                        
                    elif c.fetchall() != None:
                        list1=get_3.split(' ')
                        g_3 = ''.join(str(e) for e in list1)
                        if g_3.isalpha() == True:          
                                    
                            list2=get_7.split(' ')
                            g_7 = ''.join(str(e) for e in list2)
                            if g_7.isalpha() == True:
                                
                                if get_5.isnumeric() == True:

                                    list3=get_6.split(' ')
                                    g_6 = ''.join(str(e) for e in list3)
                                    if g_6.isalnum() == True:
                                        frame = Frame(file,width=1400,height=800).place(x=0,y=100)
                                        Label(file,text="To get reference number,Click",fg='blue',font=("Arial",16)).place(x=180,y=260)
                                        Button(frame,text="Reference No.",command=ref_no_1,font=16).place(x=440,y=305)
                                        
                                    else:
                                        entry_7.delete(0,END)
                                        Label(file,text="\'Address\' should be Alpha_Numeric!",fg='red',font=("Arial",16)).place(x=300,y=360)

                                else:
                                    entry_6.delete(0,END)
                                    Label(file,text="\'Mobile No\'  consists  of Integers!",fg='red',font=("Arial",16)).place(x=300,y=360)
                            else:
                              entry_8.delete(0,END)
                              Label(file,text="Father name contains Characters!",fg='red',font=("Arial",16)).place(x=300,y=360)
                        else:
                           entry_4.delete(0,END)
                           Label(file,text="Your Name consists of Characters!",fg='red',font=("Arial",16)).place(x=300,y=360)
            else:
                entry_5.delete(0,END)
                Label(file,text="Your \'CNIC\' should consists of Integers!",fg='red',font=("Arial",16)).place(x=300,y=360)
        else:
            entry_6.delete(0,END)
            Label(file,text="\'Mobile No\' should be of length 11",fg='red',font=("Arial",16)).place(x=300,y=360)
    else:
        entry_5.delete(0,END)
        Label(file,text="Your \'CNIC\' should be of length 13",fg='red',font=("Arial",16)).place(x=300,y=360)


def submit_2():
    global get_3
    get_3 = entry_4.get()
    global get_4
    get_4 = entry_5.get()
    global get_5
    get_5 = entry_6.get()
    global get_6
    get_6 = entry_7.get()
    global get_7
    get_7 = entry_8.get()
    counter_cnic = 0
    for num in get_4:
        counter_cnic+=1
    if counter_cnic == 13:
        counter_number = 0
        for numb in get_5:
            counter_number+=1
        if counter_number == 11:
            if get_4.isnumeric() == True:
                    c.execute("SELECT CNIC FROM Electric_Consumer_Info WHERE CNIC = ?",(get_4,))
                    count = 0
                    if c.fetchone() != None:
                        count += 1

                    if count>0:
                        Label(file,text="You already have an account,Please log in",fg='blue',font=('Arial',16)).place(x=150,y=400)
                        delete_entry()
                        Button(file,text="Log In",command=proceed_1,font=16).place(x=370,y=445)
                        
                    elif c.fetchall() != None:
                        list1=get_3.split(' ')
                        g_3 = ''.join(str(e) for e in list1)
                        if g_3.isalpha() == True:          
                                    
                            list2=get_7.split(' ')
                            g_7 = ''.join(str(e) for e in list2)
                            if g_7.isalpha() == True:
                                
                                if get_5.isnumeric() == True:

                                    list3=get_6.split(' ')
                                    g_6 = ''.join(str(e) for e in list3)
                                    if g_6.isalnum() == True:
                                        frame = Frame(file,width=1400,height=800).place(x=0,y=100)
                                        Label(file,text="To get reference number,Click",fg='blue',font=("Arial",16)).place(x=180,y=260)
                                        Button(frame,text="Reference No.",command=ref_no_2,font=16).place(x=440,y=305)
                                        
                                    else:
                                        entry_7.delete(0,END)
                                        Label(file,text="\'Address\' should be Alpha_Numeric!",fg='red',font=("Arial",16)).place(x=300,y=360)

                                else:
                                    entry_6.delete(0,END)
                                    Label(file,text="\'Mobile No\'  consists  of Integers!",fg='red',font=("Arial",16)).place(x=300,y=360)
                            else:
                              entry_8.delete(0,END)
                              Label(file,text="Father name contains Characters!",fg='red',font=("Arial",16)).place(x=300,y=360)
                        else:
                           entry_4.delete(0,END)
                           Label(file,text="Your Name consists of Characters!",fg='red',font=("Arial",16)).place(x=300,y=360)
            else:
                entry_5.delete(0,END)
                Label(file,text="Your \'CNIC\' should consists of Integers!",fg='red',font=("Arial",16)).place(x=300,y=360)
        else:
            entry_6.delete(0,END)
            Label(file,text="\'Mobile No\' should be of length 11",fg='red',font=("Arial",16)).place(x=300,y=360)
    else:
        entry_5.delete(0,END)
        Label(file,text="Your \'CNIC\' should be of length 13",fg='red',font=("Arial",16)).place(x=300,y=360)
        
def calculations_1():
    frame = Frame(file,height=800,width=1400).place(x=0,y=100)
    global get_pre_reading
    global get_current_reading

    get_pre_reading = pre_reading_entry.get()
    get_current_reading = current_reading_entry.get()
    
    if get_pre_reading.isnumeric() and get_current_reading.isnumeric():
        global units
        units = int(get_current_reading)-int(get_pre_reading)

            
        global bill
        if 0<=units<=50:
            bill = units * 4.00
            bill = round(bill)
            Label(frame,text="To print the bill,Click ",font=("Arial",16),fg='blue').place(x=200,y=260)
            Button(frame,text = "Print Bill",font=18,command=net_1).place(x=420,y=305)
        elif 51<=units<=100:
            bill = units * 9.25
            bill = round(bill)
            Label(frame,text="To print the bill,Click ",font=("Arial",16),fg='blue').place(x=200,y=260)
            Button(frame,text = "Print Bill",font=18,command=net_1).place(x=420,y=305)
        elif 101<=units<=200:
            bill = units * 11.32
            bill = round(bill)
            
            Label(frame,text="To print the bill,Click ",font=("Arial",16),fg='blue').place(x=200,y=260)
            Button(frame,text = "Print Bill",font=18,command=net_1).place(x=420,y=305)
        elif 201<=units<=300:
            bill = units * 12.33
            bill = round(bill)
            
            Label(frame,text="To print the bill,Click ",font=("Arial",16),fg='blue').place(x=200,y=260)
            Button(frame,text = "Print Bill",font=18,command=net_1).place(x=420,y=305)
        elif 301<=units<=700:
            bill = units * 14.08
            bill = round(bill)
            Label(frame,text="To print the bill,Click ",font=("Arial",16),fg='blue').place(x=200,y=260)
            Button(frame,text = "Print Bill",font=18,command=net_1).place(x=420,y=305)
        elif units>700:
            bill = units * 16.04
            bill = round(bill)
            
            Label(frame,text="To print the bill,Click ",font=("Arial",16),fg='blue').place(x=200,y=260)
            Button(frame,text = "Print Bill",font=18,command=net_1).place(x=420,y=305)
        else:
            Label(frame,text = "Invalid Input",fg="red",font=('arial',16,'bold')).place(x=300,y=400)
    else:
        pre_reading_entry.delete(0,END)
        current_reading_entry.delete(0,END)
        Label(frame,text="Invalid Input",font=("Arial",16),fg="Red").place(x=300,y=400)
   
def calculations_2():
    frame = Frame(file,height=800,width=1400).place(x=0,y=100)
    global get_pre_reading
    global get_current_reading
    get_pre_reading = pre_reading_entry.get()
    get_current_reading = current_reading_entry.get()
    
    

    if get_pre_reading.isnumeric() and get_current_reading.isnumeric():
        global units
        units = int(get_current_reading)-int(get_pre_reading)

        global bill
        if 0<=units<=50:
            bill = units * 4.00
            bill = round(bill)
            Label(frame,text="To print the bill,Click ",font=("Arial",20),fg='blue').place(x=200,y=260)
            Button(frame,text = "Print Bill",font=18,command=net_2).place(x=420,y=305)
        elif 51<=units<=100:
            bill = units * 9.25
            bill = round(bill)

            Label(frame,text="To print the bill,Click ",font=("Arial",16),fg='blue').place(x=200,y=260)
            Button(frame,text = "Print Bill",font=18,command=net_2).place(x=420,y=305)
        elif 101<=units<=200:
            bill = units * 11.32
            bill = round(bill)

            Label(frame,text="To print the bill,Click ",font=("Arial",16),fg='blue').place(x=200,y=260)
            Button(frame,text = "Print Bill",font=18,command=net_2).place(x=420,y=305)
        elif 201<=units<=300:
            bill = units * 12.33
            bill = round(bill)

            Label(frame,text="To print the bill,Click ",font=("Arial",16),fg='blue').place(x=200,y=260)
            Button(frame,text = "Print Bill",font=18,command=net_2).place(x=420,y=305)
        elif 301<=units<=700:
            bill = units * 14.08
            bill = round(bill)

            Label(frame,text="To print the bill,Click ",font=("Arial",16),fg='blue').place(x=200,y=260)
            Button(frame,text = "Print Bill",font=18,command=net_2).place(x=420,y=305)
        elif units>700:
            bill = units * 16.04
            bill = round(bill)
            Label(frame,text="To print the bill,Click ",font=("Arial",16),fg='blue').place(x=200,y=260)
            Button(frame,text = "Print Bill",font=18,command=net_2).place(x=420,y=305)
        else:
            Label(frame,text = "Invalid Input",fg="red",font=('arial',16,'bold')).place(x=300,y=400)
    else:
        pre_reading_entry.delete(0,END)
        current_reading_entry.delete(0,END)
        Label(frame,text="Invalid Input",font=("Arial",16),fg="Red").place(x=300,y=400)
        
def net_1():
    frame = Frame(file,height=800,width=1400).place(x=0,y=100)
    global net_tax
    global net_bill
    if bill<=500:
        net_tax = 0
        net_bill = bill+net_tax
    elif 500<bill<=3000:
        tax = 4/100*bill
        net_tax = round(tax)
        net_bill = bill+net_tax
    elif 3000<bill<=10000:
        tax = 9/100*bill
        net_tax = round(tax)
        net_bill = bill+net_tax
    elif 10000<bill<=30000:
        tax = 18/100*bill
        net_tax = round(tax)
        net_bill = bill+net_tax
    else:
        tax = 25/100*bill
        net_tax = round(tax)
        net_bill = bill+net_tax
    c.execute("INSERT INTO Electric_bills VALUES({},{},{},{},'{}')".format(reference_no,get_pre_reading,get_current_reading,net_bill,dmy))
    Label(file,text = ("Reference No = {}".format(reference_no)),fg='blue',font=("Arial",16,'bold')).place(x=470,y=150)
    Label(file,text = ("Units Consumed = {}".format(units)),fg='blue',font=("Arial",16,'bold')).place(x=470,y=190)
    Label(file,text = ("Gross Bill = Rs.{}".format(bill)),fg='blue',font=("Arial",16,'bold')).place(x=470,y=230)
    Label(file,text = ("Tax = Rs.{}".format(net_tax)),fg="blue",font=('arial',16,'bold')).place(x=470,y=270)
    Label(file,text = ("Net Bill = Rs.{}".format(net_bill)),fg="blue",font=('arial',16,'bold')).place(x=470,y=310)
    Label(file,text = ("Follow the following instructions to save energy and reduce bill:"),fg="red",font=('arial',16,'bold')).place(x=15,y=450)
    Label(file,text = ("1. Turn off lights when not in use and prefer natral light during day time."),fg="red",font=('arial',16,'bold')).place(x=50,y=480)
    Label(file,text = ("2. Use energy saver (15W,225W) rather than ordinary light bulb."),fg="red",font=('arial',16,'bold')).place(x=50,y=510)
    Label(file,text = ("3. Do no use heavy loads in the high energy consumption hours, from 6 PM to 10 PM."),fg="red",font=('arial',16,'bold')).place(x=50,y=540)
    Label(file,text = ("4. Use electric heaters and geezers only when required."),fg="red",font=('arial',16,'bold')).place(x=50,y=570)
    Label(file,text = ("5. Run air conditioners at optimum temperature (26 Degree)."),fg="red",font=('arial',16,'bold')).place(x=50,y=600)
    Label(file,text = ("6. Insulate the roofs instead of using cooling devices."),fg="red",font=('arial',16,'bold')).place(x=50,y=630)
    Button(frame,text='Quit',command=destroy,font=18,fg='Red').place(x=550,y=360)

    
def net_2():
    frame = Frame(file,height=800,width=1400).place(x=0,y=100)
    global net_tax
    global net_bill
    if bill<=1000:
        net_tax = 0
        net_bill = bill+net_tax
        
    elif 1000<bill<=5000:
        tax = 5/100*bill
        net_tax = round(tax)
        net_bill = bill+net_tax
       
    elif 5000<bill<=20000:
        tax = 10/100*bill
        net_tax = round(tax)
        net_bill = bill+net_tax
        
    elif 20000<bill<=50000:
        tax = 18/100*bill
        net_tax = round(tax)
        net_bill = bill+net_tax
        
    else:
        tax = 22/100*bill
        net_tax = round(tax)
        net_bill = bill+net_tax
    
    c.execute("INSERT INTO Gas_bills VALUES({},{},{},{},'{}')".format(reference_no,get_pre_reading,get_current_reading,net_bill,dmy))    
    Label(file,text = ("Reference No = {}".format(reference_no)),fg='blue',font=("Arial",16,'bold')).place(x=470,y=150)
    Label(file,text = ("Units Consumed = {}".format(units)),fg='blue',font=("Arial",16,'bold')).place(x=470,y=190)
    Label(file,text = ("Gross Bill = Rs.{}".format(bill)),fg='blue',font=("Arial",16,'bold')).place(x=470,y=230)
    Label(file,text = ("Tax = Rs.{}".format(net_tax)),fg="blue",font=('arial',16,'bold')).place(x=470,y=270)
    Label(file,text = ("Net Bill = Rs.{}".format(net_bill)),fg="blue",font=('arial',16,'bold')).place(x=470,y=310)
    Label(file,text = ("Follow the following instructions to save energy and reduce bill:"),fg="red",font=('arial',16,'bold')).place(x=15,y=450)
    Label(file,text = ("1. Turn off lights when not in use and prefer natral light during day time."),fg="red",font=('arial',16,'bold')).place(x=50,y=480)
    Label(file,text = ("2. Use energy saver (15W,225W) rather than ordinary light bulb."),fg="red",font=('arial',16,'bold')).place(x=50,y=510)
    Label(file,text = ("3. Do no use heavy loads in the high energy consumption hours, from 6 PM to 10 PM."),fg="red",font=('arial',16,'bold')).place(x=50,y=540)
    Label(file,text = ("4. Use electric heaters and geezers only when required."),fg="red",font=('arial',16,'bold')).place(x=50,y=570)
    Label(file,text = ("5. Run air conditioners at optimum temperature (26 Degree)."),fg="red",font=('arial',16,'bold')).place(x=50,y=600)
    Label(file,text = ("6. Insulate the roofs instead of using cooling devices."),fg="red",font=('arial',16,'bold')).place(x=50,y=630)
    Button(frame,text='Quit',command=destroy,font=18,fg='Red').place(x=550,y=360)
def func():
    frame_1 = Frame(file,width = 1400,height = 200,bg='Black').place(x=0,y=0)
    frame_2 = Frame(frame_1,width=1400,height=800).place(x=0,y=100)
    Label(frame_2,text="Energy Management System",font=('Times New Roman',24,'bold'),bg='Black',fg='White').place(x=480,y=40)
    Label(frame_2,text="Which bill do you want to check?",fg='Blue',font=("Arial",16)).place(x=45,y=200)
    Button(frame_2,text='Quit',command=destroy,font=18,fg='Red').place(x=350,y=390)
    Button(frame_2,text="Electricity",command=options_1,font=18).place(x=250,y=280)
    Button(frame_2,text="Gas",command=options_2,font=18).place(x=400,y=280)
button = Button(frame,text='Continue',command=func,font=18).place(x=600,y=400)    
file.mainloop()

con.commit()
con.close()

