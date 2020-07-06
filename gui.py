import os
import random
import time
from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile

import qrcode
from PIL import Image, ImageTk

#create window object 
app=Tk()
app.title('QR code Generator')
app.geometry('950x500')
app.configure(bg='light blue')

#App Description label
app_desc=StringVar()
desc_label=Label(app,text='This is a simple program to generate QR Code using an url',bg='light blue',font=('calibri',14))
desc_label.grid(row=0,column=1)
#Url Label
url_obj=StringVar()
url_label=Label(app,text='URL',bg='light blue',font=(14),pady=20)
url_label.grid(row=1,column=0,sticky=W)
#url Entry
url_entry=Entry(app,textvariable=url_obj,width=80)
url_entry.grid(row=1,column=1,columnspan=1,sticky=E)
gl_image=''
def qr_gen():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=3,
    )
    url=url_entry.get()
    if len(url)>1:
        qr.add_data(url)
        qr.make(fit=True)
        global gl_image 
        gl_image= qr.make_image(fill_color="blue", back_color="black")
        gl_image.save(os.path.abspath('qr_code.png'))
        
    else:
        qr.add_data(url)
        qr.make(fit=True)
        
        gl_image= qr.make_image(fill_color="blue", back_color="black")
        gl_image.save(os.path.abspath('qr_code.png'))
        messagebox.showwarning("Error", "Generated QR has no Data / Content")
    #Show generated image
    img_path=os.path.abspath('qr_code.png')
    img_retr=Image.open(img_path)
    image = img_retr.resize((250, 250), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(image)
    img = Label(image=render)
    img.image = render
    img.grid(row=5,column=1)
#btn to generate
button_gn = Button(app, text = "Generate", command = qr_gen,
                fg = "white", font = "calibri",
                bd = 2, bg = "blue", relief = "groove")
button_gn.grid(row=2, column=1)
#btn to download
def dowload_qrcode():
    global gl_image
    try:
               
        img_retr=os.path.abspath('qr_code.png')
        img_path=Image.open(img_retr)
        #if type(img_path) =PNGImageFile:
            
        img_saved=img_path.save(os.path.abspath('latest.png'))
        messagebox.showinfo("Download complete",'Image dowloaded to folder of this app, latest.png')
        #else:
        #messagebox.showerror("Error","Path not found")
    except FileNotFoundError:
            messagebox.showerror("Error","File not found")
download_btn = Button(app, text = "Download", command = dowload_qrcode,
                    fg = "white", font = "calibri",
                    bd = 2, bg = "green", relief = "groove")
download_btn.grid(row=3, column=1)
#btn to quit
quit_btn = Button(app, text = "Quit", command = app.destroy,
                fg = "white", font = "calibri",
                bd = 2, bg = "red", relief = "groove")
quit_btn.grid(row=4, column=1,padx=10)
#list box
listbox = Listbox(app, height = 10,  
                  width = 45,  
                  bg = "black", 
                  activestyle = 'dotbox',  
                  font = "calibri", 
                  fg = "blue") 
list_label = Label(app,bg='light blue', text = "How to Use:",font=(14))
list_label.grid(row=4,column=2)
listbox.insert(1, "1. Insert a link to a document/img/mp3/ hosted online.\n")
listbox.insert(2, "")  
listbox.insert(3, "2. Generate the qr code") 
listbox.insert(4, "") 
listbox.insert(5, "3. Scan the code using a phone") 
listbox.insert(6, "") 
listbox.insert(7, "4. Click open on the qr scanner app, this redirects") 
listbox.insert(8, " to the file") 
listbox.insert(10, "")
listbox.insert(11, "5. Download the QR Code to print / share") 
listbox.grid(row=5,column=2)



#start program
app.mainloop()
