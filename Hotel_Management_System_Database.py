import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
from time import strftime
from tkinter import ttk
import mysql.connector
import os
import openpyxl

obj = tk.Tk()

#   #CDEFDF
#   #DFB6B2
#   #FBE4D8
#   #8FB6B2


obj.title("Management")
obj.geometry("800x550+300+100")
obj.config(background="#CDEFDF")
obj.resizable(0, 0)
main_fr = Frame(obj, )
main_fr.config(background="#CDEFDF")

drink = 20
burger = 100
cherry = 10
nachos = 50
pizza = 150
biscuit = 5
roll = 15
tea = 10

head_frame = Frame(main_fr, background="#CDEFDF")

# ---------------------------------------------------------------------------------

heading_label_1 = Label(head_frame, text="Hotel Sanket", font=('arial', 30), fg="black", background="#CDEFDF")
heading_label_1.pack()
heading_label_2 = Label(head_frame, text="Management", font=('arial', 15), fg="black", background="#CDEFDF")
heading_label_2.pack(pady=5)
head_frame.grid(row=0, column=0, columnspan=2)

# ---------------------------------------------------------------------------------


label_frame_1 = LabelFrame(main_fr, borderwidth=6, bg="cyan", pady=15, background="#A6C3CE")

# drink label and entry
drink_label = Label(label_frame_1, text="Drink", bg="#A6C3CE", font=('arial', 12, 'bold'))
drink_label.grid(row=0, column=0, sticky='w', pady=5)
dr_var = IntVar()
drink_entry = Entry(label_frame_1, borderwidth=4, width=20, textvariable=dr_var)
drink_entry.grid(row=0, column=1, pady=5, padx=10)

# burger king label and entry
burger_label = Label(label_frame_1, text="Burger King", bg="#A6C3CE", font=('arial', 12, 'bold'))
burger_label.grid(row=1, column=0, sticky='w', pady=5)
br_var = IntVar()
burger_entry = Entry(label_frame_1, borderwidth=4, width=20, textvariable=br_var)
burger_entry.grid(row=1, column=1, pady=5, padx=10)

# cherry Label and entry
cherry_label = Label(label_frame_1, text="Cherry", bg="#A6C3CE", font=('arial', 12, 'bold'))
cherry_label.grid(row=2, column=0, sticky='w', pady=5)
ch_var = IntVar()
cherry_entry = Entry(label_frame_1, borderwidth=4, width=20, textvariable=ch_var)
cherry_entry.grid(row=2, column=1, pady=5, padx=10)

# nacho fries label and entry

nacho_fries_label = Label(label_frame_1, text="Nacho Fries", bg="#A6C3CE", font=('arial', 12, 'bold'))
nacho_fries_label.grid(row=3, column=0, sticky='w', pady=5)
nf_var = IntVar()
nacho_fries_entry = Entry(label_frame_1, borderwidth=4, width=20, textvariable=nf_var)
nacho_fries_entry.grid(row=3, column=1, pady=5, padx=10)

# pizza label and entry
pizza_label = Label(label_frame_1, text="Pizza", bg="#A6C3CE", font=('arial', 12, 'bold'))
pizza_label.grid(row=4, column=0, sticky='w', pady=5)
pz_var = IntVar()
pizza_entry = Entry(label_frame_1, borderwidth=4, width=20, textvariable=pz_var)
pizza_entry.grid(row=4, column=1, pady=5, padx=10)

# Biscuit label and entry
biscuit_label = Label(label_frame_1, text="Biscuit", bg="#A6C3CE", font=('arial', 12, 'bold'))
biscuit_label.grid(row=5, column=0, sticky='w', pady=5)
b_var = IntVar()
biscuit_entry = Entry(label_frame_1, borderwidth=4, width=20, textvariable=b_var)
biscuit_entry.grid(row=5, column=1, pady=5, padx=10)

# roll Label and entry

roll_label = Label(label_frame_1, text="Roll", bg="#A6C3CE", font=('arial', 12, 'bold'))
roll_label.grid(row=6, column=0, sticky='w', pady=5)
r_var = IntVar()
roll_entry = Entry(label_frame_1, borderwidth=4, width=20, textvariable=r_var)
roll_entry.grid(row=6, column=1, pady=5, padx=10)

