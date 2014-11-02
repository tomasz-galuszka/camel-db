from camel import DbManager

class TestBookable():
    
    @classmethod
    def setup_class(self):
        self.db = DbManager.DbManager()
        self.db.mysqlConnect()

    def testCheckTableBookExist(self):
        result = self.db.mysqlExecuteAndReturnObject("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'sampleapp' AND table_name='Books'")[0]
        assert result[0] == 1

    def testCheckTableBookColumns(self):
        result = self.db.mysqlExecuteAndReturnObject("SELECT column_name FROM information_schema.columns WHERE table_name='Books' AND table_schema = 'sampleapp'")
        assert result[0][0]  == 'id'
        assert result[1][0]  == 'title'
        assert result[2][0]  == 'author'
        assert result[3][0]  == 'price'
