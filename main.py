from tkinter import *
from tkinter.ttk import Combobox
import webbrowser
window=Tk()

link = ""

lbl=Label(window, text="GOOGLE DORKS", fg='black', font=("Helvetica", 16))
lbl.place(x=250, y=40)

lbl=Label(window, text="Enter Here : ", fg='black', font=("Helvetica", 16))
lbl.place(x=50, y=100)

txtfld0=Entry(window, text="enter here", bd=3, width=50)
txtfld0.place(x=200, y=100)

txtfld1=Entry(window, text="title", width= 50 )
txtfld1.place(x=250, y=170)



txtfld2=Entry(window, text="url", width= 50 )
txtfld2.place(x=250, y=220)



txtfld3=Entry(window, text="domain", width= 50 )
txtfld3.place(x=250, y=270)




txtfld4=Entry(window, text="file_type", width= 50 )
txtfld4.place(x=250, y=320)



txtfld5=Entry(window, text="query", width= 50 )
txtfld5.place(x=250, y=370)


t0=""
t1=""
t2=""
t3=""
t4=""




def inputt():
    t0=txtfld0.get()
    t1=txtfld1.get()
    t2=txtfld2.get()
    t3=txtfld3.get()
    t4=txtfld4.get()
    t5=txtfld5.get()

   
    link = t0

    if t1!="":
        link=link+"+intitle%3A"+t1
    if t2!="":
        link=link+"+inurl%3A"+t2
    if t3!="":
        link=link+"+domain%3A"+t3
    if t4!="":
        link=link+"+filetype%3A"+t4
    if t5!="":
        link=link+"+textquery%3A"+t5
    se = "https://www.google.com/search?q=" + link
    lbl6 = Label(window, text=se)
    lbl6.place(x=60, y=420)
    return link



def reset():
    txtfld0 = ""

    txtfld1 = ""






lbl1=Label(window, text="In Title : ")
lbl1.place(x=60, y=170)

lbl2=Label(window, text="In URL : ")
lbl2.place(x=60, y=220)

lbl3=Label(window, text="Domain : ")
lbl3.place(x=60, y=270)

lbl4=Label(window, text="File Type : ")
lbl4.place(x=60, y=320)

lbl5=Label(window, text="Text Query : ")
lbl5.place(x=60, y=370)


def search():
    #browser module
    link =inputt()
    se = "https://www.google.com/search?q="+ link
    url = se
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe" #ENTER YOUR BROWSER PATH
    print(url)

    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(url)


btn1=Button(window, text="Generate Final Query", fg='red',width=72,command=inputt)
btn1.place(x=60, y=460)

btn2=Button(window, text="RESET", fg='black',width=20,command=reset)
btn2.place(x=100, y=500)

btn3=Button(window, text="SEARCH", fg='black',width=20,command=search)
btn3.place(x=350, y=500)

window.title('Google Dorks')
window.geometry("670x550+10+10")
window.mainloop()