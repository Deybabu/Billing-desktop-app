from tkinter import *
import random
from tkinter import messagebox
root=Tk()
root.geometry('2200x1000')
root.title("Billing software")
bg_color='#4D0039'
#variable
c_name=StringVar()
c_phone=StringVar()
bill_no=StringVar()
item=StringVar()
rate=IntVar()
quantity=IntVar()
x=random.randint(1000,9999)
bill_no.set(str(x))
global l 
l=[]
#function
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t Weleconme to Rajib Shop")
    textarea.insert(END,f'\n\nBill Number:\t\t{bill_no.get()}')
    textarea.insert(END,f'\nCustomer Name:\t\t{c_name.get()}')
    textarea.insert(END,f'\nPhone Number:\t\t{c_phone.get()}')
    textarea.insert(END,f'\n=================================')
    textarea.insert(END,'\n Product \t\t QTY \t\t Price')
    textarea.insert(END,f'\n=================================')
    textarea.configure(font='arial 15 bold')

def additm():
    n=rate.get()
    m=quantity.get()*n
    l.append(m)
    if item.get()=='':
        messagebox.showerror('Error','Please enter item name')
    else:
        textarea.insert(END,f'\n{item.get()}\t\t{quantity.get()}\t\t{m}')

def gbill():
    if c_name.get()=='' or c_phone.get()=='':
        messagebox.showerror("Error","Customers details must be filled")
    else:
        text=textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END, text)
        textarea.insert(END,f'\n================================')
        textarea.insert(END,f'\nTotal Payable Amount:\t\t{sum(l)}')
        textarea.insert(END,f'\n===============================')
        savebill()
def savebill():
    op=messagebox.askyesno('Save bill','Do you want to save bill')
    if op>0:
        bill_details=textarea.get(1.0,END)
        f1=open("bills/"+str(bill_no.get())+".txt",'w')
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo('Saved',f'Bill no.:-{bill_no.get()} Saved succeessfully')
    else:
         return
def clear():
    cname_text.set('')
    pname_text.set('')
    item.set('')
    quantity.set(0)
    rate.set(0)
def exit():
    op=messagebox.askyesno('Exit','Do you want to exit')
    if op>0:
        root.destroy()




#customer dtatils
title=Label(root,text='Billing software',bg=bg_color,fg='white',font=(' times new roman',25,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)
F1=LabelFrame(root,text='Customer details',font=('times new roman',18,'bold'),relief=GROOVE,bd=10,bg=bg_color,fg='yellow')
F1.place(x=0,y=80,relwidth=1)
cname=Label(F1,text='Customer Name',font=('times new roman',18,'bold'),bd=10,bg=bg_color,fg='white')
cname.grid(row=0,column=0,padx=10,pady=5)
cname_text=Entry(F1,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=c_name)
cname_text.grid(row=0,column=1,padx=10,pady=5)
cphone=Label(F1,text='Customer Phone number',font=('times new roman',18,'bold'),bd=10,bg=bg_color,fg='white')
cphone.grid(row=0,column=2,padx=10,pady=5)
cphone_text=Entry(F1,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=c_phone)
cphone_text.grid(row=0,column=3,padx=10,pady=5)
#product details
F2=LabelFrame(root,text='Product Details',font=('times new roman',18,'bold'),relief=GROOVE,bd=10,bg=bg_color,fg='yellow')
F2.place(x=20,y=180,width=630,height=500)
pname=Label(F2,text='Product Name',font=('times new roman',18,'bold'),bd=10,bg=bg_color,fg='lightgreen')
pname.grid(row=0,column=0,padx=10,pady=5)
pname_text=Entry(F2,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=item)
pname_text.grid(row=0,column=1,padx=10,pady=5)
pprice=Label(F2,text='Product Price',font=('times new roman',18,'bold'),bd=10,bg=bg_color,fg='lightgreen')
pprice.grid(row=1,column=0,padx=10,pady=5)
p_price=Entry(F2,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=rate)
p_price.grid(row=1,column=1,padx=10,pady=5)
pquantity=Label(F2,text='Product Quantity',font=('times new roman',18,'bold'),bd=10,bg=bg_color,fg='lightgreen')
pquantity.grid(row=2,column=0,padx=10,pady=5)
p_quantity=Entry(F2,width=15,font='arial 15 bold',relief=SUNKEN,textvariable=quantity)
p_quantity.grid(row=2,column=1,padx=10,pady=5)
#button
b1=Button(F2,text='Add item',font='Arial 15 bold',padx=5,pady=10,bg='orange',fg='green',command=additm)
b1.grid(row=3,column=0,padx=10,pady=30)
b2=Button(F2,text='Generate bill',font='Arial 15 bold',padx=5,pady=10,bg='orange',fg='green',command=gbill)
b2.grid(row=3,column=1,padx=10,pady=30)
b3=Button(F2,text='Clear',font='Arial 15 bold',padx=5,pady=10,bg='orange',fg='green',command=clear)
b3.grid(row=4,column=0,padx=10,pady=30)
b4=Button(F2,text='Exit',font='Arial 15 bold',padx=5,pady=10,bg='orange',fg='green',command=exit)
b4.grid(row=4,column=1,padx=10,pady=30)
#bill area
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=700,y=180,width=500,height=500)

bill_title=Label(F3,text='Bill Area',font='arial 15 bold',relief=GROOVE,bd=7).pack(fill=X)
scroll_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()
welcome()
root.mainloop()