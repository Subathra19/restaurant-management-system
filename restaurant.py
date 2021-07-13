import random
import time
import datetime
import tkinter.messagebox
from tkinter import *

window=Tk()
# Colors
bg_color="royalblue3"
frame_color="royalblue2"

##########################################################
#                      Window
##########################################################


# Size of the window
window.geometry("1350x750+0+0")
# Title
window.title("Restaurant Billing System")
window.configure(background=bg_color)
window.resizable(False, False)


# Divide the screen into three frames
# 1. Title frame
top_frame= Frame(window,bg=bg_color, bd=20, pady =5, relief=RIDGE)
top_frame.pack(side=TOP)

label_title=Label(top_frame,font=('arial',58,'bold'),text="Appalam Restaurant",bd=21,bg=bg_color,fg='Cornsilk',justify=CENTER)
label_title.grid(row=0,column=0)

# 2. Receipt Frame
receipt_frame=Frame(window,bg=bg_color, bd=10, relief=RIDGE)
receipt_frame.pack(side=RIGHT)

# Divide receipt frame into three sub frames
buttons_frame=Frame(receipt_frame,bg=frame_color, bd=3, relief=RIDGE)
buttons_frame.pack(side=BOTTOM)
calculator_frame=Frame(receipt_frame,bg=frame_color, bd=6, relief=RIDGE)
calculator_frame.pack(side=TOP)
receipt_view_frame=Frame(receipt_frame,bg=frame_color, bd=4, relief=RIDGE)
receipt_view_frame.pack(side=BOTTOM)

# 3. Menu Frame
menu_frame=Frame(window,bg=bg_color, bd=10, relief=RIDGE)
menu_frame.pack(side=LEFT)

# Divide menu frame into three sub frames
cost_frame=Frame(menu_frame,bg=frame_color,bd=4)
cost_frame.pack(side=BOTTOM)
drinks_frame=Frame(menu_frame,bg=frame_color, bd=10)
drinks_frame.pack(side=TOP)

drinks_frame=Frame(menu_frame,bg=frame_color, bd=10, relief=RIDGE)
drinks_frame.pack(side=LEFT)
dishes_frame=Frame(menu_frame,bg=frame_color, bd=10, relief=RIDGE)
dishes_frame.pack(side=RIGHT)




##########################################################
#                      Global variables
##########################################################


var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder= StringVar()
Receipt_Ref= StringVar()
PaidTax= StringVar()
SubTotal= StringVar()
TotalCost= StringVar()
CostofDishes= StringVar()
CostofDrinks= StringVar()
ServiceCharge= StringVar()

text_Input= StringVar()
operator=""

E_Rose=StringVar()
E_Sangira=StringVar()
E_Cosmopolitan=StringVar()
E_MaiTai=StringVar()
E_AppleMartini=StringVar()
E_PinaColada=StringVar()
E_AgaveMargarita=StringVar() 
E_BottledWater=StringVar()  

E_GiantCrabSoup=StringVar() 
E_MuttonBiriyani=StringVar() 
E_FishFingers=StringVar() 
E_Lasanga=StringVar() 
E_PepperoniPizza=StringVar() 
E_SquidFry=StringVar() 
E_DeathByChocolate=StringVar() 
E_LijjatAppalam=StringVar() 

E_Rose.set("0")
E_Sangira.set("0")
E_Cosmopolitan.set("0")
E_MaiTai.set("0")
E_AppleMartini.set("0")
E_PinaColada.set("0")
E_AgaveMargarita.set("0")
E_BottledWater.set("0")

E_GiantCrabSoup.set("0")
E_MuttonBiriyani.set("0")
E_FishFingers.set("0")
E_Lasanga.set("0")
E_PepperoniPizza.set("0")
E_SquidFry.set("0")
E_DeathByChocolate.set("0")
E_LijjatAppalam.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))




##########################################################
#                      Function Declaration
##########################################################

