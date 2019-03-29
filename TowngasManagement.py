import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
import tkinter.messagebox
import sys

from tkinter.constants import LEFT, END, BOTTOM, TOP, ANCHOR, YES, Y, ACTIVE, \
    CENTER, BOTH, X, HORIZONTAL, VERTICAL
from tkinter import Toplevel, IntVar, ttk, StringVar, Menu
from datetime import *
# import datetime
# from monthdelta import monthdelta
import time
from _overlapped import NULL
from tkinter.ttk import Frame, Treeview
import webbrowser
from email._header_value_parser import Address

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import datetime
import math
from decimal import *

import cx_Oracle

import uuid_handler

# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
E = tk.E
N = tk.N
W = tk.W
S = tk.S

logo = "towngas.jpg"

cmb_day = (list(range(1, 32)))
cmb_month = (list(range(1,13)))
cmb_year = (list(range(1920, 2022)))

operator = "Admin"

class Towngas(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")


        container = tk.Frame(self, bg="#7aaaea")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login, Customer, Invoice, Record):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Invoice")

    def get_page(self, page_name):
        return self.frames[page_name]

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#7aaaea")
        self.controller = controller

        # self.frame = Frame(self)
        # self.frame.pack(anchor=CENTER, pady=300)

        self.label_usn = tk.Label(self)
        self.label_usn.place(relx=0.354, rely=0.451, height=11, width=67)
        self.label_usn.configure(activebackground="#f9f9f9")
        self.label_usn.configure(activeforeground="black")
        self.label_usn.configure(background="#7aaaea")
        self.label_usn.configure(disabledforeground="#a3a3a3")
        self.label_usn.configure(foreground="#000000")
        self.label_usn.configure(highlightbackground="#d9d9d9")
        self.label_usn.configure(highlightcolor="black")
        self.label_usn.configure(text='''USERNAME''')

        self.entry_usn = tk.Entry(self)
        self.entry_usn.place(relx=0.438, rely=0.444, height=20, relwidth=0.171)
        self.entry_usn.configure(background="white")
        self.entry_usn.configure(disabledforeground="#a3a3a3")
        self.entry_usn.configure(font="TkFixedFont")
        self.entry_usn.configure(foreground="#000000")
        self.entry_usn.configure(highlightbackground="#d9d9d9")
        self.entry_usn.configure(highlightcolor="black")
        self.entry_usn.configure(insertbackground="black")
        self.entry_usn.configure(selectbackground="#c4c4c4")
        self.entry_usn.configure(selectforeground="black")

        self.label_pw = tk.Label(self)
        self.label_pw.place(relx=0.354, rely=0.493, height=11, width=67)
        self.label_pw.configure(activebackground="#f9f9f9")
        self.label_pw.configure(activeforeground="black")
        self.label_pw.configure(background="#7aaaea")
        self.label_pw.configure(disabledforeground="#a3a3a3")
        self.label_pw.configure(foreground="#000000")
        self.label_pw.configure(highlightbackground="#d9d9d9")
        self.label_pw.configure(highlightcolor="black")
        self.label_pw.configure(text='''PASSWORD''')
        self.label_pw.configure(width=68)

        self.entry_pw = tk.Entry(self)
        self.entry_pw.place(relx=0.438, rely=0.486, height=20, relwidth=0.171)
        self.entry_pw.configure(background="white")
        self.entry_pw.configure(disabledforeground="#a3a3a3")
        self.entry_pw.configure(font="TkFixedFont")
        self.entry_pw.configure(foreground="#000000")
        self.entry_pw.configure(highlightbackground="#d9d9d9")
        self.entry_pw.configure(highlightcolor="black")
        self.entry_pw.configure(insertbackground="black")
        self.entry_pw.configure(selectbackground="#c4c4c4")
        self.entry_pw.configure(selectforeground="black")

        self.btn_login = tk.Button(self)
        self.btn_login.place(relx=0.469, rely=0.542, height=24, width=46)
        self.btn_login.configure(activebackground="#e88787")
        self.btn_login.configure(activeforeground="#000000")
        self.btn_login.configure(background="#ea9f9f")
        self.btn_login.configure(disabledforeground="#a3a3a3")
        self.btn_login.configure(foreground="#000000")
        self.btn_login.configure(highlightbackground="#d9d9d9")
        self.btn_login.configure(highlightcolor="black")
        self.btn_login.configure(pady="0")
        self.btn_login.configure(text='''LOGIN''')
        self.btn_login.configure(command=self.validate)

    def validate(self):
        input_un = self.entry_usn.get();
        input_pw = self.entry_pw.get();

        if input_un == "admin" and input_pw == "admin":
            # tkinter.messagebox.showinfo("Login", "You are now going to the home page")
            self.clear_field()
            self.controller.show_frame("Invoice")
            operator = "Admin"
            return operator
        else:
            tkinter.messagebox.showinfo("Login", "Wrong username or password")
            self.clear_field()

    def clear_field(self):
        self.entry_usn.delete(0, 'end')
        self.entry_pw.delete(0, 'end')

    def close(self):
        self.frame.destroy()

# class Home(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, bg="#7aaaea")
#         self.controller = controller
#
#         font11 = "-family Arial -size 12 -weight normal -slant roman " \
#                  "-underline 1 -overstrike 0"
#
#         self.top_panel = tk.Frame(self)
#         self.top_panel.place(relx=-0.0, rely=0.0, relheight=0.063
#                              , relwidth=1.002)
#         self.top_panel.configure(borderwidth="2")
#         self.top_panel.configure(background="#6f9cd6")
#         self.top_panel.configure(highlightbackground="#d9d9d9")
#         self.top_panel.configure(highlightcolor="black")
#         self.top_panel.configure(width=965)
#
#         self.top_login_text = tk.Label(self.top_panel)
#         self.top_login_text.place(relx=0.0, rely=0.0, height=21, width=875)
#         self.top_login_text.configure(activebackground="#f9f9f9")
#         self.top_login_text.configure(activeforeground="black")
#         self.top_login_text.configure(anchor=E)
#         self.top_login_text.configure(background="#6f9cd6")
#         self.top_login_text.configure(disabledforeground="#a3a3a3")
#         self.top_login_text.configure(foreground="#000000")
#         self.top_login_text.configure(highlightbackground="#d9d9d9")
#         self.top_login_text.configure(highlightcolor="black")
#         self.top_login_text.configure(text='''You have been login as:''')
#         self.top_login_text.configure(width=875)
#
#         self.top_login_id = tk.Label(self.top_panel)
#         self.top_login_id.place(relx=0.91, rely=0.0, height=21, width=85)
#         self.top_login_id.configure(activebackground="#f9f9f9")
#         self.top_login_id.configure(activeforeground="black")
#         self.top_login_id.configure(background="#6f9cd6")
#         self.top_login_id.configure(disabledforeground="#a3a3a3")
#         self.top_login_id.configure(foreground="#000000")
#         self.top_login_id.configure(highlightbackground="#d9d9d9")
#         self.top_login_id.configure(highlightcolor="black")
#         self.top_login_id.configure(text=operator)
#
#         self.top_cwd_text = tk.Label(self.top_panel)
#         self.top_cwd_text.place(relx=0.0, rely=0.444, height=21, width=135)
#         self.top_cwd_text.configure(activebackground="#f9f9f9")
#         self.top_cwd_text.configure(activeforeground="black")
#         self.top_cwd_text.configure(anchor=W)
#         self.top_cwd_text.configure(background="#6f9cd6")
#         self.top_cwd_text.configure(disabledforeground="#a3a3a3")
#         self.top_cwd_text.configure(foreground="#000000")
#         self.top_cwd_text.configure(highlightbackground="#d9d9d9")
#         self.top_cwd_text.configure(highlightcolor="black")
#         self.top_cwd_text.configure(text='''Current Work Directory:''')
#
#         self.top_cwd_bar_home = tk.Button(self.top_panel)
#         self.top_cwd_bar_home.place(relx=0.14, rely=0.444, height=21, width=45)
#         self.top_cwd_bar_home.configure(activebackground="#6f9cd6")
#         self.top_cwd_bar_home.configure(activeforeground="#000000")
#         self.top_cwd_bar_home.configure(background="#6f9cd6")
#         self.top_cwd_bar_home.configure(borderwidth="0")
#         self.top_cwd_bar_home.configure(cursor="hand2")
#         self.top_cwd_bar_home.configure(disabledforeground="#a3a3a3")
#         self.top_cwd_bar_home.configure(foreground="#000000")
#         self.top_cwd_bar_home.configure(highlightbackground="#d9d9d9")
#         self.top_cwd_bar_home.configure(highlightcolor="black")
#         self.top_cwd_bar_home.configure(pady="0")
#         self.top_cwd_bar_home.configure(text='''Home >''')
#         self.top_cwd_bar_home.configure(command=self.gotoHome)
#
#         self.btn_customer = tk.Button(self)
#         self.btn_customer.place(relx=0.104, rely=0.389, height=150, width=150)
#         self.btn_customer.configure(activebackground="#807cea")
#         self.btn_customer.configure(activeforeground="#000000")
#         self.btn_customer.configure(background="#709dd8")
#         self.btn_customer.configure(borderwidth="5")
#         self.btn_customer.configure(disabledforeground="#a3a3a3")
#         self.btn_customer.configure(font=font11)
#         self.btn_customer.configure(foreground="#000000")
#         self.btn_customer.configure(highlightbackground="#d9d9d9")
#         self.btn_customer.configure(highlightcolor="black")
#         self.btn_customer.configure(pady="0")
#         self.btn_customer.configure(text='''Customer''')
#         self.btn_customer.configure(command=self.gotoCustomer)
#
#         self.btn_record = tk.Button(self)
#         self.btn_record.place(relx=0.323, rely=0.389, height=150, width=150)
#         self.btn_record.configure(activebackground="#807cea")
#         self.btn_record.configure(activeforeground="#000000")
#         self.btn_record.configure(background="#709dd8")
#         self.btn_record.configure(borderwidth="5")
#         self.btn_record.configure(disabledforeground="#a3a3a3")
#         self.btn_record.configure(font=font11)
#         self.btn_record.configure(foreground="#000000")
#         self.btn_record.configure(highlightbackground="#d9d9d9")
#         self.btn_record.configure(highlightcolor="black")
#         self.btn_record.configure(pady="0")
#         self.btn_record.configure(text='''Record''')
#         self.btn_record.configure(command=self.gotoRecord)
#
#         self.btn_invoice = tk.Button(self)
#         self.btn_invoice.place(relx=0.542, rely=0.389, height=150, width=150)
#         self.btn_invoice.configure(activebackground="#807cea")
#         self.btn_invoice.configure(activeforeground="#000000")
#         self.btn_invoice.configure(background="#709dd8")
#         self.btn_invoice.configure(borderwidth="5")
#         self.btn_invoice.configure(disabledforeground="#a3a3a3")
#         self.btn_invoice.configure(font=font11)
#         self.btn_invoice.configure(foreground="#000000")
#         self.btn_invoice.configure(highlightbackground="#d9d9d9")
#         self.btn_invoice.configure(highlightcolor="black")
#         self.btn_invoice.configure(pady="0")
#         self.btn_invoice.configure(text='''Invoice''')
#         self.btn_invoice.configure(command=self.gotoInvoice)
#
#         self.btn_payment = tk.Button(self)
#         self.btn_payment.place(relx=0.76, rely=0.389, height=150, width=150)
#         self.btn_payment.configure(activebackground="#807cea")
#         self.btn_payment.configure(activeforeground="#000000")
#         self.btn_payment.configure(background="#709dd8")
#         self.btn_payment.configure(borderwidth="5")
#         self.btn_payment.configure(disabledforeground="#a3a3a3")
#         self.btn_payment.configure(font=font11)
#         self.btn_payment.configure(foreground="#000000")
#         self.btn_payment.configure(highlightbackground="#d9d9d9")
#         self.btn_payment.configure(highlightcolor="black")
#         self.btn_payment.configure(pady="0")
#         self.btn_payment.configure(text='''Payment''')
#
#         self.btn_logout = tk.Button(self)
#         self.btn_logout.place(relx=0.896, rely=0.931, height=40, width=90)
#         self.btn_logout.configure(activebackground="#807cea")
#         self.btn_logout.configure(activeforeground="#000000")
#         self.btn_logout.configure(background="#709dd8")
#         self.btn_logout.configure(borderwidth="5")
#         self.btn_logout.configure(disabledforeground="#a3a3a3")
#         self.btn_logout.configure(font=font11)
#         self.btn_logout.configure(foreground="#000000")
#         self.btn_logout.configure(highlightbackground="#d9d9d9")
#         self.btn_logout.configure(highlightcolor="black")
#         self.btn_logout.configure(pady="0")
#         self.btn_logout.configure(text='''Logout''')
#         self.btn_logout.configure(width=90)
#         self.btn_logout.configure(command=self.logout)
#
#     def gotoHome(self):
#         self.controller.show_frame("Home")
#
#     def gotoCustomer(self):
#         self.controller.show_frame("Customer")
#
#     def gotoInvoice(self):
#         self.controller.show_frame("Invoice")
#
#     def gotoRecord(self):
#         # warning()
#         self.controller.show_frame("Record")
#
#     def logout(self):
#         # warning()
#         self.controller.show_frame("Login")

