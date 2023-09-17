'''
BMI CALCULATOR
vücut kitle indexi
boş bırakıldığında boy kilo gir diye uyarı verdirt
numara yerine yazı girdiğinde hata verdirt çökmesin

Severe Thinness	< 16
Moderate Thinness	16 - 17
Mild Thinness	17 - 18.5
"Normal"	18.5 - 25
"Overweight"	25 - 30
"Obese Class I"	30 - 35
"Obese Class II"	35 - 40
"Obese Class III"	> 40

#BMI = Kg / (m**2)

Yapılacak güncellemeler :
1- enter tuşuna basıldığında hesaplasın

'''

import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=300)


TEXT = ["Severe Thinness", "Moderate Thinness", "Mild Thinness", "Normal", "Overweight",
        "Obese Class I", "Obese Class II", "Obese Class III"]

def showText():

    global result
    global BMI
    '''    
    if not Kg and Metre == int:
        result = "Please enter a valid number"
    '''
    if BMI > 40:
        result = TEXT[7] #Obese Class III
    elif 40 >= BMI > 35:
        result = TEXT[6] #Obese Class II
    elif 35 >= BMI > 30:
        result = TEXT[5] #Obese Class I
    elif 30 >= BMI > 25:
        result = TEXT[4] #Overweight
    elif 25 >= BMI > 18.5:
        result = TEXT[3] #Normal
    elif 18.5 >= BMI > 17:
        result = TEXT[2] #Mild Thinness
    elif 17 >= BMI > 16:
        result = TEXT[1] #Moderate Thinness
    elif 16 >= BMI:
        result = TEXT[0] #Severe Thinness

    final_label.config(text=result)


# arayüz kodları
my_label1 = tkinter.Label(text="Enter Your Weight (KG)", width=50)
my_label1.config(padx=10,pady=15)

my_label2 = tkinter.Label(text="Enter Your Height (CM)", width=50)
my_label2.config(padx=10,pady=15)

my_entry1 = tkinter.Entry(width=20)
my_entry2 = tkinter.Entry(width=20)

final_label = tkinter.Label(width=50)
final_label.config(padx=10,pady=15)
final_label.pack_forget()


number_label = tkinter.Label(width=50)
number_label.config(padx=20,pady=15)


def calculator():
    global Kg
    global BMI
    global Metre
    global result

    ### sayı da girsem str harf de girsem str alıyor. İf kurup ayrım yapamıyorum.
    ### try - except kullanarak bu sorunu çözmüş oldum
    ShowWidget() ## TEXT'i gösteriyor

    try:
        GetKg = float(my_entry1.get())
        GetMetre = float(my_entry2.get())
        print(type(GetKg))
        print(type(GetMetre))
        Kg = GetKg
        Metre = GetMetre/100

        BMI = Kg / (Metre * Metre)
        number_label.config(text=f"Your BMI: {BMI:.2f}")

        showText()
        print(BMI)

    except ValueError:
        result = "Error, Please enter valid numeric values."
        final_label.config(text=result)


def ShowWidget():    #saklı olan alttaki yazıyı göstermesi için
    final_label.pack()

#button
my_button = tkinter.Button(width=15,text="Calculate",bg="white",command=calculator)

def appinterface(): #uygulama arayüzü sırası
    my_label1.pack()
    my_entry1.pack()
    my_label2.pack()
    my_entry2.pack()
    my_button.pack()
    final_label.pack_forget()
    number_label.pack()

appinterface()

window.mainloop()


