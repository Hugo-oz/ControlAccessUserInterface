from tkinter import Entry, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END
from Conection import*


class Register(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
                                    
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0,row=0)
        self.frame2 = Frame(master, bg='navy')
        self.frame2.grid(column=0, row=1)
        self.frame3 = Frame(master)
        self.frame3.grid(rowspan=2, column=1, row=1)

        self.frame4 = Frame(master, bg='gray90')
        self.frame4.grid(column=0, row=2)

        self.userName = StringVar()
        self.registerCURP = StringVar()
        self.careerAddress = StringVar()
        self.userType = StringVar()
        self.status = StringVar()
        self.search = StringVar()

        self.dataBase = DataRegister()
        self.create_wietgs()

    def create_wietgs(self):
        Label(self.frame1, text = 'Registro de accesos',bg='gray90',fg='black', font=('Orbitron',15,'bold')).grid(column=0, row=0)
       
        Label(self.frame4, text = 'Control',fg='black', bg ='gray90', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4) 
        Button(self.frame4,command = self.searchRegisterCURP, text='Buscar por nombre', font=('Arial',8,'bold'), bg='gray50').grid(columnspan=2,column = 1, row=2)
        Entry(self.frame4,textvariable=self.search , font=('Arial',12), width=10).grid(column=0,row=2, pady=1, padx=8)
        Button(self.frame4,command = self.showAll, text='Recargar pagina', font=('Arial',10,'bold'), bg='gray50').grid(columnspan=3,column=1,row=3, pady=8)


        self.table = ttk.Treeview(self.frame3, height=21)
        self.table.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient = HORIZONTAL, command= self.table.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = Scrollbar(self.frame3, orient =VERTICAL, command = self.table.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.table.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
       
        self.table['columns'] = ('Name', 'UserType', 'Action')

        self.table.column('#0', minwidth=100, width=150, anchor='center')
        self.table.column('Name', minwidth=100, width=250 , anchor='center')
        self.table.column('UserType', minwidth=100, width=100, anchor='center' )
        self.table.column('Action', minwidth=100, width=50 , anchor='center')

        self.table.heading('#0', text='Fecha', anchor ='center')
        self.table.heading('Name', text='Nombre', anchor ='center')
        self.table.heading('UserType', text='Tipo de usuario', anchor ='center')
        self.table.heading('Action', text='Accion', anchor ='center')


        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='black')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.table.bind("<<TreeviewSelect>>", self.getRow)  # seleccionar  fila
        

    def addUserInfo(self):
        self.table.get_children()
        userName = self.userName.get()
        registerCURP = self.registerCURP.get()
        careerAddress = self.careerAddress.get()
        userType = self.userType.get()
        status = self.status.get()
        datos = (registerCURP, careerAddress, userType, status)
        if userName and registerCURP and careerAddress and userType and status !='':        
            self.table.insert('',0, text = userName, values=datos)
            self.dataBase.createUserAccess(userName, registerCURP, careerAddress, userType, status)


    def clearData(self):
        self.table.delete(*self.table.get_children())
        self.userName.set('')
        self.registerCURP.set('')
        self.careerAddress.set('')
        self.userType.set('')
        self.status.set('')

    def searchRegisterCURP(self):
        searchedRegisterCURP = self.search.get()
        searchedRegisterCURP = str("'" + searchedRegisterCURP + "'")
        searchedName = self.dataBase.searchUserAccess(searchedRegisterCURP)
        self.table.delete(*self.table.get_children())
        i = -1
        for dato in searchedName:
            i= i+1                       
            self.table.insert('',i, text = searchedName[i][0:1], values=searchedName[i][2:6])


    def showAll(self):
        self.table.delete(*self.table.get_children())
        register = self.dataBase.showUserAccess()
        i = -1
        for dato in register:
            i= i+1                       
            self.table.insert('',i, text = register[i][0:1], values=register[i][1:5])


    def deleteRow(self):
        fila = self.table.selection()
        if len(fila) !=0:        
            self.table.delete(fila)
            name = ("'"+ str(self.deleteName) + "'")       
            self.dataBase.deleleUserAccess(name)


    def getRow(self, event):
        current_item = self.table.focus()
        if not current_item:
            return
        data = self.table.item(current_item)
        self.deleteName = data['values'][0]
   

def main():
    window = Tk()
    window.wm_title("Registro de accesos")
    window.config(bg='gray90')
    window.geometry('800x500')
    window.resizable(0,0)
    app = Register(window)
    app.mainloop()

if __name__=="__main__":
    main()        