# tea label and entry

tea_label = Label(label_frame_1, text="Tea", bg="#A6C3CE", font=('arial', 12, 'bold'))
tea_label.grid(row=7, column=0, sticky='w', pady=5)
t_var = IntVar()
tea_entry = Entry(label_frame_1, borderwidth=4, width=20, textvariable=t_var)
tea_entry.grid(row=7, column=1, pady=5, padx=10)

label_frame_1.grid(row=1, column=0, sticky="NS", padx=5)

# -----------------------------------------------------------------------------------------------


label_frame_2 = LabelFrame(main_fr, height=20, width=12, borderwidth=6, bg="#8FB8CA")

# order number Label
order_no_label = Label(label_frame_2, text="Order Number :", bg="#8FB8CA", font=('arial', 12, 'bold'), fg="black")
order_no_label.grid(row=0, column=0, sticky='w', pady=5)

order_no_b_label = Label(label_frame_2, bg="#8FB8CA", width=10, font=('arial', 12, 'bold'), fg="black")
order_no_b_label.grid(row=0, column=1, sticky="W", pady=5)

# Cost Label
cost_label = Label(label_frame_2, text="Cost :", bg="#8FB8CA", font=('arial', 12, 'bold'), fg="black")
cost_label.grid(row=1, column=0, sticky='w', pady=5)
cost_b_label = Label(label_frame_2, bg="#8FB8CA", width=10, font=('arial', 12, 'bold'), fg="black")
cost_b_label.grid(row=1, column=1, pady=5)

# service cost Label
service_cost_label = Label(label_frame_2, text="Service Cost :", bg="#8FB8CA", font=('arial', 12, 'bold'), fg="black")
service_cost_label.grid(row=2, column=0, sticky='w', pady=5)
service_cost_b_label = Label(label_frame_2, bg="#8FB8CA", width=10, font=('arial', 12, 'bold'), fg="black")
service_cost_b_label.grid(row=2, column=1, pady=5)

# tax Label
tax_label = Label(label_frame_2, text="Tax :", bg="#8FB8CA", font=('arial', 12, 'bold'), fg="black")
tax_label.grid(row=3, column=0, sticky='w', pady=5)
tax_b_label = Label(label_frame_2, bg="#8FB8CA", width=10, font=('arial', 12, 'bold'), fg="black")
tax_b_label.grid(row=3, column=1, pady=5)

# sub total label

sub_total_label = Label(label_frame_2, text="Sub Total :", bg="#8FB8CA", font=('arial', 12, 'bold'), fg="black")
sub_total_label.grid(row=4, column=0, sticky='w', pady=5)
sub_total_b_label = Label(label_frame_2, bg="#8FB8CA", width=10, font=('arial', 12, 'bold'), fg="black")
sub_total_b_label.grid(row=4, column=1, pady=5)

# total number Label
total_label = Label(label_frame_2, text="Total :", bg="#8FB8CA", font=('arial', 12, 'bold'), fg="black")
total_label.grid(row=5, column=0, sticky='w', pady=5)
total_b_label = Label(label_frame_2, bg="#8FB8CA", width=10, font=('arial', 12, 'bold'), fg="black")
total_b_label.grid(row=5, column=1, sticky='e', pady=5)

label_frame_2.grid(row=1, column=1, sticky="NS", padx=5)

# ---------------------------------------------------------------------------------------
label_frame_3 = LabelFrame(main_fr, borderwidth=6, bg="#294D61", padx=5)


def on_click_price():
    obj1 = tk.Tk()
    obj1.geometry("200x300")
    Label(obj1, text="Drink  : 20 ").pack()
    Label(obj1, text="Burger King : 100 ").pack()
    Label(obj1, text="Cherry : 10 ").pack()
    Label(obj1, text="Nachho Fries : 50 ").pack()
    Label(obj1, text="Biscuit : 5 ").pack()
    Label(obj1, text="Tea : 10 ").pack()
    Label(obj1, text="Roll : 15 ").pack()
    obj1.mainloop()


r_num = ""


def randm():
    global r_num
    for i in range(4):
        a = random.randint(1, 9)
        r_num = r_num + str(a)


