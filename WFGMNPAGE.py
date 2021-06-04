import tkinter.ttk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import WFGGLOBAL as Wg
import WFGFILEREAD1 as Wr1
import time


root = Tk()
root.geometry('1000x600')
root.resizable(0,0)
style=Style()
style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'red')

root.title('WellsFargo Advisor Extractor')
Label(root, text ='Welcome to WellsFargo Advisor Extraction process', font = 'arial 20')
display = Entry(root)


Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

display = Entry(root)
File_success = StringVar()
Notify = StringVar()
pb1= tkinter.ttk.Progressbar(root, orient=HORIZONTAL, length=100, mode='indeterminate')
pb1.pack(expand=True)
pb1.place(x=290, y=500)



Notify.set("\n"
           "\nDefault location for Storing the results CSV File is C:/Users/P7165881/Desktop/Brodridge/        "
           "\n")

def Exit():
    root.destroy()


def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
    File_success.set("")

def Browse():

    Wg.File_Input = filedialog.askopenfile(initialdir="C:/Users/P7165881/Desktop/Brodridge/")


    try:
        File_success.set( Wg.File_Input.name + ' File opened Successfully')
        Text.set(Wg.File_Input.name)
    except AttributeError:
        File_success.set('No File selected, Please select a File')
        Text.set(" ")

    Label(root, font='arial 12', textvariable=File_success).place(x=60, y=280)


def Start():

    input_file = Wg.File_Input.name
    print('this is File : ' + input_file)
    Wr1.Start_Process(input_file)
    Label(root, font='arial 12 bold', text='Completed the extraction process, Files :').place(x=60, y=320)
    Label(root, font='arial 12 bold', text=Wg.File_output1 + ',').place(x=70, y=340)
    Label(root, font='arial 12 bold', text=Wg.File_output2 + ',').place(x=70, y=360)
    Label(root, font='arial 12 bold', text='are created successfully').place(x=290, y=380)

def step():
    #print(range1)
    print('started step')
    for i in range(5):
        root.update_idletasks()
        pb1['value'] += 20

        time.sleep(1)


Label(root, font= 'arial 12', text='Location of Input file containing Members').place(x= 60,y=60)

Entry(root, font = 'arial 10', textvariable = Text,width =50).place(x=390, y = 60)

btn1= Button(root,text ='Browse' ,command = Browse).place(x=790, y = 60)
btn_help= Button(root,text ='HELP' ,command = Browse).place(x=880, y = 60)
lable1 = tkinter.ttk.Label(root, font = 'arial 12 bold', textvariable =Notify,background="light green" ).place(x=60, y = 100)

tkinter.ttk.Label(select=lable1).pack(fill= tkinter.X, pady=10)

print(tkinter.X)
btn2 = Button(root,text ='RESET' ,command = Reset).place(x=80, y = 230)
btn3 = Button(root,text ='EXIT' ,style = 'W.TButton',command = Exit).place(x=180, y = 230)
btn4 = Button(root,text ='Start' ,command = Start).place(x=280, y = 230)

root.mainloop()