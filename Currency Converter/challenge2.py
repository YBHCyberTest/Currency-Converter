import requests as req
from tkinter import *
from CurrencyExchanger import currencies, exchange
# from tkinter import ttk
import tkinter.ttk as tk

def convert1(event):
  amount = float(string1.get())
  fromm = combo1.get()
  to = combo2.get()
  string2.set(exchange(fromm, to, amount))

def convert2(event):
  amount = float(string2.get())
  fromm = combo2.get()
  to = combo1.get()
  string1.set(exchange(fromm, to, amount))

def start():
  global label0, string1, combo1, combo2, string2
  project = Tk()
  project.title("Convert Money ")
  project.geometry("700x400")
  project.resizable(False, False)

  label = Label(text="Welcome to Real Time Currency Converter", bg="yellow", fg="black",
                width="500", font=("Raphtalia", 20)).pack()


  # Label 0
  label0 = Label(project, text="... Your Money ...", font=("Sakalangkong", 20))
  label0.place(x=250, y=60)

  # Label1
  label1 = Label(project, text="First Value :", font=("Raphtalia", 20))
  label1.place(x=100, y=130)

  # Label2
  # label2 = Label(project, text="Secound Money :", font=("Arial Bold", 20))
  label2 = Label(project, text="Second Value :", font=("Raphtalia", 20))
  label2.place(x=440, y=130)

  # combo1
  selected_month = StringVar()
  combo1 = tk.Combobox(project, textvariable=selected_month)
  combo1["value"] = currencies
  combo1.current(142)
  combo1.bind("<<ComboboxSelected>>", convert1)
  combo1.place(x=100, y=175)

  # combo2
  combo2 = tk.Combobox()
  combo2["value"] = currencies
  combo2.current(148)
  combo2.bind("<<ComboboxSelected>>", convert2)
  combo2.place(x=450, y=175)


  # Text1
  string1 = StringVar()
  txt1 = Entry(project, width=15, textvariable=string1)
  txt1.bind("<KeyRelease>", convert1)
  txt1.place(x=120, y=210)

  # Text2
  string2 = StringVar()
  txt2 = Entry(project, width=15, textvariable=string2)
  txt2.bind("<KeyRelease>", convert2)
  txt2.place(x=470, y=210)

  project.mainloop()