def on_total():
    global to_cost
    randm()
    order_no_b_label.config(text=r_num)

    to_cost = (dr_var.get() * drink) + (br_var.get() * burger) + (ch_var.get() * cherry) \
              + (nf_var.get() * nachos) + (pz_var.get() * pizza) + (b_var.get() * biscuit) \
              + (r_var.get() * roll) + (t_var.get() * tea)
    cost_b_label.config(text=to_cost)

    ser_cost = to_cost * 0.02
    service_cost_b_label.config(text=ser_cost)

    tax_val = to_cost * 0.18
    tax_b_label.config(text=tax_val)

    sub_total = to_cost + ser_cost
    sub_total_b_label.config(text=sub_total)

    total_val = sub_total + tax_val
    total_b_label.config(text=total_val)


def on_click_reset():
    global r_num
    t_var.set(0)
    r_var.set(0)
    b_var.set(0)
    pz_var.set(0)
    nf_var.set(0)
    ch_var.set(0)
    br_var.set(0)
    dr_var.set(0)
    order_no_b_label.config(text="")
    cost_b_label.config(text="")
    service_cost_b_label.config(text="")
    tax_b_label.config(text="")
    service_cost_b_label.config(text="")
    sub_total_b_label.config(text="")
    total_b_label.config(text="")
    r_num = ""


def on_bill():
    global dr_var, br_var, ch_var, nf_var, pz_var, b_var, r_var, t_var, r_num
    to_cost = (dr_var.get() * drink) + (br_var.get() * burger) + (ch_var.get() * cherry) \
              + (nf_var.get() * nachos) + (pz_var.get() * pizza) + (b_var.get() * biscuit) \
              + (r_var.get() * roll) + (t_var.get() * tea)
    ser_cost = to_cost * 0.02
    tax_val = to_cost * 0.18
    tax_val = round(tax_val, 2)
    sub_total = to_cost + ser_cost
    total_val = sub_total + tax_val
    obj2 = Toplevel(obj)
    # obj2.geometry("800x600+300+100")
    obj2.title("Bill Area")

    billframe = Frame(obj2, bd=8, relief=GROOVE, background="white")
    billframe.pack()

    billlabel = Label(billframe, text="Bill Area", font=('times new roman', 15, 'bold'), bd=8, relief=GROOVE)
    billlabel.pack(fill=X)
    textarea = Text(billframe, width=50)  # yscrollcommand=scrollbar.set)

    textarea.insert(END, "\t\t    HOTEL SANKET\n")
    textarea.insert(END, "\t\tAdress:Lorem ispum,23-10\n")
    textarea.insert(END, "\t \t   Telp. 11223344\n")
    textarea.insert(END, "**************************************************\n")
    textarea.insert(END, "\t\t  CASH RECIEPT\n")
    textarea.insert(END, "**************************************************\n")
    textarea.insert(END, f"INVOICE NO:{r_num}\n")
    textarea.insert(END, "ITEMS\t\tQUANTITY\t\tPRICE\t   TOTAL\n")
    textarea.insert(END, "==================================================\n")
    if drink_entry.get() != '0':
        textarea.insert(END, f"Drink\t\t  {drink_entry.get()}\t\t{drink}\t   {dr_var.get() * drink} Rs\n")
    if burger_entry.get() != '0':
        textarea.insert(END, f"Burger\t\t  {burger_entry.get()}\t\t{burger}\t   {br_var.get() * burger} Rs\n")
    if cherry_entry.get() != '0':
        textarea.insert(END, f"Cherry\t\t  {cherry_entry.get()}\t\t{cherry}\t   {ch_var.get() * cherry} Rs\n")
    if nacho_fries_entry.get() != '0':
        textarea.insert(END, f"Nacho Fries\t\t  {nacho_fries_entry.get()}\t\t{nachos}\t   {nf_var.get() * nachos} Rs\n")
    if pizza_entry.get() != '0':
        textarea.insert(END, f"Pizza\t\t  {pizza_entry.get()}\t\t{pizza}\t   {pz_var.get() * pizza} Rs\n")
    if biscuit_entry.get() != '0':
        textarea.insert(END, f"Biscuit\t\t  {biscuit_entry.get()}\t\t{biscuit}\t   {b_var.get() * biscuit} Rs\n")
    if roll_entry.get() != '0':
        textarea.insert(END, f"Roll\t\t  {roll_entry.get()}\t\t{roll}\t   {r_var.get() * roll} Rs\n")
    if tea_entry.get() != '0':
        textarea.insert(END, f"Tea\t\t  {tea_entry.get()}\t\t{tea}\t   {t_var.get() * tea} Rs\n")

    textarea.insert(END, "==================================================\n")
    textarea.insert(END, f"Service Cost\t\t{ser_cost}\n")
    textarea.insert(END, f"Tax Value\t\t{tax_val}\n")
    textarea.insert(END, f"Sub Total\t\t{sub_total}\n")
    textarea.insert(END, "==================================================\n")
    textarea.insert(END, f"GROSS TOTAL : \t\t\t\t\t{total_val}\n")
    if total_val == 0.0:
        messagebox.showerror("Error", "Add At least 1 item to Generate Bill ")
        obj2.destroy()

    textarea.pack()
    if not os.path.exists('bills'):
        os.mkdir('bills')

    def sv_pr():
        bill = textarea.get(1.0, END)
        with open(f'bills/{r_num}.txt', "w") as f:
            f.write(bill)
            messagebox.showinfo("Sucess", f"Bill {r_num} saved sucessfilly")
            randm()
            obj2.after(2000, lambda: obj2.destroy())

    sv_pr_btn = Button(billframe, text="Save&Print", width=10, bd=5, command=sv_pr)
    sv_pr_btn.pack()
    obj2.mainloop()


