import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import PIL.Image
import PIL.ImageTk
import random
import datetime
from functools import partial
#from cassandra.cluster import Cluster
#cluster = Cluster(['127.0.0.1'])
#session = cluster.connect()
#untuk memakai ketiga diatas harus menjalankan cassandra.bat -f nya terlebih dahulu di command prompt(run as admin)


class window1: #HOME
    def __init__(self, master):
        self.master= master
        self.master.title("TOPPAY")
        self.master.config(bg="orange")

        lebar=500
        tinggi=300

        #membuat frame berada ditengah
        setTengahX = (self.master.winfo_screenwidth()-lebar)//2
        setTengahY = (self.master.winfo_screenheight()-tinggi)//2
        self.master.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        

        title=Label(self.master, text= "Selamat Datang Di Aplikasi TOPPAY", font = ("OCR A Extended", 15, 'bold'), bg= "orange", fg = "black")
        title.pack()

        path = r"C:\Users\zakiyah\Pictures\topup.png"
    
        im = PIL.Image.open(path)
        photo = PIL.ImageTk.PhotoImage(im)

        label = Label(self.master, image=photo)
        label.image = photo 
        label.pack(side=TOP, expand=True)
        
        
        tmblsignin = Button(self.master, text="SIGN IN <<<", command=self.new_window3, bg="white", font = ("helvetica", 20))
        tmblsignin.pack(fill=X, side=RIGHT)
     
        tmblsignup = Button(self.master, text=">>> SIGN UP", command=self.new_window2, bg="white", font = ("helvetica", 20))
        tmblsignup.pack(fill="both", side=LEFT)
        
#membuat perintah untuk tampilan baru
    def new_window2 (self) :
        self.master.destroy()
        self.newwindow = Tk()
        self.app=window2(self.newwindow)

    def new_window3 (self) :
        self.master.destroy()
        self.new_window3 = Tk()
        self.app=window3(self.new_window3)

class window2: #SIGN UP 
    def __init__ (self, master) :
        self.master= master
        self.master.title("SIGN UP")
        
        lebar=370
        tinggi=250

        #membuat frame berada ditengah
        setTengahX = (self.master.winfo_screenwidth()-lebar)//2
        setTengahY = (self.master.winfo_screenheight()-tinggi)//2
        self.master.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.master.config(bg="orange")
        self.frame = Frame(self.master, bg= "orange")
        self.frame.pack()
        
        
        nama = Label(self.frame, text="Nama        :", font=15, bg= "orange", height=2).grid(row=0)
        entrynama =Entry(self.frame, width=30, font=15).grid(row=0, column=1)
        nmrhp = Label(self.frame, text="Nomor HP :", font=15, bg= "orange", height=2).grid(row=1)
        entrynmrhp =Entry(self.frame, width=30, font=15).grid(row=1, column=1)
        username = Label(self.frame, text="Username :", font=15, bg= "orange", height=2).grid(row=2)
        entryusername =Entry(self.frame, width=30, font=15).grid(row=2, column=1)
        pswd = Label(self.frame, text="Password :", font=15, bg= "orange", height=2).grid(row=3)
        password = StringVar()
        entrypswd =Entry(self.frame, textvariable=password, show='*', width=30, font=15).grid(row=3, column=1)

        tmblok =Button(self.frame, text='  OK   ', font=15, command= self.message).grid(row=6, column=0, pady=10)
        tmblkembali =Button(self.frame, text='Kembali', font=15, command= self.tampilanawal).grid(row=6, column=1)

    def message(self):
        messagebox.showinfo("", "Data Berhasil Disimpan")

    def tampilanawal(self):
        self.master.destroy()
        self.newwindow = Tk()
        self.app=window1(self.newwindow)
        