class funcdeclare:
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Exit", "Are you sure?")
        if iExit>0:
            window.destroy()
            return

    def Reset(self):
        E_Rose.set("0")
        E_Sangira.set("0")
        E_Cosmopolitan.set("0")
        E_MaiTai.set("0")
        E_AppleMartini.set("0")
        E_PinaColada.set("0")
        E_AgaveMargarita.set("0")
        E_BottledWater.set("0")

        E_GiantCrabSoup.set("0")
        E_MuttonBiriyani.set("0")
        E_FishFingers.set("0")
        E_Lasanga.set("0")
        E_PepperoniPizza.set("0")
        E_SquidFry.set("0")
        E_DeathByChocolate.set("0")
        E_LijjatAppalam.set("0")

        CostofDishes.set("0")
        CostofDrinks.set("0")
        ServiceCharge.set("0")
        SubTotal.set("0")
        PaidTax.set("0")
        TotalCost.set("0")

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)

        txtRose.configure(state =DISABLED)
        txtSangira.configure(state=DISABLED)
        txtCosmopolitan.configure(state=DISABLED)
        txtMaiTai.configure(state=DISABLED)
        txtAppleMartini.configure(state=DISABLED)
        txtPinaColada.configure(state=DISABLED)
        txtAgaveMargarita.configure(state=DISABLED)
        txtBottledWater.configure(state=DISABLED)

        txtGiantCrabSoup.configure(state=DISABLED)
        txtMuttonBiriyani.configure(state=DISABLED)
        txtFishFingers.configure(state=DISABLED)
        txtLasanga.configure(state=DISABLED)
        txtPepperoniPizza.configure(state=DISABLED)
        txtSquidFry.configure(state=DISABLED)
        txtDeathByChocolate.configure(state=DISABLED)
        txtLijjatAppalam.configure(state=DISABLED)

    def CostofItem(self):
        Item1=float(E_Rose.get())
        Item2=float(E_Sangira.get())
        Item3=float(E_Cosmopolitan.get())
        Item4=float(E_MaiTai.get())
        Item5=float(E_AppleMartini.get())
        Item6=float(E_PinaColada.get())
        Item7=float(E_AgaveMargarita.get())
        Item8=float(E_BottledWater.get())

        Item9=float(E_GiantCrabSoup.get())
        Item10=float(E_MuttonBiriyani.get())
        Item11=float(E_FishFingers.get())
        Item12=float(E_Lasanga.get())
        Item13=float(E_PepperoniPizza.get())
        Item14=float(E_SquidFry.get())
        Item15=float(E_DeathByChocolate.get())
        Item16=float(E_LijjatAppalam.get())

        PriceofDrinks=((Item1 * 399 ) + (Item2 * 399) + (Item3 * 399) + (Item4 * 399)
                       + (Item5 * 399) + (Item6 * 399) + (Item7 * 399) + (Item8 * 50))
        PriceofDishes=((Item9 * 450) + (Item10 * 1299) + (Item11 * 599) + (Item12 * 799)
                       + (Item13 * 449) + (Item14 * 399) + (Item15 * 699) + (Item16 * 100))

        DrinksPrice="Rs", str('%.2f'%(PriceofDrinks))
        DishesPrice="Rs", str('%.2f'%(PriceofDishes))
        CostofDishes.set(DishesPrice)
        CostofDrinks.set(DrinksPrice)
        SC="Rs", str('%.2f'%(2.5))
        ServiceCharge.set(SC)

        SubTotalofITEMS="Rs", str('%.2f'%(PriceofDrinks + PriceofDishes + 2.5))
        SubTotal.set(SubTotalofITEMS)

        Tax="Rs", str('%.2f'%((PriceofDrinks + PriceofDishes + 2.5)*0.5))
        PaidTax.set(Tax)
        TT=((PriceofDrinks + PriceofDishes + 2.5) * 0.5)
        TC="Rs", str('%.2f'%(PriceofDishes + PriceofDrinks + 2.5 + TT))
        TotalCost.set(TC)


    def checkRose(self):
        if(var1.get()==1):
            txtRose.configure(state= NORMAL)
            txtRose.focus()
            txtRose.delete('0', END)
            E_Rose.set("")
        elif(var1.get()==0):
            txtRose.configure(state= DISABLED)
            E_Rose.set("0")
    def checkSangira(self):
        if(var2.get()==1):
            txtSangira.configure(state= NORMAL)
            txtSangira.focus()
            txtSangira.delete('0', END)
            E_Sangira.set("")
        elif(var2.get()==0):
            txtSangira.configure(state= DISABLED)
            E_Sangira.set("0")
    def checkCosmopolitan(self):
        if(var3.get()==1):
            txtCosmopolitan.configure(state= NORMAL)
            txtCosmopolitan.focus()
            txtCosmopolitan.delete('0', END)
            E_Cosmopolitan.set("")
        elif(var3.get()==0):
            txtCosmopolitan.configure(state= DISABLED)
            E_Cosmopolitan.set("0")
    def checkMaiTai(self):
        if(var4.get()==1):
            txtMaiTai.configure(state= NORMAL)
            txtMaiTai.focus()
            txtMaiTai.delete('0', END)
            E_MaiTai.set("")
        elif(var4.get()==0):
            txtMaiTai.configure(state= DISABLED)
            E_MaiTai.set("0")
    def checkAppleMartini(self):
        if(var5.get()==1):
            txtAppleMartini.configure(state= NORMAL)
            txtAppleMartini.focus()
            txtAppleMartini.delete('0', END)
            E_AppleMartini.set("")
        elif(var5.get()==0):
            txtAppleMartini.configure(state= DISABLED)
            E_AppleMartini.set("0")
    def checkPinaColada(self):
        if(var6.get()==1):
            txtPinaColada.configure(state= NORMAL)
            txtPinaColada.focus()
            txtPinaColada.delete('0', END)
            E_PinaColada.set("")
        elif(var6.get()==0):
            txtPinaColada.configure(state= DISABLED)
            E_PinaColada.set("0")
    def checkAgaveMargarita(self):
        if(var7.get()==1):
            txtAgaveMargarita.configure(state= NORMAL)
            txtAgaveMargarita.focus()
            txtAgaveMargarita.delete('0', END)
            E_AgaveMargarita.set("")
        elif(var7.get()==0):
            txtAgaveMargarita.configure(state= DISABLED)
            E_AgaveMargarita.set("0")
    def checkBottledWater(self):
        if(var8.get()==1):
            txtBottledWater.configure(state= NORMAL)
            txtBottledWater.focus()
            txtBottledWater.delete('0', END)
            E_BottledWater.set("")
        elif(var8.get()==0):
            txtBottledWater.configure(state= DISABLED)
            E_BottledWater.set("0")
    def checkGiantCrabSoup(self):
        if(var9.get()==1):
            txtGiantCrabSoup.configure(state= NORMAL)
            txtGiantCrabSoup.focus()
            txtGiantCrabSoup.delete('0', END)
            E_GiantCrabSoup.set("")
        elif(var9.get()==0):
            txtGiantCrabSoup.configure(state= DISABLED)
            E_GiantCrabSoup.set("0")
    def checkMuttonBiriyani(self):
        if(var10.get()==1):
            txtMuttonBiriyani.configure(state= NORMAL)
            txtMuttonBiriyani.focus()
            txtMuttonBiriyani.delete('0', END)
            E_MuttonBiriyani.set("")
        elif(var10.get()==0):
            txtMuttonBiriyani.configure(state= DISABLED)
            E_MuttonBiriyani.set("0")
    def checkFishFingers(self):
        if(var11.get()==1):
            txtFishFingers.configure(state= NORMAL)
            txtFishFingers.focus()
            txtFishFingers.delete('0', END)
            E_FishFingers.set("")
        elif(var11.get()==0):
            txtFishFingers.configure(state= DISABLED)
            E_FishFingers.set("0")
    def checkLasanga(self):
        if(var12.get()==1):
            txtLasanga.configure(state= NORMAL)
            txtLasanga.focus()
            txtLasanga.delete('0', END)
            E_Lasanga.set("")
        elif(var12.get()==0):
            txtLasanga.configure(state= DISABLED)
            E_Lasanga.set("0")
    def checkPepperoniPizza(self):
        if(var13.get()==1):
            txtPepperoniPizza.configure(state= NORMAL)
            txtPepperoniPizza.focus()
            txtPepperoniPizza.delete('0', END)
            E_PepperoniPizza.set("")
        elif(var13.get()==0):
            txtPepperoniPizza.configure(state= DISABLED)
            E_PepperoniPizza.set("0")
    def checkSquidFry(self):
        if(var14.get()==1):
            txtSquidFry.configure(state= NORMAL)
            txtSquidFry.focus()
            txtSquidFry.delete('0', END)
            E_SquidFry.set("")
        elif(var14.get()==0):
            txtSquidFry.configure(state= DISABLED)
            E_SquidFry.set("0")
    def checkDeathByChocolate(self):
        if(var15.get()==1):
            txtDeathByChocolate.configure(state= NORMAL)
            txtDeathByChocolate.focus()
            txtDeathByChocolate.delete('0', END)
            E_DeathByChocolate.set("")
        elif(var15.get()==0):
            txtDeathByChocolate.configure(state= DISABLED)
            E_DeathByChocolate.set("0")
    def checkLijjatAppalam(self):
        if(var16.get()==1):
            txtLijjatAppalam.configure(state= NORMAL)
            txtLijjatAppalam.focus()
            txtLijjatAppalam.delete('0', END)
            E_LijjatAppalam.set("")
        elif(var16.get()==0):
            txtLijjatAppalam.configure(state= DISABLED)
            E_LijjatAppalam.set("0")

    def Receipt(self):
        txtReceipt.delete("1.0",END)
        x= random.randint(10903, 609235)
        randomRef= str(x)
        Receipt_Ref.set("BILL" + randomRef)

        txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() + "\t" + DateofOrder.get() + "\n")
        txtReceipt.insert(END, 'Item:\t\t\t' + "No of Items\n")
        txtReceipt.insert(END, 'Rose: \t\t\t\t' + E_Rose.get() + "\n")
        txtReceipt.insert(END, 'Sangira: \t\t\t\t' + E_Sangira.get() + "\n")
        txtReceipt.insert(END, 'Cosmopolitan: \t\t\t\t' + E_Cosmopolitan.get() + "\n")
        txtReceipt.insert(END, 'MaiTai: \t\t\t\t' + E_MaiTai.get() + "\n")
        txtReceipt.insert(END, 'Apple Martini: \t\t\t\t' + E_AppleMartini.get() + "\n")
        txtReceipt.insert(END, 'Pina Colada: \t\t\t\t' + E_PinaColada.get() + "\n")
        txtReceipt.insert(END, 'Agave Margarita: \t\t\t\t' + E_AgaveMargarita.get() + "\n")
        txtReceipt.insert(END, 'Bottled Water: \t\t\t\t' + E_BottledWater.get() + "\n")
        txtReceipt.insert(END, 'Giant Crab Soup: \t\t\t\t' + E_GiantCrabSoup.get() + "\n")
        txtReceipt.insert(END, 'Mutton Biriyani: \t\t\t\t' + E_MuttonBiriyani.get() + "\n")
        txtReceipt.insert(END, 'Fish Fingers: \t\t\t\t' + E_FishFingers.get() + "\n")
        txtReceipt.insert(END, 'Lasanga: \t\t\t\t' + E_Lasanga.get() + "\n")
        txtReceipt.insert(END, 'Pepperon Pizza: \t\t\t\t' + E_PepperoniPizza.get() + "\n")
        txtReceipt.insert(END, 'Squid Fry: \t\t\t\t' + E_SquidFry.get() + "\n")
        txtReceipt.insert(END, 'Death By Chocolate: \t\t\t\t' + E_DeathByChocolate.get() + "\n")
        txtReceipt.insert(END, 'Lijjat Appalam: \t\t\t\t' + E_LijjatAppalam.get() + "\n")