# price button
price_button = Button(label_frame_3, text="Price", borderwidth=5, padx=8, pady=6, command=on_click_price,
                      font=('arial', 12, 'bold'))
price_button.grid(row=0, column=0, padx=20, pady=10)

# total button
total_button = Button(label_frame_3, text="Total", borderwidth=5, padx=8, pady=6, command=on_total,
                      font=('arial', 12, 'bold'))
total_button.grid(row=0, column=1, padx=15)
# reset button

reset_button = Button(label_frame_3, text="Reset", borderwidth=5, padx=5, pady=6, font=('arial', 12, 'bold'),
                      command=on_click_reset)
reset_button.grid(row=0, column=2, padx=15)

bill_button = Button(label_frame_3, text="Bill", borderwidth=5, padx=8, pady=6, font=('arial', 12, 'bold'),
                     command=on_bill)
bill_button.grid(row=0, column=3, padx=15)

# quit button
quit_button = Button(label_frame_3, text="Quit", borderwidth=5, padx=8, pady=6, command=lambda: obj.destroy(),
                     font=('arial', 12, 'bold'))
quit_button.grid(row=0, column=4, padx=20)

label_frame_3.grid(row=2, column=0, columnspan=2, sticky="WE", pady=10, padx=5)

# --------------------------------------------------------------------------------------------------

frame_4 = Frame(main_fr, bg="#CDEFDF")
# ----------------------------------------------------
clock_frame = Frame(frame_4, bd=5, bg="#CDEFDF")

clock_label = Label(frame_4, bg="black", fg="red", font=('arial', 15, 'bold'), bd=5)


def clock():
    tiime = strftime('%H:%M:%S')
    clock_label.config(text=tiime)
    clock_label.after(1000, clock)


clock_label.pack(anchor='center', ipadx=30, ipady=10, pady=15)
clock()
clock_frame.pack()

# ----------------------------------------------------
calc_frame = Frame(frame_4, bg="#522B5B")
calc_label_frame = LabelFrame(frame_4, borderwidth=5)
expression = ""


def number(num):
    global expression
    expression = expression + str(num)
    calc_text.set(expression)


def clear_number():
    global expression
    expression = ""
    calc_text.set(0)


def equal():
    global expression
    total = int(eval(expression))
    calc_text.set(total)


calc_text = IntVar()
r_label = Entry(calc_label_frame, font=('verdana', 15, 'bold'), fg="black", width=10, textvariable=calc_text)
r_label.grid(row=0, column=0, columnspan=5, sticky="W", ipadx=5)
Button(calc_label_frame, text='7', width=4, height=2, bg='#072E33', fg="white", command=lambda: number(7)).grid(row=1,
                                                                                                                column=0)
