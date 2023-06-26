from tkinter import Entry, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END
from Conection import*


class Register(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
                                    
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0,row=0)
        self.frame2 = Frame(master, bg='gray90')
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
        Label(self.frame1, text = 'Registro de usuarios',bg='gray90',fg='black', font=('Orbitron',15,'bold')).grid(column=0, row=0)
        
        Label(self.frame2, text = 'Agregar Nuevo Usuario',fg='black', bg ='gray90', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame2, text = 'Nombre',fg='black', bg ='gray90', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame2, text = 'Registro/CURP',fg='black', bg ='gray90', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame2, text = 'Carrera/Direccion',fg='black', bg ='gray90', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        Label(self.frame2, text = 'Tipo de usuario', fg='black',bg ='gray90', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        Label(self.frame2, text = 'Estado',fg='black', bg ='gray90', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)

        Entry(self.frame2,textvariable=self.userName , font=('Arial',12)).grid(column=1,row=1, padx =5)
        Entry(self.frame2,textvariable=self.registerCURP , font=('Arial',12)).grid(column=1,row=2)
        Entry(self.frame2,textvariable=self.careerAddress , font=('Arial',12)).grid(column=1,row=3)
        Entry(self.frame2,textvariable=self.userType , font=('Arial',12)).grid(column=1,row=4)
        Entry(self.frame2,textvariable=self.status , font=('Arial',12)).grid(column=1,row=5)
       
        Label(self.frame4, text = 'Control',fg='black', bg ='gray90', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=1, pady=1, padx=4)         
        Button(self.frame4,command= self.addUserInfo, text='Agregar usuario', font=('Arial',10,'bold'), bg='gray70').grid(columnspan=3, column=1,row=0, pady=1, padx=1)  
        Button(self.frame4,command = self.deleteRow, text='Eliminar usuario', font=('Arial',10,'bold'), bg='gray70').grid(column=0,row=3, padx=4)
        Button(self.frame4,command = self.searchRegisterCURP, text='Buscar', font=('Arial',8,'bold'), bg='gray70').grid(columnspan=2,column = 1, row=2)
        Entry(self.frame4,textvariable=self.search , font=('Arial',12), width=10).grid(column=0,row=2, pady=1, padx=8)
        Button(self.frame4,command = self.showAll, text='Recargar pagina', font=('Arial',10,'bold'), bg='gray70').grid(columnspan=3,column=1,row=3, pady=8)


        self.table = ttk.Treeview(self.frame3, height=21)
        self.table.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient = HORIZONTAL, command= self.table.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = Scrollbar(self.frame3, orient =VERTICAL, command = self.table.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.table.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
       
        self.table['columns'] = ('Name', 'CareerAddress', 'UserType', 'Status')

        self.table.column('#0', minwidth=100, width=250, anchor='center')
        self.table.column('Name', minwidth=100, width=100 , anchor='center')
        self.table.column('CareerAddress', minwidth=100, width=200, anchor='center' )
        self.table.column('UserType', minwidth=100, width=100 , anchor='center')
        self.table.column('Status', minwidth=50, width=50, anchor='center')

        self.table.heading('#0', text='Nombre', anchor ='center')
        self.table.heading('Name', text='Registro/Curp', anchor ='center')
        self.table.heading('CareerAddress', text='Carrera/Direccion', anchor ='center')
        self.table.heading('UserType', text='Tipo de usuario', anchor ='center')
        self.table.heading('Status', text='Estado', anchor ='center')


        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='black')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='gray90')
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
            self.dataBase.createUserInfo(userName, registerCURP, careerAddress, userType, status)


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
        nombre_buscado = self.dataBase.searchUserInfo(searchedRegisterCURP)
        self.table.delete(*self.table.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.table.insert('',i, text = nombre_buscado[i][0:1], values=nombre_buscado[i][2:6])


    def showAll(self):
        self.table.delete(*self.table.get_children())
        registro = self.dataBase.showUserInfo()
        i = -1
        for dato in registro:
            i= i+1                       
            self.table.insert('',i, text = registro[i][0:1], values=registro[i][1:6])


    def deleteRow(self):
        fila = self.table.selection()
        if len(fila) !=0:        
            self.table.delete(fila)
            name = ("'"+ str(self.deleteName) + "'")       
            self.dataBase.deleleUserInfo(name)


    def getRow(self, event):
        current_item = self.table.focus()
        if not current_item:
            return
        data = self.table.item(current_item)
        self.deleteName = data['values'][0]
   

def main():
    ventana = Tk()
    ventana.wm_title("Registro de usuarios")
    ventana.config(bg='gray90')
    ventana.geometry('1085x500')
    ventana.resizable(0,0)
    app = Register(ventana)
    app.mainloop()

if __name__=="__main__":
    main()        