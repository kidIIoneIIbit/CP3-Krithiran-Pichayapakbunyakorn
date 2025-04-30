from tkinter import *

def leftclickbotton(event):
    print(float(textBoxWeight.get())/((float(textBoxHeight.get())/100)**2))
    labelResult.configure(text=float(textBoxWeight.get())/((float(textBoxHeight.get())/100)**2))
    result = float(textBoxWeight.get())/((float(textBoxHeight.get())/100)**2)
    if result > 29.9:
        labelBMI.configure(text="อ้วนมาก พบแพทย์ด่วน!", fg="red")
    elif result > 24.9:
        labelBMI.configure(text="อ้วนเกินควรออกกำลังกาย", fg="orange")
    elif result > 22.9:
        labelBMI.configure(text="น้ำหนักเกินเกณฑ์", fg="yellow")
    elif result > 18.5:
        labelBMI.configure(text="น้ำหนักปกติ", fg="green")
    else:
        labelBMI.configure(text="ผอมเกินไป", fg="red")
def rightclickbotton(event):
    print("RIght Click!!!")
    
def Doubleclickbotton(event):
    print("Double Click!!!")
    
MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง (cm)").grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelHeight = Label(MainWindow,text="น้ำหนัก (kg)").grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calcalateButton = Button(MainWindow,text="คำนวณ")
calcalateButton.bind("<Button-1>",leftclickbotton)
calcalateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
labelBMI = Label(MainWindow,text="ระดับ")
labelBMI.grid(row=2,column=2)
MainWindow.mainloop()
