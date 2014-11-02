from camel import DbManager

class TestPersonTable():
    
    @classmethod
    def setup_class(self):
        self.db = DbManager.DbManager()
        self.db.mysqlConnect()

    def testCheckTablePersonExist(self):
        result = self.db.mysqlExecuteAndReturnObject("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'sampleapp' AND table_name='Persons'")[0]
        assert result[0] == 1

    def testCheckTablePersonColumns(self):
        result = self.db.mysqlExecuteAndReturnObject("SELECT column_name FROM information_schema.columns WHERE table_name='Persons' AND table_schema = 'sampleapp'")
        assert result[0][0]  == 'id'
        assert result[1][0]  == 'last_name'
        assert result[2][0]  == 'first_name'
        assert result[3][0]  == 'address'
        assert result[4][0]  == 'city'
        assert result[5][0]  == 'wiek'