obj=funcdeclare()


##########################################################
#                      Information
##########################################################

# 2. Information on the menu frame

#----------------------------Drinks-----------------------
Rose=Checkbutton(drinks_frame, text='Rose', variable=var1, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= frame_color, command=obj.checkRose).grid(row=0,sticky=W)
Sangira=Checkbutton(drinks_frame, text='Sangira', variable=var2, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= frame_color, command=obj.checkSangira).grid(row=1,sticky=W)
Cosmopolitan=Checkbutton(drinks_frame, text='Cosmopolitan', variable=var3, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= frame_color, command=obj.checkCosmopolitan).grid(row=2,sticky=W)
MaiTai=Checkbutton(drinks_frame, text='MaiTai', variable=var4, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= frame_color, command=obj.checkMaiTai).grid(row=3,sticky=W)
AppleMartini=Checkbutton(drinks_frame, text='Apple Martini', variable=var5, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= frame_color, command=obj.checkAppleMartini).grid(row=4,sticky=W)
PinaColada=Checkbutton(drinks_frame, text='Pina Colada', variable=var6, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= frame_color, command=obj.checkPinaColada).grid(row=5,sticky=W)
AgaveMargarita=Checkbutton(drinks_frame, text='Agave Margarita', variable=var7, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= frame_color, command=obj.checkAgaveMargarita).grid(row=6,sticky=W)
BottledWater=Checkbutton(drinks_frame, text='Bottled Water', variable=var8, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= frame_color, command=obj.checkBottledWater).grid(row=7,sticky=W)

