from tkinter import *
import tkinter as tk
root=tk.Tk()
root.title('Calculator')

operator=""
def btnClick(num):
    global operator
    operator+= str(num)
    text_input.set(operator)

def btnClear():
    global operator
    operator=""
    text_input.set("")

def btnEqual():
    global operator
    ans=str(eval(operator))
    text_input.set(ans)
    operator = ""



text_input=StringVar()
calc_disp=Entry(root,font=('helvetica',20),bg='#BFD245',textvariable=text_input,bd=20,
                justify='right',insertwidth=4).grid(columnspan=4)

btn1=Button(root,font=('helvetica',20),text='1',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick(1)).grid(row=1,column=0)
btn2=Button(root,font=('helvetica',20),text='2',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick(2)).grid(row=1,column=1)
btn3=Button(root,font=('helvetica',20),text='3',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick(3)).grid(row=1,column=2)

btn_add=Button(root,font=('helvetica',20),text='+',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick('+')).grid(row=1,column=3)

btn4=Button(root,font=('helvetica',20),text='4',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(root,font=('helvetica',20),text='5',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(root,font=('helvetica',20),text='6',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick(6)).grid(row=2,column=2)

btn_sub=Button(root,font=('helvetica',20),text='-',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick('-')).grid(row=2,column=3)

btn7=Button(root,font=('helvetica',20),text='7',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick(7)).grid(row=3,column=0)
btn8=Button(root,font=('helvetica',20),text='8',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick(8)).grid(row=3,column=1)
btn9=Button(root,font=('helvetica',20),text='9',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick(9)).grid(row=3,column=2)

btn_mul=Button(root,font=('helvetica',20),text='*',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick('*')).grid(row=3,column=3)

btnC=Button(root,font=('helvetica',20),text='C',padx=12,pady=12,bd=8,bg='gray',fg='red',command=lambda:btnClear()).grid(row=4,column=0)

btn0=Button(root,font=('helvetica',20),text='0',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick(0)).grid(row=4,column=1)
btn_eql=Button(root,font=('helvetica',20),text='=',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnEqual()).grid(row=4,column=2)

btn_div=Button(root,font=('helvetica',20),text='/',padx=12,pady=12,bd=8,bg='gray',command=lambda:btnClick('/')).grid(row=4,column=3)


root.mainloop()