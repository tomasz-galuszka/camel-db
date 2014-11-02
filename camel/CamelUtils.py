import glob
import json
import re
import shutil
from ConfigParser import SafeConfigParser

class CamelUtils:
    
    def getConnectionParams(self):
        params = []
        parser = SafeConfigParser()
        parser.read('config.ini')
        
        params.append(parser.get('DEFAULT', 'Hostname'))
        params.append(parser.get('DEFAULT', 'Username'))
        params.append(parser.get('DEFAULT', 'Password'))
        params.append(parser.get('DEFAULT', 'Dbname'))
        
        params.append(parser.get('CAMEL', 'ChangesetsDir'))
        params.append(parser.get('CAMEL', 'ChangesetsHistoryDir'))
        params.append(parser.get('CAMEL', 'BackupDir'))
        
        params.append(parser.get('ROOT', 'UserName'))
        params.append(parser.get('ROOT', 'Password'))
        
        return params
    
    def getChangesets(self, directory):  # return array of *.js files from directory
        files = glob.glob(directory + "*.js")
        result = []
        for f in files:
            result.append((f, self.parseJson(f)))
            
        result.sort();
        sorted(result, key=lambda result: result[1]['version'])
        return result
    
    def getTests(self, schemaVersion):
        files = glob.glob("tests/camel-tests.js")
        result = []
        for f in files:
            parsed = self.parseJson(f)
            for item in parsed:
                if item['dbversion'] == int(schemaVersion):
                    result.append(item['tests'])
        return result
    
    def parseJson(self, changsetFile):  # parse jsonFile
        json_data = open(changsetFile)
        data = json.load(json_data)
        json_data.close()
        return data

    def replace(self, f, pattern, subst):
        file_handle = open(f, 'r')
        file_string = file_handle.read()
        file_handle.close()
    
        file_string = (re.sub(pattern, subst, file_string))
    
        file_handle = open(f, 'w')
        file_handle.write(file_string)
        file_handle.close()
        
    def moveFile(self, filePath, destinationPath):
        shutil.move(filePath, destinationPath)
