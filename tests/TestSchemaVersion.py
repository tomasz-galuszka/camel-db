from camel import DbManager

class TestSchemaVersion():
    
    @classmethod
    def setup_class(self):
        self.db = DbManager.DbManager()
        self.db.mysqlConnect()
        
    def testCheckSchemaVersion(self):
        result = self.db.mysqlExecuteAndReturnObject("SELECT camel_get_schema_version()")[0]
        assert result[0] == 2