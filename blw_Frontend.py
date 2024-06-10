from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import datetime
import blw

class BLWApp():
    def __init__(self, master):
        self.master = master
        self.master.title('Banaras Locomotive Works')
        self.master.geometry('1080x750')
        self.master.config(bg='Navajo white')

        # ==================================================Variables=================================================
        self.pid = StringVar()
        self.pn = StringVar()
        self.po = StringVar()
        self.date = StringVar()
        self.cat = StringVar()
        self.lts = StringVar()
        self.total = DoubleVar()
        self.s = DoubleVar()
        self.d = DoubleVar()

        # ==================================================Functions=================================================
        def Tuple(event):
            try:
                global st
                index = self.list.curselection()[0]
                st = self.list.get(index)

                self.pid_entry.delete(0, END)
                self.pid_entry.insert(END, st[1])
                self.pn_entry.delete(0, END)
                self.pn_entry.insert(END, st[2])
                self.po_entry.delete(0, END)
                self.po_entry.insert(END, st[3])
                self.Date_entry.delete(0, END)
                self.Date_entry.insert(END, st[4])
                self.cat_entry.delete(0, END)
                self.cat_entry.insert(END, st[5])
                self.lts_entry.delete(0, END)
                self.lts_entry.insert(END, st[6])
                self.total_entry.delete(0, END)
                self.total_entry.insert(END, st[7])
                self.s_entry.delete(0, END)
                self.s_entry.insert(END, st[8])
                self.d_entry.delete(0, END)
                self.d_entry.insert(END, st[9])
            except IndexError:
                pass

        def Insert():
            if (len(self.pid.get()) != 0):
                blw.insert(self.pid.get(), self.pn.get(), self.po.get(), self.date.get(),
                                   self.cat.get(), self.lts.get(), self.total.get(), self.s.get(),
                                   self.d.get())
                self.list.delete(0, END)
                self.list.insert(END, (self.pid.get(), self.pn.get(), self.po.get(), self.date.get(),
                                       self.cat.get(), self.lts.get(), self.total.get(), self.s.get(),
                                       self.d.get()))

        def View():
            self.list.delete(0, END)
            for row in blw.view():
                self.list.insert(END, row, str(' '))

        def Reset():
            self.pid.set(' ')
            self.pn.set(' ')
            self.po.set(' ')
            #self.date.set(' ')
            self.cat.set(' ')
            self.lts.set(' ')
            self.s.set(' ')
            self.d.set(' ')
            self.Display.delete('1.0', END)
            self.list.delete(0, END)

        def Delete():
            blw.delete(st[0])
            Reset()
            View()

        def Receipt():
            self.Display.delete('1.0', END)
            self.Display.insert(END, '\t\tRECEIPT' + '\n\n')
            self.Display.insert(
                END, '\tPRODUCT NUMBER .\t:' + self.pid.get() + '\n')
            self.Display.insert(END, '\tPRODUCT NAME:' +
                                self.pn.get() + '\n')
            self.Display.insert(END, '\tPURCHASE ORDER\t:'+
                                self.po.get() + '\n')
            self.Display.insert(
                END, '\tDATE\t:'+ self.date.get() + '\n')
            self.Display.insert(
                END, '\tCATEGORY\t:'+ self.cat.get() + '\n')
            self.Display.insert(
                END, '\t LONG TERM SUPPORT\t:'+ self.lts.get() + '\n\n')

            x1 = (self.var_1.get())
            x2 = (self.s.get())
            x3 = (x1 - x2)

            """self.Display.insert(END, '\tTotal Amount:' str(x1) + '\n')
            self.Display.insert(END, '\tSTOCK:' str(x2) + '\n')
            self.Display.insert(END, '\tDEMAND\t:' str(x3) + '\n')"""

            self.due.set(x3)

        def Search():
            self.list.delete(0, END)
            for row in blw.search(self.pid.get(), self.pn.get(), self.po.get(), self.date.get(),
                                          self.cat.get(), self.lts.get(), self.total.get(), self.s.get(),
                                          self.d.get()):
                self.list.insert(END, row, str(' '))

        def Update():
            blw.delete(st[0])
            Insert()

        def Exit():
            Exit = tkinter.messagebox.askyesno(
                'Attention', 'Confirm, if you want to Exit')
            if Exit > 0:
                root.destroy()
                return

        # ==================================================Frames===================================================
        Main_Frame = Frame(self.master, bg='Navajo white')
        Main_Frame.grid()

        Title_Frame = LabelFrame(
            Main_Frame, width=1080, height=100, bg='Navajo white', relief='ridge', bd=15)
        Title_Frame.pack(side=TOP)

        self.lblTitle = Label(Title_Frame, font=('arial', 40, 'bold'), text='Banaras Locomotive Works',
                              bg='navajowhite', padx=3)
        self.lblTitle.grid(padx=393)

        Data_Frame = Frame(Main_Frame, width=1350, height=350,
                           bg='Navajo white', relief='ridge', bd=15)
        Data_Frame.pack(side=TOP, padx=15,pady=10)

        Frame_1 = LabelFrame(Data_Frame, width=850, height=350, bg='Navajo white', relief='ridge', bd=13,
                             text='DASHBOARD', font=('arial', 15, 'bold'))
        Frame_1.pack(side=LEFT, padx=10,pady=10)

        Frame_2 = LabelFrame(Data_Frame, width=495, height=350, bg='Navajo white', relief='ridge', bd=13,
                             text='RECEIPT', font=('arial', 15, 'bold'))
        Frame_2.pack(side=RIGHT, padx=10,pady=10)

        List_Frame = Frame(Main_Frame, width=1350, height=150,
                           bg='Navajo white', relief='ridge', bd=15)
        List_Frame.pack(side=TOP, padx=15,pady=10)

        Button_Frame = Frame(Main_Frame, width=1350, height=80,
                             bg='Navajo white', relief='ridge', bd=15)
        Button_Frame.pack(side=TOP)

        # ===================================================Labels================================================
        self.pid_label = Label(Frame_1, text='PRODUCT NUMBER : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.pid_label.grid(row=0, column=0, padx=15, sticky=W)

        self.pn_label = Label(Frame_1, text='PRODUCT NAME : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.pn_label.grid(row=1, column=0, padx=15, sticky=W)

        self.po_label = Label(Frame_1, text='PURCHASE ORDER :', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.po_label.grid(row=2, column=0, padx=15, sticky=W)

        self.Date_label = Label(Frame_1, text='DATE : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.Date_label.grid(row=3, column=0, padx=15, sticky=W)

        self.cat_label = Label(Frame_1, text='CATEGORY : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.cat_label.grid(row=4, column=0, padx=15, sticky=W)

        self.lts_label = Label(Frame_1, text='LONG TERM SUPPORT: ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.lts_label.grid(row=5, column=0, padx=15, sticky=W)

        self.total_label = Label(Frame_1, text='TOTAL AMOUNT : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.total_label.grid(row=2, column=2, padx=5, sticky=W)

        self.s_label = Label(Frame_1, text='STOCK : ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.s_label.grid(row=3, column=2, padx=5, sticky=W)

        self.d_label = Label(Frame_1, text='DEMAND: ', font=(
            'arial', 14, 'bold'), bg='Navajo white')
        self.d_label.grid(row=4, column=2, padx=5, sticky=W)

        # ==================================================Entries=================================================
        self.var_1 = DoubleVar(Frame_1, value='रु 36265')
        d1 = datetime.date.today()
        self.date.set(d1)

        self.pid_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.pid)
        self.pid_entry.grid(row=0, column=1, padx=15, pady=5)

        self.pn_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.pn)
        self.pn_entry.grid(row=1, column=1, padx=15, pady=5)

        self.po_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.po)
        self.po_entry.grid(row=2, column=1, padx=15, pady=5)

        self.Date_entry = Entry(Frame_1, font=(
            'arial', 14), textvariable=self.date)
        self.Date_entry.grid(row=3, column=1, padx=15, pady=5)

        self.cat_entry = ttk.Combobox(Frame_1, values=(' '),
                                         font=('arial', 14), width=19, textvariable=self.cat)
        self.cat_entry.grid(row=4, column=1, padx=15, pady=5)

        self.lts_entry = ttk.Combobox(Frame_1, values=(' '), font=('arial', 14), width=19,
                                      textvariable=self.lts)
        self.lts_entry.grid(row=5, column=1, padx=15, pady=5)

        self.total_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.var_1, state='readonly')
        self.total_entry.grid(row=2, column=3, padx=8, pady=5)

        self.s_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.s)
        self.s_entry.grid(row=3, column=3, pady=5)

        self.d_entry = Entry(Frame_1, font=(
            'arial', 14), width=10, textvariable=self.d)
        self.d_entry.grid(row=4, column=3, pady=7)

        # ==================================================Frame_2=================================================
        self.Display = Text(Frame_2, width=42, height=12,
                            font=('arial', 14, 'bold'))
        self.Display.grid(row=0, column=0, padx=3)

        # =============================================List box and scrollbar===========================================
        sb = Scrollbar(List_Frame)
        sb.grid(row=0, column=1, sticky='ns')

        self.list = Listbox(List_Frame, font=(
            'arial', 13, 'bold'), width=140, height=8)
        self.list.bind('<<ListboxSelect>>', Tuple)
        self.list.grid(row=0, column=0)
        sb.config(command=self.list.yview)

        # ==================================================Buttons=================================================
        btnSave = Button(Button_Frame, text='SAVE', font=(
            'arial', 14, 'bold'), width=10, command=Insert)
        btnSave.grid(row=0, column=0, padx=5, pady=5)

        btnDisplay = Button(Button_Frame, text='DISPLAY', font=(
            'arial', 14, 'bold'), width=10, command=View)
        btnDisplay.grid(row=0, column=1, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='RESET', font=(
            'arial', 14, 'bold'), width=10, command=Reset)
        btnReset.grid(row=0, column=2, padx=5, pady=5)

        btnReset = Button(Button_Frame, text='UPDATE', font=(
            'arial', 14, 'bold'), width=10, command=Update)
        btnReset.grid(row=0, column=3, padx=5, pady=5)

        btnSearch = Button(Button_Frame, text='SEARCH', font=(
            'arial', 14, 'bold'), width=10, command=Search)
        btnSearch.grid(row=0, column=4, padx=5, pady=5)

        btnDelete = Button(Button_Frame, text='DELETE', font=(
            'arial', 14, 'bold'), width=10, command=Delete)
        btnDelete.grid(row=0, column=5, padx=5, pady=5)

        btnReceipt = Button(Button_Frame, text='RECEIPT', font=(
            'arial', 14, 'bold'), width=10, command=Receipt)
        btnReceipt.grid(row=0, column=6, padx=5, pady=5)

        btnExit = Button(Button_Frame, text='EXIT', font=(
            'arial', 14, 'bold'), width=10, command=Exit)
        btnExit.grid(row=0, column=7, padx=5, pady=5)


root = Tk()
obj = BLWApp(root)
root.mainloop()