Button(calc_label_frame, text='8', width=4, height=2, bg='#072E33', fg="white", command=lambda: number(8)).grid(row=1,
                                                                                                                column=1)
Button(calc_label_frame, text='9', width=4, height=2, bg='#072E33', fg="white", command=lambda: number(9)).grid(row=1,
                                                                                                                column=2)
Button(calc_label_frame, text='x', width=4, height=2, bg='#072E33', fg="white", command=lambda: number("*")).grid(row=1,
                                                                                                                  column=3)
Button(calc_label_frame, text='4', width=4, height=2, bg='#072E33', fg="white", command=lambda: number(4)).grid(row=2,
                                                                                                                column=0)
Button(calc_label_frame, text='5', width=4, height=2, bg='#072E33', fg="white", command=lambda: number(5)).grid(row=2,
                                                                                                                column=1)
Button(calc_label_frame, text='6', width=4, height=2, bg='#072E33', fg="white", command=lambda: number(6)).grid(row=2,
                                                                                                                column=2)
Button(calc_label_frame, text='-', width=4, height=2, bg='#072E33', fg="white", command=lambda: number("-")).grid(row=2,
                                                                                                                  column=3)
Button(calc_label_frame, text='1', width=4, height=2, bg='#072E33', fg="white", command=lambda: number(1)).grid(row=3,
                                                                                                                column=0)
Button(calc_label_frame, text='2', width=4, height=2, bg='#072E33', fg="white", command=lambda: number(2)).grid(row=3,
                                                                                                                column=1)
Button(calc_label_frame, text='3', width=4, height=2, bg='#072E33', fg="white", command=lambda: number(3)).grid(row=3,
                                                                                                                column=2)
Button(calc_label_frame, text='+', width=4, height=2, bg='#072E33', fg="white", command=lambda: number("+")).grid(row=3,
                                                                                                                  column=3)
Button(calc_label_frame, text='C', width=4, height=2, bg='#072E33', fg="white", command=clear_number).grid(row=4,
                                                                                                           column=0)
Button(calc_label_frame, text='0', width=4, height=2, bg='#072E33', fg="white", command=lambda: number(0)).grid(row=4,
                                                                                                                column=1)
Button(calc_label_frame, text='=', width=4, height=2, bg='#072E33', fg="white", command=equal).grid(row=4, column=2)
Button(calc_label_frame, text='/', width=4, height=2, bg='#072E33', fg="white", command=lambda: number("/")).grid(row=4,
                                                                                                                  column=3)

calc_label_frame.pack()
calc_frame.pack()


# --------------------------------------------------------------------------
# def clr_txt():


def clear_txt():
    t = txt_area.get("1.0", "end-1c")
    txt_area.delete("1.0", END)
    txt_area.insert("1.0", "Enter your text")


clr_btn_label = Label(frame_4, bg="#CDEFDF")
clr_btn = Button(clr_btn_label, text="Clear", width=9, height=1, font=('arial', 10), bd=5, command=clear_txt)
clr_btn.pack(side='left', pady=5)
clr_btn_label.pack()
# ----------------------------------------------------

txt_entry_frame = Frame(frame_4, bg="yellow")
txt_area = Text(frame_4, height=10, width=25, bd=5)
txt_area.pack(padx=5, pady=5)

txt_entry_frame.pack(padx=5)

frame_4.grid(row=0, column=2, rowspan=5, sticky="n")

main_fr.pack()

