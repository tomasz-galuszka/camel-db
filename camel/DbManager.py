import MySQLdb
from CamelUtils import CamelUtils

class DbManager:
    # connection params
    hostName = ""
    userName = ""
    passwd = ""
    dbName = ""
    connection = None
    
    def __init__(self):
        params = CamelUtils().getConnectionParams()
        self.hostName = params[0]
        self.userName = params[1]
        self.passwd = params[2]
        self.dbName = params[3]
    
    def mysqlConnect(self):  # execute mysqlQuery
        if self.connection:
            return
        print ' --Creating connection...'
        DbManager.connection = MySQLdb.connect(self.hostName, self.userName, self.passwd, self.dbName)
        print " ---Connected !"
    
    def mysqlExecuteAndReturnObject(self, query):  # execute mysql query , returns object
        c = self.connection.cursor()
        c.execute(query)
        self.connection.commit()
        
        print ' ---- Execute: %s' % query
        result = c.fetchall()
        c.close()
        
        return result
    
    def mysqlExecute(self, query):  # execute mysql query
        c = self.connection.cursor()
        print ' ---- Execute: %s' % query
        c.execute(query)
        c.close()
        DbManager.connection.commit()
    
    def mysqlDisconnect(self):  # drop db connection
        self.connection.close()
        print " ---Disconnected !"