class Customer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#7aaaea")
        self.controller = controller

        font12 = "-family {Comic Sans MS} -size 16 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 20 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"
        font9 = "-family {Franklin Gothic Demi Cond} -size 16 -weight " \
                "normal -slant roman -underline 1 -overstrike 0"
        font11 = "-family {Franklin Gothic Demi Cond} -size 16 -weight" \
                 " normal -slant roman -underline 1 -overstrike 0"
        font10 = "-family {Segoe UI} -size 20 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"

        self.left_panel = tk.Frame(self)
        self.left_panel.place(relx=0.0, rely=0.056, relheight=0.944
                              , relwidth=0.193)
        self.left_panel.configure(borderwidth="2")
        self.left_panel.configure(background="#5eaad6")
        self.left_panel.configure(highlightbackground="#d9d9d9")
        self.left_panel.configure(highlightcolor="black")
        self.left_panel.configure(width=185)

        # self.left_btn_logout = tk.Button(self.left_panel)
        # self.left_btn_logout.place(relx=0.027, rely=0.949, height=30, width=175)
        # self.left_btn_logout.configure(activebackground="#807cea")
        # self.left_btn_logout.configure(activeforeground="#000000")
        # self.left_btn_logout.configure(background="#709dd8")
        # self.left_btn_logout.configure(borderwidth="3")
        # self.left_btn_logout.configure(disabledforeground="#a3a3a3")
        # self.left_btn_logout.configure(font=font11)
        # self.left_btn_logout.configure(foreground="#000000")
        # self.left_btn_logout.configure(highlightbackground="#d9d9d9")
        # self.left_btn_logout.configure(highlightcolor="black")
        # self.left_btn_logout.configure(pady="0")
        # self.left_btn_logout.configure(text='''Logout''')
        # self.left_btn_logout.configure(command=self.logout)

        self.left_btn_invoice = tk.Button(self.left_panel)
        self.left_btn_invoice.place(relx=0.003, rely=0.007, height=131, width=179)
        self.left_btn_invoice.configure(activebackground="#807cea")
        self.left_btn_invoice.configure(activeforeground="#000000")
        self.left_btn_invoice.configure(background="#579dc6")
        self.left_btn_invoice.configure(borderwidth="0")
        self.left_btn_invoice.configure(cursor="hand2")
        self.left_btn_invoice.configure(disabledforeground="#a3a3a3")
        self.left_btn_invoice.configure(font=font10)
        self.left_btn_invoice.configure(foreground="#000000")
        self.left_btn_invoice.configure(highlightbackground="#d9d9d9")
        self.left_btn_invoice.configure(highlightcolor="black")
        self.left_btn_invoice.configure(pady="0")
        self.left_btn_invoice.configure(text='''Invoice''')
        self.left_btn_invoice.configure(command=self.gotoInvoice)

        self.left_btn_customer = tk.Button(self.left_panel)
        self.left_btn_customer.place(relx=0.003, rely=0.207, height=131, width=179)
        self.left_btn_customer.configure(activebackground="#807cea")
        self.left_btn_customer.configure(activeforeground="#000000")
        self.left_btn_customer.configure(background="#4d8baf")
        self.left_btn_customer.configure(borderwidth="0")
        self.left_btn_customer.configure(cursor="hand2")
        self.left_btn_customer.configure(disabledforeground="#bcbcbc")
        self.left_btn_customer.configure(font=font10)
        self.left_btn_customer.configure(foreground="#000000")
        self.left_btn_customer.configure(highlightbackground="#d9d9d9")
        self.left_btn_customer.configure(highlightcolor="black")
        self.left_btn_customer.configure(pady="0")
        self.left_btn_customer.configure(text='''Register''')

        self.left_btn_record = tk.Button(self.left_panel)
        self.left_btn_record.place(relx=0.003, rely=0.407, height=131, width=179)
        self.left_btn_record.configure(activebackground="#807cea")
        self.left_btn_record.configure(activeforeground="#000000")
        self.left_btn_record.configure(background="#579dc6")
        self.left_btn_record.configure(borderwidth="0")
        self.left_btn_record.configure(cursor="hand2")
        self.left_btn_record.configure(disabledforeground="#a3a3a3")
        self.left_btn_record.configure(font=font10)
        self.left_btn_record.configure(foreground="#000000")
        self.left_btn_record.configure(highlightbackground="#d9d9d9")
        self.left_btn_record.configure(highlightcolor="black")
        self.left_btn_record.configure(pady="0")
        self.left_btn_record.configure(text='''Record''')
        self.left_btn_record.configure(command=self.gotoRecord)

        # self.left_btn_payment = tk.Button(self.left_panel)
        # self.left_btn_payment.place(relx=0.003, rely=0.607, height=131, width=179)
        # self.left_btn_payment.configure(activebackground="#807cea")
        # self.left_btn_payment.configure(activeforeground="#000000")
        # self.left_btn_payment.configure(background="#579dc6")
        # self.left_btn_payment.configure(borderwidth="0")
        # self.left_btn_payment.configure(cursor="hand2")
        # self.left_btn_payment.configure(disabledforeground="#a3a3a3")
        # self.left_btn_payment.configure(font=font10)
        # self.left_btn_payment.configure(foreground="#000000")
        # self.left_btn_payment.configure(highlightbackground="#d9d9d9")
        # self.left_btn_payment.configure(highlightcolor="black")
        # self.left_btn_payment.configure(pady="0")
        # self.left_btn_payment.configure(text='''Payment''')

        self.top_panel = tk.Frame(self)
        self.top_panel.place(relx=-0.0, rely=0.0, relheight=0.063
                             , relwidth=1.002)
        self.top_panel.configure(borderwidth="2")
        self.top_panel.configure(background="#6f9cd6")
        self.top_panel.configure(highlightbackground="#d9d9d9")
        self.top_panel.configure(highlightcolor="black")
        self.top_panel.configure(width=965)

        self.top_login_text = tk.Label(self.top_panel)
        self.top_login_text.place(relx=0.0, rely=0.0, height=21, width=875)
        self.top_login_text.configure(activebackground="#f9f9f9")
        self.top_login_text.configure(activeforeground="black")
        self.top_login_text.configure(anchor=E)
        self.top_login_text.configure(background="#6f9cd6")
        self.top_login_text.configure(disabledforeground="#a3a3a3")
        self.top_login_text.configure(foreground="#000000")
        self.top_login_text.configure(highlightbackground="#d9d9d9")
        self.top_login_text.configure(highlightcolor="black")
        self.top_login_text.configure(text='''You have been login as:''')

        self.top_login_id = tk.Label(self.top_panel)
        self.top_login_id.place(relx=0.91, rely=0.0, height=21, width=85)
        self.top_login_id.configure(activebackground="#f9f9f9")
        self.top_login_id.configure(activeforeground="black")
        self.top_login_id.configure(background="#6f9cd6")
        self.top_login_id.configure(disabledforeground="#a3a3a3")
        self.top_login_id.configure(foreground="#000000")
        self.top_login_id.configure(highlightbackground="#d9d9d9")
        self.top_login_id.configure(highlightcolor="black")
        self.top_login_id.configure(text=operator)

        self.top_cwd_text = tk.Label(self.top_panel)
        self.top_cwd_text.place(relx=0.0, rely=0.444, height=21, width=135)
        self.top_cwd_text.configure(activebackground="#f9f9f9")
        self.top_cwd_text.configure(activeforeground="black")
        self.top_cwd_text.configure(anchor=W)
        self.top_cwd_text.configure(background="#6f9cd6")
        self.top_cwd_text.configure(disabledforeground="#a3a3a3")
        self.top_cwd_text.configure(foreground="#000000")
        self.top_cwd_text.configure(highlightbackground="#d9d9d9")
        self.top_cwd_text.configure(highlightcolor="black")
        self.top_cwd_text.configure(text='''Current Work Directory:''')

        self.top_cwd_bar_home = tk.Button(self.top_panel)
        self.top_cwd_bar_home.place(relx=0.14, rely=0.444, height=21, width=45)
        self.top_cwd_bar_home.configure(activebackground="#6f9cd6")
        self.top_cwd_bar_home.configure(activeforeground="#000000")
        self.top_cwd_bar_home.configure(background="#6f9cd6")
        self.top_cwd_bar_home.configure(borderwidth="0")
        self.top_cwd_bar_home.configure(cursor="hand2")
        self.top_cwd_bar_home.configure(disabledforeground="#a3a3a3")
        self.top_cwd_bar_home.configure(foreground="#000000")
        self.top_cwd_bar_home.configure(highlightbackground="#d9d9d9")
        self.top_cwd_bar_home.configure(highlightcolor="black")
        self.top_cwd_bar_home.configure(pady="0")
        self.top_cwd_bar_home.configure(text='''Home >''')
        self.top_cwd_bar_home.configure(command=self.gotoHome)

        self.top_cwd_bar_customer = tk.Button(self.top_panel)
        self.top_cwd_bar_customer.place(relx=0.187, rely=0.444, height=21
                                        , width=65)
        self.top_cwd_bar_customer.configure(activebackground="#6f9cd6")
        self.top_cwd_bar_customer.configure(activeforeground="#000000")
        self.top_cwd_bar_customer.configure(background="#6f9cd6")
        self.top_cwd_bar_customer.configure(borderwidth="0")
        self.top_cwd_bar_customer.configure(cursor="hand2")
        self.top_cwd_bar_customer.configure(disabledforeground="#a3a3a3")
        self.top_cwd_bar_customer.configure(foreground="#000000")
        self.top_cwd_bar_customer.configure(highlightbackground="#d9d9d9")
        self.top_cwd_bar_customer.configure(highlightcolor="black")
        self.top_cwd_bar_customer.configure(pady="0")
        self.top_cwd_bar_customer.configure(text='''Register >''')

        self.text_cusinfo = tk.Label(self)
        self.text_cusinfo.place(relx=0.198, rely=0.069, height=35, width=223)
        self.text_cusinfo.configure(background="#7aaaea")
        self.text_cusinfo.configure(disabledforeground="#a3a3a3")
        self.text_cusinfo.configure(font=font12)
        self.text_cusinfo.configure(foreground="#000000")
        self.text_cusinfo.configure(text='''Customer Information''')

        self.text_customer_id = tk.Label(self)
        self.text_customer_id.place(relx=0.271, rely=0.153, height=20, width=35)
        self.text_customer_id.configure(activebackground="#f9f9f9")
        self.text_customer_id.configure(activeforeground="black")
        self.text_customer_id.configure(background="#7aaaea")
        self.text_customer_id.configure(disabledforeground="#a3a3a3")
        self.text_customer_id.configure(foreground="#000000")
        self.text_customer_id.configure(highlightbackground="#d9d9d9")
        self.text_customer_id.configure(highlightcolor="black")
        self.text_customer_id.configure(text='''HKID:''')
        self.text_customer_id.configure(width=35)

        self.entry_customer_id = tk.Entry(self)
        self.entry_customer_id.place(relx=0.313, rely=0.153, height=20
                                     , relwidth=0.119)
        self.entry_customer_id.configure(background="#ffffff")
        self.entry_customer_id.configure(disabledbackground="#c9c9c9")
        self.entry_customer_id.configure(disabledforeground="#a3a3a3")
        self.entry_customer_id.configure(font="TkFixedFont")
        self.entry_customer_id.configure(foreground="#000000")
        self.entry_customer_id.configure(insertbackground="black")
        self.entry_customer_id.configure(width=114)

        self.text_firstname = tk.Label(self)
        self.text_firstname.place(relx=0.266, rely=0.194, height=21, width=37)
        self.text_firstname.configure(background="#7aaaea")
        self.text_firstname.configure(disabledforeground="#a3a3a3")
        self.text_firstname.configure(foreground="#000000")
        self.text_firstname.configure(text='''Name:''')

        self.entry_firstname = tk.Entry(self)
        self.entry_firstname.place(relx=0.313, rely=0.194, height=20
                                   , relwidth=0.119)
        self.entry_firstname.configure(background="#ffffff")
        self.entry_firstname.configure(disabledbackground="#c9c9c9")
        self.entry_firstname.configure(disabledforeground="#a3a3a3")
        self.entry_firstname.configure(font="TkFixedFont")
        self.entry_firstname.configure(foreground="#000000")
        self.entry_firstname.configure(highlightbackground="#d9d9d9")
        self.entry_firstname.configure(highlightcolor="black")
        self.entry_firstname.configure(insertbackground="black")
        self.entry_firstname.configure(selectbackground="#c4c4c4")
        self.entry_firstname.configure(selectforeground="black")

        self.btn_search = tk.Button(self)
        self.btn_search.place(relx=0.448, rely=0.153, height=20, width=46)
        self.btn_search.configure(activebackground="#ea9f9f")
        self.btn_search.configure(activeforeground="#000000")
        self.btn_search.configure(background="#ea9f9f")
        self.btn_search.configure(disabledforeground="#a3a3a3")
        self.btn_search.configure(foreground="#000000")
        self.btn_search.configure(highlightbackground="#d9d9d9")
        self.btn_search.configure(highlightcolor="black")
        self.btn_search.configure(pady="0")
        self.btn_search.configure(text='''Search''')
        self.btn_search.configure(command=self.search_info)

        self.text_gender = tk.Label(self)
        self.text_gender.place(relx=0.25, rely=0.236, height=21, width=67)
        self.text_gender.configure(activebackground="#f9f9f9")
        self.text_gender.configure(activeforeground="black")
        self.text_gender.configure(background="#7aaaea")
        self.text_gender.configure(disabledforeground="#a3a3a3")
        self.text_gender.configure(foreground="#000000")
        self.text_gender.configure(highlightbackground="#d9d9d9")
        self.text_gender.configure(highlightcolor="black")
        self.text_gender.configure(text='''Gender:''')

        self.var = tk.StringVar()
        self.rbtn_m = tk.Radiobutton(self)
        self.rbtn_m.place(relx=0.313, rely=0.236, relheight=0.035
                          , relwidth=0.041)
        self.rbtn_m.configure(activebackground="#7aaaea")
        self.rbtn_m.configure(activeforeground="#000000")
        self.rbtn_m.configure(background="#7aaaea")
        self.rbtn_m.configure(disabledforeground="#a3a3a3")
        self.rbtn_m.configure(foreground="#000000")
        self.rbtn_m.configure(highlightbackground="#d9d9d9")
        self.rbtn_m.configure(highlightcolor="black")
        self.rbtn_m.configure(justify=LEFT)
        self.rbtn_m.configure(variable=self.var)
        self.rbtn_m.configure(value="M")
        self.rbtn_m.configure(text='''M''')
        self.rbtn_m.configure(state="normal")

        self.rbtn_f = tk.Radiobutton(self)
        self.rbtn_f.place(relx=0.365, rely=0.236, relheight=0.035
                          , relwidth=0.041)
        self.rbtn_f.configure(activebackground="#7aaaea")
        self.rbtn_f.configure(activeforeground="#000000")
        self.rbtn_f.configure(background="#7aaaea")
        self.rbtn_f.configure(disabledforeground="#a3a3a3")
        self.rbtn_f.configure(foreground="#000000")
        self.rbtn_f.configure(highlightbackground="#d9d9d9")
        self.rbtn_f.configure(highlightcolor="black")
        self.rbtn_f.configure(justify=LEFT)
        self.rbtn_f.configure(variable=self.var)
        self.rbtn_f.configure(value="F")
        self.rbtn_f.configure(text='''F''')
        self.rbtn_f.configure(state="normal")


        self.text_birthday = tk.Label(self)
        self.text_birthday.place(relx=0.245, rely=0.285, height=21, width=67)
        self.text_birthday.configure(activebackground="#f9f9f9")
        self.text_birthday.configure(activeforeground="black")
        self.text_birthday.configure(background="#7aaaea")
        self.text_birthday.configure(disabledforeground="#a3a3a3")
        self.text_birthday.configure(foreground="#000000")
        self.text_birthday.configure(highlightbackground="#d9d9d9")
        self.text_birthday.configure(highlightcolor="black")
        self.text_birthday.configure(text='''Birthday:''')

        self.day = tk.StringVar()
        self.combo_birthday_day = ttk.Combobox(self)
        self.combo_birthday_day.place(relx=0.313, rely=0.292, relheight=0.029
                                      , relwidth=0.045)
        self.combo_birthday_day.configure(textvariable=self.day)
        self.combo_birthday_day.configure(width=43)
        self.combo_birthday_day.configure(takefocus="")
        self.combo_birthday_day['values'] = (list(range(1, 32)))
        self.combo_birthday_day.configure(state="readonly")

        self.month = tk.StringVar()
        self.combo_birthday_month = ttk.Combobox(self)
        self.combo_birthday_month.place(relx=0.365, rely=0.292, relheight=0.029
                                        , relwidth=0.076)
        self.combo_birthday_month.configure(textvariable=self.month)
        self.combo_birthday_month.configure(width=73)
        self.combo_birthday_month.configure(takefocus="")
        self.combo_birthday_month['values'] = (list(range(1, 13)))
        self.combo_birthday_month.configure(state="readonly")

        self.year = tk.StringVar()
        self.combo_birthday_year = ttk.Combobox(self)
        self.combo_birthday_year.place(relx=0.448, rely=0.292, relheight=0.029
                                       , relwidth=0.076)
        self.combo_birthday_year.configure(textvariable=self.year)
        self.combo_birthday_year.configure(takefocus="")
        self.combo_birthday_year['values'] = (list(range(1920, 2022)))
        self.combo_birthday_year.configure(state="readonly")

        self.text_phone1 = tk.Label(self)
        self.text_phone1.place(relx=0.245, rely=0.347, height=21, width=57)
        self.text_phone1.configure(activebackground="#f9f9f9")
        self.text_phone1.configure(activeforeground="black")
        self.text_phone1.configure(background="#7aaaea")
        self.text_phone1.configure(disabledforeground="#a3a3a3")
        self.text_phone1.configure(foreground="#000000")
        self.text_phone1.configure(highlightbackground="#d9d9d9")
        self.text_phone1.configure(highlightcolor="black")
        self.text_phone1.configure(text='''Phone no.:''')

        self.entry_phone1 = tk.Entry(self)
        self.entry_phone1.place(relx=0.313, rely=0.347, height=20
                                , relwidth=0.119)
        self.entry_phone1.configure(background="#ffffff")
        self.entry_phone1.configure(disabledbackground="#c9c9c9")
        self.entry_phone1.configure(disabledforeground="#a3a3a3")
        self.entry_phone1.configure(font="TkFixedFont")
        self.entry_phone1.configure(foreground="#000000")
        self.entry_phone1.configure(highlightbackground="#d9d9d9")
        self.entry_phone1.configure(highlightcolor="black")
        self.entry_phone1.configure(insertbackground="black")
        self.entry_phone1.configure(selectbackground="#c4c4c4")
        self.entry_phone1.configure(selectforeground="black")

        # self.btn_update_cus = tk.Button(self)
        # self.btn_update_cus.place(relx=0.313, rely=0.403, height=22, width=49)
        # self.btn_update_cus.configure(activebackground="#ea9f9f")
        # self.btn_update_cus.configure(activeforeground="#000000")
        # self.btn_update_cus.configure(background="#ea9f9f")
        # self.btn_update_cus.configure(disabledforeground="#a3a3a3")
        # self.btn_update_cus.configure(foreground="#000000")
        # self.btn_update_cus.configure(highlightbackground="#d9d9d9")
        # self.btn_update_cus.configure(highlightcolor="black")
        # self.btn_update_cus.configure(pady="0")
        # self.btn_update_cus.configure(text='''Update''')
        # self.btn_update_cus.configure(command=self.update_customer)

        self.text_metre = tk.Label(self)
        self.text_metre.place(relx=0.198, rely=0.444, height=35, width=142)
        self.text_metre.configure(anchor=W)
        self.text_metre.configure(background="#7aaaea")
        self.text_metre.configure(disabledforeground="#a3a3a3")
        self.text_metre.configure(font=font12)
        self.text_metre.configure(foreground="#000000")
        self.text_metre.configure(text='''Metre Details''')

        self.text_address = tk.Label(self)
        self.text_address.place(relx=0.25, rely=0.514, height=21, width=67)
        self.text_address.configure(activebackground="#f9f9f9")
        self.text_address.configure(activeforeground="black")
        self.text_address.configure(background="#7aaaea")
        self.text_address.configure(disabledforeground="#a3a3a3")
        self.text_address.configure(foreground="#000000")
        self.text_address.configure(highlightbackground="#d9d9d9")
        self.text_address.configure(highlightcolor="black")
        self.text_address.configure(text='''Address:''')

        self.entry_address = tk.Entry(self)
        self.entry_address.place(relx=0.313, rely=0.514, height=20
                                 , relwidth=0.338)
        self.entry_address.configure(background="#ffffff")
        self.entry_address.configure(disabledbackground="#c9c9c9")
        self.entry_address.configure(disabledforeground="#a3a3a3")
        self.entry_address.configure(font="TkFixedFont")
        self.entry_address.configure(foreground="#000000")
        self.entry_address.configure(highlightbackground="#d9d9d9")
        self.entry_address.configure(highlightcolor="black")
        self.entry_address.configure(insertbackground="black")
        self.entry_address.configure(selectbackground="#c4c4c4")
        self.entry_address.configure(selectforeground="black")
        self.entry_address.configure(width=324)

        self.entry_address2 = tk.Entry(self)
        self.entry_address2.place(relx=0.313, rely=0.556, height=20
                                  , relwidth=0.338)
        self.entry_address2.configure(background="#ffffff")
        self.entry_address2.configure(disabledbackground="#c9c9c9")
        self.entry_address2.configure(disabledforeground="#a3a3a3")
        self.entry_address2.configure(font="TkFixedFont")
        self.entry_address2.configure(foreground="#000000")
        self.entry_address2.configure(highlightbackground="#d9d9d9")
        self.entry_address2.configure(highlightcolor="black")
        self.entry_address2.configure(insertbackground="black")
        self.entry_address2.configure(selectbackground="#c4c4c4")
        self.entry_address2.configure(selectforeground="black")

        self.text_district = tk.Label(self)
        self.text_district.place(relx=0.25, rely=0.597, height=21, width=67)
        self.text_district.configure(activebackground="#f9f9f9")
        self.text_district.configure(activeforeground="black")
        self.text_district.configure(background="#7aaaea")
        self.text_district.configure(disabledforeground="#a3a3a3")
        self.text_district.configure(foreground="#000000")
        self.text_district.configure(highlightbackground="#d9d9d9")
        self.text_district.configure(highlightcolor="black")
        self.text_district.configure(text='''District:''')

        self.district = tk.StringVar()
        self.combo_district = ttk.Combobox(self)
        self.combo_district.place(relx=0.313, rely=0.597, relheight=0.029
                                  , relwidth=0.149)
        self.combo_district.configure(textvariable=self.district)
        self.combo_district.configure(takefocus="")
        self.combo_district['values'] = ("NT", "KW", "HK")

        self.btn_update_metre = tk.Button(self)
        self.btn_update_metre.place(relx=0.313, rely=0.653, height=22, width=30)
        self.btn_update_metre.configure(activebackground="#ea9f9f")
        self.btn_update_metre.configure(activeforeground="#000000")
        self.btn_update_metre.configure(background="#ea9f9f")
        self.btn_update_metre.configure(disabledforeground="#a3a3a3")
        self.btn_update_metre.configure(foreground="#000000")
        self.btn_update_metre.configure(highlightbackground="#d9d9d9")
        self.btn_update_metre.configure(highlightcolor="black")
        self.btn_update_metre.configure(pady="0")
        self.btn_update_metre.configure(text='''Add''')
        self.btn_update_metre.configure(command=self.update_customer)

        self.cus_rel_id = uuid_handler.random_uuid()

    def search_info(self):
        hkid = self.entry_customer_id.get()

        conn = cx_Oracle.connect('std039/cestd039@144.214.177.102/xe')
        cursor = conn.cursor()
        cursor2 = conn.cursor()
        result = cursor.execute("SELECT * FROM CUSTOMER WHERE HKID = '%s'" %(hkid))
        result2 = cursor2.execute("SELECT to_char(birthday,'DD'), to_char(birthday,'MM'), to_char(birthday,'YYYY') FROM CUSTOMER WHERE HKID = '%s'" %(hkid))

        if not result:
            tk.messagebox.showwarning("Warning", "No record")
        else:
            for i in result:
                self.entry_firstname.insert(END, i[1])
                if i[2] == "M":
                    self.rbtn_f.configure(state='disabled')
                    self.rbtn_m.configure(state='active')
                elif i[2] == "F":
                    self.rbtn_m.configure(state='disabled')
                    self.rbtn_f.configure(state='active')

                for bd in result2:
                    day = int(bd[0]) -1
                    month = int(bd[1]) -1
                    year = int(bd[2]) -1920
                    self.combo_birthday_day.current(day)
                    self.combo_birthday_month.current(month)
                    self.combo_birthday_year.current(year)

                self.entry_phone1.insert(END, i[5])



    def update_customer(self):
        #variables
        hkid = (self.entry_customer_id.get()).upper()
        name = (self.entry_firstname.get()).upper()
        gender = (self.var.get()).upper()
        birthday = self.day.get() + "/" + self.month.get() + "/" + self.year.get()
        birthday = "TO_DATE('%s', 'DD/MM/YYYY')" % (birthday)
        phoneno = self.entry_phone1.get()
        address1 = (self.entry_address.get()).upper()
        address2 = (self.entry_address2.get()).upper()
        district = (self.district.get()).upper()

        conn = cx_Oracle.connect('std039/cestd039@144.214.177.102/xe')
        info_string = "'%s','%s','%s',%s,'%s','%s'" %(name,gender,hkid,birthday,phoneno,self.cus_rel_id)
        statement = "INSERT INTO CUSTOMER (name,sex,hkid,birthday,tel,rel_id) VALUES (%s)" %(info_string)
        cursor = conn.cursor()
        cursor.execute(statement)
        conn.commit()
        cursor.close()

        cursor_q = conn.cursor()
        result_q = cursor_q.execute("SELECT * FROM CUSTOMER WHERE rel_id = '%s'" % (self.cus_rel_id))
        conn.commit()
        for metre_cus_id in result_q:

            metre_rel_id = uuid_handler.random_uuid()

            conn = cx_Oracle.connect('std039/cestd039@144.214.177.102/xe')
            info_string = "'%s','%s','%s','%s','%s'" % (metre_cus_id[0], address1, address2, district, metre_rel_id)
            statement = "INSERT INTO METRE (customer_id,address_1,address_2,district,rel_id) VALUES (%s)" % (info_string)
            cursor = conn.cursor()
            cursor.execute(statement)
            cursor.close()

            cursor = conn.cursor()
            cursor.execute("SELECT ID FROM METRE WHERE REL_ID = '%s'" %(metre_rel_id))
            result = cursor.fetchall()

            for invoice_metre_id in result:

                invoice_rel_id = uuid_handler.random_uuid()

                month = int(time.strftime("%m")) -2
                year = int(time.strftime("%Y"))
                date = ("%s/%s/%s" %("01", month, year))
                date = "TO_DATE('%s', 'DD/MM/YYYY')" %(date)
                sql = "INSERT INTO INVOICE (METRE_ID, ISSUE_DATE, REL_ID) VALUES ('%s', %s, '%s')" %(invoice_metre_id[0], date, invoice_rel_id)
                cursor2 = conn.cursor()
                cursor2.execute(sql)
                conn.commit()
                # conn.close()


                cursor3 = conn.cursor()
                cursor3.execute("SELECT ID FROM INVOICE WHERE REL_ID = '%s'" %(invoice_rel_id))
                result3 = cursor3.fetchall()

                for id in result3:
                    payment_rel_id = uuid_handler.random_uuid()
                    sql_pay = "INSERT INTO PAYMENT_RECORD (INVOICE_ID, AMOUNT_PAID, BALANCE, REL_ID) VALUES ('%s','%s','%s','%s')" %(id[0], 0, 0, payment_rel_id)
                    pay_cur = conn.cursor()
                    pay_cur.execute(sql_pay)
                    conn.commit()

                    tk.messagebox.showinfo("Message", "Customer information insert successful")

    def gotoHome(self):
        # warning()
        qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")
        if qa == "yes":

            self.entry_customer_id.delete(0, 'end')
            self.entry_firstname.delete(0, 'end')
            self.entry_address.delete(0, 'end')
            self.entry_address2.delete(0, 'end')
            self.combo_district.set('')
            self.combo_birthday_day.set('')
            self.combo_birthday_month.set('')
            self.combo_birthday_year.set('')
            self.entry_phone1.delete(0, 'end')

            self.controller.show_frame("Home")
        else:
            None

    def gotoInvoice(self):
        # warning()
        qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")
        if qa == "yes":

            self.entry_customer_id.delete(0, 'end')
            self.entry_firstname.delete(0, 'end')
            self.entry_address.delete(0, 'end')
            self.entry_address2.delete(0, 'end')
            self.combo_district.set('')
            self.combo_birthday_day.set('')
            self.combo_birthday_month.set('')
            self.combo_birthday_year.set('')
            self.entry_phone1.delete(0, 'end')

            self.controller.show_frame("Invoice")
        else:
            None

    def gotoRecord(self):
        # warning()
        qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")
        if qa == "yes":

            self.entry_customer_id.delete(0, 'end')
            self.entry_firstname.delete(0, 'end')
            self.entry_address.delete(0, 'end')
            self.entry_address2.delete(0, 'end')
            self.combo_district.set('')
            self.combo_birthday_day.set('')
            self.combo_birthday_month.set('')
            self.combo_birthday_year.set('')
            self.entry_phone1.delete(0, 'end')

            self.controller.show_frame("Record")
        else:
            None

    def logout(self):
        # warning()
        qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")
        if qa == "yes":

            self.entry_customer_id.delete(0, 'end')
            self.entry_firstname.delete(0, 'end')
            self.entry_address.delete(0, 'end')
            self.entry_address2.delete(0, 'end')
            self.combo_district.set('')
            self.combo_birthday_day.set('')
            self.combo_birthday_month.set('')
            self.combo_birthday_year.set('')
            self.entry_phone1.delete(0, 'end')

            self.controller.show_frame("Login")
        else:
            None


