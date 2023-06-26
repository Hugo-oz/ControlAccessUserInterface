import pyodbc 
 
class DataRegister():

    def __init__(self):
        self.connection=pyodbc.connect('DRIVER={SQL Server};SERVER=;DATABASE=Users;UID=;PWD=;')



    def createUserInfo(self,UserName, RegisterCurp, CareerAddress, UserType, Status):
        cur = self.connection.cursor()
        sql='''INSERT INTO UserInfo (UserName, RegisterCURP, CareerAddress, USerType, Status) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(UserName, RegisterCurp, CareerAddress, UserType, Status)
        cur.execute(sql)
        self.connection.commit()    
        cur.close()


    def showUserInfo(self):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM UserInfo" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def searchUserInfo(self, UserName):
        cur = self.connection.cursor()
        sql = "SELECT * FROM UserInfo WHERE UserName = {}".format(UserName)
        cur.execute(sql)
        name = cur.fetchall()
        cur.close()     
        return name 

    def deleleUserInfo(self,RegisterCURP):
        cur = self.connection.cursor()
        sql='''DELETE FROM UserInfo WHERE RegisterCURP = {}'''.format(RegisterCURP)
        cur.execute(sql)
        self.connection.commit()    
        cur.close()