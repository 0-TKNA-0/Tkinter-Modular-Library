import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("All About Buttons")
window.geometry("600x400")

# Standard Button Widget
standardButtonString = tk.StringVar(value = "Standard Value")
standardButton = ttk.Button(
    window, 
    text = "Standard Button",
    command = lambda: print("DEBUG : STANDARD BUTTON PRESSED"),
    textvariable = standardButtonString)
standardButton.pack()

# Check Button Widget
# checkButtonVar = tk.StringVar() # CHECKS IF CHECK BUTTON IS ENABLED / DISABLED (STRING VERSION)
# checkButtonVar = tk.BooleanVar() # CHECKS IF CHECK BUTTON IS ENABLED / DISABLED (BOOLEAN VERSION)
checkButtonVar = tk.IntVar(value = 10) # CHECKS IF CHECK BUTTON IS ENABLED / DISABLED (INTEGER VERSION)
check1Button = ttk.Checkbutton(
    window, 
    text = "CheckBox #1",
    command = lambda: print(checkButtonVar.get()),
    variable = checkButtonVar,
    onvalue = 10,
    offvalue = 5)
check1Button.pack()

check2Button = ttk.Checkbutton(
    window,
    text = "CheckBox #2",
    command = lambda: checkButtonVar.set(5)) # Sets Check Button #1 to false when this is true 
check2Button.pack()


# Radio Buttons Widget
radioButtonVar = tk.StringVar()
radio1Button = ttk.Radiobutton(
    window, 
    text = "Radio Button #1",
    value = "Radio #1",
    variable = radioButtonVar,
    command = lambda: print(radioButtonVar.get()))
radio1Button.pack()

radio2Button = ttk.Radiobutton(
    window, 
    text = "Radio Button #2",
    value = 2,
    variable = radioButtonVar,
    command = lambda: print(radioButtonVar.get()))
radio2Button.pack(pady=(0, 30))

#--------------------------------------
# HELPFUL EXERCISE
def NEWRadioButtonChecker():
    print(NEWRadioVar.get()," : ", NEWCheckButtonVar.get())
    NEWCheckButtonVar.set(False)


NEWCheckButtonVar = tk.BooleanVar(value = True)
NEWCheckButton = ttk.Checkbutton(
    window, 
    text = "NEW CHECK BUTTON",
    variable = NEWCheckButtonVar,
    command = lambda: print(NEWRadioVar.get()))
NEWCheckButton.pack()


NEWRadioVar = tk.StringVar()
NEWRadio1Button = ttk.Radiobutton(
    window, 
    text = "NEW RADIO #1 BUTTON", 
    value = "A",
    variable = NEWRadioVar, 
    command = NEWRadioButtonChecker)
NEWRadio1Button.pack()

NEWRadio2Button = ttk.Radiobutton(
    window, 
    text = "NEW RADIO #2 BUTTON", 
    value = "B", 
    variable = NEWRadioVar,
    command = NEWRadioButtonChecker)
NEWRadio2Button.pack()


# Run window
window.mainloop()