class Invoice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#7aaaea")
        self.controller = controller

        font10 = "-family {Segoe UI} -size 20 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"
        font11 = "-family {Franklin Gothic Demi Cond} -size 16 -weight" \
                 " normal -slant roman -underline 1 -overstrike 0"
        font9 = "-family {Comic Sans MS} -size 16 -weight normal " \
                "-slant roman -underline 0 -overstrike 0"

        self.left_panel = tk.Frame(self)
        self.left_panel.place(relx=0.0, rely=0.056, relheight=0.944
                              , relwidth=0.193)
        self.left_panel.configure(borderwidth="2")
        self.left_panel.configure(background="#5eaad6")
        self.left_panel.configure(highlightbackground="#d9d9d9")
        self.left_panel.configure(highlightcolor="black")
        self.left_panel.configure(width=185)

        # self.left_btn_logout = tk.Button(self.left_panel)
        # self.left_btn_logout.place(relx=0.027, rely=0.949, height=30, width=175)
        # self.left_btn_logout.configure(activebackground="#807cea")
        # self.left_btn_logout.configure(activeforeground="#000000")
        # self.left_btn_logout.configure(background="#709dd8")
        # self.left_btn_logout.configure(borderwidth="3")
        # self.left_btn_logout.configure(disabledforeground="#a3a3a3")
        # self.left_btn_logout.configure(font=font11)
        # self.left_btn_logout.configure(foreground="#000000")
        # self.left_btn_logout.configure(highlightbackground="#d9d9d9")
        # self.left_btn_logout.configure(highlightcolor="black")
        # self.left_btn_logout.configure(pady="0")
        # self.left_btn_logout.configure(text='''Logout''')
        # self.left_btn_logout.configure(command=self.logout)

        self.left_btn_invoice = tk.Button(self.left_panel)
        self.left_btn_invoice.place(relx=0.003, rely=0.007, height=131, width=179)
        self.left_btn_invoice.configure(activebackground="#807cea")
        self.left_btn_invoice.configure(activeforeground="#000000")
        self.left_btn_invoice.configure(background="#4d8baf")
        self.left_btn_invoice.configure(borderwidth="0")
        self.left_btn_invoice.configure(cursor="hand2")
        self.left_btn_invoice.configure(disabledforeground="#a3a3a3")
        self.left_btn_invoice.configure(font=font10)
        self.left_btn_invoice.configure(foreground="#000000")
        self.left_btn_invoice.configure(highlightbackground="#d9d9d9")
        self.left_btn_invoice.configure(highlightcolor="black")
        self.left_btn_invoice.configure(pady="0")
        self.left_btn_invoice.configure(text='''Invoice''')

        self.left_btn_customer = tk.Button(self.left_panel)
        self.left_btn_customer.place(relx=0.003, rely=0.207, height=131, width=179)
        self.left_btn_customer.configure(activebackground="#807cea")
        self.left_btn_customer.configure(activeforeground="#000000")
        self.left_btn_customer.configure(background="#579dc6")
        self.left_btn_customer.configure(borderwidth="0")
        self.left_btn_customer.configure(cursor="hand2")
        self.left_btn_customer.configure(disabledforeground="#bcbcbc")
        self.left_btn_customer.configure(font=font10)
        self.left_btn_customer.configure(foreground="#000000")
        self.left_btn_customer.configure(highlightbackground="#d9d9d9")
        self.left_btn_customer.configure(highlightcolor="black")
        self.left_btn_customer.configure(pady="0")
        self.left_btn_customer.configure(text='''Register''')
        self.left_btn_customer.configure(command=self.gotoCustomer)

        self.left_btn_record = tk.Button(self.left_panel)
        self.left_btn_record.place(relx=0.003, rely=0.407, height=131, width=179)
        self.left_btn_record.configure(activebackground="#807cea")
        self.left_btn_record.configure(activeforeground="#000000")
        self.left_btn_record.configure(background="#579dc6")
        self.left_btn_record.configure(borderwidth="0")
        self.left_btn_record.configure(cursor="hand2")
        self.left_btn_record.configure(disabledforeground="#a3a3a3")
        self.left_btn_record.configure(font=font10)
        self.left_btn_record.configure(foreground="#000000")
        self.left_btn_record.configure(highlightbackground="#d9d9d9")
        self.left_btn_record.configure(highlightcolor="black")
        self.left_btn_record.configure(pady="0")
        self.left_btn_record.configure(text='''Record''')
        self.left_btn_record.configure(command=self.gotoRecord)

        # self.left_btn_payment = tk.Button(self.left_panel)
        # self.left_btn_payment.place(relx=0.003, rely=0.607, height=131, width=179)
        # self.left_btn_payment.configure(activebackground="#807cea")
        # self.left_btn_payment.configure(activeforeground="#000000")
        # self.left_btn_payment.configure(background="#579dc6")
        # self.left_btn_payment.configure(borderwidth="0")
        # self.left_btn_payment.configure(cursor="hand2")
        # self.left_btn_payment.configure(disabledforeground="#a3a3a3")
        # self.left_btn_payment.configure(font=font10)
        # self.left_btn_payment.configure(foreground="#000000")
        # self.left_btn_payment.configure(highlightbackground="#d9d9d9")
        # self.left_btn_payment.configure(highlightcolor="black")
        # self.left_btn_payment.configure(pady="0")
        # self.left_btn_payment.configure(text='''Payment''')

        self.top_panel = tk.Frame(self)
        self.top_panel.place(relx=-0.0, rely=0.0, relheight=0.063
                             , relwidth=1.002)
        self.top_panel.configure(borderwidth="2")
        self.top_panel.configure(background="#6f9cd6")
        self.top_panel.configure(highlightbackground="#d9d9d9")
        self.top_panel.configure(highlightcolor="black")
        self.top_panel.configure(width=965)

        self.top_login_text = tk.Label(self.top_panel)
        self.top_login_text.place(relx=0.0, rely=0.0, height=21, width=875)
        self.top_login_text.configure(activebackground="#f9f9f9")
        self.top_login_text.configure(activeforeground="black")
        self.top_login_text.configure(anchor=E)
        self.top_login_text.configure(background="#6f9cd6")
        self.top_login_text.configure(disabledforeground="#a3a3a3")
        self.top_login_text.configure(foreground="#000000")
        self.top_login_text.configure(highlightbackground="#d9d9d9")
        self.top_login_text.configure(highlightcolor="black")
        self.top_login_text.configure(text='''You have been login as:''')

        self.top_login_id = tk.Label(self.top_panel)
        self.top_login_id.place(relx=0.91, rely=0.0, height=21, width=85)
        self.top_login_id.configure(activebackground="#f9f9f9")
        self.top_login_id.configure(activeforeground="black")
        self.top_login_id.configure(background="#6f9cd6")
        self.top_login_id.configure(disabledforeground="#a3a3a3")
        self.top_login_id.configure(foreground="#000000")
        self.top_login_id.configure(highlightbackground="#d9d9d9")
        self.top_login_id.configure(highlightcolor="black")
        self.top_login_id.configure(text=operator)

        self.top_cwd_text = tk.Label(self.top_panel)
        self.top_cwd_text.place(relx=0.0, rely=0.444, height=21, width=135)
        self.top_cwd_text.configure(activebackground="#f9f9f9")
        self.top_cwd_text.configure(activeforeground="black")
        self.top_cwd_text.configure(anchor=W)
        self.top_cwd_text.configure(background="#6f9cd6")
        self.top_cwd_text.configure(disabledforeground="#a3a3a3")
        self.top_cwd_text.configure(foreground="#000000")
        self.top_cwd_text.configure(highlightbackground="#d9d9d9")
        self.top_cwd_text.configure(highlightcolor="black")
        self.top_cwd_text.configure(text='''Current Work Directory:''')

        self.top_cwd_bar_home = tk.Button(self.top_panel)
        self.top_cwd_bar_home.place(relx=0.14, rely=0.444, height=21, width=45)
        self.top_cwd_bar_home.configure(activebackground="#6f9cd6")
        self.top_cwd_bar_home.configure(activeforeground="#000000")
        self.top_cwd_bar_home.configure(background="#6f9cd6")
        self.top_cwd_bar_home.configure(borderwidth="0")
        self.top_cwd_bar_home.configure(cursor="hand2")
        self.top_cwd_bar_home.configure(disabledforeground="#a3a3a3")
        self.top_cwd_bar_home.configure(foreground="#000000")
        self.top_cwd_bar_home.configure(highlightbackground="#d9d9d9")
        self.top_cwd_bar_home.configure(highlightcolor="black")
        self.top_cwd_bar_home.configure(pady="0")
        self.top_cwd_bar_home.configure(text='''Home >''')
        self.top_cwd_bar_home.configure(command=self.gotoHome)

        self.top_cwd_bar_invoice = tk.Button(self.top_panel)
        self.top_cwd_bar_invoice.place(relx=0.187, rely=0.444, height=21
                                       , width=55)
        self.top_cwd_bar_invoice.configure(activebackground="#6f9cd6")
        self.top_cwd_bar_invoice.configure(activeforeground="#000000")
        self.top_cwd_bar_invoice.configure(background="#6f9cd6")
        self.top_cwd_bar_invoice.configure(borderwidth="0")
        self.top_cwd_bar_invoice.configure(cursor="hand2")
        self.top_cwd_bar_invoice.configure(disabledforeground="#a3a3a3")
        self.top_cwd_bar_invoice.configure(foreground="#000000")
        self.top_cwd_bar_invoice.configure(highlightbackground="#d9d9d9")
        self.top_cwd_bar_invoice.configure(highlightcolor="black")
        self.top_cwd_bar_invoice.configure(pady="0")
        self.top_cwd_bar_invoice.configure(text='''Invoice >''')
        self.top_cwd_bar_invoice.configure(width=55)

        self.invoice_customer = tk.Frame(self)
        self.invoice_customer.place(relx=0.193, rely=0.063, relheight=0.257
                                    , relwidth=0.807)
        self.invoice_customer.configure(borderwidth="2")
        self.invoice_customer.configure(background="#7aaaea")
        self.invoice_customer.configure(width=775)

        self.text_cusinfo = tk.Label(self.invoice_customer)
        self.text_cusinfo.place(relx=0.013, rely=0.054, height=35, width=223)
        self.text_cusinfo.configure(activebackground="#f9f9f9")
        self.text_cusinfo.configure(activeforeground="black")
        self.text_cusinfo.configure(anchor=W)
        self.text_cusinfo.configure(background="#7aaaea")
        self.text_cusinfo.configure(disabledforeground="#a3a3a3")
        self.text_cusinfo.configure(font=font9)
        self.text_cusinfo.configure(foreground="#000000")
        self.text_cusinfo.configure(highlightbackground="#d9d9d9")
        self.text_cusinfo.configure(highlightcolor="black")
        self.text_cusinfo.configure(text='''Metre Information''')

        self.text_customer_id = tk.Label(self.invoice_customer)
        self.text_customer_id.place(relx=0.105, rely=0.324, height=20, width=55)
        self.text_customer_id.configure(activebackground="#f9f9f9")
        self.text_customer_id.configure(activeforeground="black")
        self.text_customer_id.configure(background="#7aaaea")
        self.text_customer_id.configure(disabledforeground="#a3a3a3")
        self.text_customer_id.configure(foreground="#000000")
        self.text_customer_id.configure(highlightbackground="#d9d9d9")
        self.text_customer_id.configure(highlightcolor="black")
        self.text_customer_id.configure(text='''Metre ID:''')

        self.entry_customer_id = tk.Entry(self.invoice_customer)
        self.entry_customer_id.place(relx=0.181, rely=0.324, height=20
                                     , relwidth=0.147)
        self.entry_customer_id.configure(background="#ffffff")
        self.entry_customer_id.configure(disabledbackground="#c9c9c9")
        self.entry_customer_id.configure(disabledforeground="#a3a3a3")
        self.entry_customer_id.configure(font="TkFixedFont")
        self.entry_customer_id.configure(foreground="#000000")
        self.entry_customer_id.configure(highlightbackground="#d9d9d9")
        self.entry_customer_id.configure(highlightcolor="black")
        self.entry_customer_id.configure(insertbackground="black")
        self.entry_customer_id.configure(selectbackground="#c4c4c4")
        self.entry_customer_id.configure(selectforeground="black")

        self.text_firstname = tk.Label(self.invoice_customer)
        self.text_firstname.place(relx=0.104, rely=0.486, height=21, width=67)
        self.text_firstname.configure(activebackground="#f9f9f9")
        self.text_firstname.configure(activeforeground="black")
        self.text_firstname.configure(background="#7aaaea")
        self.text_firstname.configure(disabledforeground="#a3a3a3")
        self.text_firstname.configure(foreground="#000000")
        self.text_firstname.configure(highlightbackground="#d9d9d9")
        self.text_firstname.configure(highlightcolor="black")
        self.text_firstname.configure(text='''Name:''')

        self.entry_firstname = tk.Entry(self.invoice_customer)
        self.entry_firstname.place(relx=0.181, rely=0.486, height=20
                                   , relwidth=0.147)
        self.entry_firstname.configure(background="#ffffff")
        self.entry_firstname.configure(disabledbackground="#c9c9c9")
        self.entry_firstname.configure(disabledforeground="#a3a3a3")
        self.entry_firstname.configure(font="TkFixedFont")
        self.entry_firstname.configure(foreground="#000000")
        self.entry_firstname.configure(highlightbackground="#d9d9d9")
        self.entry_firstname.configure(highlightcolor="black")
        self.entry_firstname.configure(insertbackground="black")
        self.entry_firstname.configure(selectbackground="#c4c4c4")
        self.entry_firstname.configure(selectforeground="black")
        self.entry_firstname.configure(state="disabled")

        # self.text_lastname = tk.Label(self.invoice_customer)
        # self.text_lastname.place(relx=0.348, rely=0.486, height=21, width=67)
        # self.text_lastname.configure(activebackground="#f9f9f9")
        # self.text_lastname.configure(activeforeground="black")
        # self.text_lastname.configure(background="#7aaaea")
        # self.text_lastname.configure(disabledforeground="#a3a3a3")
        # self.text_lastname.configure(foreground="#000000")
        # self.text_lastname.configure(highlightbackground="#d9d9d9")
        # self.text_lastname.configure(highlightcolor="black")
        # self.text_lastname.configure(text='''Last name:''')
        #
        # self.entry_lastname = tk.Entry(self.invoice_customer)
        # self.entry_lastname.place(relx=0.439, rely=0.486, height=20
        #                           , relwidth=0.147)
        # self.entry_lastname.configure(background="#ffffff")
        # self.entry_lastname.configure(disabledbackground="#c9c9c9")
        # self.entry_lastname.configure(disabledforeground="#a3a3a3")
        # self.entry_lastname.configure(font="TkFixedFont")
        # self.entry_lastname.configure(foreground="#000000")
        # self.entry_lastname.configure(highlightbackground="#d9d9d9")
        # self.entry_lastname.configure(highlightcolor="black")
        # self.entry_lastname.configure(insertbackground="black")
        # self.entry_lastname.configure(selectbackground="#c4c4c4")
        # self.entry_lastname.configure(selectforeground="black")
        # self.entry_lastname.configure(state="disabled")

        self.text_address = tk.Label(self.invoice_customer)
        self.text_address.place(relx=0.09, rely=0.636, height=21, width=70)
        self.text_address.configure(activebackground="#f9f9f9")
        self.text_address.configure(activeforeground="black")
        self.text_address.configure(background="#7aaaea")
        self.text_address.configure(disabledforeground="#a3a3a3")
        self.text_address.configure(foreground="#000000")
        self.text_address.configure(highlightbackground="#d9d9d9")
        self.text_address.configure(highlightcolor="black")
        self.text_address.configure(text='''Address ID:''')

        # self.entry_address = ttk.Combobox(self.invoice_customer)
        # self.entry_address.place(relx=0.181, rely=0.649, height=20
        #                          , relwidth=0.418)
        # self.entry_address.configure(background="#ffffff")
        # self.entry_address.configure(font="TkFixedFont")
        # self.entry_address.configure(foreground="#000000")

        self.entry_address = ttk.Entry(self.invoice_customer)
        self.entry_address.place(relx=0.181, rely=0.649, height=20
                                 , relwidth=0.418)
        # self.entry_address.configure(background="#ffffff")
        self.entry_address.configure(font="TkFixedFont")
        self.entry_address.configure(foreground="#000000")

        # self.entry_metre_id = tk.Entry(self.invoice_customer)
        # self.entry_metre_id.place(relx=0.606, rely=0.649, height=20
        #                               , relwidth=0.108)
        # self.entry_metre_id.configure(background="white")
        # self.entry_metre_id.configure(disabledforeground="#a3a3a3")
        # self.entry_metre_id.configure(foreground="#000000")
        # self.entry_metre_id.configure(highlightbackground="#d9d9d9")
        # self.entry_metre_id.configure(highlightcolor="black")
        # self.entry_metre_id.configure(insertbackground="black")
        # self.entry_metre_id.configure(selectbackground="#c4c4c4")
        # self.entry_metre_id.configure(selectforeground="black")

        self.text_phone1 = tk.Label(self.invoice_customer)
        self.text_phone1.place(relx=0.097, rely=0.811, height=21, width=57)
        self.text_phone1.configure(activebackground="#f9f9f9")
        self.text_phone1.configure(activeforeground="black")
        self.text_phone1.configure(background="#7aaaea")
        self.text_phone1.configure(disabledforeground="#a3a3a3")
        self.text_phone1.configure(foreground="#000000")
        self.text_phone1.configure(highlightbackground="#d9d9d9")
        self.text_phone1.configure(highlightcolor="black")
        self.text_phone1.configure(text='''Phone no.:''')

        self.entry_phone1 = tk.Entry(self.invoice_customer)
        self.entry_phone1.place(relx=0.181, rely=0.811, height=20
                                , relwidth=0.147)
        self.entry_phone1.configure(background="#ffffff")
        self.entry_phone1.configure(disabledbackground="#c9c9c9")
        self.entry_phone1.configure(disabledforeground="#a3a3a3")
        self.entry_phone1.configure(font="TkFixedFont")
        self.entry_phone1.configure(foreground="#000000")
        self.entry_phone1.configure(highlightbackground="#d9d9d9")
        self.entry_phone1.configure(highlightcolor="black")
        self.entry_phone1.configure(insertbackground="black")
        self.entry_phone1.configure(selectbackground="#c4c4c4")
        self.entry_phone1.configure(selectforeground="black")
        self.entry_phone1.configure(state="disabled")

        self.btn_search = tk.Button(self.invoice_customer)
        self.btn_search.place(relx=0.335, rely=0.324, height=20, width=46)
        self.btn_search.configure(activebackground="#ea9f9f")
        self.btn_search.configure(activeforeground="#000000")
        self.btn_search.configure(background="#ea9f9f")
        self.btn_search.configure(disabledforeground="#a3a3a3")
        self.btn_search.configure(foreground="#000000")
        self.btn_search.configure(highlightbackground="#d9d9d9")
        self.btn_search.configure(highlightcolor="black")
        self.btn_search.configure(pady="0")
        self.btn_search.configure(text='''Search''')
        self.btn_search.configure(command=self.search)

        self.invoice_first_month = tk.Frame(self)
        self.invoice_first_month.place(relx=0.193, rely=0.319, relheight=0.201
                                       , relwidth=0.807)
        self.invoice_first_month.configure(borderwidth="2")
        self.invoice_first_month.configure(background="#7aaaea")
        self.invoice_first_month.configure(highlightbackground="#d9d9d9")
        self.invoice_first_month.configure(highlightcolor="black")
        self.invoice_first_month.configure(width=775)

        self.text_first_month = tk.Label(self.invoice_first_month)
        self.text_first_month.place(relx=0.013, rely=0.069, height=35, width=223)

        self.text_first_month.configure(activebackground="#f9f9f9")
        self.text_first_month.configure(activeforeground="black")
        self.text_first_month.configure(anchor=W)
        self.text_first_month.configure(background="#7aaaea")
        self.text_first_month.configure(disabledforeground="#a3a3a3")
        self.text_first_month.configure(font=font9)
        self.text_first_month.configure(foreground="#000000")
        self.text_first_month.configure(highlightbackground="#d9d9d9")
        self.text_first_month.configure(highlightcolor="black")
        self.text_first_month.configure(text='''First Month Detail''')

        self.text_fmsd = tk.Label(self.invoice_first_month)
        self.text_fmsd.place(relx=0.045, rely=0.414, height=20, width=95)
        self.text_fmsd.configure(activebackground="#f9f9f9")
        self.text_fmsd.configure(activeforeground="black")
        self.text_fmsd.configure(background="#7aaaea")
        self.text_fmsd.configure(disabledforeground="#a3a3a3")
        self.text_fmsd.configure(foreground="#000000")
        self.text_fmsd.configure(highlightbackground="#d9d9d9")
        self.text_fmsd.configure(highlightcolor="black")
        self.text_fmsd.configure(text='''Period start from''')
        self.text_fmsd.configure(width=95)

        fmsd = tk.StringVar()
        fmed = tk.StringVar()
        smsd = tk.StringVar()
        smed = tk.StringVar()

        fmsm = tk.StringVar()
        fmem = tk.StringVar()
        smsm = tk.StringVar()
        smem = tk.StringVar()

        fmsy = tk.StringVar()
        fmey = tk.StringVar()
        smsy = tk.StringVar()
        smey = tk.StringVar()

        self.combo_fmsd_day = ttk.Combobox(self.invoice_first_month)
        self.combo_fmsd_day.place(relx=0.181, rely=0.414, relheight=0.145
                                  , relwidth=0.068)
        self.combo_fmsd_day.configure(textvariable=fmsd)
        self.combo_fmsd_day.configure(width=53)
        self.combo_fmsd_day.configure(takefocus="")
        self.combo_fmsd_day['values'] = cmb_day
        self.combo_fmsd_day.configure(state="readonly")

        self.combo_fmsd_month = ttk.Combobox(self.invoice_first_month)
        self.combo_fmsd_month.place(relx=0.258, rely=0.414, relheight=0.145
                                    , relwidth=0.081)
        self.combo_fmsd_month.configure(textvariable=fmsm)
        self.combo_fmsd_month.configure(width=63)
        self.combo_fmsd_month.configure(takefocus="")
        self.combo_fmsd_month['values'] = cmb_month
        self.combo_fmsd_month.configure(state="readonly")

        self.combo_fmsd_year = ttk.Combobox(self.invoice_first_month)
        self.combo_fmsd_year.place(relx=0.348, rely=0.414, relheight=0.145
                                   , relwidth=0.094)
        self.combo_fmsd_year.configure(textvariable=fmsy)
        self.combo_fmsd_year.configure(width=73)
        self.combo_fmsd_year.configure(takefocus="")
        self.combo_fmsd_year['values'] = cmb_year
        self.combo_fmsd_year.configure(state="readonly")

        self.text_fmed = tk.Label(self.invoice_first_month)
        self.text_fmed.place(relx=0.155, rely=0.621, height=20, width=15)
        self.text_fmed.configure(activebackground="#f9f9f9")
        self.text_fmed.configure(activeforeground="black")
        self.text_fmed.configure(background="#7aaaea")
        self.text_fmed.configure(disabledforeground="#a3a3a3")
        self.text_fmed.configure(foreground="#000000")
        self.text_fmed.configure(highlightbackground="#d9d9d9")
        self.text_fmed.configure(highlightcolor="black")
        self.text_fmed.configure(text='''to''')
        self.text_fmed.configure(width=15)

        self.combo_fmed_day = ttk.Combobox(self.invoice_first_month)
        self.combo_fmed_day.place(relx=0.181, rely=0.621, relheight=0.145
                                  , relwidth=0.068)
        self.combo_fmed_day.configure(textvariable=fmed)
        self.combo_fmed_day.configure(takefocus="")
        self.combo_fmed_day['values'] = cmb_day
        self.combo_fmed_day.configure(state="readonly")

        self.combo_fmed_month = ttk.Combobox(self.invoice_first_month)
        self.combo_fmed_month.place(relx=0.258, rely=0.621, relheight=0.145
                                    , relwidth=0.081)
        self.combo_fmed_month.configure(textvariable=fmem)
        self.combo_fmed_month.configure(takefocus="")
        self.combo_fmed_month['values'] = cmb_month
        self.combo_fmed_month.configure(state="readonly")

        self.combo_fmed_year = ttk.Combobox(self.invoice_first_month)
        self.combo_fmed_year.place(relx=0.348, rely=0.621, relheight=0.145
                                   , relwidth=0.094)
        self.combo_fmed_year.configure(textvariable=fmey)
        self.combo_fmed_year.configure(takefocus="")
        self.combo_fmed_year['values'] = cmb_year
        self.combo_fmed_year.configure(state="readonly")

        self.text_fm_unit = tk.Label(self.invoice_first_month)
        self.text_fm_unit.place(relx=0.142, rely=0.828, height=20, width=25)
        self.text_fm_unit.configure(activebackground="#f9f9f9")
        self.text_fm_unit.configure(activeforeground="black")
        self.text_fm_unit.configure(background="#7aaaea")
        self.text_fm_unit.configure(disabledforeground="#a3a3a3")
        self.text_fm_unit.configure(foreground="#000000")
        self.text_fm_unit.configure(highlightbackground="#d9d9d9")
        self.text_fm_unit.configure(highlightcolor="black")
        self.text_fm_unit.configure(text='''Unit''')
        self.text_fm_unit.configure(width=25)

        self.entry_fm_unit = tk.Entry(self.invoice_first_month)
        self.entry_fm_unit.place(relx=0.181, rely=0.828, height=20
                                 , relwidth=0.07)
        self.entry_fm_unit.configure(background="white")
        self.entry_fm_unit.configure(disabledforeground="#a3a3a3")
        self.entry_fm_unit.configure(font="TkFixedFont")
        self.entry_fm_unit.configure(foreground="#000000")
        self.entry_fm_unit.configure(insertbackground="black")
        self.entry_fm_unit.configure(width=54)

        self.invoice_second_month = tk.Frame(self)
        self.invoice_second_month.place(relx=0.193, rely=0.521, relheight=0.229
                                          , relwidth=0.807)
        self.invoice_second_month.configure(borderwidth="2")
        self.invoice_second_month.configure(background="#7aaaea")
        self.invoice_second_month.configure(highlightbackground="#d9d9d9")
        self.invoice_second_month.configure(highlightcolor="black")
        self.invoice_second_month.configure(width=775)

        self.text_second_month = tk.Label(self.invoice_second_month)
        self.text_second_month.place(relx=0.013, rely=0.061, height=35
                                     , width=223)
        self.text_second_month.configure(activebackground="#f9f9f9")
        self.text_second_month.configure(activeforeground="black")
        self.text_second_month.configure(anchor=W)
        self.text_second_month.configure(background="#7aaaea")
        self.text_second_month.configure(disabledforeground="#a3a3a3")
        self.text_second_month.configure(font=font9)
        self.text_second_month.configure(foreground="#000000")
        self.text_second_month.configure(highlightbackground="#d9d9d9")
        self.text_second_month.configure(highlightcolor="black")
        self.text_second_month.configure(text='''Second Month Detail''')

        self.text_smsd = tk.Label(self.invoice_second_month)
        self.text_smsd.place(relx=0.045, rely=0.364, height=20, width=95)
        self.text_smsd.configure(activebackground="#f9f9f9")
        self.text_smsd.configure(activeforeground="black")
        self.text_smsd.configure(background="#7aaaea")
        self.text_smsd.configure(disabledforeground="#a3a3a3")
        self.text_smsd.configure(foreground="#000000")
        self.text_smsd.configure(highlightbackground="#d9d9d9")
        self.text_smsd.configure(highlightcolor="black")
        self.text_smsd.configure(text='''Period start from''')

        self.combo_smsd_day = ttk.Combobox(self.invoice_second_month)
        self.combo_smsd_day.place(relx=0.181, rely=0.364, relheight=0.127
                                  , relwidth=0.068)
        self.combo_smsd_day.configure(textvariable=smsd)
        self.combo_smsd_day.configure(takefocus="")
        self.combo_smsd_day['values'] = cmb_day
        self.combo_smsd_day.configure(state="readonly")

        self.combo_smsd_month = ttk.Combobox(self.invoice_second_month)
        self.combo_smsd_month.place(relx=0.258, rely=0.364, relheight=0.127
                                    , relwidth=0.081)
        self.combo_smsd_month.configure(textvariable=smsm)
        self.combo_smsd_month.configure(takefocus="")
        self.combo_smsd_month['values'] = cmb_month
        self.combo_smsd_month.configure(state="readonly")

        self.combo_smsd_year = ttk.Combobox(self.invoice_second_month)
        self.combo_smsd_year.place(relx=0.348, rely=0.364, relheight=0.127
                                   , relwidth=0.094)
        self.combo_smsd_year.configure(textvariable=smsy)
        self.combo_smsd_year.configure(takefocus="")
        self.combo_smsd_year['values'] = cmb_year
        self.combo_smsd_year.configure(state="readonly")

        self.text_smed = tk.Label(self.invoice_second_month)
        self.text_smed.place(relx=0.155, rely=0.545, height=20, width=15)
        self.text_smed.configure(activebackground="#f9f9f9")
        self.text_smed.configure(activeforeground="black")
        self.text_smed.configure(background="#7aaaea")
        self.text_smed.configure(disabledforeground="#a3a3a3")
        self.text_smed.configure(foreground="#000000")
        self.text_smed.configure(highlightbackground="#d9d9d9")
        self.text_smed.configure(highlightcolor="black")
        self.text_smed.configure(text='''to''')

        self.combo_smed_day = ttk.Combobox(self.invoice_second_month)
        self.combo_smed_day.place(relx=0.181, rely=0.545, relheight=0.127
                                  , relwidth=0.068)
        self.combo_smed_day.configure(textvariable=smed)
        self.combo_smed_day.configure(takefocus="")
        self.combo_smed_day['values'] = cmb_day
        self.combo_smed_day.configure(state="readonly")

        self.combo_smed_month = ttk.Combobox(self.invoice_second_month)
        self.combo_smed_month.place(relx=0.258, rely=0.545, relheight=0.127
                                    , relwidth=0.081)
        self.combo_smed_month.configure(textvariable=smem)
        self.combo_smed_month.configure(takefocus="")
        self.combo_smed_month['values'] = cmb_month
        self.combo_smed_month.configure(state="readonly")

        self.combo_smed_year = ttk.Combobox(self.invoice_second_month)
        self.combo_smed_year.place(relx=0.348, rely=0.545, relheight=0.127
                                   , relwidth=0.094)
        self.combo_smed_year.configure(textvariable=smey)
        self.combo_smed_year.configure(takefocus="")
        self.combo_smed_year['values'] = cmb_year
        self.combo_smed_year.configure(state="readonly")

        self.text_sm_unit = tk.Label(self.invoice_second_month)
        self.text_sm_unit.place(relx=0.142, rely=0.727, height=20, width=25)
        self.text_sm_unit.configure(activebackground="#f9f9f9")
        self.text_sm_unit.configure(activeforeground="black")
        self.text_sm_unit.configure(background="#7aaaea")
        self.text_sm_unit.configure(disabledforeground="#a3a3a3")
        self.text_sm_unit.configure(foreground="#000000")
        self.text_sm_unit.configure(highlightbackground="#d9d9d9")
        self.text_sm_unit.configure(highlightcolor="black")
        self.text_sm_unit.configure(text='''Unit''')

        self.entry_sm_unit = tk.Entry(self.invoice_second_month)
        self.entry_sm_unit.place(relx=0.181, rely=0.727, height=20
                                 , relwidth=0.07)
        self.entry_sm_unit.configure(background="white")
        self.entry_sm_unit.configure(disabledforeground="#a3a3a3")
        self.entry_sm_unit.configure(font="TkFixedFont")
        self.entry_sm_unit.configure(foreground="#000000")
        self.entry_sm_unit.configure(highlightbackground="#d9d9d9")
        self.entry_sm_unit.configure(highlightcolor="black")
        self.entry_sm_unit.configure(insertbackground="black")
        self.entry_sm_unit.configure(selectbackground="#c4c4c4")
        self.entry_sm_unit.configure(selectforeground="black")

        self.invoice_extra_cost = tk.Frame(self)
        self.invoice_extra_cost.place(relx=0.193, rely=0.75, relheight=0.194
                                        , relwidth=0.807)
        self.invoice_extra_cost.configure(borderwidth="2")
        self.invoice_extra_cost.configure(background="#7aaaea")
        self.invoice_extra_cost.configure(highlightbackground="#d9d9d9")
        self.invoice_extra_cost.configure(highlightcolor="black")
        self.invoice_extra_cost.configure(width=775)

        self.text_extra_cost = tk.Label(self.invoice_extra_cost)
        self.text_extra_cost.place(relx=0.013, rely=0.071, height=35, width=113)
        self.text_extra_cost.configure(activebackground="#f9f9f9")
        self.text_extra_cost.configure(activeforeground="black")
        self.text_extra_cost.configure(anchor=W)
        self.text_extra_cost.configure(background="#7aaaea")
        self.text_extra_cost.configure(disabledforeground="#a3a3a3")
        self.text_extra_cost.configure(font=font9)
        self.text_extra_cost.configure(foreground="#000000")
        self.text_extra_cost.configure(highlightbackground="#d9d9d9")
        self.text_extra_cost.configure(highlightcolor="black")
        self.text_extra_cost.configure(text='''Extra Cost''')
        self.text_extra_cost.configure(width=113)

        self.yesandno = tk.StringVar()
        # self.check_extra_cost = tk.Checkbutton(self.invoice_extra_cost)
        # self.check_extra_cost.place(relx=0.168, rely=0.143, relheight=0.107
        #                             , relwidth=0.027)
        # self.check_extra_cost.configure(activebackground="#7aaaea")
        # self.check_extra_cost.configure(activeforeground="#000000")
        # self.check_extra_cost.configure(background="#7aaaea")
        # self.check_extra_cost.configure(disabledforeground="#a3a3a3")
        # self.check_extra_cost.configure(foreground="#000000")
        # self.check_extra_cost.configure(highlightbackground="#d9d9d9")
        # self.check_extra_cost.configure(highlightcolor="black")
        # self.check_extra_cost.configure(justify=LEFT)
        # self.check_extra_cost.configure(variable=che76)
        # self.check_extra_cost.configure(width=21)
        # self.check_extra_cost.configure(command=self.ec_checked)

        self.ep_yes = tk.Radiobutton(self.invoice_extra_cost)
        self.ep_yes.place(relx=0.168, rely=0.107, relheight=0.179
                          , relwidth=0.049)
        self.ep_yes.configure(activebackground="#7aaaea")
        self.ep_yes.configure(activeforeground="#000000")
        self.ep_yes.configure(background="#7aaaea")
        self.ep_yes.configure(disabledforeground="#a3a3a3")
        self.ep_yes.configure(foreground="#000000")
        self.ep_yes.configure(highlightbackground="#d9d9d9")
        self.ep_yes.configure(highlightcolor="black")
        self.ep_yes.configure(justify=LEFT)
        self.ep_yes.configure(text='''Yes''')
        self.ep_yes.configure(value="Yes")
        self.ep_yes.configure(width=38)
        self.ep_yes.configure(variable=self.yesandno)
        self.ep_yes.configure(command=self.ep_ys)

        self.ep_no = tk.Radiobutton(self.invoice_extra_cost)
        self.ep_no.place(relx=0.232, rely=0.107, relheight=0.179
                                , relwidth=0.049)
        self.ep_no.configure(activebackground="#7aaaea")
        self.ep_no.configure(activeforeground="#000000")
        self.ep_no.configure(background="#7aaaea")
        self.ep_no.configure(disabledforeground="#a3a3a3")
        self.ep_no.configure(foreground="#000000")
        self.ep_no.configure(highlightbackground="#d9d9d9")
        self.ep_no.configure(highlightcolor="black")
        self.ep_no.configure(justify=LEFT)
        self.ep_no.configure(text='''No''')
        self.ep_no.configure(value="No")
        self.ep_no.configure(width=38)
        self.ep_no.configure(variable=self.yesandno)
        self.ep_no.configure(command=self.ep_n)

        # che77 = StringVar()
        # self.check_sp = tk.Checkbutton(self.invoice_extra_cost)
        # self.check_sp.place(relx=0.065, rely=0.357, relheight=0.179
        #                     , relwidth=0.111)
        # self.check_sp.configure(activebackground="#7aaaea")
        # self.check_sp.configure(activeforeground="#000000")
        # self.check_sp.configure(background="#7aaaea")
        # self.check_sp.configure(disabledforeground="#a3a3a3")
        # self.check_sp.configure(foreground="#000000")
        # self.check_sp.configure(highlightbackground="#d9d9d9")
        # self.check_sp.configure(highlightcolor="black")
        # self.check_sp.configure(justify=LEFT)
        # self.check_sp.configure(text='''Spare parts''')
        # self.check_sp.configure(variable=che77)
        # self.check_sp.configure(state="disabled")
        # self.check_sp.configure(command=self.sp_checked)
        #
        # self.entry_sp = tk.Entry(self.invoice_extra_cost)
        # self.entry_sp.place(relx=0.194, rely=0.357, height=20, relwidth=0.07)
        # self.entry_sp.configure(background="white")
        # self.entry_sp.configure(disabledforeground="#a3a3a3")
        # self.entry_sp.configure(font="TkFixedFont")
        # self.entry_sp.configure(foreground="#000000")
        # self.entry_sp.configure(insertbackground="black")
        # self.entry_sp.configure(width=54)
        # self.entry_sp.configure(state="disabled")
        #
        # che78 = StringVar()
        # self.check_install = tk.Checkbutton(self.invoice_extra_cost)
        # self.check_install.place(relx=0.065, rely=0.571, relheight=0.179
        #                          , relwidth=0.111)
        # self.check_install.configure(activebackground="#7aaaea")
        # self.check_install.configure(activeforeground="#000000")
        # self.check_install.configure(background="#7aaaea")
        # self.check_install.configure(disabledforeground="#a3a3a3")
        # self.check_install.configure(foreground="#000000")
        # self.check_install.configure(highlightbackground="#d9d9d9")
        # self.check_install.configure(highlightcolor="black")
        # self.check_install.configure(justify=LEFT)
        # self.check_install.configure(selectcolor="#ffffff")
        # self.check_install.configure(text='''Install parts''')
        # self.check_install.configure(variable=che78)
        # self.check_install.configure(state="disabled")
        # self.check_install.configure(command=self.install_checked)
        #
        # self.entry_install = tk.Entry(self.invoice_extra_cost)
        # self.entry_install.place(relx=0.194, rely=0.571, height=20
        #                          , relwidth=0.07)
        # self.entry_install.configure(background="white")
        # self.entry_install.configure(disabledforeground="#a3a3a3")
        # self.entry_install.configure(font="TkFixedFont")
        # self.entry_install.configure(foreground="#000000")
        # self.entry_install.configure(highlightbackground="#d9d9d9")
        # self.entry_install.configure(highlightcolor="black")
        # self.entry_install.configure(insertbackground="black")
        # self.entry_install.configure(selectbackground="#c4c4c4")
        # self.entry_install.configure(selectforeground="black")
        # self.entry_install.configure(state="disabled")

        self.text_item = tk.Label(self.invoice_extra_cost)
        self.text_item.place(relx=0.129, rely=0.357, height=21, width=33)
        self.text_item.configure(background="#7aaaea")
        self.text_item.configure(disabledforeground="#a3a3a3")
        self.text_item.configure(foreground="#000000")
        self.text_item.configure(text='''Item:''')

        self.entry_item = tk.Entry(self.invoice_extra_cost)
        self.entry_item.place(relx=0.181, rely=0.357, height=20, relwidth=0.186)
        self.entry_item.configure(background="white")
        self.entry_item.configure(disabledforeground="#a3a3a3")
        self.entry_item.configure(font="TkFixedFont")
        self.entry_item.configure(foreground="#000000")
        self.entry_item.configure(insertbackground="black")
        self.entry_item.configure(width=144)
        self.entry_item.configure(state="disabled")

        self.text_amount = tk.Label(self.invoice_extra_cost)
        self.text_amount.place(relx=0.103, rely=0.571, height=21, width=56)
        self.text_amount.configure(background="#7aaaea")
        self.text_amount.configure(disabledforeground="#a3a3a3")
        self.text_amount.configure(foreground="#000000")
        self.text_amount.configure(text='''Amount:''')

        self.entry_amount = tk.Entry(self.invoice_extra_cost)
        self.entry_amount.place(relx=0.181, rely=0.571, height=20
                                , relwidth=0.083)
        self.entry_amount.configure(background="white")
        self.entry_amount.configure(disabledforeground="#a3a3a3")
        self.entry_amount.configure(font="TkFixedFont")
        self.entry_amount.configure(foreground="#000000")
        self.entry_amount.configure(insertbackground="black")
        self.entry_amount.configure(width=64)
        self.entry_amount.insert(0, "0")
        self.entry_amount.configure(state="disabled")

        # che79 = StringVar()
        # self.check_maintenance = tk.Checkbutton(self.invoice_extra_cost)
        # self.check_maintenance.place(relx=0.065, rely=0.786, relheight=0.179
        #                              , relwidth=0.124)
        # self.check_maintenance.configure(activebackground="#7aaaea")
        # self.check_maintenance.configure(activeforeground="#000000")
        # self.check_maintenance.configure(background="#7aaaea")
        # self.check_maintenance.configure(disabledforeground="#a3a3a3")
        # self.check_maintenance.configure(foreground="#000000")
        # self.check_maintenance.configure(highlightbackground="#d9d9d9")
        # self.check_maintenance.configure(highlightcolor="black")
        # self.check_maintenance.configure(justify=LEFT)
        # self.check_maintenance.configure(text='''Maintenance''')
        # self.check_maintenance.configure(variable=che79)
        # self.check_maintenance.configure(width=96)
        # self.check_maintenance.configure(state="disabled")
        # self.check_maintenance.configure(command=self.maintenance_checked)
        #
        # self.entry_maintenance = tk.Entry(self.invoice_extra_cost)
        # self.entry_maintenance.place(relx=0.194, rely=0.786, height=20
        #                              , relwidth=0.07)
        # self.entry_maintenance.configure(background="white")
        # self.entry_maintenance.configure(disabledforeground="#a3a3a3")
        # self.entry_maintenance.configure(font="TkFixedFont")
        # self.entry_maintenance.configure(foreground="#000000")
        # self.entry_maintenance.configure(highlightbackground="#d9d9d9")
        # self.entry_maintenance.configure(highlightcolor="black")
        # self.entry_maintenance.configure(insertbackground="black")
        # self.entry_maintenance.configure(selectbackground="#c4c4c4")
        # self.entry_maintenance.configure(selectforeground="black")
        # self.entry_maintenance.configure(state="disabled")
        #
        # self.rm_1 = tk.Button(self.invoice_extra_cost)
        # self.rm_1.place(relx=0.284, rely=0.357, height=20, width=51)
        # self.rm_1.configure(activebackground="#ea9f9f")
        # self.rm_1.configure(activeforeground="#000000")
        # self.rm_1.configure(background="#ea9f9f")
        # self.rm_1.configure(disabledforeground="#a3a3a3")
        # self.rm_1.configure(foreground="#000000")
        # self.rm_1.configure(highlightbackground="#d9d9d9")
        # self.rm_1.configure(highlightcolor="black")
        # self.rm_1.configure(pady="0")
        # self.rm_1.configure(text='''remove''')
        # self.rm_1.configure(command=self.rm1)
        #
        # self.rm_2 = tk.Button(self.invoice_extra_cost)
        # self.rm_2.place(relx=0.284, rely=0.571, height=20, width=51)
        # self.rm_2.configure(activebackground="#ea9f9f")
        # self.rm_2.configure(activeforeground="#000000")
        # self.rm_2.configure(background="#ea9f9f")
        # self.rm_2.configure(disabledforeground="#a3a3a3")
        # self.rm_2.configure(foreground="#000000")
        # self.rm_2.configure(highlightbackground="#d9d9d9")
        # self.rm_2.configure(highlightcolor="black")
        # self.rm_2.configure(pady="0")
        # self.rm_2.configure(text='''remove''')
        # self.rm_2.configure(command=self.rm2)
        #
        # self.rm_3 = tk.Button(self.invoice_extra_cost)
        # self.rm_3.place(relx=0.284, rely=0.786, height=20, width=51)
        # self.rm_3.configure(activebackground="#ea9f9f")
        # self.rm_3.configure(activeforeground="#000000")
        # self.rm_3.configure(background="#ea9f9f")
        # self.rm_3.configure(disabledforeground="#a3a3a3")
        # self.rm_3.configure(foreground="#000000")
        # self.rm_3.configure(highlightbackground="#d9d9d9")
        # self.rm_3.configure(highlightcolor="black")
        # self.rm_3.configure(pady="0")
        # self.rm_3.configure(text='''remove''')
        # self.rm_3.configure(command=self.rm3)

        self.btn_submit = tk.Button(self)
        self.btn_submit.place(relx=0.885, rely=0.958, height=22, width=47)
        self.btn_submit.configure(activebackground="#ea9f9f")
        self.btn_submit.configure(activeforeground="#000000")
        self.btn_submit.configure(background="#ea9f9f")
        self.btn_submit.configure(disabledforeground="#d38f8f")
        self.btn_submit.configure(foreground="#000000")
        self.btn_submit.configure(highlightbackground="#d9d9d9")
        self.btn_submit.configure(highlightcolor="black")
        self.btn_submit.configure(pady="0")
        self.btn_submit.configure(text='''Submit''')
        self.btn_submit.configure(width=47)
        self.btn_submit.configure(state="disabled")
        self.btn_submit.configure(command=self.submit)

        # self.btn_reset = tk.Button(self)
        # self.btn_reset.place(relx=0.948, rely=0.958, height=22, width=39)
        # self.btn_reset.configure(activebackground="#ea9f9f")
        # self.btn_reset.configure(activeforeground="#000000")
        # self.btn_reset.configure(background="#ea9f9f")
        # self.btn_reset.configure(disabledforeground="#a3a3a3")
        # self.btn_reset.configure(foreground="#000000")
        # self.btn_reset.configure(highlightbackground="#d9d9d9")
        # self.btn_reset.configure(highlightcolor="black")
        # self.btn_reset.configure(pady="0")
        # self.btn_reset.configure(text='''Reset''')
        # self.btn_reset.configure(command=self.reset)

        # self.btn_generate = tk.Button(self)
        # self.btn_generate.place(relx=0.813, rely=0.958, height=22, width=58)
        # self.btn_generate.configure(activebackground="#ea9f9f")
        # self.btn_generate.configure(activeforeground="#000000")
        # self.btn_generate.configure(background="#ea9f9f")
        # self.btn_generate.configure(disabledforeground="#a3a3a3")
        # self.btn_generate.configure(foreground="#000000")
        # self.btn_generate.configure(highlightbackground="#d9d9d9")
        # self.btn_generate.configure(highlightcolor="black")
        # self.btn_generate.configure(pady="0")
        # self.btn_generate.configure(text='''Generate''')
        # self.btn_generate.configure(command=self.generate)

        global index
        index = ''

        self.metre_rel_id1 = uuid_handler.random_uuid()
        self.metre_rel_id2 = uuid_handler.random_uuid()
        self.ep_rel_id = uuid_handler.random_uuid()
        self.invoice_rel_id = uuid_handler.random_uuid()

    def search(self):
        global index
        input_id = self.entry_customer_id.get()
        # print(input_id)
        self.ad_list = []
        connstr = "std039/cestd039@144.214.177.102:1521/xe"
        conn = cx_Oracle.connect(connstr)
        cursor = conn.cursor()
        # sql = "SELECT * FROM CUSTOMER WHERE HKID = '%s'" %(input_id)
        cursor.execute("SELECT * FROM METRE WHERE ID = %s" %(input_id))
        result = cursor.fetchall()

        if result:
            for i in result:
                metre_id = i[0]
                cus_id = i[1]
                cursor2 = conn.cursor()
                cursor2.execute("SELECT * FROM CUSTOMER WHERE ID = %s" %(cus_id))
                result2 = cursor2.fetchall()
                for j in result2:

                    address = str(i[2]) + ", " + str(i[3]) + ", " + str(i[4])
                    # address = str(j[2]) + "," + str(j[3]) + "," + str(j[4]) + "  (" + uuid_handler.bytes_to_hex(j[0]) + ")"
                    # address = address.replace(" ", "_")

                    cus_id = j[0]
                    self.entry_address.delete(0, 'end')
                    self.entry_address.insert(END, address)
                    # self.entry_metre_id.delete(0, 'end')
                    # self.entry_metre_id.insert(END, metre_id)

                    self.entry_firstname.configure(state="normal")
                    self.entry_firstname.delete(0, 'end')
                    self.entry_firstname.insert(END, j[1])
                    self.entry_firstname.configure(state="disabled")

                    self.entry_phone1.configure(state="normal")
                    self.entry_phone1.delete(0, 'end')
                    self.entry_phone1.insert(END, j[5])
                    self.entry_phone1.configure(state="disabled")

                    if self.entry_phone1.get() != "":
                        self.btn_submit.configure(state="normal")
        elif not result:
            self.entry_address.delete(0, 'end')
            self.entry_firstname.configure(state="normal")
            self.entry_firstname.delete(0, 'end')
            self.entry_firstname.configure(state="disabled")
            self.entry_phone1.configure(state="normal")
            self.entry_phone1.delete(0, 'end')
            self.entry_phone1.configure(state="disabled")
            tk.messagebox.showwarning("Warning", "No such data")

    def submit(self):
        try:
            metre_id = self.entry_customer_id.get()
            # print(metre_id)
            fm_unit = Decimal(self.entry_fm_unit.get())
            for_fm_date = self.combo_fmsd_day.get() + "/" + self.combo_fmsd_month.get() + "/" +self.combo_fmsd_year.get()
            for_fm_date = "TO_DATE('%s', 'DD/MM/YYYY')" % (for_fm_date)
            print("1")

            for_fmed_date = self.combo_fmed_day.get() + "/" + self.combo_fmed_month.get() + "/" + self.combo_fmed_year.get()

            sm_unit = Decimal(self.entry_sm_unit.get())
            for_sm_date = self.combo_smsd_day.get() + "/" + self.combo_smsd_month.get() + "/" +self.combo_smsd_year.get()
            for_sm_date = "TO_DATE('%s', 'DD/MM/YYYY')" % (for_sm_date)
            print("2")

            for_smed_date = self.combo_smed_day.get() + "/" + self.combo_smed_month.get() + "/" + self.combo_smed_year.get()

            input_user = 1


            item = self.entry_item.get()
            amount = Decimal(self.entry_amount.get())
            status = self.yesandno.get()

            print("3")

            fm = Decimal(cal(fm_unit))
            print("33")
            sm = Decimal(cal(sm_unit))
            print("4")
            megaj = Decimal(48)
            fuel_ca = Decimal(0.0198)
            monthly_mc = Decimal(9.50)
            monthly_mc2 = Decimal(19)
            print("5")

            fuel_ca1 = Decimal(fm_unit * megaj * fuel_ca)
            fuel_ca2 = Decimal(sm_unit * megaj * fuel_ca)

            print("data got")

            connstr = "std039/cestd039@144.214.177.102:1521/xe"
            conn = cx_Oracle.connect(connstr)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO READING (METRE_ID, UNIT, READING_FOR_MONTH, REL_ID) VALUES ('%s', '%s', %s, '%s')" %(metre_id, fm_unit, for_fm_date, self.metre_rel_id1))


            cursor2 = conn.cursor()
            cursor2.execute("INSERT INTO READING (METRE_ID, UNIT, READING_FOR_MONTH, REL_ID) VALUES ('%s', '%s', %s, '%s')" %(metre_id, sm_unit, for_sm_date, self.metre_rel_id2))


            cur_bal = conn.cursor()
            cur_bal.execute("SELECT BALANCE FROM METRE WHERE ID = '%s'" %(metre_id))
            result_bal = cur_bal.fetchall()
            for b in result_bal:
                bl = Decimal(b[0])
                if status == "Yes":
                    ex = amount
                    total_amount = Decimal(fm + sm + ex + bl + fuel_ca1 + fuel_ca2 + monthly_mc2)
                    cure = conn.cursor()
                    cure.execute("INSERT INTO EXTRA_PAYMENT (METRE_ID, ITEM, REL_ID) VALUES ('%s', '%s', '%s')" %(metre_id, item, self.ep_rel_id))
                    cursor3 = conn.cursor()
                    cursor3.execute("INSERT INTO INVOICE (READING_1, READING_2, TOTAL_EXTRA_PAYMENT, METRE_ID, REL_ID, TOTAL) VALUES (%s, %s, %s, '%s', '%s', '%s')" % (fm_unit, sm_unit, amount, metre_id, self.invoice_rel_id, total_amount))

                else:
                    total_amount = Decimal(fm + sm + bl + fuel_ca1 + fuel_ca2 + monthly_mc2)
                    cursor3 = conn.cursor()
                    cursor3.execute("INSERT INTO INVOICE (READING_1, READING_2, METRE_ID, REL_ID, TOTAL) VALUES (%s, %s, '%s', '%s', '%s')" %(fm_unit, sm_unit, metre_id, self.invoice_rel_id, total_amount))


                conn.commit()
                message = tkinter.messagebox.askquestion("Message", "All details insert successful! Would you like to generate an invoice?")
                print(message)
                if message == 'yes':
                    print("ready")
                    new_conn = cx_Oracle.connect("std039/cestd039@144.214.177.102:1521/xe")
                    cursor_invoice = new_conn.cursor()
                    cursor_invoice.execute("SELECT * FROM INVOICE INNER JOIN METRE ON INVOICE.METRE_ID = METRE.ID WHERE INVOICE.REL_ID = '%s'" %(self.invoice_rel_id))
                    print("0")
                    gen_result = cursor_invoice.fetchall()

                    print("1")
                    for all in gen_result:

                        cursor_extra = new_conn.cursor()
                        cursor_extra.execute("SELECT * FROM (SELECT ITEM FROM EXTRA_PAYMENT WHERE METRE_ID = '%s' ORDER BY START_DATE DESC) WHERE ROWNUM = 1" %(all[5]))
                        print("2")
                        result_extra = cursor_extra.fetchall()
                        print("3")
                        print(result_extra)
                        if result_extra:
                            for e in result_extra:
                                print(e[0])
                                print("3.0")
                                # new1_conn = cx_Oracle.connect("std039/cestd039@144.214.177.102:1521/xe")
                                cursor_last_month = new_conn.cursor()
                                print("3.1")
                                cursor_last_month.execute("SELECT * FROM (SELECT * FROM PAYMENT_RECORD JOIN INVOICE ON PAYMENT_RECORD.INVOICE_ID = INVOICE.ID WHERE INVOICE.METRE_ID = '%s' ORDER BY PAYMENT_RECORD.DATE_PAID DESC) WHERE ROWNUM = 1" %(all[5]))
                                print("4")
                                result_last = cursor_last_month.fetchall()
                                print("5")
                                for l in result_last:
                                    print("6.0")
                                    cursor_customer = new_conn.cursor()
                                    print("6.01")
                                    cursor_customer.execute("SELECT NAME FROM CUSTOMER JOIN METRE ON METRE.CUSTOMER_ID = CUSTOMER.ID WHERE METRE.ID = '%s'" % (l[11]))
                                    print("6")
                                    gen_result2 = cursor_customer.fetchall()
                                    print("7")
                                    for n in gen_result2:
                                        print("data got")

                                        #units
                                        megaj = Decimal(48)
                                        fuel_ca = Decimal(0.0198)
                                        monthly_mc = Decimal(9.50)

                                        last_due = Decimal(l[13])
                                        last_paid = Decimal(l[2])
                                        last_paid_date = str(l[3])
                                        balance = Decimal(l[4])

                                        first_reading = all[1]
                                        second_reading = all[2]

                                        first_megaj = int(first_reading * megaj)
                                        second_megaj = int(second_reading * megaj)

                                        first_amount = Decimal(all[1])
                                        second_amount = Decimal(all[2])

                                        first_standard_gc = fm
                                        second_standard_gc = sm

                                        first_fca = Decimal(first_reading * fuel_ca)
                                        second_fca = Decimal(second_reading * fuel_ca)

                                        first_subtotal = 0 + first_standard_gc + first_fca + monthly_mc
                                        second_subtotal = 0 + second_standard_gc + second_fca + monthly_mc

                                        extra_name = e[0]
                                        extra_amount = all[3]

                                        total = all[7]
                                        ocf = Decimal(total - math.floor(total))
                                        #units end
                                        #invoice details
                                        invoice_id = all[0]
                                        invoice_metre_id = all[5]

                                        # issue_date = str(all[3])
                                        # print(issue_date)
                                        issue_date = datetime.date.today()
                                        due_date = datetime.date.today()+ datetime.timedelta(days=10)
                                        print("gen1")

                                        first_startd = str(self.combo_fmsd_day.get() + " " + self.combo_fmsd_month.get() + " " +self.combo_fmsd_year.get())
                                        first_endd = str(self.combo_fmed_day.get() + " " + self.combo_fmed_month.get() + " " + self.combo_fmed_year.get())
                                        second_startd = str(self.combo_smsd_day.get() + " " + self.combo_smsd_month.get() + " " +self.combo_smsd_year.get())
                                        second_endd = str(self.combo_smed_day.get() + " " + self.combo_smed_month.get() + " " + self.combo_smed_year.get())
                                        print("gen2")


                                        address1 = str(all[9])
                                        address2 = str(all[10])
                                        address3 = str(all[11])
                                        address4 = "HK"
                                        print("gen3")
                                        customer_id = all[8]
                                        print("gen4")

                                        customer_name = str(n[0])
                                        # invoice details end
                                        print("gen5")

                                        self.canvas = canvas.Canvas("Bill_%s.pdf" % (invoice_id), pagesize=letter)
                                        print("5.1")
                                        self.canvas.setLineWidth(.3)
                                        self.canvas.setFont('Helvetica-Bold', 16)
                                        self.canvas.drawImage(logo, 20, 730, width=130, height=50, mask=None)
                                        self.canvas.setFont('Helvetica-Bold', 12)
                                        self.canvas.drawRightString(580, 750, "Account Number: %s" % (customer_id))  # customer id
                                        print("5.2")
                                        self.canvas.setFont('Helvetica-Bold', 16)
                                        self.canvas.line(320, 740, 580, 740)
                                        self.canvas.line(320, 690, 580, 690)
                                        self.canvas.line(320, 740, 320, 690)
                                        self.canvas.line(580, 740, 580, 690)
                                        print("5.3")
                                        self.canvas.drawString(350, 720, "Account due: $%.2f" % (total))  # total bill amount
                                        self.canvas.drawString(350, 700, "Please pay by %s" % (due_date.strftime('%Y %b %d')))  # due date
                                        print("gen6")

                                        self.canvas.setFont('Courier-Oblique', 18)
                                        self.canvas.drawString(50, 700, "%s" % (customer_name))  # customer name
                                        self.canvas.drawString(50, 680, "%s" % (address1))  # customer address 1
                                        self.canvas.drawString(50, 665, "%s" % (address2))  # customer address 2
                                        self.canvas.drawString(50, 650, "%s" % (address3))  # customer address 3
                                        self.canvas.drawString(50, 635, "%s" % (address4))  # customer address 4
                                        print("gen7")

                                        self.canvas.setFont('Helvetica-Bold', 12)
                                        self.canvas.line(30, 607, 90, 607)
                                        self.canvas.line(30, 607, 30, 590)
                                        self.canvas.line(90, 607, 90, 590)
                                        self.canvas.drawString(40, 595, 'Bill Info')
                                        self.canvas.drawString(95, 595, 'Billing date: %s' % (issue_date.strftime('%Y %b %d')))  # billing date
                                        self.canvas.drawRightString(530, 595, 'Sub-Total')
                                        self.canvas.line(30, 590, 580, 590)
                                        print("gen8")

                                        self.canvas.drawString(30, 575, "Previous bill amount")
                                        self.canvas.drawRightString(430, 575, "%0.2f" % (last_due))  # pevious total
                                        self.canvas.drawString(30, 560, "Payment received : 22 DEC 2016")  #
                                        self.canvas.drawRightString(430, 560, "- %0.2f" % (last_paid))  #
                                        self.canvas.drawString(30, 545, "Balance brought forward")
                                        self.canvas.line(380, 558, 430, 558)
                                        self.canvas.drawRightString(430, 545, "%0.2f" % (balance))  # subtotal of Balance brought forward
                                        self.canvas.line(380, 540, 430, 540)
                                        self.canvas.drawRightString(530, 545, "$%0.2f" % (balance))  # subtotal of Balance brought forward
                                        print("gen9")

                                        self.canvas.setFont('Courier-Oblique', 10)
                                        self.canvas.line(30, 520, 375, 520)
                                        self.canvas.line(30, 495, 375, 495)
                                        self.canvas.drawCentredString(90, 510, "From: %s" % (first_startd))
                                        self.canvas.drawCentredString(215, 510, "1 unit = %s MJ" % (megaj))
                                        self.canvas.drawCentredString(325, 510, "Consumption(MJ):")
                                        self.canvas.line(30, 507, 375, 507)
                                        self.canvas.drawCentredString(90, 497, "To: %s" % (first_endd))
                                        self.canvas.drawCentredString(215, 497, "%s units *  %s MJ" % (first_reading, megaj))
                                        self.canvas.drawCentredString(325, 497, "%s" % (first_megaj))
                                        self.canvas.line(155, 520, 155, 495)
                                        self.canvas.line(375, 520, 375, 495)
                                        self.canvas.line(270, 520, 270, 495)
                                        self.canvas.line(30, 520, 30, 495)
                                        print("gen10")

                                        self.canvas.setFont('Helvetica-Bold', 12)
                                        self.canvas.drawString(30, 480, "Standard gas charge")
                                        self.canvas.drawRightString(430, 480, "$%0.2f" % (first_standard_gc))  # Standard gas charge 1
                                        self.canvas.drawString(30, 465, "Fuel cost adjustment (1.980 cents per MJ)")
                                        self.canvas.drawRightString(430, 465, "%0.2f" % (first_fca))  # Fuel cost adjustment 1
                                        self.canvas.drawString(30, 450, "Monthly maintainance Charge")
                                        self.canvas.drawRightString(430, 450, "%0.2f" % (monthly_mc))  # Monthly maintainance Charge
                                        self.canvas.drawRightString(430, 435, "%0.2f" % (first_subtotal))  # subtotal of  Standard gas charge 1
                                        self.canvas.line(380, 448, 430, 448)
                                        self.canvas.drawRightString(530, 435, "$%0.2f" % (first_subtotal))  # subtotal of  Standard gas charge 1
                                        self.canvas.line(380, 430, 430, 430)
                                        print("gen11")

                                        self.canvas.setFont('Courier-Oblique', 10)
                                        self.canvas.line(30, 425, 375, 425)
                                        self.canvas.line(30, 400, 375, 400)
                                        self.canvas.drawCentredString(90, 415, "From: %s" % (second_startd))
                                        self.canvas.drawCentredString(215, 415, "1 unit = %s MJ" % (megaj))
                                        self.canvas.drawCentredString(325, 415, "Consumption(MJ):")
                                        self.canvas.line(30, 413, 375, 413)
                                        self.canvas.drawCentredString(90, 403, "To: %s" % (second_endd))
                                        self.canvas.drawCentredString(215, 403, "%s units *  %s MJ" % (second_reading, megaj))
                                        self.canvas.drawCentredString(325, 403, "%s" % (second_megaj))
                                        self.canvas.line(270, 425, 270, 400)
                                        self.canvas.line(155, 425, 155, 400)
                                        self.canvas.line(375, 425, 375, 400)
                                        self.canvas.line(30, 425, 30, 400)
                                        print("12")

                                        self.canvas.setFont('Helvetica-Bold', 12)
                                        self.canvas.drawString(30, 385, "Standard gas charge")
                                        self.canvas.drawRightString(430, 385, "$%0.2f" % (second_standard_gc))  # Standard gas charge 2
                                        self.canvas.drawString(30, 370, "Fuel cost adjustment (1.980 cents per MJ)")
                                        self.canvas.drawRightString(430, 370, "%0.2f" % (second_fca))  # Fuel cost adjustment 2
                                        self.canvas.drawString(30, 355, "Monthly maintainance Charge")
                                        self.canvas.drawRightString(430, 355, "%0.2f" % (monthly_mc))  # Monthly maintainance Charge
                                        self.canvas.drawRightString(430, 340, "%0.2f" % (second_subtotal))  # subtotal of  Standard gas charge 2
                                        self.canvas.line(380, 353, 430, 353)
                                        self.canvas.drawRightString(530, 340, "$%0.2f" % (second_subtotal))  # subtotal of  Standard gas charge 2
                                        self.canvas.line(380, 335, 430, 335)
                                        print("13")

                                        # canvas.drawString(30, 300, "%s" % (extra1_name))  # extra item detail 1
                                        # canvas.drawRightString(430, 300, "$%0.2f" % (extra1_cost))  # extra item cost 1
                                        print(type(e[0]))
                                        self.canvas.drawString(30, 285, '%s' % (str(e[0])))  # extra item detail 2
                                        print("13.1")
                                        self.canvas.drawRightString(430, 285, "%0.2f" % (float(extra_amount)))  # extra item cost 2
                                        print("13.2")
                                        self.canvas.drawRightString(430, 270, "%0.2f" % (float(extra_amount)))  # subtotal of  extra item
                                        print("13.3")
                                        self.canvas.line(380, 283, 430, 283)
                                        self.canvas.drawRightString(530, 270, "$%0.2f" % (float(extra_amount)))  # subtotal of  extra item
                                        print("13.4")
                                        self.canvas.line(380, 265, 430, 265)
                                        print("14")

                                        self.canvas.drawString(30, 220, "Total bill amount")
                                        self.canvas.drawRightString(530, 220, "%0.2f" % (float(total)))  # cost of all item
                                        self.canvas.drawString(30, 205, "Odd cents to be carried forward")
                                        self.canvas.drawRightString(530, 205, "- %0.2f" % (ocf))  # Odd cents to be carried forward
                                        self.canvas.drawString(30, 190, "Amount due")
                                        self.canvas.line(480, 203, 530, 203)
                                        self.canvas.drawRightString(530, 190, "%0.2f" % (total))  # total bay amount
                                        self.canvas.line(480, 185, 530, 185)
                                        print("15")

                                        self.canvas.line(30, 100, 580, 100)
                                        self.canvas.drawCentredString(300, 60, "Invoice ID: %s" % (invoice_id))  # invoice id
                                        print("16")

                                        self.canvas.showPage()
                                        self.canvas.save()
                                        print("17")

                                        print("done")
                                        tkinter.messagebox.showinfo("Information", "Generation completed.")
                else:
                    print("ready")
                    new_conn = cx_Oracle.connect("std039/cestd039@144.214.177.102:1521/xe")
                    cursor_invoice = new_conn.cursor()
                    cursor_invoice.execute(
                        "SELECT * FROM INVOICE INNER JOIN METRE ON INVOICE.METRE_ID = METRE.ID WHERE INVOICE.REL_ID = '%s'" % (
                        self.invoice_rel_id))
                    print("0")
                    gen_result = cursor_invoice.fetchall()

                    print("1")
                    for all in gen_result:

                        cursor_extra = new_conn.cursor()
                        cursor_extra.execute(
                            "SELECT * FROM (SELECT ITEM FROM EXTRA_PAYMENT WHERE METRE_ID = '%s' ORDER BY START_DATE DESC) WHERE ROWNUM = 1" % (
                            all[5]))
                        print("2")
                        result_extra = cursor_extra.fetchall()
                        print("3")
                        print(result_extra)
                        if result_extra:
                            for e in result_extra:
                                print(e[0])
                                print("3.0")
                                # new1_conn = cx_Oracle.connect("std039/cestd039@144.214.177.102:1521/xe")
                                cursor_last_month = new_conn.cursor()
                                print("3.1")
                                cursor_last_month.execute(
                                    "SELECT * FROM (SELECT * FROM PAYMENT_RECORD JOIN INVOICE ON PAYMENT_RECORD.INVOICE_ID = INVOICE.ID WHERE INVOICE.METRE_ID = '%s' ORDER BY PAYMENT_RECORD.DATE_PAID DESC) WHERE ROWNUM = 1" % (
                                    all[5]))
                                print("4")
                                result_last = cursor_last_month.fetchall()
                                print("5")
                                for l in result_last:
                                    print("6.0")
                                    cursor_customer = new_conn.cursor()
                                    print("6.01")
                                    cursor_customer.execute(
                                        "SELECT NAME FROM CUSTOMER JOIN METRE ON METRE.CUSTOMER_ID = CUSTOMER.ID WHERE METRE.ID = '%s'" % (
                                        l[11]))
                                    print("6")
                                    gen_result2 = cursor_customer.fetchall()
                                    print("7")
                                    for n in gen_result2:
                                        print("data got")

                                        # units
                                        megaj = Decimal(48)
                                        fuel_ca = Decimal(0.0198)
                                        monthly_mc = Decimal(9.50)

                                        last_due = Decimal(l[13])
                                        last_paid = Decimal(l[2])
                                        last_paid_date = str(l[3])
                                        balance = Decimal(l[4])

                                        first_reading = all[1]
                                        second_reading = all[2]

                                        first_megaj = int(first_reading * megaj)
                                        second_megaj = int(second_reading * megaj)

                                        first_amount = Decimal(all[1])
                                        second_amount = Decimal(all[2])

                                        first_standard_gc = fm
                                        second_standard_gc = sm

                                        first_fca = Decimal(first_reading * fuel_ca)
                                        second_fca = Decimal(second_reading * fuel_ca)

                                        first_subtotal = 0 + first_standard_gc + first_fca + monthly_mc
                                        second_subtotal = 0 + second_standard_gc + second_fca + monthly_mc

                                        # extra_name = e[0]
                                        # extra_amount = all[3]

                                        total = all[7]
                                        ocf = Decimal(total - math.floor(total))
                                        # units end
                                        # invoice details
                                        invoice_id = all[0]
                                        invoice_metre_id = all[5]

                                        # issue_date = str(all[3])
                                        # print(issue_date)
                                        issue_date = datetime.date.today()
                                        due_date = datetime.date.today() + datetime.timedelta(days=10)
                                        print("gen1")

                                        first_startd = str(
                                            self.combo_fmsd_day.get() + " " + self.combo_fmsd_month.get() + " " + self.combo_fmsd_year.get())
                                        first_endd = str(
                                            self.combo_fmed_day.get() + " " + self.combo_fmed_month.get() + " " + self.combo_fmed_year.get())
                                        second_startd = str(
                                            self.combo_smsd_day.get() + " " + self.combo_smsd_month.get() + " " + self.combo_smsd_year.get())
                                        second_endd = str(
                                            self.combo_smed_day.get() + " " + self.combo_smed_month.get() + " " + self.combo_smed_year.get())
                                        print("gen2")

                                        address1 = str(all[9])
                                        address2 = str(all[10])
                                        address3 = str(all[11])
                                        address4 = "HK"
                                        print("gen3")
                                        customer_id = all[8]
                                        print("gen4")

                                        customer_name = str(n[0])
                                        # invoice details end
                                        print("gen5")

                                        self.canvas = canvas.Canvas("Bill_%s.pdf" % (invoice_id), pagesize=letter)
                                        print("5.1")
                                        self.canvas.setLineWidth(.3)
                                        self.canvas.setFont('Helvetica-Bold', 16)
                                        self.canvas.drawImage(logo, 20, 730, width=130, height=50, mask=None)
                                        self.canvas.setFont('Helvetica-Bold', 12)
                                        self.canvas.drawRightString(580, 750,
                                                                    "Account Number: %s" % (customer_id))  # customer id
                                        print("5.2")
                                        self.canvas.setFont('Helvetica-Bold', 16)
                                        self.canvas.line(320, 740, 580, 740)
                                        self.canvas.line(320, 690, 580, 690)
                                        self.canvas.line(320, 740, 320, 690)
                                        self.canvas.line(580, 740, 580, 690)
                                        print("5.3")
                                        self.canvas.drawString(350, 720,
                                                               "Account due: $%.2f" % (total))  # total bill amount
                                        self.canvas.drawString(350, 700, "Please pay by %s" % (
                                        due_date.strftime('%Y %b %d')))  # due date
                                        print("gen6")

                                        self.canvas.setFont('Courier-Oblique', 18)
                                        self.canvas.drawString(50, 700, "%s" % (customer_name))  # customer name
                                        self.canvas.drawString(50, 680, "%s" % (address1))  # customer address 1
                                        self.canvas.drawString(50, 665, "%s" % (address2))  # customer address 2
                                        self.canvas.drawString(50, 650, "%s" % (address3))  # customer address 3
                                        self.canvas.drawString(50, 635, "%s" % (address4))  # customer address 4
                                        print("gen7")

                                        self.canvas.setFont('Helvetica-Bold', 12)
                                        self.canvas.line(30, 607, 90, 607)
                                        self.canvas.line(30, 607, 30, 590)
                                        self.canvas.line(90, 607, 90, 590)
                                        self.canvas.drawString(40, 595, 'Bill Info')
                                        self.canvas.drawString(95, 595, 'Billing date: %s' % (
                                        issue_date.strftime('%Y %b %d')))  # billing date
                                        self.canvas.drawRightString(530, 595, 'Sub-Total')
                                        self.canvas.line(30, 590, 580, 590)
                                        print("gen8")

                                        self.canvas.drawString(30, 575, "Previous bill amount")
                                        self.canvas.drawRightString(430, 575, "%0.2f" % (last_due))  # pevious total
                                        self.canvas.drawString(30, 560, "Payment received : 22 DEC 2016")  #
                                        self.canvas.drawRightString(430, 560, "- %0.2f" % (last_paid))  #
                                        self.canvas.drawString(30, 545, "Balance brought forward")
                                        self.canvas.line(380, 558, 430, 558)
                                        self.canvas.drawRightString(430, 545, "%0.2f" % (
                                        balance))  # subtotal of Balance brought forward
                                        self.canvas.line(380, 540, 430, 540)
                                        self.canvas.drawRightString(530, 545, "$%0.2f" % (
                                        balance))  # subtotal of Balance brought forward
                                        print("gen9")

                                        self.canvas.setFont('Courier-Oblique', 10)
                                        self.canvas.line(30, 520, 375, 520)
                                        self.canvas.line(30, 495, 375, 495)
                                        self.canvas.drawCentredString(90, 510, "From: %s" % (first_startd))
                                        self.canvas.drawCentredString(215, 510, "1 unit = %s MJ" % (megaj))
                                        self.canvas.drawCentredString(325, 510, "Consumption(MJ):")
                                        self.canvas.line(30, 507, 375, 507)
                                        self.canvas.drawCentredString(90, 497, "To: %s" % (first_endd))
                                        self.canvas.drawCentredString(215, 497,
                                                                      "%s units *  %s MJ" % (first_reading, megaj))
                                        self.canvas.drawCentredString(325, 497, "%s" % (first_megaj))
                                        self.canvas.line(155, 520, 155, 495)
                                        self.canvas.line(375, 520, 375, 495)
                                        self.canvas.line(270, 520, 270, 495)
                                        self.canvas.line(30, 520, 30, 495)
                                        print("gen10")

                                        self.canvas.setFont('Helvetica-Bold', 12)
                                        self.canvas.drawString(30, 480, "Standard gas charge")
                                        self.canvas.drawRightString(430, 480, "$%0.2f" % (
                                        first_standard_gc))  # Standard gas charge 1
                                        self.canvas.drawString(30, 465, "Fuel cost adjustment (1.980 cents per MJ)")
                                        self.canvas.drawRightString(430, 465,
                                                                    "%0.2f" % (first_fca))  # Fuel cost adjustment 1
                                        self.canvas.drawString(30, 450, "Monthly maintainance Charge")
                                        self.canvas.drawRightString(430, 450, "%0.2f" % (
                                        monthly_mc))  # Monthly maintainance Charge
                                        self.canvas.drawRightString(430, 435, "%0.2f" % (
                                        first_subtotal))  # subtotal of  Standard gas charge 1
                                        self.canvas.line(380, 448, 430, 448)
                                        self.canvas.drawRightString(530, 435, "$%0.2f" % (
                                        first_subtotal))  # subtotal of  Standard gas charge 1
                                        self.canvas.line(380, 430, 430, 430)
                                        print("gen11")

                                        self.canvas.setFont('Courier-Oblique', 10)
                                        self.canvas.line(30, 425, 375, 425)
                                        self.canvas.line(30, 400, 375, 400)
                                        self.canvas.drawCentredString(90, 415, "From: %s" % (second_startd))
                                        self.canvas.drawCentredString(215, 415, "1 unit = %s MJ" % (megaj))
                                        self.canvas.drawCentredString(325, 415, "Consumption(MJ):")
                                        self.canvas.line(30, 413, 375, 413)
                                        self.canvas.drawCentredString(90, 403, "To: %s" % (second_endd))
                                        self.canvas.drawCentredString(215, 403,
                                                                      "%s units *  %s MJ" % (second_reading, megaj))
                                        self.canvas.drawCentredString(325, 403, "%s" % (second_megaj))
                                        self.canvas.line(270, 425, 270, 400)
                                        self.canvas.line(155, 425, 155, 400)
                                        self.canvas.line(375, 425, 375, 400)
                                        self.canvas.line(30, 425, 30, 400)
                                        print("12")

                                        self.canvas.setFont('Helvetica-Bold', 12)
                                        self.canvas.drawString(30, 385, "Standard gas charge")
                                        self.canvas.drawRightString(430, 385, "$%0.2f" % (
                                        second_standard_gc))  # Standard gas charge 2
                                        self.canvas.drawString(30, 370, "Fuel cost adjustment (1.980 cents per MJ)")
                                        self.canvas.drawRightString(430, 370,
                                                                    "%0.2f" % (second_fca))  # Fuel cost adjustment 2
                                        self.canvas.drawString(30, 355, "Monthly maintainance Charge")
                                        self.canvas.drawRightString(430, 355, "%0.2f" % (
                                        monthly_mc))  # Monthly maintainance Charge
                                        self.canvas.drawRightString(430, 340, "%0.2f" % (
                                        second_subtotal))  # subtotal of  Standard gas charge 2
                                        self.canvas.line(380, 353, 430, 353)
                                        self.canvas.drawRightString(530, 340, "$%0.2f" % (
                                        second_subtotal))  # subtotal of  Standard gas charge 2
                                        self.canvas.line(380, 335, 430, 335)
                                        print("13")

                                        # canvas.drawString(30, 300, "%s" % (extra1_name))  # extra item detail 1
                                        # canvas.drawRightString(430, 300, "$%0.2f" % (extra1_cost))  # extra item cost 1
                                        # print(type(e[0]))
                                        # self.canvas.drawString(30, 285, '%s' % (str(e[0])))  # extra item detail 2
                                        # print("13.1")
                                        # self.canvas.drawRightString(430, 285, "%0.2f" % (
                                        # float(extra_amount)))  # extra item cost 2
                                        # print("13.2")
                                        # self.canvas.drawRightString(430, 270, "%0.2f" % (
                                        # float(extra_amount)))  # subtotal of  extra item
                                        # print("13.3")
                                        # self.canvas.line(380, 283, 430, 283)
                                        # self.canvas.drawRightString(530, 270, "$%0.2f" % (
                                        # float(extra_amount)))  # subtotal of  extra item
                                        # print("13.4")
                                        # self.canvas.line(380, 265, 430, 265)
                                        # print("14")

                                        self.canvas.drawString(30, 220, "Total bill amount")
                                        self.canvas.drawRightString(530, 220,
                                                                    "%0.2f" % (float(total)))  # cost of all item
                                        self.canvas.drawString(30, 205, "Odd cents to be carried forward")
                                        self.canvas.drawRightString(530, 205, "- %0.2f" % (
                                        ocf))  # Odd cents to be carried forward
                                        self.canvas.drawString(30, 190, "Amount due")
                                        self.canvas.line(480, 203, 530, 203)
                                        self.canvas.drawRightString(530, 190, "%0.2f" % (total))  # total bay amount
                                        self.canvas.line(480, 185, 530, 185)
                                        print("15")

                                        self.canvas.line(30, 100, 580, 100)
                                        self.canvas.drawCentredString(300, 60,
                                                                      "Invoice ID: %s" % (invoice_id))  # invoice id
                                        print("16")

                                        self.canvas.showPage()
                                        self.canvas.save()
                                        print("17")

                                        print("done")
                                        tkinter.messagebox.showinfo("Information", "Generation completed.")
        except:
            tk.messagebox.showerror("Warning", "Missing data or incorrect format")


    def showaddress(self, event):
        global index
        index = self.ad_list.index(self.entry_address.get())

    def ep_ys(self):
        # self.check_sp.configure(state="normal")
        # self.check_install.configure(state="normal")
        # self.check_maintenance.configure(state="normal")

        self.entry_item.configure(state="normal")
        self.entry_amount.configure(state="normal")

    def ep_n(self):
        # self.check_sp.configure(state="disabled")
        # self.check_install.configure(state="disabled")
        # self.check_maintenance.configure(state="disabled")
        #
        # self.entry_sp.configure(state="disabled")
        # self.entry_install.configure(state="disabled")
        # self.entry_maintenance.configure(state="disabled")

        self.entry_item.configure(state="disabled")
        self.entry_amount.configure(state="disabled")

    def rm1(self):
        self.check_sp.configure(state="disabled")
        self.entry_sp.delete(0, 'end')
        self.rm_1.destroy()

    def rm2(self):
        self.check_install.configure(state="disabled")
        self.entry_install.delete(0, 'end')
        self.rm_2.destroy()

    def rm3(self):
        self.check_maintenance.configure(state="disabled")
        self.entry_maintenance.delete(0, 'end')
        self.rm_3.destroy()

    # # def ec_checked(self):
    #     self.check_sp.configure(state="normal")
    #     self.check_install.configure(state="normal")
    #     self.check_maintenance.configure(state="normal")

    def sp_checked(self):
        self.entry_sp.configure(state="normal")

    def install_checked(self):
        self.entry_install.configure(state="normal")

    def maintenance_checked(self):
        self.entry_maintenance.configure(state="normal")

    def gotoHome(self):
        # warning()
        qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")
        if qa == "yes":
            self.controller.show_frame("Home")
        else:
            None

    def gotoCustomer(self):
        # warning()
        qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")
        if qa == "yes":
            self.controller.show_frame("Customer")
        else:
            None

    def gotoRecord(self):
        # warning()
        qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")
        if qa == "yes":
            self.controller.show_frame("Record")
        else:
            None

    def logout(self):
        # warning()
        qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")
        if qa == "yes":
            self.controller.show_frame("Login")
        else:
            None

    def reset(self):
        tk.Entry().delete(0, 'end')