def window(e):
    obj1 = Toplevel(obj)
    obj1.geometry("800x600+300+100")
    obj1.title("Customer Details")

    main_fr = Frame(obj1)

    # def close():
    #     obj1.destroy()

    def search(event=None):
        mydb = mysql.connector.connect(host="localhost",
                                       password="123456789@ok",
                                       user="root",
                                       auth_plugin="mysql_native_password",
                                       database="sys")
        crsr = mydb.cursor()

        qry = "select Cust_mobile from cust_dtls where Cust_mobile="+num_var.get()
        crsr.execute(qry)
        result = crsr.fetchone()

        if result == None:
            blank_label.config(text="Customer dosen't Exsist ",font=('verdana','bold'))
            # print("Customer dosen't Exsist ")
        # elif result == " ":
        #     blank_label.config(text="Please enter a number")
        else:
            blank_label.config(text=result)
            # print("Customer Exsist")
            # print(result)

    label_frame = Frame(main_fr)
    name_label = Label(label_frame, text="Name", font=('verdana ', 12, 'bold'), width=12, height=1)
    name_label.grid(row=0, column=0, padx=5, sticky="w")

    mobile_label = Label(label_frame, text="Mobile No.", font=('verdana ', 12, 'bold'), width=12, height=1)
    mobile_label.grid(row=0, column=1, padx=5)

    add_label = Label(label_frame, text="Customer Address", font=('verdana ', 12, 'bold'), width=14, height=1)
    add_label.grid(row=0, column=2, padx=5)

    place_label = Label(label_frame, text="Place", font=('verdana ', 12, 'bold'), width=12, height=1)
    place_label.grid(row=0, column=3, padx=5)

    state_label = Label(label_frame, text="State/Area", font=('verdana ', 12, 'bold'), width=12, height=1)
    state_label.grid(row=0, column=4, padx=5)

    srch_btn = Button(label_frame, text="Search", font=('verdana ', 12, 'bold'),command=search)
    srch_btn.grid(row=1, column=5, padx=5)
    obj1.bind("<Return>", search)


    # name num addd place statearea    search

    def data_save():
        name = name_var.get()
        mobile = num_var.get()
        address = add_var.get()
        place = plac_var.get()
        state = stat_var.get()
        # print(name,mobile,address,place,state)
        mydb = mysql.connector.connect(host="localhost",
                                       password="123456789@ok",
                                       user="root",
                                       auth_plugin="mysql_native_password",
                                       database="sys")

        crsr = mydb.cursor()
        qry = "insert into cust_dtls(Cust_name ,Cust_mobile, Cust_address ,place,state) values (%s,%s,%s,%s,%s)"
        value = (name,mobile,address,place,state)
        crsr.execute(qry,value)
        mydb.commit()
        messagebox.showinfo("sucess","Number Saved Suceesfully")

    name_var = StringVar()
    name_entry = Entry(label_frame, width=21, textvariable=name_var)
    name_entry.grid(row=1, column=0, padx=5, ipady=2, sticky="w", pady=5, )

    num_var = StringVar()
    num_entry = Entry(label_frame, width=21, textvariable=num_var)
    num_entry.grid(row=1, column=1, padx=5, ipady=2, sticky="w", pady=5)

    add_var = StringVar()
    add_entry = Entry(label_frame, width=25, textvariable=add_var)
    add_entry.grid(row=1, column=2, padx=5, ipady=2, sticky="w", pady=5)

    plac_var = StringVar()
    place_entry = Entry(label_frame, width=21, textvariable=plac_var)
    place_entry.grid(row=1, column=3, padx=5, ipady=2, sticky="w", pady=5)

    stat_var = StringVar()
    state_entry = Entry(label_frame, width=21, textvariable=stat_var)
    state_entry.grid(row=1, column=4, padx=5, ipady=2, sticky="w", pady=5)

    blank_label = Label(label_frame, bg="white", height=30, width=112)
    blank_label.grid(row=2, column=0, columnspan=6)

    label_frame.grid(row=0, column=0)

    btn_frme = Frame(main_fr)

    ok_btk = Button(btn_frme, text="OK", font=('verdana ', 12, 'bold'), width=10, bg="white",command=lambda :obj1.destroy())
    ok_btk.grid(row=0, column=0, sticky="e", padx=40, pady=20)

    # new_btk = Button(btn_frme, text="New", font=('verdana ', 12, 'bold'), width=10, bg="white")
    # new_btk.grid(row=0, column=1, sticky="e", padx=40, pady=20)

    save_btk = Button(btn_frme, text="Save", font=('verdana ', 12, 'bold'), width=10, bg="white",command=data_save)
    save_btk.grid(row=0, column=2, sticky="e", padx=40, pady=20)

    cancel_btk = Button(btn_frme, text="Cancel", font=('verdana ', 12, 'bold'), width=10, bg="white",command=lambda :obj1.destroy())
    cancel_btk.grid(row=0, column=3, sticky="e", padx=40, pady=20)

    btn_frme.grid(row=1, column=0)


    main_fr.pack()



    obj1.mainloop()
obj.bind("<F4>",window)

obj.mainloop()