#----------------------------Entry Box for Drinks-----------------------
txtRose= Entry(drinks_frame,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Rose)
txtRose.grid(row=0,column=1)
txtSangira= Entry(drinks_frame,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Sangira)
txtSangira.grid(row=1,column=1)
txtCosmopolitan= Entry(drinks_frame,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Cosmopolitan)
txtCosmopolitan.grid(row=2,column=1)
txtMaiTai= Entry(drinks_frame,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_MaiTai)
txtMaiTai.grid(row=3,column=1)
txtAppleMartini= Entry(drinks_frame,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_AppleMartini)
txtAppleMartini.grid(row=4,column=1)
txtPinaColada= Entry(drinks_frame,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_PinaColada)
txtPinaColada.grid(row=5,column=1)
txtAgaveMargarita= Entry(drinks_frame,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_AgaveMargarita)
txtAgaveMargarita.grid(row=6,column=1)
txtBottledWater= Entry(drinks_frame,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_BottledWater)
txtBottledWater.grid(row=7,column=1)


#----------------------------Dishes-----------------------
GiantCrabSoup=Checkbutton(dishes_frame, text='Giant Crab Soup', variable=var9, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= frame_color, command=obj.checkGiantCrabSoup).grid(row=0,sticky=W)
MuttonBiriyani=Checkbutton(dishes_frame, text='Mutton Biriyani', variable=var10, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= frame_color, command=obj.checkMuttonBiriyani).grid(row=1,sticky=W)
FishFingers=Checkbutton(dishes_frame, text='Fish Fingers', variable=var11, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= frame_color, command=obj.checkFishFingers).grid(row=2,sticky=W)
Lasanga=Checkbutton(dishes_frame, text='Lasanga', variable=var12, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= frame_color, command=obj.checkLasanga).grid(row=3,sticky=W)
PepperoniPizza=Checkbutton(dishes_frame, text='Pepperoni Pizza', variable=var13, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= frame_color, command=obj.checkPepperoniPizza).grid(row=4,sticky=W)
SquidFry=Checkbutton(dishes_frame, text='Squid Fry', variable=var14, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= frame_color, command=obj.checkSquidFry).grid(row=5,sticky=W)
DeathByChocolate=Checkbutton(dishes_frame, text='Death By Chocolate', variable=var15, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= frame_color, command=obj.checkDeathByChocolate).grid(row=6,sticky=W)
LijjatAppalam=Checkbutton(dishes_frame, text='Lijjat Appalam', variable=var16, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= frame_color, command=obj.checkLijjatAppalam).grid(row=7,sticky=W)