class Record(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#7aaaea")
        self.controller = controller

        font10 = "-family {Segoe UI} -size 20 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"
        font11 = "-family {Franklin Gothic Demi Cond} -size 16 -weight" \
                 " normal -slant roman -underline 1 -overstrike 0"
        font12 = "-family {Comic Sans MS} -size 16 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font12_2 = "-family {Comic Sans MS} -size 8 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 20 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"

        self.left_panel = tk.Frame(self)
        self.left_panel.place(relx=0.0, rely=0.056, relheight=0.944
                              , relwidth=0.193)
        self.left_panel.configure(borderwidth="2")
        self.left_panel.configure(background="#5eaad6")
        self.left_panel.configure(highlightbackground="#d9d9d9")
        self.left_panel.configure(highlightcolor="black")
        self.left_panel.configure(width=185)

        # self.left_btn_logout = tk.Button(self.left_panel)
        # self.left_btn_logout.place(relx=0.027, rely=0.949, height=30, width=175)
        # self.left_btn_logout.configure(activebackground="#807cea")
        # self.left_btn_logout.configure(activeforeground="#000000")
        # self.left_btn_logout.configure(background="#709dd8")
        # self.left_btn_logout.configure(borderwidth="3")
        # self.left_btn_logout.configure(disabledforeground="#a3a3a3")
        # self.left_btn_logout.configure(font=font11)
        # self.left_btn_logout.configure(foreground="#000000")
        # self.left_btn_logout.configure(highlightbackground="#d9d9d9")
        # self.left_btn_logout.configure(highlightcolor="black")
        # self.left_btn_logout.configure(pady="0")
        # self.left_btn_logout.configure(text='''Logout''')
        # self.left_btn_logout.configure(command=self.logout)

        self.left_btn_invoice = tk.Button(self.left_panel)
        self.left_btn_invoice.place(relx=0.003, rely=0.007, height=131, width=179)
        self.left_btn_invoice.configure(activebackground="#807cea")
        self.left_btn_invoice.configure(activeforeground="#000000")
        self.left_btn_invoice.configure(background="#579dc6")
        self.left_btn_invoice.configure(borderwidth="0")
        self.left_btn_invoice.configure(cursor="hand2")
        self.left_btn_invoice.configure(disabledforeground="#a3a3a3")
        self.left_btn_invoice.configure(font=font10)
        self.left_btn_invoice.configure(foreground="#000000")
        self.left_btn_invoice.configure(highlightbackground="#d9d9d9")
        self.left_btn_invoice.configure(highlightcolor="black")
        self.left_btn_invoice.configure(pady="0")
        self.left_btn_invoice.configure(text='''Invoice''')
        self.left_btn_invoice.configure(command=self.gotoInvoice)

        self.left_btn_customer = tk.Button(self.left_panel)
        self.left_btn_customer.place(relx=0.003, rely=0.207, height=131, width=179)
        self.left_btn_customer.configure(activebackground="#807cea")
        self.left_btn_customer.configure(activeforeground="#000000")
        self.left_btn_customer.configure(background="#579dc6")
        self.left_btn_customer.configure(borderwidth="0")
        self.left_btn_customer.configure(cursor="hand2")
        self.left_btn_customer.configure(disabledforeground="#bcbcbc")
        self.left_btn_customer.configure(font=font10)
        self.left_btn_customer.configure(foreground="#000000")
        self.left_btn_customer.configure(highlightbackground="#d9d9d9")
        self.left_btn_customer.configure(highlightcolor="black")
        self.left_btn_customer.configure(pady="0")
        self.left_btn_customer.configure(text='''Register''')
        self.left_btn_customer.configure(command=self.gotoCustomer)

        self.left_btn_record = tk.Button(self.left_panel)
        self.left_btn_record.place(relx=0.003, rely=0.407, height=131, width=179)
        self.left_btn_record.configure(activebackground="#807cea")
        self.left_btn_record.configure(activeforeground="#000000")
        self.left_btn_record.configure(background="#4d8baf")
        self.left_btn_record.configure(borderwidth="0")
        self.left_btn_record.configure(cursor="hand2")
        self.left_btn_record.configure(disabledforeground="#a3a3a3")
        self.left_btn_record.configure(font=font10)
        self.left_btn_record.configure(foreground="#000000")
        self.left_btn_record.configure(highlightbackground="#d9d9d9")
        self.left_btn_record.configure(highlightcolor="black")
        self.left_btn_record.configure(pady="0")
        self.left_btn_record.configure(text='''Record''')

        self.top_panel = tk.Frame(self)
        self.top_panel.place(relx=-0.0, rely=0.0, relheight=0.063
                             , relwidth=1.002)
        self.top_panel.configure(borderwidth="2")
        self.top_panel.configure(background="#6f9cd6")
        self.top_panel.configure(highlightbackground="#d9d9d9")
        self.top_panel.configure(highlightcolor="black")
        self.top_panel.configure(width=965)

        self.top_login_text = tk.Label(self.top_panel)
        self.top_login_text.place(relx=0.0, rely=0.0, height=21, width=875)
        self.top_login_text.configure(activebackground="#f9f9f9")
        self.top_login_text.configure(activeforeground="black")
        self.top_login_text.configure(anchor=E)
        self.top_login_text.configure(background="#6f9cd6")
        self.top_login_text.configure(disabledforeground="#a3a3a3")
        self.top_login_text.configure(foreground="#000000")
        self.top_login_text.configure(highlightbackground="#d9d9d9")
        self.top_login_text.configure(highlightcolor="black")
        self.top_login_text.configure(text='''You have been login as:''')

        self.top_login_id = tk.Label(self.top_panel)
        self.top_login_id.place(relx=0.91, rely=0.0, height=21, width=85)
        self.top_login_id.configure(activebackground="#f9f9f9")
        self.top_login_id.configure(activeforeground="black")
        self.top_login_id.configure(background="#6f9cd6")
        self.top_login_id.configure(disabledforeground="#a3a3a3")
        self.top_login_id.configure(foreground="#000000")
        self.top_login_id.configure(highlightbackground="#d9d9d9")
        self.top_login_id.configure(highlightcolor="black")
        self.top_login_id.configure(text=operator)

        self.top_cwd_text = tk.Label(self.top_panel)
        self.top_cwd_text.place(relx=0.0, rely=0.444, height=21, width=135)
        self.top_cwd_text.configure(activebackground="#f9f9f9")
        self.top_cwd_text.configure(activeforeground="black")
        self.top_cwd_text.configure(anchor=W)
        self.top_cwd_text.configure(background="#6f9cd6")
        self.top_cwd_text.configure(disabledforeground="#a3a3a3")
        self.top_cwd_text.configure(foreground="#000000")
        self.top_cwd_text.configure(highlightbackground="#d9d9d9")
        self.top_cwd_text.configure(highlightcolor="black")
        self.top_cwd_text.configure(text='''Current Work Directory:''')

        self.top_cwd_bar_home = tk.Button(self.top_panel)
        self.top_cwd_bar_home.place(relx=0.14, rely=0.444, height=21, width=45)
        self.top_cwd_bar_home.configure(activebackground="#6f9cd6")
        self.top_cwd_bar_home.configure(activeforeground="#000000")
        self.top_cwd_bar_home.configure(background="#6f9cd6")
        self.top_cwd_bar_home.configure(borderwidth="0")
        self.top_cwd_bar_home.configure(cursor="hand2")
        self.top_cwd_bar_home.configure(disabledforeground="#a3a3a3")
        self.top_cwd_bar_home.configure(foreground="#000000")
        self.top_cwd_bar_home.configure(highlightbackground="#d9d9d9")
        self.top_cwd_bar_home.configure(highlightcolor="black")
        self.top_cwd_bar_home.configure(pady="0")
        self.top_cwd_bar_home.configure(text='''Home >''')
        self.top_cwd_bar_home.configure(command=self.gotoHome)

        self.top_cwd_bar_invoice = tk.Button(self.top_panel)
        self.top_cwd_bar_invoice.place(relx=0.187, rely=0.444, height=21
                                       , width=55)
        self.top_cwd_bar_invoice.configure(activebackground="#6f9cd6")
        self.top_cwd_bar_invoice.configure(activeforeground="#000000")
        self.top_cwd_bar_invoice.configure(background="#6f9cd6")
        self.top_cwd_bar_invoice.configure(borderwidth="0")
        self.top_cwd_bar_invoice.configure(cursor="hand2")
        self.top_cwd_bar_invoice.configure(disabledforeground="#a3a3a3")
        self.top_cwd_bar_invoice.configure(foreground="#000000")
        self.top_cwd_bar_invoice.configure(highlightbackground="#d9d9d9")
        self.top_cwd_bar_invoice.configure(highlightcolor="black")
        self.top_cwd_bar_invoice.configure(pady="0")
        self.top_cwd_bar_invoice.configure(text='''Record >''')
        self.top_cwd_bar_invoice.configure(width=55)

        self.invoice_customer = tk.Frame(self)
        self.invoice_customer.place(relx=0.193, rely=0.063, relheight=0.882
                                    , relwidth=0.807)
        self.invoice_customer.configure(borderwidth="2")
        self.invoice_customer.configure(background="#7aaaea")
        self.invoice_customer.configure(highlightbackground="#d9d9d9")
        self.invoice_customer.configure(highlightcolor="black")
        self.invoice_customer.configure(width=775)

        self.text_record = tk.Label(self.invoice_customer)
        self.text_record.place(relx=0.013, rely=0.013, height=35, width=83)
        self.text_record.configure(activebackground="#f9f9f9")
        self.text_record.configure(activeforeground="black")
        self.text_record.configure(anchor=W)
        self.text_record.configure(background="#7aaaea")
        self.text_record.configure(disabledforeground="#a3a3a3")
        self.text_record.configure(font=font12)
        self.text_record.configure(foreground="#000000")
        self.text_record.configure(highlightbackground="#d9d9d9")
        self.text_record.configure(highlightcolor="black")
        self.text_record.configure(text='''Records''')
        self.text_record.configure(width=83)

        self.entry_search = tk.Entry(self.invoice_customer)
        self.entry_search.place(relx=0.142, rely=0.031, height=20
                                , relwidth=0.173)
        self.entry_search.configure(background="white")
        self.entry_search.configure(disabledforeground="#a3a3a3")
        self.entry_search.configure(font=font12_2)
        self.entry_search.configure(foreground="#000000")
        self.entry_search.configure(insertbackground="black")
        self.entry_search.configure(width=134)
        self.entry_search.insert(0, "(INVOICE ID)")

        self.btn_search = tk.Button(self.invoice_customer)
        self.btn_search.place(relx=0.323, rely=0.031, height=20, width=47)
        self.btn_search.configure(activebackground="#ea9f9f")
        self.btn_search.configure(activeforeground="#000000")
        self.btn_search.configure(background="#ea9f9f")
        self.btn_search.configure(disabledforeground="#a3a3a3")
        self.btn_search.configure(foreground="#000000")
        self.btn_search.configure(highlightbackground="#d9d9d9")
        self.btn_search.configure(highlightcolor="black")
        self.btn_search.configure(pady="0")
        self.btn_search.configure(text='''Search''')
        self.btn_search.configure(command=self.search)

        self.btn_showall = tk.Button(self.invoice_customer)
        self.btn_showall.place(relx=0.4, rely=0.031, height=20, width=57)
        self.btn_showall.configure(activebackground="#ea9f9f")
        self.btn_showall.configure(activeforeground="#000000")
        self.btn_showall.configure(background="#ea9f9f")
        self.btn_showall.configure(disabledforeground="#a3a3a3")
        self.btn_showall.configure(foreground="#000000")
        self.btn_showall.configure(highlightbackground="#d9d9d9")
        self.btn_showall.configure(highlightcolor="black")
        self.btn_showall.configure(pady="0")
        self.btn_showall.configure(text='''Show All''')
        self.btn_showall.configure(width=57)
        self.btn_showall.configure(command=self.showall)

        self.tree = ttk.Treeview(self.invoice_customer, show="headings", height=5)
        self.tree.place(relx=0.026, rely=0.079, relheight=0.85, relwidth=0.923)
        self.tree["columns"] = ("INVOICE_ID", "ISSUE_DATE", "METRE_ID", "FIRST_MONTH_UNIT", "SECOND_MONTH_UNIT", "CUSTOMER_NAME", "ADDRESS", "EXTRA_COST", "TOTAL")
        self.tree.column("INVOICE_ID", width=20)
        self.tree.column("ISSUE_DATE", width=60)
        self.tree.column("METRE_ID", width=20)
        self.tree.column("FIRST_MONTH_UNIT", width=20)
        self.tree.column("SECOND_MONTH_UNIT", width=20)
        self.tree.column("CUSTOMER_NAME", width=30)
        self.tree.column("ADDRESS", width=80)
        self.tree.column("EXTRA_COST", width=20)
        self.tree.column("TOTAL", width=20)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.title(),
                              command=lambda c=col: sortby(self.tree, c, 0))

        connstr = "std039/cestd039@144.214.177.102:1521/xe"
        conn = cx_Oracle.connect(connstr)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM INVOICE")
        result = cursor.fetchall()
        item = self.tree.get_children()
        for r in item:
            self.tree.delete(r)

        for a in result:
            invoice_id = a[0]
            reading1 = a[1]
            meter_id = a[5]
            cursor4 = conn.cursor()
            cursor4.execute("SELECT * FROM METRE WHERE ID = '%s'" % (meter_id))
            result4 = cursor4.fetchall()

            for k in result4:
                cus_id = k[1]
                cursor5 = conn.cursor()
                cursor5.execute("SELECT NAME FROM CUSTOMER WHERE ID = '%s'" % (cus_id))
                result5 = cursor5.fetchall()
                address = str(k[2]) + ", " + str(k[3]) + ", " + str(k[4])

                balance = float(k[6])
                if a[1] == 0:
                    if a[2] == 0:
                        # total = balance
                        self.tree.insert("", 0, values=(
                        invoice_id, str(a[4]), meter_id, a[1], a[2], result5, address, a[3], '%.2f' %float(a[7])))
                    else:
                        # total = fm + sm + a[3] + balance
                        self.tree.insert("", 0, values=(
                        invoice_id, str(a[4]), meter_id, a[1], a[2], result5, address, a[3], '%.2f' %float(a[7])))
                else:
                    # total = fm + sm + a[3] + balance
                    self.tree.insert("", 0, values=(invoice_id, str(a[4]), meter_id, a[1], a[2], result5, address, a[3], '%.2f' %float(a[7])))

                conn.commit()

        self.ysb = tk.Scrollbar(self.invoice_customer, orient=VERTICAL)
        self.ysb.place(relx=0.948, rely=0.079, relheight=0.85
                       , relwidth=0.032)
        self.xsb = tk.Scrollbar(self.invoice_customer, orient=HORIZONTAL)
        self.xsb.place(relx=0.026, rely=0.929, relheight=0.039
                              , relwidth=0.923)

        self.tree.bind("<Double-1>", self.doubleClick)
        self.tree.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.ysb.configure(command=self.tree.yview)
        self.xsb.configure(command=self.tree.xview)

    def showall(self):
        connstr = "std039/cestd039@144.214.177.102:1521/xe"
        conn = cx_Oracle.connect(connstr)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM INVOICE")
        result = cursor.fetchall()
        item = self.tree.get_children()
        self.entry_search.delete(0, 'end')
        for r in item:
            self.tree.delete(r)

        for a in result:
            invoice_id = a[0]
            reading1 = a[1]
            meter_id = a[5]
            cursor4 = conn.cursor()
            cursor4.execute("SELECT * FROM METRE WHERE ID = '%s'" % (meter_id))
            result4 = cursor4.fetchall()

            for k in result4:
                cus_id = k[1]
                cursor5 = conn.cursor()
                cursor5.execute("SELECT NAME FROM CUSTOMER WHERE ID = '%s'" % (cus_id))
                result5 = cursor5.fetchall()
                address = str(k[2]) + ", " + str(k[3]) + ", " + str(k[4])

                fm = cal(a[1])
                sm = cal(a[2])
                if a[1] == 0:
                    if a[2] == 0:
                        total = 0
                        self.tree.insert("", 0, values=(
                            invoice_id, str(a[4]), meter_id, a[1], a[2], result5, address, a[3], a[7]))
                    else:
                        total = fm + sm + a[3]
                        self.tree.insert("", 0, values=(
                            invoice_id, str(a[4]), meter_id, a[1], a[2], result5, address, a[3], a[7]))
                else:
                    total = fm + sm + a[3]

                    self.tree.insert("", 0, values=(
                    invoice_id, str(a[4]), meter_id, a[1], a[2], result5, address, a[3], a[7]))

                conn.commit()

    def search(self):
        user_input = self.entry_search.get()
        print(user_input)

        connstr = "std039/cestd039@144.214.177.102:1521/xe"
        conn = cx_Oracle.connect(connstr)
        cursor = conn.cursor()

        pointer = cursor.execute("SELECT * FROM INVOICE WHERE ID = '%s'" % (user_input))
        result = cursor.fetchall()
        if result:
            item = self.tree.get_children()
            for r in item:
                self.tree.delete(r)

            for a in result:
                invoice_id = a[0]
                reading1 = a[1]
                meter_id = a[5]
                cursor4 = conn.cursor()
                cursor4.execute("SELECT * FROM METRE WHERE ID = '%s'" % (meter_id))
                result4 = cursor4.fetchall()

                for k in result4:
                    cus_id = k[1]
                    cursor5 = conn.cursor()
                    cursor5.execute("SELECT NAME FROM CUSTOMER WHERE ID = '%s'" % (cus_id))
                    result5 = cursor5.fetchall()
                    address = str(k[2]) + ", " + str(k[3]) + ", " + str(k[4])

                    fm = cal(a[1])
                    sm = cal(a[2])
                    if a[1] == 0:
                        if a[2] == 0:
                            total = 0
                            self.tree.insert("", 0, values=(
                                invoice_id, str(a[4]), meter_id, a[1], a[2], result5, address, a[3], a[7]))
                        else:
                            total = fm + sm + a[3]
                            self.tree.insert("", 0, values=(
                                invoice_id, str(a[4]), meter_id, a[1], a[2], result5, address, a[3], a[7]))
                    else:
                        total = fm + sm + a[3]

                        self.tree.insert("", 0, values=(
                        invoice_id, str(a[4]), meter_id, a[1], a[2], result5, address, a[3], a[7]))

                    conn.commit()

        elif not result:
            nodata = tk.messagebox.askquestion("Warning", "No such data. Would you like to insert new information?")
            if nodata == "yes":
                self.controller.show_frame("Invoice")


    def doubleClick(self, event):
        selected_invoice_id = self.tree.item(self.tree.selection())['values'][0]
        print(selected_invoice_id)
        selected_meter = self.tree.item(self.tree.selection())['values'][2]
        selected_amount = self.tree.item(self.tree.selection())['values'][8]
        # print(selected_invoice_id)
        # print(selected_meter)
        connstr = "std039/cestd039@144.214.177.102:1521/xe"
        conn = cx_Oracle.connect(connstr)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PAYMENT_RECORD WHERE INVOICE_ID = '%s'" %(selected_invoice_id))
        result = cursor.fetchall()

        for j in result:
            cursor2 = conn.cursor()
            reading_id = j[3]
            cursor2.execute("SELECT * FROM READING WHERE ID = '%s'" %(reading_id))
            result2 = cursor2.fetchall()


        font11 = "-family {Comic Sans MS} -size 16 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"

        self.view = Toplevel(self, bg="#7aaaea")
        self.view.title("Invoice Details")
        self.view.geometry("400x700+1004+135")

        self.frame_payment = tk.Frame(self.view)
        self.frame_payment.place(relx=0.0, rely=0.0, relheight=0.429
                                 , relwidth=1.0)
        self.frame_payment.configure(borderwidth="2")
        self.frame_payment.configure(background="#7aaaea")
        self.frame_payment.configure(width=125)

        self.text_details = tk.Label(self.frame_payment)
        self.text_details.place(relx=0.025, rely=0.033, height=35, width=202)
        self.text_details.configure(activebackground="#f9f9f9")
        self.text_details.configure(activeforeground="black")
        self.text_details.configure(background="#7aaaea")
        self.text_details.configure(disabledforeground="#a3a3a3")
        self.text_details.configure(font=font11)
        self.text_details.configure(foreground="#000000")
        self.text_details.configure(highlightbackground="#d9d9d9")
        self.text_details.configure(highlightcolor="black")
        self.text_details.configure(text='''Invoice Information''')

        self.text_invoice_id = tk.Label(self.frame_payment)
        self.text_invoice_id.place(relx=0.05, rely=0.167, height=21, width=61)
        self.text_invoice_id.configure(background="#7aaaea")
        self.text_invoice_id.configure(disabledforeground="#a3a3a3")
        self.text_invoice_id.configure(foreground="#000000")
        self.text_invoice_id.configure(text='''Invoice ID:''')

        self.entry_invoice_id = tk.Entry(self.frame_payment)
        self.entry_invoice_id.place(relx=0.25, rely=0.167, height=20
                                    , relwidth=0.26)
        self.entry_invoice_id.configure(background="white")
        self.entry_invoice_id.configure(disabledforeground="#a3a3a3")
        self.entry_invoice_id.configure(font="TkFixedFont")
        self.entry_invoice_id.configure(foreground="#000000")
        self.entry_invoice_id.configure(insertbackground="black")
        self.entry_invoice_id.configure(width=104)
        self.entry_invoice_id.insert(END, selected_invoice_id)
        self.entry_invoice_id.configure(state="disabled")

        self.text_metre_id = tk.Label(self.frame_payment)
        self.text_metre_id.place(relx=0.075, rely=0.3, height=21, width=54)
        self.text_metre_id.configure(activebackground="#f9f9f9")
        self.text_metre_id.configure(activeforeground="black")
        self.text_metre_id.configure(background="#7aaaea")
        self.text_metre_id.configure(disabledforeground="#a3a3a3")
        self.text_metre_id.configure(foreground="#000000")
        self.text_metre_id.configure(highlightbackground="#d9d9d9")
        self.text_metre_id.configure(highlightcolor="black")
        self.text_metre_id.configure(text='''Metre ID:''')


        self.entry_customer_id = tk.Entry(self.frame_payment)
        self.entry_customer_id.place(relx=0.25, rely=0.3, height=20
                                     , relwidth=0.26)
        self.entry_customer_id.configure(background="white")
        self.entry_customer_id.configure(disabledforeground="#a3a3a3")
        self.entry_customer_id.configure(font="TkFixedFont")
        self.entry_customer_id.configure(foreground="#000000")
        self.entry_customer_id.configure(insertbackground="black")
        self.entry_customer_id.configure(width=104)
        self.entry_customer_id.insert(END, selected_meter)
        self.entry_customer_id.configure(state="disabled")

        self.text_amount_due = tk.Label(self.frame_payment)
        self.text_amount_due.place(relx=0.025, rely=0.433, height=21, width=73)
        self.text_amount_due.configure(activebackground="#f9f9f9")
        self.text_amount_due.configure(activeforeground="black")
        self.text_amount_due.configure(background="#7aaaea")
        self.text_amount_due.configure(disabledforeground="#a3a3a3")
        self.text_amount_due.configure(foreground="#000000")
        self.text_amount_due.configure(highlightbackground="#d9d9d9")
        self.text_amount_due.configure(highlightcolor="black")
        self.text_amount_due.configure(text='''Amount due:''')

        self.entry_amount_due = tk.Entry(self.frame_payment)
        self.entry_amount_due.place(relx=0.25, rely=0.433,height=20, relwidth=0.26)
        self.entry_amount_due.configure(background="white")
        self.entry_amount_due.configure(disabledforeground="#a3a3a3")
        self.entry_amount_due.configure(font="TkFixedFont")
        self.entry_amount_due.configure(foreground="#000000")
        self.entry_amount_due.configure(insertbackground="black")
        self.entry_amount_due.configure(width=104)
        self.entry_amount_due.insert(END, selected_amount)
        self.entry_amount_due.configure(state="disabled")

        self.text_amount_pay = tk.Label(self.frame_payment)
        self.text_amount_pay.place(relx=0.025, rely=0.567, height=21, width=75)
        self.text_amount_pay.configure(background="#7aaaea")
        self.text_amount_pay.configure(disabledforeground="#a3a3a3")
        self.text_amount_pay.configure(foreground="#000000")
        self.text_amount_pay.configure(text='''Amount pay:''')

        self.entry_amount_pay = tk.Entry(self.frame_payment)
        self.entry_amount_pay.place(relx=0.25, rely=0.567, height=20
                                    , relwidth=0.26)
        self.entry_amount_pay.configure(background="white")
        self.entry_amount_pay.configure(disabledforeground="#a3a3a3")
        self.entry_amount_pay.configure(foreground="#000000")
        self.entry_amount_pay.configure(insertbackground="black")
        self.entry_amount_pay.configure(width=104)

        self.text_balance = tk.Label(self.frame_payment)
        self.text_balance.place(relx=0.088, rely=0.70, height=21, width=50)
        self.text_balance.configure(background="#7aaaea")
        self.text_balance.configure(disabledforeground="#a3a3a3")
        self.text_balance.configure(foreground="#000000")
        self.text_balance.configure(text='''Balance:''')

        self.text_balance_amount = tk.Label(self.frame_payment)
        self.text_balance_amount.place(relx=0.25, rely=0.70, height=21
                                       , width=104)
        self.text_balance_amount.configure(anchor=W)
        self.text_balance_amount.configure(background="#7aaaea")
        self.text_balance_amount.configure(disabledforeground="#a3a3a3")
        self.text_balance_amount.configure(foreground="#000000")
        self.text_balance_amount.configure(text='')
        self.text_balance_amount.configure(width=104)

        self.btn_pay = tk.Button(self.frame_payment)
        self.btn_pay.place(relx=0.45, rely=0.833, height=24, width=30)
        self.btn_pay.configure(activebackground="#ea9f9f")
        self.btn_pay.configure(activeforeground="#000000")
        self.btn_pay.configure(background="#ea9f9f")
        self.btn_pay.configure(disabledforeground="#a3a3a3")
        self.btn_pay.configure(foreground="#000000")
        self.btn_pay.configure(highlightbackground="#d9d9d9")
        self.btn_pay.configure(highlightcolor="black")
        self.btn_pay.configure(pady="0")
        self.btn_pay.configure(text='''Pay''')
        self.btn_pay.configure(command=self.pay)

        connstr = "std039/cestd039@144.214.177.102:1521/xe"
        conn = cx_Oracle.connect(connstr)
        cursor = conn.cursor()
        sql1 = cursor.execute("SELECT * FROM PAYMENT_RECORD WHERE INVOICE_ID = '%s'" % (selected_invoice_id))
        print(sql1)
        result2 = cursor.fetchall()
        if result2:
            for paid in result2:
                self.entry_amount_pay.insert(0, paid[2])
                self.entry_amount_pay.configure(state="disabled")
                self.text_balance_amount.configure(text=paid[4])
                self.btn_pay.configure(state="disabled")

        self.frame_history = tk.Frame(self.view)
        self.frame_history.place(relx=0.0, rely=0.429, relheight=0.571
                                 , relwidth=1.0)
        self.frame_history.configure(borderwidth="2")
        self.frame_history.configure(background="#7aaaea")
        self.frame_history.configure(width=125)

        self.text_history = tk.Label(self.frame_history)
        self.text_history.place(relx=0.025, rely=0.025, height=35, width=167)
        self.text_history.configure(background="#7aaaea")
        self.text_history.configure(disabledforeground="#a3a3a3")
        self.text_history.configure(foreground="#000000")
        self.text_history.configure(font=font11)
        self.text_history.configure(text='''Payment History''')

        self.history = ttk.Treeview(self.frame_history, show="headings", height=5)
        self.history.place(relx=0.05, rely=0.15, relheight=0.788
                                 , relwidth=0.85)
        self.history["columns"] = ("Record", "Invoice_ID", "Pay_Date", "Amount", "Balance")
        self.history.column("Record", width=10)
        self.history.column("Invoice_ID", width=15)
        self.history.column("Pay_Date", width=20)
        self.history.column("Amount", width=20)
        self.history.column("Balance", width=20)

        self.btn_refresh = tk.Button(self.frame_history)
        self.btn_refresh.place(relx=0.825, rely=0.075, height=24, width=50)
        self.btn_refresh.configure(activebackground="#ea9f9f")
        self.btn_refresh.configure(activeforeground="#000000")
        self.btn_refresh.configure(background="#ea9f9f")
        self.btn_refresh.configure(disabledforeground="#a3a3a3")
        self.btn_refresh.configure(foreground="#000000")
        self.btn_refresh.configure(highlightbackground="#d9d9d9")
        self.btn_refresh.configure(highlightcolor="black")
        self.btn_refresh.configure(pady="0")
        self.btn_refresh.configure(text='''Refresh''')

        for col in self.history["columns"]:
            self.history.heading(col, text=col.title(),
                                 command=lambda c=col: sortby(self.history, c, 0))

        connstr = "std039/cestd039@144.214.177.102:1521/xe"
        conn = cx_Oracle.connect(connstr)
        cursor = conn.cursor()
        sql = "select * from payment_record inner join invoice on payment_record.invoice_id = invoice.id where invoice.metre_id = %s" % (selected_meter)
        cursor.execute(sql)
        result = cursor.fetchall()

        for i in result:
            self.history.insert("", 0, values=(i[0], i[1], str(i[3]), i[2], i[4]))
        conn.commit()
        cursor.close()

        self.his_ysb = tk.Scrollbar(self.frame_history, orient=VERTICAL)
        self.his_ysb.place(relx=0.9, rely=0.15, relheight=0.788
                                  , relwidth=0.05)

        self.history.configure(yscrollcommand=self.his_ysb.set)
        self.his_ysb.configure(command=self.history.yview)

    def pay(self):
        pay_rel_id = uuid_handler.random_uuid()

        invoice_id = self.entry_invoice_id.get()
        amount_due = float(self.entry_amount_due.get())
        print(amount_due)
        amount_paid = self.entry_amount_pay.get()
        print(amount_paid)

        balance = float(amount_paid) - amount_due
        balance = Decimal(balance).quantize(Decimal('0.00'))

        selected_meter = self.tree.item(self.tree.selection())['values'][2]

        connstr = "std039/cestd039@144.214.177.102:1521/xe"
        conn = cx_Oracle.connect(connstr)
        cur = conn.cursor()
        sql = "INSERT INTO PAYMENT_RECORD (INVOICE_ID, AMOUNT_PAID, BALANCE, REL_ID) VALUES (%s, %s, %s, '%s')" %(invoice_id, amount_paid, balance, pay_rel_id)
        cur.execute(sql)
        print(sql)
        conn.commit()

        q_balance = conn.cursor()
        q_balance.execute("select balance from metre inner join invoice on invoice.metre_id = metre.id where invoice.id = '%s'" %(invoice_id))
        q_result = q_balance.fetchall()

        for b in q_result:
            old_balance = float(b[0])
            new_balance = float(balance) + old_balance

            cur_update_balance = conn.cursor()
            cur_update_balance.execute("UPDATE METRE SET BALANCE = '%s' WHERE ID = '%s'" %(new_balance, selected_meter))
            conn.commit()

        tk.messagebox.showinfo("Message", "Transaction Done. Payment accepted")
        self.view.destroy()

    def refresh(self):
        invoice_id = self.entry_invoice_id.get()
        metre_id = self.entry_customer_id.get()

        connstr = "std039/cestd039@144.214.177.102:1521/xe"
        conn = cx_Oracle.connect(connstr)
        cur = conn.cursor()
        sql = "select * from payment_record inner join invoice on payment_record.invoice_id = invoice.id where invoice.metre_id = %s" %(metre_id)
        result = cur.execute(sql)
        result.fetchall()

        item = self.history.get_children()
        for r in item:
            self.tree.delete(r)

        for i in result:
            self.history.insert("", 0, values=(i[0], i[1], str(i[3]), i[2], i[4]))

        conn.commit()
        cur.close()
        conn.close()

    def gotoHome(self):
        # warning()
        qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")
        if qa == "yes":
            self.controller.show_frame("Home")
        else:
            None

    def gotoInvoice(self):
        # warning()
        qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")
        if qa == "yes":
            self.controller.show_frame("Invoice")
        else:
            None

    def gotoCustomer(self):
        # warning()
        qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")
        if qa == "yes":
            self.controller.show_frame("Customer")
        else:
            None

    def logout(self):
        # warning()
        qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")
        if qa == "yes":
            self.controller.show_frame("Login")
        else:
            None

