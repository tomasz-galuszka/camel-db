from CamelUtils import CamelUtils
from DbManager import DbManager

class CamelSchema:

    MYSQL_SCHEMA_VERSION = "SELECT camel_get_schema_version()"
    MYSQL_UPDATE_SCHEMA_VERSION = "SELECT camel_update_version(%(current)01d, %(new)01d)"
    db = None
    camelUtils = None
    
    def __init__(self):
        self.db = DbManager()
        self.db.mysqlConnect()
        self.camelUtils = CamelUtils()

    def executeChangesets(self, directory):  # execute changesets
        queryCounter = 0;
        for change in self.camelUtils.getChangesets(directory):
            if change[1]["closed"] is False:
                print " ----Open change: %s" % change[0]
                dbSchemaVersion = self.getSchemaVersion()
                if dbSchemaVersion == change[1]["version"]:
                    queryCounter += 1
                    for sql in change[1]["sql"]:
                        self.executeQuery(sql[0])
                    self.camelUtils.replace(change[0], "\"closed\" : false", "\"closed\" : true")
                else:
                    print " -----Incorrect db version."
                    print " -----Databse schema version is: %d" % dbSchemaVersion + ", version in file is : %d" % change[1]["version"]
            
        if queryCounter != 0:
            print " ----Query executions complete :)"
        print " ----Executed queries: %d" % queryCounter    
    
    def updateSchema(self, newSchema):
        currentSchema = self.getSchemaVersion()
        if currentSchema >= newSchema:
            print " ----Current schema is: %(current)01d ,new: %(new)01d" % {"current": currentSchema, "new": newSchema}
            print " -----Downgrade schema is not available!"
        else:
            print " ---UPDATE SCHEMA: FROM %(current)01d to %(new)01d" % {"current": currentSchema, "new": newSchema}
            self.executeQuery(CamelSchema.MYSQL_UPDATE_SCHEMA_VERSION % {"current": currentSchema, "new": newSchema})
    
    def executeQuery(self, query):
        self.db.mysqlExecute(query)
    
    def executeQueryAndReturnObject(self, query):
        return self.db.mysqlExecuteAndReturnObject(query)[0]
        
    def getSchemaVersion(self):
        result = self.executeQueryAndReturnObject(self.MYSQL_SCHEMA_VERSION)[0]
        return result
        
    def disconnect(self):
        self.db.mysqlDisconnect()