class window3: #SIGN IN AS (Admin/Customer)
    def __init__ (self, master) :
        self.master= master
        self.master.title("SIGN IN")

        lebar=300
        tinggi=170

        #membuat frame berada ditengah
        setTengahX = (self.master.winfo_screenwidth()-lebar)//2
        setTengahY = (self.master.winfo_screenheight()-tinggi)//2
        self.master.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.master.config(bg="orange")
        self.frame = Frame(self.master, bg= "orange")
        self.frame.pack()

        title=Label(self.frame, text= "SIGN IN AS:", height=2, font = ("OCR A Extended", 15, "bold"), bg= "orange", fg = "black")
        title.pack(side=TOP)

        tmbladmin = Button(self.frame, text=" ADMIN ", width=50, bg="white", font = ("calibri", 20), command=self.new_window4)
        tmbladmin.pack(fill=X, expand=True)
     
        tmblcustomer = Button(self.frame, text="CUSTOMER", width=50, bg="white", font = ("calibri", 20), command=self.new_window5)
        tmblcustomer.pack(fill=X, side=BOTTOM, expand=True)

    def new_window4 (self) :
        self.master.destroy()
        self.newwindow = Tk()
        self.app=window4(self.newwindow)

    def new_window5 (self) :
        self.master.destroy()
        self.newwindow = Tk()
        self.app=window5(self.newwindow)

class window4: #SIGN IN Admin
    def __init__ (self, master) :
        self.master= master
        self.master.title("Admin")

        lebar=370
        tinggi=140

        #membuat frame berada ditengah
        setTengahX = (self.master.winfo_screenwidth()-lebar)//2
        setTengahY = (self.master.winfo_screenheight()-tinggi)//2
        self.master.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.master.config(bg="orange")
        self.frame = Frame(self.master, bg= "orange")
        self.frame.pack()

        usernameadmin= Label(self.frame, text="Username:", font=15, bg= "orange").grid(row=2)
        username = StringVar()
        usernameadmin =Entry(self.frame, textvariable=username, width=30, font=15).grid(row=2, column=1)
        
        passwordadmin= Label(self.frame, text="Password:", font=15, bg= "orange").grid(row=3)
        password = StringVar()
        passwordadmin =Entry(self.frame,textvariable=password, show='*', width=30, font=15).grid(row=3, column=1)

        tmblok =Button(self.frame, text='  OK   ', font=15, command=self.new_window8).grid(row=6, column=0, pady=10)
        tmblkembali =Button(self.frame, text='Kembali', font=15, command= self.tampilanawal).grid(row=6, column=1)

#membuat perintah untuk tampilan baru
    def new_window8 (self) :
        self.master.destroy()
        self.newwindow = Tk()
        self.app=window8(self.newwindow)

    def tampilanawal(self):
        self.master.destroy()
        self.newwindow = Tk()
        self.app=window1(self.newwindow)

class window5: #SIGN IN Customer
    def __init__ (self, master) :
        self.master= master
        self.master.title("Customer")

        lebar=370
        tinggi=140
        
        #membuat frame berada ditengah
        setTengahX = (self.master.winfo_screenwidth()-lebar)//2
        setTengahY = (self.master.winfo_screenheight()-tinggi)//2
        self.master.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
        self.master.config(bg="orange")
        self.frame = Frame(self.master, bg= "orange")
        self.frame.pack()

        usrnm = Label(self.frame, text="Username :", font=15, bg= "orange").grid(row=3)
        username = StringVar()
        usrnm =Entry(self.frame, textvariable=username, width=30, font=15).grid(row=3, column=1)
        
        pswd = Label(self.frame, text="Password  :", font=15, bg= "orange").grid(row=4)
        password = StringVar()
        pswd =Entry(self.frame, textvariable=password, show='*', width=30, font=15).grid(row=4, column=1)

        tmblok =Button(self.frame, text='  OK   ', font=15, command=self.new_window6).grid(row=6, column=0, pady=10)
        tmblkembali =Button(self.frame, text='Kembali', font=15, command= self.tampilanawal).grid(row=6, column=1)

    def new_window6 (self) :
        self.master.destroy()
        self.newwindow = Tk()
        self.app=window6(self.newwindow)

    def tampilanawal(self):
        self.master.destroy()
        self.newwindow = Tk()
        self.app=window1(self.newwindow)

