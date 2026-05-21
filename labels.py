import tkinter as tk

def disc_calculator():
    shopping_amt = float(entry1.get())
    disc_amt=0
    if shopping_amt>=3000:
        disc_amt = 0.03*shopping_amt
    elif shopping_amt>=2000:
        disc_amt = 0.02*shopping_amt
    
    elif shopping_amt>1000:
        disc_amt=0.010*shopping_amt
    
    else:
        pass

    final_label.configure(text= f"Discount amount = {disc_amt:.2f}")




app = tk.Tk()
app.title("Discount Calculator")
label1 = tk.Label(app,text= 'Enter the Shopping Amount',padx=15,pady=10,font=("Helvetica",15,'bold'))
label1.grid(row=0,column=0)

entry1 = tk.Entry(app,width=20)
entry1.grid(row=0,column=1)

final_label = tk.Label(app,text= 'Discount amount = ',padx=20,pady=15,font=('Robota',15,'bold' ),)
final_label.grid(row=2,column=0)

calc_but = tk.Button(app,text = "Calculate Discount",padx=10 ,pady=10,font=('Robota',10,'bold'),width =25,command=disc_calculator,bg='red').grid(row=3,column =0)


app.mainloop()