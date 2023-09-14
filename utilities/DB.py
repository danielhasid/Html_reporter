
import pyodbc

from utilities.BaseClass import BaseClass


class TestDeleteUser(BaseClass):
    def __init__(self):
        self.log = self.get_Logger()
        try:
            self.log.info("ATTEMPTING DATABASE CONNECTION")
            self.conn = pyodbc.connect(
                "Driver={ODBC Driver 18 for SQL Server};Server=ofakimdev-dbsrv.database.windows.net;Database=ofakimdb_Copy;UID=dbadmin;PWD=Mq#86Eyq!D;")
        except Exception as error:
            self.log.info(f"UNABLE TO CONNECT TO DATABASE\n{error}")


    def delete(self,request):
        cursor = self.conn.cursor()
        sql = "delete from Beneficiary where bankAccountHolderEmail = '" + str(request) + "'"
        try:
            cursor.execute(sql)
            cursor.commit()
            status = f"Delete {request} executed"
            return status
        except pyodbc as error:
            return error
        finally:
            cursor.close()

    def existUser(self,request):
        cursor = self.conn.cursor()
        sql = "select count(*) from Beneficiary where bankAccountHolderEmail = '" + str(request) + "'"
        try:
            rows = cursor.execute(sql)
            return rows
        except pyodbc as error:
            return error
        finally:
            cursor.close()


    def deletePayer(self,request):
        cursor = self.conn.cursor()
        sql = "delete from Payers where SetupProfileId = '" + str(request) + "'"
        try:
            rows = cursor.execute(sql)
            return rows
        except pyodbc as error:
            return error
        finally:
            cursor.close()

    def existPayer(self,request):
        cursor = self.conn.cursor()
        sql = "select count(*) from Payers where SetupProfileId = '" + str(request) + "'"
        try:
            rows = cursor.execute(sql)
            return rows
        except pyodbc as error:
            return error
        finally:
            cursor.close()