class window6: #Layanan Customer
    def __init__ (self, master) :
        self.master= master
        self.master.title("TOPPAY")

        lebar=400
        tinggi=500

        setTengahX = (self.master.winfo_screenwidth()-lebar)//2
        setTengahY = (self.master.winfo_screenheight()-tinggi)//2
        self.master.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))


#membuat perintah untuk tampilan yang terdiri dari tab
        tab_control = ttk.Notebook(self.master)
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab3 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Token Pulsa')
        tab_control.add(tab2, text='Token Listrik')
        tab_control.add(tab3, text='Notifikasi')

        #Tampilan Pulsa
        nmrhp = Label(tab1, text= 'Nomor HP        :', font = ("times new roman",15, "bold")).grid(row=0, column=0, pady=5)
        nmrhp = Entry(tab1, width=25, font=20).grid(column=1, row=0, pady=5)
        kartu = Label(tab1, text= 'Kartu Provider :', font = ("times new roman",15, "bold")).grid(row=1, column=0, pady=5)
        kartu = Entry(tab1, width=25, font=20).grid(column=1, row=1, pady=5)
        
        tombol1 =Button(tab1, text=' 5.000 \n \n(Rp7.000) ', font=20, command=self.new_window7).grid(row=5, column=0, pady=10)
        tombol2 =Button(tab1, text='10.000 \n \n(Rp12.000)', font=20, command=self.new_window7).grid(row=5, column=1)
        tombol3 =Button(tab1, text='20.000 \n \n(Rp22.000)', font=20, command=self.new_window7).grid(row=6, column=0, pady=10)
        tombol4 =Button(tab1, text='25.000 \n \n(Rp27.000)', font=20, command=self.new_window7).grid(row=6, column=1)
        tombol5 =Button(tab1, text='50.000 \n \n(Rp52.000)', font=20, command=self.new_window7).grid(row=7, column=0, pady=10)
        tombol6 =Button(tab1, text='100.000 \n \n(Rp102.000)', font=20, command=self.new_window7).grid(row=7, column=1)
        tombol8 =Button(tab1, text='Keluar', width=20, font=30, bg="black", fg="white", command=self.keluar).grid(row=9, column=1, pady=10)


        #Tampilan Token Listrik
        nmrmtr = Label(tab2, text= 'Nomor Meteran :', font = ("times new roman",15, "bold")).grid(row=0, column=0, pady=5)
        nmrmtr = Entry(tab2, width=25, font=20).grid(column=1, row=0, pady=5)
        tombol9 =Button(tab2, text=' 20.000 \n \n(Rp22.000) ', font=20, command=self.new_window7).grid(row=4, column=0, pady=10)
        tombol10 =Button(tab2, text='50.000 \n \n(Rp52.000)', font=20, command=self.new_window7).grid(row=4, column=1)
        tombol11 =Button(tab2, text='100.000 \n \n(Rp102.000)', font=20, command=self.new_window7).grid(row=5, column=0, pady=10)
        tombol12 =Button(tab2, text='200.000 \n \n(Rp202.000)', font=20, command=self.new_window7).grid(row=5, column=1)
        tombol13 =Button(tab2, text='500.000 \n \n(Rp505.000)', font=20, command=self.new_window7).grid(row=6, column=0, pady=10)
        tombol14 =Button(tab2, text='1.000.000 \n \n(Rp1.005.000)', font=20, command=self.new_window7).grid(row=6, column=1)
        tombol16 =Button(tab2, text='Keluar', width=20, font=30, bg="black", fg="white", command=self.keluar).grid(row=8, column=1)
        
        tab_control.pack(expand=1, fill='both')
        
    def new_window7 (self) :
        self.master.destroy()
        self.newwindow = Tk()
        self.app=window7(self.newwindow)


    def keluar(self):
        msgbox = messagebox.askquestion ('Keluar','Kamu yakin akan keluar dari aplikasi',icon = 'warning')
        if msgbox == 'yes':
            self.master.destroy()
            self.newwindow = Tk()
            self.app=window1(self.newwindow)