def warning():
    qa = tkinter.messagebox.askquestion("Warning", "Are you sure to leave? All unsave information will be lost")


def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # get values from selected column to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # sort values in order
    try:
        # if the values are integer
        data.sort(key=lambda child: int(child[0]), reverse=descending)
        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        # switch the heading so it will sort in the opposite direction
        tree.heading(col, command=lambda col=col: sortby(tree, col, \
            int(not descending)))
    except:
        # if the values are letters
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        # switch the heading so it will sort in the opposite direction
        tree.heading(col, command=lambda col=col: sortby(tree, col, \
            int(not descending)))


def cal(amount) :
    price = 0

    standard = Decimal(48)
    amount = float(amount * standard)

    first_500 = 0.25
    next_2000 = 0.249
    next_5000 = 0.2486
    next_10000 = 0.2476
    next_15000 = 0.2466
    next_25000 = 0.2453
    next_50000_1 = 0.2443
    next_50000_2 = 0.2434
    next_50000_3 = 0.2424
    next_50000_4 = 0.2415
    over_257500 = 0.2405

    if amount <= 500:
        price = amount * first_500

    elif amount <= 2500:
        price = 500 * first_500 + (amount - 500) * next_2000

    elif amount <= 7500:
        price = 500 * first_500 + 2000 * next_2000 + (amount - 2500) * next_5000

    elif amount <= 17500:
        price = 500 * first_500 + 2000 * next_2000 + 5000 * next_5000 + (amount - 7500) * next_10000

    elif amount <= 32500:
        price = 500 * first_500 + 2000 * next_2000 + 5000 * next_5000 + 10000 * next_10000 + (
                                                                                                 amount - 17500) * next_15000

    elif amount <= 57500:
        price = 500 * first_500 + 2000 * next_2000 + 5000 * next_5000 + 10000 * next_10000 + 15000 * next_15000 + (
                                                                                                                      amount - 32500) * next_25000

    elif amount <= 107500:
        price = 500 * first_500 + 2000 * next_2000 + 5000 * next_5000 + 10000 * next_10000 + 15000 * next_15000 + 25000 * next_25000 + (
                                                                                                                                           amount - 57500) * next_50000_1

    elif amount <= 157500:
        price = 500 * first_500 + 2000 * next_2000 + 5000 * next_5000 + 10000 * next_10000 + 15000 * next_15000 + 25000 * next_25000 + 50000 * next_50000_1 + (
                                                                                                                                                                  amount - 107500) * next_50000_2

    elif amount <= 207500:
        price = 500 * first_500 + 2000 * next_2000 + 5000 * next_5000 + 10000 * next_10000 + 15000 * next_15000 + 25000 * next_25000 + 50000 * next_50000_1 + 50000 * next_50000_2 + (
                                                                                                                                                                                         amount - 157500) * next_50000_3

    elif amount <= 257500:
        price = 500 * first_500 + 2000 * next_2000 + 5000 * next_5000 + 10000 * next_10000 + 15000 * next_15000 + 25000 * next_25000 + 50000 * next_50000_1 + 50000 * next_50000_2 + 50000 * next_50000_3 + (
                                                                                                                                                                                                                amount - 207500) * next_50000_4

    elif amount > 257500:
        price = 500 * first_500 + 2000 * next_2000 + 5000 * next_5000 + 10000 * next_10000 + 15000 * next_15000 + 25000 * next_25000 + 50000 * next_50000_1 + 50000 * next_50000_2 + 50000 * next_50000_3 + 50000 * next_50000_4 + (
                                                                                                                                                                                                                                       amount - 257500) * over_257500

    if price < 20:
        price = 20

    price = Decimal(price).quantize(Decimal('0.00'))
    return price


if __name__ == "__main__":
    app = Towngas()
    app.geometry("960x720+430+157")
    app.title("TowngasManagement")
    app.configure(background="#7aaaea")
    app.mainloop()
