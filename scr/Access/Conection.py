import pyodbc 
 
class DataRegister():

    def __init__(self):
        self.connection=pyodbc.connect('DRIVER={SQL Server};SERVER=;DATABASE=;UID=;PWD=;')



    def createUserAccess(self,Date, userName, userType, action):
        cur = self.connection.cursor()
        sql='''INSERT INTO UserAccess (Date, UserName, UserType, Action) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(Date, userName, userType, action)
        cur.execute(sql)
        self.connection.commit()    
        cur.close()


    def showUserAccess(self):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM UserAccess" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def searchUserAccess(self, userName):
        cur = self.connection.cursor()
        sql = "SELECT * FROM UserAccess WHERE UserName = {}".format(userName)
        cur.execute(sql)
        name = cur.fetchall()
        cur.close()     
        return name 

    def deleleUserAccess(self,RegisterCURP):
        cur = self.connection.cursor()
        sql='''DELETE FROM UserAccess WHERE RegisterCURP = {}'''.format(RegisterCURP)
        cur.execute(sql)
        self.connection.commit()    
        cur.close()