class window7: #Pembayaran
    def __init__ (self, master) :
        self.master= master
        self.master.title("Pembayaran")

        lebar=400
        tinggi=300

        setTengahX = (self.master.winfo_screenwidth()-lebar)//2
        setTengahY = (self.master.winfo_screenheight()-tinggi)//2
        self.master.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))

        rad1 = Radiobutton(self.master,text='Kartu Kredit',  font=20, value=1)
        no = Label(self.master, text= 'No :',  font=20).grid(row=3, column=0)
        no = Entry(self.master,  font=20).grid(column=1, row=3)
        rad2 = Radiobutton(self.master,text='Kartu Debit',  font=20, value=2)
        teksno = Label(self.master, text= 'No :',  font=20).grid(row=5, column=0)
        teksno = Entry(self.master,  font=20).grid(column=1, row=5)
        rad3 = Radiobutton(self.master,text='Cash           ',  font=20, value=3)

        rad1.grid(column=0, row=2)
        rad2.grid(column=0, row=4)
        rad3.grid(column=0, row=6)
        tmblbyr =Button(self.master, text='Bayar  ',  font=20, command=self.message).grid(row=8, column=0, pady=15)
        tmblkmbl =Button(self.master, text='Kembali',  font=20, command=self.kembali).grid(row=8, column=1)

    def message(self):
        messagebox.showinfo("Status", "Transaksi Berhasil")

    def kembali(self):
        self.master.destroy()
        self.newwindow = Tk()
        self.app=window6(self.newwindow)
    