#----------------------------Entry Box for Dishes-----------------------
txtGiantCrabSoup= Entry(dishes_frame,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_GiantCrabSoup)
txtGiantCrabSoup.grid(row=0,column=1)
txtMuttonBiriyani= Entry(dishes_frame,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_MuttonBiriyani)
txtMuttonBiriyani.grid(row=1,column=1)
txtFishFingers= Entry(dishes_frame,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_FishFingers)
txtFishFingers.grid(row=2,column=1)
txtLasanga= Entry(dishes_frame,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Lasanga)
txtLasanga.grid(row=3,column=1)
txtPepperoniPizza= Entry(dishes_frame,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_PepperoniPizza)
txtPepperoniPizza.grid(row=4,column=1)
txtSquidFry= Entry(dishes_frame,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_SquidFry)
txtSquidFry.grid(row=5,column=1)
txtDeathByChocolate= Entry(dishes_frame,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_DeathByChocolate)
txtDeathByChocolate.grid(row=6,column=1)
txtLijjatAppalam= Entry(dishes_frame,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_LijjatAppalam)
txtLijjatAppalam.grid(row=7,column=1)

#----------------------------Total Cost-----------------------
label_CostofDrinks =Label(cost_frame, font=('arial',14,'bold'),text='Cost of Drinks\t',bg=frame_color,fg='black')
label_CostofDrinks.grid(row=0,column=0, sticky=W)
txtCostofDrinks= Entry(cost_frame, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0, column=1)

label_CostofDishes =Label(cost_frame, font=('arial',14,'bold'),text='Cost of Dishes\t',bg=frame_color,fg='black')
label_CostofDishes.grid(row=1,column=0, sticky=W)
txtCostofDishes= Entry(cost_frame, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=CostofDishes)
txtCostofDishes.grid(row=1, column=1)

label_ServiceCharge =Label(cost_frame, font=('arial',14,'bold'),text='Service Charge\t',bg=frame_color,fg='black')
label_ServiceCharge.grid(row=2,column=0, sticky=W)
lblServiceCharge= Entry(cost_frame, bg='white',width=40, bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=ServiceCharge)
lblServiceCharge.grid(row=2, column=1)

