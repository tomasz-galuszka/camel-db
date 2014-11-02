from camel.DbManager import DbManager
import os
import datetime
from camel import CamelUtils

class CamelBackup():
    
    hostName = ""
    userName = ""
    passwd = ""
    dbName = ""
    changesetsDir = ""
    changesetsHistoryDir = ""
    backupDir = ""
    
    db = None
    camelUtils = None

    def __init__(self):
        self.db = DbManager()
        self.camelUtils = CamelUtils.CamelUtils()
        
        params = self.camelUtils.getConnectionParams()
        self.hostName = params[0]
        self.dbName = params[3]
        self.changesetsDir = params[4]
        self.changesetsHistoryDir = params[5]
        self.backupDir = params[6]
        self.userName = params[7]
        self.passwd = params[8]
        
    def backup(self):
        backupfile = self.dbName + "_"+ datetime.datetime.now().isoformat() + ".sql.gz"
        
        cmd = "echo ' ----Backup " + self.dbName + " database to "+ self.backupDir + backupfile + "'"
        os.system(cmd)
        
        cmd = "mysqldump -u " + self.userName + " -h " + self.hostName + " -p" + self.passwd + " --opt --routines --flush-privileges --single-transaction --database "
        cmd += self.dbName +  " | gzip -9 --rsyncable > "+ self.backupDir + backupfile
        os.system(cmd)
        
        self.organizeChangesets()
        
    def organizeChangesets(self):
        print " -----Moving closed changesets to history..."
        counter = 0
        for change in self.camelUtils.getChangesets(self.changesetsDir):
            if change[1]["closed"] is True:
                ++counter
                print " ------Move %s" % change[0] + " do " + self.changesetsHistoryDir
                self.camelUtils.moveFile(change[0], self.changesetsHistoryDir)
                
        print " -----Moved: %d" % counter
                
    def restore(self, backupFilePath):
        cmd = "mysql -u " + self.userName + " -h " + self.hostName + " -p" + self.passwd + " < scripts/create_database.sql "
        os.system(cmd)
        
        cmd = "gunzip < " + backupFilePath +" | mysql -u " + self.userName + " -h " + self.hostName + " -p" + self.passwd + " " + self.dbName
        os.system(cmd)