#tampilan untuk data transaksi pelanggan (tampilan admin)
judul_kolom = ("ID Payment","Username","Tanggal Transaksi","Nomor HP", "Nomor Meteran","Jenis Pembelian")
class window8(): #tampilan admin (daftar transaksi customer)
    def __init__ (self, master) :
        self.master= master
        self.master.title("Admin")

        lebar=1200
        tinggi=600

        setTengahX = (self.master.winfo_screenwidth()-lebar)//2
        setTengahY = (self.master.winfo_screenheight()-tinggi)//2
        self.master.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))

        title=Label(self.master, text= "Daftar Transaksi Customer", height=2, font = ("helvatica", 15, "bold"), bg="orange", fg = "black")
        title.pack(fill=X)
        
        mainFrame = Frame(self.master)
        mainFrame.pack(side=TOP,fill=X)
        tmbl = Frame(self.master)
        tmbl.pack(side=TOP, fill=X)
        tabel = Frame(self.master)
        tabel.pack(expand=YES, side=TOP,fill=Y)
       
        Label(mainFrame, text='  ').grid(row=0, column=0)
        Label(tmbl, text='  ').grid(row=1, column=0)

        Label(mainFrame, text='ID Payment').grid(row=1, column=0, sticky=W,padx=20)
        Label(mainFrame, text=':').grid(row=1, column=1, sticky=W,pady=5,padx=10)
        self.entryid = Entry(mainFrame, width=30, font=15)
        self.entryid.grid(row=1, column=2,sticky=W)


        Label(mainFrame, text="Username").grid(row=2, column=0, sticky=W,padx=20)
        Label(mainFrame, text=':').grid(row=2, column=1, sticky=W,pady=5,padx=10)
        self.entryusrnm = Entry(mainFrame, width=30, font=15)
        self.entryusrnm.grid(row=2, column=2,sticky=W)

        Label(mainFrame, text="Tanggal Transaksi").grid(row=3, column=0, sticky=W,padx=20)
        Label(mainFrame, text=':').grid(row=3, column=1, sticky=W,pady=5,padx=10)

        #set tgl
        tgl = Frame(mainFrame)
        tgl.grid(row=3,column=2,sticky=W)
        self.entHari = Entry(tgl, width=5, font=15)
        self.entHari.grid(row=1, column=0,sticky=W)
        self.entBulan = Entry(tgl, width=5, font=15)
        self.entBulan.grid(row=1, column=1,sticky=W,padx=2)
        self.entTahun = Entry(tgl, width=8, font=15)
        self.entTahun.grid(row=1, column=2,sticky=W,padx=2)
        Label(tgl, text='(dd/mm/yyyy)').grid(row=1, column=3, sticky=E,padx=5)
                

        Label(mainFrame, text="Nomor HP").grid(row=5, column=0, sticky=W,padx=20)
        Label(mainFrame, text=':').grid(row=5, column=1, sticky=W,pady=5,padx=10)
        self.entryhp = Entry(mainFrame, width=30, font=15)
        self.entryhp.grid(row=5, column=2,sticky=W)

        Label(mainFrame, text="Nomor Meteran").grid(row=6, column=0, sticky=W,padx=20)
        Label(mainFrame, text=':').grid(row=6, column=1, sticky=W,pady=5,padx=10)
        self.entnmrmtr = Entry(mainFrame, width=30, font=15)
        self.entnmrmtr.grid(row=6, column=2,sticky=W)

        Label(mainFrame, text="Jenis Pembelian").grid(row=7, column=0, sticky=W,padx=20)
        Label(mainFrame, text=':').grid(row=7, column=1, sticky=W,pady=5,padx=10)
        self.entryjenis = Entry(mainFrame, width=30, font=15)
        self.entryjenis.grid(row=7, column=2,sticky=W)


        self.tmblsave = Button(tmbl, text='Save', width=12, relief=FLAT, bd=2, bg="black", fg="white")
        self.tmblsave.grid(row=0, column=1,padx=5)

        self.tmblupdate = Button(tmbl, text='Update', width=13, relief=FLAT, bd=2, bg="black", fg="white")
        self.tmblupdate.grid(row=0,column=2,pady=10, padx=5)
                
        self.tmblclear = Button(tmbl, text='Clear', width=13, relief=FLAT, bd=2, bg="black", fg="white")
        self.tmblclear.grid(row=0,column=3,pady=10, padx=5)

        self.tmblkeluar = Button(tmbl, text='Keluar', command=self.keluar, width=13, relief=FLAT, bd=2, bg="red", fg="white")
        self.tmblkeluar.grid(row=0,column=4,pady=10, padx=5)


        # buat frame untuk tabel beserta scrollbar-nya
        fr_data = Frame(tabel, bd=10)
        fr_data.pack(fill=BOTH, expand=YES)
         
        # buat tabel dengan Treeview
        self.Tabel = ttk.Treeview(fr_data, columns=judul_kolom, show='headings')
        self.Tabel.bind("<Double-1>")
        
        # buat scrollbar
        vertical = Scrollbar(fr_data, orient='vertical', 
                command=self.Tabel.yview)
        horizontal = Scrollbar(fr_data, orient='horizontal', 
                command=self.Tabel.xview)
        # pasang dengan layout manager pack()       
        vertical.pack(side=RIGHT, fill=Y)
        horizontal.pack(side=BOTTOM, fill=X)
        self.Tabel.pack(side=LEFT, fill=BOTH)
             
         
        # isi judul tabel
        for kolom in judul_kolom:
            self.Tabel.heading(kolom, text=kolom)
                     
    def keluar(self): #keluar dr tampilan adimin ke tampilan awal(home)
        msgbox = messagebox.askquestion ('Keluar','Kamu yakin akan keluar dari aplikasi',icon = 'warning')
        if msgbox == 'yes':
            self.master.destroy()
            self.newwindow = Tk()
            self.app=window1(self.newwindow)

if __name__ == '__main__':

    root = Tk()
    app = window1(root)
    