#----------------------------Payment Information-----------------------
label_PaidTax =Label(cost_frame, font=('arial',14,'bold'),text='\tPaid Tax',bg=frame_color,fg='black')
label_PaidTax.grid(row=0,column=2, sticky=W)
txtPaidTax= Entry(cost_frame, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=PaidTax)
txtPaidTax.grid(row=0, column=3)

label_SubTotal =Label(cost_frame, font=('arial',14,'bold'),text='\tSub Total',bg=frame_color,fg='black')
label_SubTotal.grid(row=1,column=2, sticky=W)
txtSubTotal= Entry(cost_frame, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=SubTotal)
txtSubTotal.grid(row=1, column=3)

label_TotalCost =Label(cost_frame, font=('arial',14,'bold'),text='\tTotal Cost',bg='Powder Blue',fg='black')
label_TotalCost.grid(row=2,column=2, sticky=W)
txtTotalCost= Entry(cost_frame, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=TotalCost)
txtTotalCost.grid(row=2, column=3)

# 3. Information on the Receipt frame

#----------------------------Receipt Information-----------------------
txtReceipt= Text(receipt_view_frame, width=46, height=12, bg='white', bd=4, font=('arial',12,'bold'))
txtReceipt.grid(row=0, column=0)


#----------------------------Buttons-----------------------

btnTotal=Button(buttons_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Total", bg=frame_color, command=obj.CostofItem).grid(row=0,column=0)
btnReceipt=Button(buttons_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Receipt", bg=frame_color, command=obj.Receipt).grid(row=0,column=1)
btnReset=Button(buttons_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Reset", bg=frame_color, command=obj.Reset).grid(row=0,column=2)
btnExit=Button(buttons_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Exit", bg=frame_color, command=obj.iExit).grid(row=0,column=3)

#----------------------------Calculator-----------------------
class calcfunc:
    def btnClick(self,numbers):
        global operator
        operator= operator + str(numbers)
        text_Input.set(operator)

    def btnClear(self):
        global operator
        operator = ""
        text_Input.set("")

    def btnEquals(self):
        global operator
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator = ""

    txtDisplay= Entry(calculator_frame, width=45, bg='white', bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable= text_Input)
    txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
    txtDisplay.insert(0,"0")

obj1=calcfunc()

#=======================================================Calculator Buttons=================================================

btn7=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="7", bg=frame_color, command=lambda:obj1.btnClick(7)).grid(row=2,column=0)
btn8=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="8", bg=frame_color, command=lambda:obj1.btnClick(8)).grid(row=2,column=1)
btn9=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="9", bg=frame_color, command=lambda:obj1.btnClick(9)).grid(row=2,column=2)
btnAdd=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="+", bg=frame_color, command=lambda:obj1.btnClick("+")).grid(row=2,column=3)

#=======================================================Calculator Buttons=================================================

btn4=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="4", bg=frame_color, command=lambda:obj1.btnClick(4)).grid(row=3,column=0)
btn5=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="5", bg=frame_color, command=lambda:obj1.btnClick(5)).grid(row=3,column=1)
btn6=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="6", bg=frame_color, command=lambda:obj1.btnClick(6)).grid(row=3,column=2)
btnSub=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="-", bg=frame_color, command=lambda:obj1.btnClick("-")).grid(row=3,column=3)

#=======================================================Calculator Buttons=================================================

btn1=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="1", bg=frame_color, command=lambda:obj1.btnClick(1)).grid(row=4,column=0)
btn2=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="2", bg=frame_color, command=lambda:obj1.btnClick(2)).grid(row=4,column=1)
btn3=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="3", bg=frame_color, command=lambda:obj1.btnClick(3)).grid(row=4,column=2)
btnMulti=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="*", bg=frame_color, command=lambda:obj1.btnClick("*")).grid(row=4,column=3)

#=======================================================Calculator Buttons=================================================

btn0=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="0", bg=frame_color, command=lambda:obj1.btnClick(0)).grid(row=5,column=0)
btnClear=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="C", bg=frame_color, command=obj1.btnClear).grid(row=5,column=1)
btnEquals=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="=", bg=frame_color, command=obj1.btnEquals).grid(row=5,column=2)
btnDiv=Button(calculator_frame, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="/", bg=frame_color, command=lambda:obj1.btnClick("/")).grid(row=5,column=3)


window.mainloop()
