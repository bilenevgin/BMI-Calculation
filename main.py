import tkinter



def bmi_calculation():
    weight = text_area_weight.get("1.0", "end")
    height = text_area_height.get("1.0", "end")

    if weight and height:
        try:
            weight = float(weight)
            height = float(height)/100
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                label_bmi.config(text =f"BMI: {bmi:.2f} You are Under weight")
            elif 18.5 <= bmi < 25:
                label_bmi.config(text=f"BMI: {bmi:.2f} You are Normal weight")
            elif 25 <= bmi < 30:
                label_bmi.config(text=f"BMI: {bmi:.2f} You are Over weight")
            elif 30 <= bmi < 35:
                label_bmi.config(text=f"BMI: {bmi:.2f} You are first degree Obesity")
            elif 35 <= bmi < 40:
                label_bmi.config(text=f"BMI: {bmi:.2f} You are second degree Obesity")
            elif bmi >= 40:
                label_bmi.config(text=f"BMI: {bmi:.2f} You are third degree Obesity")

        except:
            label_bmi.config(text ="Please enter valid values")









my_window = tkinter.Tk()
my_window.title("BMI")
my_window.geometry("400x400")



my_label_weight = tkinter.Label(my_window, text="Enter your weight (kg)")
my_label_weight.place(relx = 0.34 , rely = 0.21)



text_area_weight = tkinter.Text(my_window, font=("Arial", 12), height=1, width=13)
text_area_weight.place(relx = 0.34 , rely = 0.30)



my_label_height = tkinter.Label(my_window, text="Enter your height (cm)")
my_label_height.place(relx=0.34, rely=0.40)


text_area_height = tkinter.Text(my_window, width=15, height=1)
text_area_height.place(relx = 0.34 , rely = 0.47)



label_bmi = tkinter.Label(my_window, text= "")
label_bmi.place(relx=0.33, rely=0.68)



my_button = tkinter.Button(my_window, text="Calculate", command=bmi_calculation)
my_button.place(relx=0.42, rely=0.56)







my_window.mainloop()